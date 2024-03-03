#include <iostream>

// Function to add two numbers
int add(int a, int b) {
    return a + b;
}

// Class representing a simple point in 2D space
class Point {
private:
    int x;
    int y;

public:
    Point(int x_, int y_) : x(x_), y(y_) {}

    int getX() const {
        return x;
    }

    int getY() const {
        return y;
    }
};

// Class representing a rectangle
class Rectangle {
private:
    Point topLeft;
    Point bottomRight;

public:
    Rectangle(const Point& topLeft_, const Point& bottomRight_) : topLeft(topLeft_), bottomRight(bottomRight_) {}

    int calculateArea() const {
        int width = bottomRight.getX() - topLeft.getX();
        int height = bottomRight.getY() - topLeft.getY();
        return width * height;
    }
};

int main() {
    Point p1(1, 1);
    Point p2(4, 5);
    Rectangle rect(p1, p2);

    std::cout << "Area of rectangle: " << rect.calculateArea() << std::endl;
    std::cout << "Sum of 3 and 5: " << add(3, 5) << std::endl;

    return 0;
}
