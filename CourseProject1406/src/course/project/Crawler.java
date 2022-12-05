package course.project;
import java.io.IOException;
import java.net.MalformedURLException;
import java.util.ArrayList;
import java.util.HashMap;

public class Crawler {
	private static HashMap<Link, Integer> data = new HashMap<Link, Integer>();
	private static HashMap<String, Double> IDFs = new HashMap<String, Double>();
	public static int crawl(String seed){
		ImprovedQueue queue = new ImprovedQueue(new Link(seed));
		Link url = queue.removestart();
//		System.out.println(url.getIncomingLinks().isem);

		int count = 1;
		while (true) {
			data = parse(url);

			for (Link outgoingLink: url.getOutgoingLinks()) {
					if (!queue.contains(outgoingLink) && outgoingLink.getOutgoingLinks() == null){
						queue.addend(outgoingLink);
					}
			}

			if (queue.size() == 0) {
				break;
			}

			url = queue.removestart();
			count+=1;


		}
		//Gets the mapping of the urls to the numbers as well as the pageranks, O(n^3)
		//    pageRanks,mapping = createPageRanks(data)

		//Adds the pageranks to the dictionary
		//    for rank in range(len(pageRanks)):
		//        data[mapping[rank]]["pageRank"] = pageRanks[rank]

		//Creates all the files for searchdata.py to use
		//    createFiles(data,IDFs)

		return count;
	}

	public static HashMap<Link, Integer> parse(Link url){
		data.putIfAbsent(url, 1);
		url.setOutgoingLinks(new ArrayList<Link>());
		String parsed = "";
		try {
			parsed = WebRequester.readURL("http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html");
//			System.out.println(parsed);
		}catch(MalformedURLException e){
			e.printStackTrace();
		}catch(IOException e){
			e.printStackTrace();
		}

		for (String s: parsed.split("/n")){
			System.out.println(s);

		}


		return data;
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
		if (!data.containsKey(url)){
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
			sum+= (double)pi.get(i) * (double)b.get(i);
		}
		return sum;
	}

	public static void main(String[] args) {
		Crawler.crawl("http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html");
	}

	public static double log2(double lognum){
		return Math.log(lognum) / Math.log(2);
	}

	public ArrayList<Object> createPageRanks(){
		double ALPHA = 0.1;
		double DISTANCE_THRESHOLD = 0.0001;
		ArrayList<ArrayList<Double>> matrix = new ArrayList<ArrayList<Double>>();
		ArrayList<Link> mapping = new ArrayList<Link>(data.keySet());

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

		ArrayList<Double> pi = new ArrayList<Double>();
		for (int i = 0; i <length;i++){
			pi.add(1.0/length);
		}
		double euclideanDistance = 1;

		double count = 0;
		while (euclideanDistance>=DISTANCE_THRESHOLD){
			count++;
			ArrayList<Double> newPi = new ArrayList<Double>();
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

	public ArrayList<ArrayList<Double>> multScalar(ArrayList<ArrayList<Double>> matrix, double scale){
		ArrayList<ArrayList<Double>> resultMatrix = new ArrayList<>();
		for (int i = 0; i < matrix.size(); i++){
			for (int j = 0; j <matrix.size(); j++){
				resultMatrix.get(i).set(j, matrix.get(i).get(j)*scale);
			}
		}
		return resultMatrix;
	}

	public ArrayList<ArrayList<Double>> multMatrix(ArrayList<ArrayList<Double>> a, ArrayList<ArrayList<Double>> b){
		ArrayList<ArrayList<Double>> resultMatrix = new ArrayList<>();
		if ((a.size() != b.get(0).size()) && (b.size()!= a.get(0).size())){
			return null;
		}
		double dotProduct = 0;
		for (int row = 0; row < a.size(); row++){
			for (int col = 0; col < b.get(0).size(); col++){
				for (int element = 0; element < a.get(row).size(); element++){
					dotProduct += a.get(row).get(element) * b.get(element).get(col);
				}
				resultMatrix.get(row).set(col,dotProduct);
				dotProduct = 0;
			}
		}
		return resultMatrix;
	}

	public double euclideanDistance(ArrayList<Double> a, ArrayList<Double> b){
		double sum = 0;
		for (int i = 0; i < a.size(); i++){
			sum += Math.pow(a.get(i)- b.get(i),2);
		}
		return Math.sqrt(sum);
	}


}
