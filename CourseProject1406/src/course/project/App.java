package course.project;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;

public class App extends Application{
  public void start(Stage primaryStage){
    MainPane addPane = new MainPane("Web Crawler");
    addPane.relocate(10,10);

    Pane mainPane = new Pane();
    mainPane.getChildren().add(addPane);
    Scene scene = new Scene(mainPane, 600, 600);
    primaryStage.setTitle("Web Crawler"); // Set window title
    primaryStage.setScene(scene);
    primaryStage.show();
  }
  
  public static void main(String[] args){
    launch(args);
  } 
}