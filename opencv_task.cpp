#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>

using namespace cv;
using namespace std;

string matTypeToString(int type) {
    string r;
    uchar depth = type & CV_MAT_DEPTH_MASK;
    uchar chans = 1 + (type >> CV_CN_SHIFT);
    switch (depth) {
        case CV_8U:  r = "8U"; break;
        case CV_8S:  r = "8S"; break;
        case CV_16U: r = "16U"; break;
        case CV_16S: r = "16S"; break;
        case CV_32S: r = "32S"; break;
        case CV_32F: r = "32F"; break;
        case CV_64F: r = "64F"; break;
        default:     r = "User"; break;
    }
    r += "C";
    r += (chans + '0');
    return r;
}

int main() {
    Mat img = imread("test.jpg");
    if (img.empty()) {
        cerr << "❌ 无法读取图片！" << endl;
        return -1;
    }

    // 输出图像信息
    cout << "===== 图像基本信息 =====" << endl;
    cout << "宽度: " << img.cols << endl;
    cout << "高度: " << img.rows << endl;
    cout << "通道数: " << img.channels() << endl;
    cout << "数据类型: " << matTypeToString(img.type()) << endl;
    cout << "========================" << endl;

    // ============== 核心修改：简化窗口显示 ==============
    // 1. 显示原图（按任意键继续）
    imshow("1. 原始图像", img);
    waitKey(0);  // 按任意键关闭当前窗口，打开下一个

    // 2. 灰度图转换 + 显示
    Mat gray_img;
    cvtColor(img, gray_img, COLOR_BGR2GRAY);
    imshow("2. 灰度图像", gray_img);
    waitKey(0);

    // 3. 裁剪图 + 显示
    Rect roi(0, 0, 100, 100);
    Mat cropped = img(roi);
    imshow("3. 裁剪图像(100x100)", cropped);
    waitKey(0);

    // 保存文件（自动保存，不用管）
    imwrite("gray_output.jpg", gray_img);
    imwrite("cropped_output.jpg", cropped);

    cout << "✅ 所有图片保存完成！" << endl;
    destroyAllWindows();
    return 0;
}