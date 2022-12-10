package course.project;

import java.io.*;
import java.net.MalformedURLException;
import java.util.ArrayList;
import java.util.HashMap;

public class Crawler {
	private static HashMap<Link, Integer> data = new HashMap<>();
	private static HashMap<String, Double> IDFs = new HashMap<>();
	public static int crawl(String seed){
		ImprovedQueue queue = new ImprovedQueue(new Link(seed));
		Link url = queue.removestart();

		int count = 1;
		while (true) {
			System.out.println(queue);
			parse(url);

			for (Link outgoingLink: url.getOutgoingLinks()) {
				System.out.println(outgoingLink);
				if (!queue.contains(outgoingLink) && outgoingLink.getOutgoingLinks() == null){
					queue.addend(outgoingLink);
				}
			}
			if (queue.size() == 0) {
				break;
			}

			url = queue.removestart();
			count+=1;

			for (String word: url.getCountAll().keySet()){
				IDFs.putIfAbsent(word, IDFs.get(word)+1);
			}
		}

		ArrayList<Object> pageRankResult = createPageRanks();
		ArrayList<Double> pageRanks = (ArrayList<Double>) pageRankResult.get(0);
		ArrayList<Link> mapping = (ArrayList<Link>) pageRankResult.get(1);

		for (int i = 0; i < mapping.size(); i++) {
			mapping.get(i).setPageRank(pageRanks.get(i));
		}

		createFiles();
		return count;
	}

	public static void parse(Link url){
		data.putIfAbsent(url, 1);
		url.setOutgoingLinks(new ArrayList<Link>());
		String parsed = "";
		try {
			parsed = WebRequester.readURL(url.getUrl());
//			System.out.println(parsed);
		}catch(MalformedURLException e){
			e.printStackTrace();
		}catch(IOException e){
			e.printStackTrace();
		}

		String[] parsedArr = parsed.split("\n");
//		System.out.println(parsed);
//		System.out.println("The length of tedaf " + parsedArr.length);

		for (String s : parsedArr){
//			System.out.println(s);
			if (s.contains("title")){

				url.setTitle(s.substring(s.indexOf("<title>") + 7, s.indexOf("</title>")));
			} else if (s.contains("href")){
				Link outgoingLink;
				if (s.contains("http")){
					outgoingLink =  new Link(s.substring(s.indexOf("href") + 5, s.indexOf(">")));
				} else {

					outgoingLink = new Link(url.getRelativeLink()+s.substring((s.indexOf("./") + 1), s.indexOf(">")-1));
					System.out.println(outgoingLink.getUrl());
				}
				url.addOutgoingLink(outgoingLink);
				outgoingLink.addIncomingLink(url);
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

	public static void createFiles(){
		File file = new File("pages");
		if (file.exists()){
			deleteFolder(file);
		}
		file.mkdir();

		file = new File("IDFs");
		if (file.exists()){
			deleteFolder(file);
		}
		file.mkdir();

		for (Link l: data.keySet()){
			String path = l.getUrl().replace("/", "{").replace(":", "}").replace('.','(');
			file = new File("pages" + File.separator + path);
			file.mkdir();

			try {
				FileOutputStream out;
				out = new FileOutputStream("pages" + File.separator + path + File.separator + "outgoinglinks.txt");
				for (Link outgoingLink : l.getOutgoingLinks()) {
					out.write(' ');
					for (char c : outgoingLink.getUrl().toCharArray()) {
						out.write(c);
					}
				}
				out.close();

				out = new FileOutputStream("pages" + File.separator + path + File.separator + "incominglinks.txt");
				for (Link incominglink : l.getIncomingLinks()) {
					out.write(' ');
					for (char c : incominglink.getUrl().toCharArray()) {
						out.write(c);
					}
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
//
//				Scanner in = new Scanner(new FileReader("resources" + File.separator + "myAccount2.txt"));
//
//				String name = in.nextLine();
//				int acc = in.nextInt();
//				float bal = in.nextFloat();
//				aBankAccount = new BankAccount(name, bal, acc);
//
//				System.out.println(aBankAccount);
//				in.close();
//			} catch (FileNotFoundException e) {
//				System.out.println("Error: Cannot open file for reading");
//			} catch (NoSuchElementException e) {
//				System.out.println("Error: EOF encountered, file may be corrupt");
//			}
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

	public static double getIdf(String word, Integer totalUrls){
		double counter;
		if (IDFs.containsKey(word)){
			counter = IDFs.get(word);
		}else{
			return 0.0;
		}
		return log2((double)totalUrls/(1+counter));
	}

	public static double getTf(Link url, String word){
		if (!data.containsKey(url)){
			return 0.0;
		}
		if (url.getCountAll().containsKey(word)){
			return (double)url.getCountAll().get(word)/(double)url.getWordCount();
		}
		return 0.0;
	}

	public static double getTfIdf(Link url, String word){
		return log2(1.0 + getTf(url, word)) * getIdf(word, data.size());
	}

	public static double dotProduct(ArrayList<Double> pi, ArrayList<Double> b){
		double sum = 0.0;
		for(int i = 0; i < pi.size(); i++){
			sum+= pi.get(i) * b.get(i);
		}
		return sum;
	}

	public static void main(String[] args) {
		Crawler.crawl("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
	}

	public static double log2(double lognum){
		return Math.log(lognum) / Math.log(2);
	}

	public static ArrayList<Object> createPageRanks(){
		double ALPHA = 0.1;
		double DISTANCE_THRESHOLD = 0.0001;
		ArrayList<ArrayList<Double>> matrix = new ArrayList<>();
		ArrayList<Link> mapping = new ArrayList<>(data.keySet());

		int length = mapping.size();

		for (int i = 0; i < length; i++){
			matrix.add(new ArrayList<Double>());
			for (int j = 0; j <length; j++){
				ArrayList<Link> ogIndexes = mapping.get(i).getOutgoingLinks();
				if (ogIndexes.size() == 0){
					matrix.get(i).add( ((1.0/length) * (1.0-ALPHA)) + (ALPHA/(double)length) );
				}else{
					matrix.get(i).add( ogIndexes.contains(mapping.get(j)) ? ( ((1.0/ogIndexes.size()) * (1.0-ALPHA)) + (ALPHA/length)) : (ALPHA/length));
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

		ArrayList<Object> result = new ArrayList<>();
		result.add(pi);
		result.add(mapping);
		return result;

	}
	public static double euclideanDistance(ArrayList<Double> a, ArrayList<Double> b){
		double sum = 0;
		for (int i = 0; i < a.size(); i++){
			sum += Math.pow(a.get(i)- b.get(i),2);
		}
		return Math.sqrt(sum);
	}


}
