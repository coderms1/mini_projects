// File: ShapeGUI.java
// Project: Draw Shapes w/ GUI
// Date: 4-8-2025

/*
   This Java program creates a GUI that lets users draw 
       and move rectangles and squares. Users can click to place shapes, 
           drag them around, and can also use their pointer to draw freehand lines. 
           The "Clear" button wipes everything clean for a fresh start.  
       It uses custom painting logic and IntelliJ's interactive Swing components, 
   in order to create a most basic interactive canvas.
*/

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.Line2D;
import java.util.ArrayList;
import java.util.List;

public class ShapeGUI {
    private JPanel mainPanel;
    private JLabel labelX;
    private JButton buttonRectangle;
    private JButton buttonSquare;
    private JButton buttonClear;
    private JTextField textFieldX;
    private JLabel labelY;
    private JTextField textFieldY;
    private JLabel labelWidth;
    private JTextField textFieldWidth;
    private JLabel labelHeight;
    private JTextField textFieldHeight;
    private JPanel drawingPanel;
    private JLabel titleLabel;

    // Stores DRAWN SHAPES in an ARRAYLIST
    private final List<Shape> shapesToDraw = new ArrayList<>();
    // LINE BEING DRAWN
    private final List<Line2D> linesDrawn = new ArrayList<>();

    // SHAPE BEING DRAGGED
    private Shape draggedShape = null;
    private int dragOffsetX, dragOffsetY;

    // COORDINATES for the drawingPanel Grid
    private int x, y, x2, y2;

    public ShapeGUI() {
        Color bgColor = new Color(114, 222, 250); // LIGHT BLUE
        mainPanel.setBackground(bgColor);

        // RECTANGLE BUTTON -- LOGIC
        buttonRectangle.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    int rectX = x;
                    int rectY = y;
                    int width = Integer.parseInt(textFieldWidth.getText());
                    int height = Integer.parseInt(textFieldHeight.getText());

                    shapesToDraw.add(new Rectangle(rectX, rectY, width, height));
                    drawingPanel.repaint();
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(null, "Enter a VALID number");
                }
            }
        });

        // SQUARE BUTTON -- LOGIC
        buttonSquare.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    int squareX = x;
                    int squareY = y;
                    int length = Integer.parseInt(textFieldWidth.getText());
                    shapesToDraw.add(new Square(squareX, squareY, length));
                    drawingPanel.repaint();
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(null, "Enter a VALID number");
                }
            }
        });

        // CLEAR BUTTON -- LOGIC
        buttonClear.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // CLEAR ALL SHAPES, LINES, TEXTFIELDS
                shapesToDraw.clear();
                linesDrawn.clear(); // Also clear lines
                textFieldX.setText("");
                textFieldY.setText("");
                textFieldWidth.setText("");
                textFieldHeight.setText("");
                drawingPanel.repaint();
            }
        });
    }

    private void createUIComponents() {
        // JPANEL that Enables LINE DRAWING
        drawingPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                setBackground(Color.LIGHT_GRAY);

                // Draw saved lines first
                Graphics2D g2 = (Graphics2D) g;
                g2.setColor(Color.BLACK);
                for (Line2D line : linesDrawn) {
                    g2.draw(line);
                }

                // FOR EACH LOOP to DRAW ALL SHAPES w/ COLORS
                for (Shape s : shapesToDraw) {
                    if (s instanceof Rectangle && !(s instanceof Square)) {
                        ((Rectangle) s).draw(g, Color.BLUE);
                    } else if (s instanceof Square) {
                        ((Square) s).draw(g, Color.RED);
                    }
                }
            }
        };

        // MOUSE PRESSING Method - THE LAST ONE CLICKED CHOSEN
        drawingPanel.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                x = e.getX();
                y = e.getY();
                textFieldX.setText(String.valueOf(x));
                textFieldY.setText(String.valueOf(y));
                draggedShape = null;

                // This loops through in a REVERSE to PICK the TOP SHAPE
                for (int i = shapesToDraw.size() - 1; i >= 0; i--) {
                    Shape s = shapesToDraw.get(i);
                    if (s instanceof Square) {
                        int sx = s.x;
                        int sy = s.y;
                        int sl = ((Square) s).width;
                        if (x >= sx && x <= sx + sl && y >= sy && y <= sy + sl) {
                            draggedShape = s;
                            dragOffsetX = x - sx;
                            dragOffsetY = y - sy;
                            break;
                        }
                    } else if (s instanceof Rectangle) {
                        int rx = s.x;
                        int ry = s.y;
                        int rw = ((Rectangle) s).width;
                        int rh = ((Rectangle) s).height;
                        if (x >= rx && x <= rx + rw && y >= ry && y <= ry + rh) {
                            draggedShape = s;
                            dragOffsetX = x - rx;
                            dragOffsetY = y - ry;
                            break;
                        }
                    }
                }
            }

            @Override
            public void mouseReleased(MouseEvent e) {
                // This is WHERE the DRAGGED SHAPE stops
                draggedShape = null;
            }
        });

        // *BONUS FEATURE* added to allow the user to DRAG & MOVE the SHAPES
        drawingPanel.addMouseMotionListener(new MouseMotionAdapter() {
            @Override
            public void mouseDragged(MouseEvent e) {
                x2 = e.getX();
                y2 = e.getY();

                if (draggedShape != null) {
                    draggedShape.x = x2 - dragOffsetX;
                    draggedShape.y = y2 - dragOffsetY;
                    drawingPanel.repaint();
                } else {
                    // ADD LINE TO ARRAY for PERSISTENCE
                    linesDrawn.add(new Line2D.Float(x, y, x2, y2));
                    x = x2;
                    y = y2;
                    drawingPanel.repaint();
                }
            }
        });
    }

    public static void main(String[] args) {
        // LAUNCHES the GUI (firing on all cylinders!)
        JFrame frame = new JFrame("ShapeGUI");
        frame.setContentPane(new ShapeGUI().mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1200, 900);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
