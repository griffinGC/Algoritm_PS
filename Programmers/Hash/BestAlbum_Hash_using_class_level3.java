package Programmers.Hash;

import java.util.*;

public class BestAlbum_Hash_using_class_level3 {
    static class Music {
        int plays;
        int id;
        String genres;

        public Music(int id, int plays, String genres) {
            this.id = id;
            this.plays = plays;
            this.genres = genres;
        }

        public void addPlays(int plays) {
            this.plays += plays;
        }

        public int getPlays() {
            return plays;
        }

        public int getId() {
            return id;
        }

        public String getGenres() {
            return genres;
        }
    }

    static int[] solution(String[] genres, int[] plays) {
        // 그냥 모든 albumList
        LinkedList<Music> albumList = new LinkedList<>();
        // 최초로 들어오는 원소들의 위치 필요
        // 들어오는 장르들에 대한 정렬이 필요 => 최초값과 누적 값을 정렬하는 것이 필요
        Map<String, Music> bigHit = new HashMap<>();
        for (int i = 0; i < genres.length; i++) {
            albumList.add(new Music(i, plays[i], genres[i]));
            if (bigHit.containsKey(genres[i])) {
                Music music = bigHit.get(genres[i]);
                music.addPlays(plays[i]);
                bigHit.put(genres[i], music);
            } else {
                bigHit.put(genres[i], new Music(i, plays[i], genres[i]));
            }
        }
        // 총 플레이 횟수와 장르, 최초 id를 가진 map이 bigHit
        Set<String> setList = bigHit.keySet();
        for (String st : setList) {
            Music mu = bigHit.get(st);
            System.out.println(mu.getGenres() + " / " + mu.getId() + " / " + mu.getPlays());
        }

        List<String> gSort = new ArrayList<>(bigHit.keySet());
        // 장르를 우선 정렬
        Collections.sort(gSort, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return bigHit.get(o2).getPlays() - bigHit.get(o1).getPlays();
            }
        });
        // 장르별로 정렬 완료
        System.out.println("gSort : " + gSort);
        // 장르별로 2곡 뽑기 2개를 뽑아온 것
        List<Integer> maxData = new ArrayList<>();
        // 각 장르에 대해서 계산
        for (int i = 0; i < gSort.size(); i++) {
            // 장르값 가져옴
            String nowGenre = gSort.get(i);
            List<Music> gList = new ArrayList<>();
            int aSize = albumList.size();
            for (int j = 0; j < albumList.size(); j++)
                // 모든 albumList에 대해서 genre가 같을때만 더해줌 => 모든 것들을 더해줌
                if (nowGenre.equals(albumList.get(j).getGenres())) {
                    gList.add(albumList.get(j));
//                        albumList.remove(j);
            }
            System.out.println("new begin");
            // gList에는 장르가 같은 모든 것들이 들어가 있음
            for (Music mu : gList) {
                System.out.println(mu.getGenres() + " / " + mu.getId() + " / " + mu.getPlays());
            }
            Collections.sort(gList, new Comparator<Music>() {
                @Override
                public int compare(Music o1, Music o2) {
                    return o2.getPlays() - o1.getPlays();
                }
            });
            for(int k = 0; k<2; k++){
                if(k<gList.size()){
                    maxData.add(gList.get(k).getId());
                }
            }
        }

        System.out.println(maxData);

        Integer[] temp = maxData.toArray(new Integer[maxData.size()]);
        int[] answer = Arrays.stream(temp).mapToInt(Integer::intValue).toArray();
//        System.out.println(answer);
        return answer;
    }


    public static void main(String[] args) {
//        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
//        int[] plays = {500, 600, 150, 800, 2500};
//        String[] genres = {"classic", "pop", "classic", "classic", "pop","d","d","d"};
//        int[] plays = {500, 600, 150, 800, 100,2000,1000,800};
        // 1번만 나온 경우
//        String[] genres = {"classic", "pop", "classic", "classic", "pop","d"};
//        int[] plays = {500, 600, 150, 800, 100,20 00};

        // 합이 같을 경우 => classic 이 작으므로 먼저 나와야 함
//        String[] genres = {"classic", "pop", "classic", "classic", "pop","d"};
//        int[] plays = {500, 600, 0, 200, 100,0};
        // 장르가 1개 밖에 없는 경우
        // result : [4, 1, 3, 0]

//        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
//        int[] plays = {500, 600, 501, 800, 900};

//        String[] genres = {"1","2","3","4","5","6"};
//        int[] plays = {1,2,3,4,5,6};


        String[] genres = {"a", "b", "a", "b", "c"};
        int[] plays = {100, 200, 300, 400, 500};
//            result: [3, 1, 4, 2, 0]
        System.out.println(Arrays.toString(solution(genres, plays)));
    }
}


