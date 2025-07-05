// File: Rectangle.java
// Project: Draw Shapes w/ GUI

import java.awt.*;

public class Rectangle extends Shape {
    protected int width;
    protected int height;

    // The RECTANGLE CONSTRUCTOR - (Default)
    public Rectangle() {
        super();
        this.width = 10;
        this.height = 10;
    }

    // This CONSTRUCTOR contains ALL PARAMETERS
    public Rectangle(int x, int y, int width, int height) {
        super(x, y);
        this.width = width;
        this.height = height;
    }

    // This is the DRAW METHOD
    public void draw(Graphics g, Color c) {
        g.setColor(c);
        g.fillRect(x, y, width, height);
    }
}
