package course.project;

import javafx.scene.control.*;
import javafx.scene.layout.Pane;

import java.util.ArrayList;
import java.util.List;

public class AppView extends Pane {

  private ListView<String> linkList;
  private SearchButtonPane searchButtonPane;
  private TextField searchField;
  private RadioButton radio1;

  public AppView(String title) {
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

    radio1 = new RadioButton("On/Off");
    radio1.relocate(150, 60);

    linkList = new ListView<String>();
    linkList.relocate(10, 100);
    linkList.setPrefSize(540,250);

    searchButtonPane = new SearchButtonPane();
    searchButtonPane.relocate(180, 180);
    searchButtonPane.setPrefSize(305,30);



    // Add all labels and textfields to the pane
    innerPane.getChildren().addAll(label1, label2,
            searchField, radio1, searchButtonPane, linkList);
    
    // Make a title for border and add it as well as inner pane to main pane
    Label titleLabel = new Label(); // Title to be placed onto border
    titleLabel.setText(title); // Incoming constructor parameter
    titleLabel.setStyle("-fx-background-color: white; \n" +
                        "-fx-translate-y: -8; \n" +
                        "-fx-translate-x: 10;");

    getChildren().addAll(innerPane, titleLabel);
  }

  public RadioButton getRadio1(){
    return radio1;
  }

  public TextField getSearchField(){
    return searchField;
  }
  public SearchButtonPane getSearchButtonPane() {
    return searchButtonPane;
  }

  public void update(Search model, int selectedItem){
    List<SearchResult> results;
    results = model.getSearchResults();

    linkList.getItems().clear();

    for (int i =0; i<results.size();i++){
      linkList.getItems().add(String.format("%2d.  %s        %.3f", i+1, results.get(i).getTitle(), results.get(i).getScore()));
      //String.format("%0.2d. %s %-30d", i, results.get(i).getTitle(), results.get(i).getScore())
    }
    linkList.getSelectionModel().select(selectedItem);
  }
}