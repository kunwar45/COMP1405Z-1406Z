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
	

	public static void main(String[] args) {
		Crawler.crawl("http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html");
	}

	public static double log2(double lognum){
		return Math.log(lognum) / Math.log(2);
	}
}
