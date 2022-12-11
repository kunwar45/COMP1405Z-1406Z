package course.project;

import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.layout.Pane;

public class SearchButtonPane extends Pane {

    private Button searchButton;

    public Button getSearchButton() {
        return searchButton;
    }

    public SearchButtonPane() {
        Pane innerPane = new Pane();

        searchButton = new Button("search");

        searchButton.setText("Search");
        searchButton.setAlignment(Pos.CENTER_LEFT);
        searchButton.setDisable(false);
        searchButton.relocate(60,200);
        searchButton.setPrefSize(100, 30);

        innerPane.getChildren().add(searchButton);

        getChildren().add(innerPane);
    }

}
