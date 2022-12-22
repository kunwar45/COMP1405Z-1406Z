package course.project;

import java.io.*;
import java.net.MalformedURLException;
import java.util.ArrayList;
import java.util.HashMap;

public class Crawler {
	private final double ALPHA = 0.1;
	private final double DISTANCE_THRESHOLD = 0.0001;
	private HashMap<String,Link> data = new HashMap<>();
	private HashMap<String, Double> IDFs = new HashMap<>();
	private ImprovedQueue queue;
	private ArrayList<Double> pageRanks;
	private ArrayList<Link> mapping;

	public int crawl(String seed){
		//Creates queue for the urls that will be crawled
		queue = new ImprovedQueue(new Link(seed));
		Link url = queue.removestart();

		int count = 1;
		while (true) {
			parse(url);

			//Adds URLs to the queue if they have not already been crawled and are not already in the queue
			for (Link outgoingLink: url.getOutgoingLinks()) {
				if (!queue.contains(outgoingLink) && data.get(outgoingLink.getUrl()).getOutgoingLinks()==null ) {
					queue.addend(outgoingLink);
				}
			}

			//Generates the IDFs of the words in the urls
			for (String word: url.getCountAll().keySet()){
				IDFs.putIfAbsent(word,0.0);
				IDFs.replace(word,IDFs.get(word)+1);
			}

			//Breaks the loop if there are no more URLs to crawl
			if (queue.size() == 0) {
				break;
			}

			url = queue.removestart();
			count+=1;

		}

		createPageRanks();

		//Uses the mapping to assign the pageRanks to the Link objects
		for (int i = 0; i < mapping.size(); i++) {
			mapping.get(i).setPageRank(pageRanks.get(i));
		}

		createFiles();
		return count; //Returns the number of links parsed
	}

	public void parse(Link url){
		//Puts the link into the data hashmap
		data.putIfAbsent(url.getUrl(), url);
		url.setOutgoingLinks(new ArrayList<Link>());
		String parsed = "";
		try {
			parsed = WebRequester.readURL(url.getUrl());
		}catch(MalformedURLException e){
			e.printStackTrace();
		}catch(IOException e){
			e.printStackTrace();
		}

		String[] parsedArr = parsed.split("\n");

		for (String s : parsedArr){
			if (s.contains("title")){

				url.setTitle(s.substring(s.indexOf("<title>") + 7, s.indexOf("</title>")));
			} else if (s.contains("href")){
				Link outgoingLink;
				if (s.contains("http")){
					outgoingLink =  new Link(s.substring(s.indexOf("href") + 5, s.indexOf(">")));
				} else {

					outgoingLink = new Link(url.getRelativeLink()+s.substring((s.indexOf("./") + 1), s.indexOf(">")-1));
				}
				url.addOutgoingLink(outgoingLink);
				data.putIfAbsent(outgoingLink.getUrl(), outgoingLink);
				data.get(outgoingLink.getUrl()).addIncomingLink(url);

			} else if ((s.contains(">") && (!s.contains("<")))){
				url.setWordCount(url.getWordCount() + 1);

				url.addCountAll(s.substring(s.indexOf(">")), url.getSpecificCountAll(s)+1);

			} else if ((s.contains("<") && (s.charAt(0) != '<'))){
				url.setWordCount(url.getWordCount() + 1);

				url.addCountAll(s.substring(0, s.indexOf(">")), url.getSpecificCountAll(s)+1);

			} else if (!s.contains("<") && (!s.contains(">"))){
				url.setWordCount(url.getWordCount() + 1);
				url.addCountAll(s, url.getSpecificCountAll(s)+1);
			}

		}
	}

