package course.project;

import javafx.geometry.Pos;
import javafx.scene.control.*;
import javafx.scene.layout.Pane;

import java.util.ArrayList;

public class MainPane extends Pane {

  private ListView<SearchResult> linkList;
  private SearchButtonPane searchButtonPane;
  private TextField searchField;

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

    searchField = new TextField();
    searchField.relocate(150, 20);
    searchField.setPrefSize(300, 30);

    RadioButton radio1 = new RadioButton("Yes");
    radio1.relocate(140, 55);
    RadioButton radio2 = new RadioButton("No");
    radio2.relocate(140, 75);

    linkList = new ListView<SearchResult>();
    linkList.relocate(10, 40);
    linkList.setPrefSize(540,150);

    searchButtonPane = new SearchButtonPane();
    searchButtonPane.relocate(250, 240);
    searchButtonPane.setPrefSize(305,30);



    // Add all labels and textfields to the pane
    innerPane.getChildren().addAll(label1, label2,
            searchField, radio1, radio2, searchButtonPane, linkList);
    
    // Make a title for border and add it as well as inner pane to main pane
    Label titleLabel = new Label(); // Title to be placed onto border
    titleLabel.setText(title); // Incoming constructor parameter
    titleLabel.setStyle("-fx-background-color: white; \n" +
                        "-fx-translate-y: -8; \n" +
                        "-fx-translate-x: 10;");

    getChildren().addAll(innerPane, titleLabel);
  }

  public TextField getSearchField(){
    return searchField;
  }
  public SearchButtonPane getSearchButtonPane() {
    return searchButtonPane;
  }

  public void update(Search model, int selectedItem){
    ArrayList<SearchResult> list;
    list = model.getSearchResults();

    linkList.getItems().clear();

    for (int i =0; i<list.size();i++){
      linkList.getItems().add(list.get(i));
    }

    linkList.getSelectionModel().select(selectedItem);


  }
}