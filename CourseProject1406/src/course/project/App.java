package course.project;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;

public class App extends Application{

  SearchData model;

  public App() {model = new SearchData();}
  public void start(Stage primaryStage){

    model = new SearchData();
    AppView view = new AppView("Web Crawler");
    view.update(model, 0);
    view.relocate(10,10);

    Pane mainPane = new Pane();
    mainPane.getChildren().add(view);
    Scene scene = new Scene(mainPane, 600, 600);
    primaryStage.setTitle("Web Crawler"); // Set window title
    primaryStage.setScene(scene);
    primaryStage.show();

    view.getSearchButtonPane().getSearchButton().setOnAction(new EventHandler<ActionEvent>() {
      @Override
      public void handle(ActionEvent actionEvent) {
        model.search(view.getSearchField().getText(), view.getRadio1().isSelected(), 10);
        view.update(model, 0);
      }
    });

  }
  
  public static void main(String[] args){
    launch(args);
  } 
}