	//Creates all the files from the Link objects
	public void createFiles(){
		//For each Link parsed
		for (Link l: data.values()){
			String path = l.getUrl().replace("/", "{").replace(":", "}").replace('.','(');
			File file = new File("pages" + File.separator + path);
			file.mkdir();

			try {
				FileOutputStream out;
				out = new FileOutputStream("pages" + File.separator + path + File.separator + "outgoinglinks.txt");
				for (Link outgoingLink : l.getOutgoingLinks()) {
					for (char c : outgoingLink.getUrl().toCharArray()) {
						out.write(c);
					}
					out.write(' ');
				}
				out.close();

				out = new FileOutputStream("pages" + File.separator + path + File.separator + "incominglinks.txt");
				for (Link incominglink : l.getIncomingLinks()) {
					for (char c : incominglink.getUrl().toCharArray()) {
						out.write(c);
					}
					out.write(' ');
				}
				out.close();

				// Writes the word count, tf and the tfidf for each word in the url, and also writes the idfs for each word
				file = new File("pages" + File.separator + path + File.separator + "countAll");
				file.mkdir();
				HashMap<String,Integer> countAll = l.getCountAll();
				for (String word : countAll.keySet()) {
					out = new FileOutputStream("pages" + File.separator + path + File.separator + "countAll" + File.separator + word + ".txt");
					for (char c : (""+countAll.get(word)).toCharArray()) {
						out.write(c);
					}
					out.write(' ');

					for (char c :(""+getTfIdf(l,word)).toCharArray() ){
						out.write(c);
					}
					out.write(' ');

					for (char c :(""+getTf(l,word)).toCharArray() ){
						out.write(c);
					}
					out.close();

					file = new File("IDFs" + File.separator + word + ".txt");
					if (!file.exists()) {
						out = new FileOutputStream("IDFs" + File.separator + word + ".txt");
						for (char c : (""+getIdf(word, data.size())).toCharArray()) {
							out.write(c);
						}
						out.close();
					}

				}

				out = new FileOutputStream("pages" + File.separator + path + File.separator + "wordCount.txt");
				for (char c : (""+l.getWordCount()).toCharArray()) {
					out.write(c);
				}
				out.close();

				out = new FileOutputStream("pages" + File.separator + path + File.separator + "pageRank.txt");
				for (char c : (""+l.getPageRank()).toCharArray()) {
					out.write(c);
				}
				out.close();

				out = new FileOutputStream("pages" + File.separator + path + File.separator + "title.txt");
				for (char c : (""+l.getTitle()).toCharArray()) {
					out.write(c);
				}
				out.close();

			} catch (FileNotFoundException e) {
				System.out.println("" + l.getUrl() + " Not found");
			} catch (IOException e){
				System.out.println("" + l.getUrl() + " IOException");
			}
		}
	}
	public static void deleteFolder(File file){
		for (File f : file.listFiles()){
			if (f.isDirectory()){
				deleteFolder(f);
			}else{
				f.delete();
			}
		}
		file.delete();
	}
	public double getIdf(String word, Integer totalUrls){
		double counter;
		if (IDFs.containsKey(word)){
			counter = IDFs.get(word);
		}else{
			return 0.0;
		}
		return log2((double)totalUrls/(1+counter));
	}

	public double getTf(Link url, String word){
		if (!data.containsKey(url.getUrl())){
			return 0.0;
		}
		if (url.getCountAll().containsKey(word)){
			return (double)url.getCountAll().get(word)/(double)url.getWordCount();
		}
		return 0.0;
	}

	public double getTfIdf(Link url, String word){
		return log2(1.0 + getTf(url, word)) * getIdf(word, data.size());
	}

	public double dotProduct(ArrayList<Double> pi, ArrayList<Double> b){
		double sum = 0.0;
		for(int i = 0; i < pi.size(); i++){
			sum+= pi.get(i) * b.get(i);
		}
		return sum;
	}

	public double log2(double lognum){
		return Math.log(lognum) / Math.log(2);
	}

	public void createPageRanks(){
		ArrayList<ArrayList<Double>> matrix = new ArrayList<>();
		mapping = new ArrayList<>(data.values());

		int length = mapping.size();

		//For each Url
		for (int i = 0; i < length; i++){
			matrix.add(new ArrayList<Double>()); //Creates a new Arraylist (acts as a row)
			HashMap<String,Link> ogIndexes = new HashMap<>();
			for (Link l:data.get(mapping.get(i).getUrl()).getOutgoingLinks()){
				ogIndexes.put(l.getUrl(), l);
			}
			for (int j = 0; j <length; j++){
				if (ogIndexes.size() == 0){
					matrix.get(i).add( ((1.0/(double)length) * (1.0-ALPHA)) + (ALPHA/(double)length) );
				}else{
					if (ogIndexes.containsKey(mapping.get(j).getUrl())){
						matrix.get(i).add( ((1.0/ogIndexes.size()) * (1.0-ALPHA)) + (ALPHA/length));
					}else{
						matrix.get(i).add((ALPHA/length));
					}
				}
			}
		}

		ArrayList<Double> pi = new ArrayList<>();
		for (int i = 0; i <length;i++){
			pi.add(1.0/length);
		}
		double euclideanDistance = 1;

		double count = 0;
		while (euclideanDistance>=DISTANCE_THRESHOLD){
			count++;
			ArrayList<Double> newPi = new ArrayList<>();
			for (int i = 0; i < length;i++){
				ArrayList<Double> cols = new ArrayList<>();
				for (ArrayList<Double> j: matrix){
					cols.add(j.get(i));
				}
				newPi.add(dotProduct(pi,cols));
			}
			euclideanDistance = euclideanDistance(pi,newPi);
			pi = newPi;
		}
		pageRanks = pi;
	}
	public double euclideanDistance(ArrayList<Double> a, ArrayList<Double> b){
		double sum = 0;
		for (int i = 0; i < a.size(); i++){
			sum += Math.pow(a.get(i)- b.get(i),2);
		}
		return Math.sqrt(sum);
	}
}
