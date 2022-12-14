package course.project;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class SearchData implements ProjectTester {

	private List<SearchResult> searchResults;
	private Crawler crawler;
	private Search searchObj

	public void initialize(){
		File file = new File("pages");
		if (file.exists()){
			Crawler.deleteFolder(file);
		}
		file.mkdir();

		file = new File("IDFs");
		if (file.exists()){
			Crawler.deleteFolder(file);
		}
		file.mkdir();
	}

	public void crawl(String seedURL){
		crawler = new Crawler();
		crawler.crawl(seedURL);
	}

	public List<String> getOutgoingLinks(String URL){
			String newURL = URL.replace('/','{').replace(':','}').replace('.','(');
			File file = new File("pages" + File.separator + newURL);
			if (file.exists()){
				return List.of(readFile("pages" + File.separator + newURL + File.separator + "outgoinglinks.txt").split(" "));
			}
		return null;
	}

	public List<String> getIncomingLinks(String URL){
		String newURL = URL.replace('/','{').replace(':','}').replace('.','(');
		File file = new File("pages" + File.separator + newURL);
		if (file.exists()){
			return List.of(readFile("pages" + File.separator + newURL + File.separator + "incominglinks.txt").split(" "));
		}
		return null;
	}

	public double getPageRank(String URL){
		String newURL = URL.replace('/','{').replace(':','}').replace('.','(');
		File file = new File("pages" + File.separator + newURL);
		if (file.exists()){
			return Double.parseDouble(readFile("pages" + File.separator + newURL + File.separator + "pageRank.txt"));
		}
		return -1;
	}

	public String getTitle(String URL){
		String newURL = URL.replace('/','{').replace(':','}').replace('.','(');
		File file = new File("pages" + File.separator + newURL);
		if (file.exists()){
			return readFile("pages" + File.separator + newURL + File.separator + "title.txt");
		}
		return null;
	}

	public double getIDF(String word) {
		String path = "IDFs" + File.separator + word + ".txt";
		File file = new File(path);
		if (file.exists()){
			return Double.parseDouble(readFile(path));
		}
		return 0;
	}

	public double getTF(String URL, String word){
		String newURL = URL.replace('/','{').replace(':','}').replace('.','(');
		File file = new File("pages" + File.separator + newURL);
		if (file.exists()){
			file = new File("pages" + File.separator + newURL + File.separator + "countAll" + File.separator + word + ".txt");
			if (file.exists()){
				return Double.parseDouble(readFile("pages" + File.separator + newURL + File.separator + "countAll" + File.separator + word + ".txt").split(" ")[2]);
			}
		}
		return 0;
	}

	public double getTFIDF(String URL, String word){
		String newURL = URL.replace('/','{').replace(':','}').replace('.','(');
		File file = new File("pages" + File.separator + newURL);
		if (file.exists()){
			file = new File("pages" + File.separator + newURL + File.separator + "countAll" + File.separator + word + ".txt");
			if (file.exists()){
				return Double.parseDouble(readFile("pages" + File.separator + newURL + File.separator + "countAll" + File.separator + word + ".txt").split(" ")[1]);
			}
		}
		return 0;
	}

	public ArrayList<SearchResult> search(String query, boolean boost, int X) {
		searchObj = new Search();
		return searchObj.search(query, boost,X);
	}

//	public List<SearchResult> getSearchResults(){
//		return searchResults;
//
//		Search search = new Search();
//		return search.search(query, boost,X);
//	}

	public static String readFile(String path){
		String result = "";
		try {
			FileInputStream in = new FileInputStream(path);
			while(in.available() > 0){
				result+= (char)in.read() + "";
			}
			in.close();
		} catch (FileNotFoundException e) {
			System.out.println("Error: Cannot open file for reading");
		} catch (IOException e) {
			System.out.println("Error: Cannot read from file");
		}
		return result;
	}

	public static void main(String[] args) {

	}

}
