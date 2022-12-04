package course.project;

import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;
import javafx.scene.layout.Pane;

public class MainPane extends Pane {
  //Constructor for our AddressPane
  ///Takes a String, which represents the title of the pane (e.g., 'Contact Address')
  public MainPane(String title) {
    //Create an inner pane and set its style
    //This will hold all our components
    Pane innerPane = new Pane();
    innerPane.setStyle("-fx-background-color: white; " +
                       "-fx-border-color: gray; " +
                       "-fx-padding: 4 4;"); // margin spacing at bottom right
    
    // Create the labels and textfields
    Label label1 = new Label("Search Query:");
    label1.relocate(10, 20);
    label1.setPrefSize(80, 30);
    Label label2 = new Label("Page Rank Boost:");
    label2.relocate(10, 55);
    label2.setPrefSize(120, 30);


    
    TextField nameField = new TextField();
    nameField.relocate(150, 20);
    nameField.setPrefSize(300, 30);

    RadioButton radio1 = new RadioButton("Yes");
    radio1.relocate(140, 55);
    RadioButton radio2 = new RadioButton("No");
    radio2.relocate(140, 75);

    Button b = new Button("search");

    b.setText("Search");
    b.setAlignment(Pos.CENTER_LEFT);
    b.setDisable(false);
    b.relocate(60,200);
    b.setPrefSize(100, 30);

    // Add all labels and textfields to the pane
    innerPane.getChildren().addAll(label1, label2,
                                   nameField, radio1, radio2, b);
    
    // Make a title for border and add it as well as inner pane to main pane
    Label titleLabel = new Label(); // Title to be placed onto border
    titleLabel.setText(title); // Incoming constructor parameter
    titleLabel.setStyle("-fx-background-color: white; \n" +
                        "-fx-translate-y: -8; \n" +
                        "-fx-translate-x: 10;");

    getChildren().addAll(innerPane, titleLabel);
  }
}