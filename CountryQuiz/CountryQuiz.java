// Java (CIT 215): Lab 8
// Program: Country Gui w/ Quiz
// Due Date: 04-01-2025
// Author: Matthew Simone

import javax.swing.*;
import java.awt.*;
import java.nio.file.*;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Objects;

public class CountryQuiz {
    private JPanel panel1;
    private JLabel imageLabel;
    private JLabel outputLabel;
    private JLabel scoreLabel;
    private JTextField answerField;
    private JButton submitButton;
    private JPanel southPanel;
    private List<CountryQ> countries = new ArrayList<>();
    private Map<String, CountryQ> countryMap = new HashMap<>();
    private int currentIndex = 0;
    private int score = 0;

    public CountryQuiz() {
        setupUI();
        loadCountries();
        populateCountryMap();
        displayQuizQuestion();
        submitButton.addActionListener(e -> checkAnswer());
    }

    private void setupUI() {
        panel1.setPreferredSize(new Dimension(550, 350));
        scoreLabel = new JLabel("Score: 0");
        answerField = new JTextField(20);
        createUIComponents();
        panel1.add(scoreLabel, BorderLayout.NORTH);
        panel1.add(imageLabel, BorderLayout.CENTER);
        panel1.add(outputLabel, BorderLayout.WEST);
        southPanel = new JPanel(new FlowLayout());
        southPanel.add(answerField);
        southPanel.add(submitButton);
        panel1.add(southPanel, BorderLayout.SOUTH);
    }

    private void loadCountries() {
        try {
            List<String> lines = Files.readAllLines(
                    Paths.get(Objects.requireNonNull(getClass().getClassLoader()
                            .getResource("countries-data.csv")).toURI()),
                    StandardCharsets.UTF_8);
            lines.remove(0);
            for (String line : lines) {
                String[] data = line.split(",");
                countries.add(new CountryQ(data[0], data[1], data[2], data[3]));
            }
        } catch (Exception e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }

    private void populateCountryMap() {
        for (CountryQ country : countries) {
            countryMap.put(country.getName().toLowerCase(), country);
        }
    }

    private void displayQuizQuestion() {
        if (!countries.isEmpty()) {
            Random random = new Random();
            currentIndex = random.nextInt(countries.size());
            CountryQ current = countries.get(currentIndex);
            imageLabel.setIcon(new ImageIcon(
                    getClass().getClassLoader().getResource("map-images/" + current.getImagefile())));
            outputLabel.setText("What country is this?");
            answerField.setText("");
        }
    }

    private void checkAnswer() {
        String userAnswer = answerField.getText().trim().toLowerCase();
        CountryQ current = countries.get(currentIndex);

        if (userAnswer.equals(current.getName().toLowerCase())) {
            score++;
            scoreLabel.setText("Score: " + score);
            JOptionPane.showMessageDialog(panel1, "Correct!! ✅\n\nKeep up the good work! 👍");
        } else {
            JOptionPane.showMessageDialog(panel1,
                    "INCORRECT!! ❌ 👎\n" + current.toString());
        }

        displayQuizQuestion();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Country Quiz");
            frame.setContentPane(new CountryQuiz().panel1);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.pack();
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });
    }

    private void createUIComponents() {
        imageLabel = new JLabel();
        imageLabel.setHorizontalAlignment(JLabel.CENTER);
        outputLabel = new JLabel("What country is this?");
        outputLabel.setHorizontalAlignment(JLabel.CENTER);
        submitButton = new JButton("Submit Answer");
    }
}
