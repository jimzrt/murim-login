# Fidelity Gate — Chapter 131

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.
Do not invent `current` spans that are absent from the assembled English.
Do not report a glossary-correct rendering as a defect merely because the
baseline used an older synonym.

Return exactly one JSON object and no Markdown fence:

{
  "summary": "brief assessment",
  "findings": [
    {
      "id": "F01",
      "severity": "critical|major|minor",
      "source": "source location",
      "current": "exact uniquely occurring English span",
      "defect": "specific fidelity defect",
      "replacement": "finished replacement only when necessary",
      "rationale": "source-grounded reason",
      "confidence": 0.0
    }
  ]
}

Use an empty findings array when the chapter is faithful. A critical or major
finding blocks promotion; minor findings are recorded for human inspection.

## Korean source

```text
  1|＃131화
  2|
  3|
  4|
  5|“자, 갓 잡은 돼지가 한 근에 스무 푼! 싸다, 싸!”
  6|
  7|“어머, 어쩜 좋아. 가락지가 너무 잘 어울린다. 원래 은자 한 냥인데 손가락이 예쁘니까 반 냥. 어때?”
  8|
  9|“이 단환으로 말씀드릴 것 같으면, 한 알만 먹어도 정신이 맑아지고 힘이 불끈 솟는…….”
 10|
 11|거리는 끝없이 늘어선 가판과 시전 상인들의 쩌렁쩌렁한 외침으로 가득했다.
 12|
 13|사람들로 빽빽하게 채워진 태원(太原)의 거리를 본 나는 혀를 내둘렀다.
 14|
 15|‘사람 진짜 많네.’
 16|
 17|면면도 제법 다양하다. 저잣거리 상인들은 물론, 돌팔이 약장수와 매끄러운 비단옷을 걸친 자도 있고 궁기가 줄줄 흐르는 거지들도 있다.
 18|
 19|허리춤에 검을 패용한 무림인들도 심심찮게 보였지만 사람들은 별다른 관심을 보이지 않고 제 할 일을 계속했다.
 20|
 21|‘산서성의 성도(成都)라더니.’
 22|
 23|산서성에는 수십여 개의 현읍이 존재하지만, 그중에서도 태원이 차지하는 위치는 각별하다.
 24|
 25|여러 가지 이점을 가진 덕분에 까마득한 과거엔 어느 왕조(王朝)가 도읍으로 삼았던 적도 있단다.
 26|
 27|물론 그 왕조는 멸망한 지 오래지만, 그 후에도 태원은 발전을 거듭해 왔다……고 혁무진한테 들었다.
 28|
 29|‘그게 태원진가가 삼백 년을 버틸 수 있었던 이유겠지.’
 30|
 31|풍부한 물자와 인력. 그리고 경제력.
 32|
 33|생각해 보면 웬 망나니 하나가 가문 공금을 털어 기루에 죄다 쏟아부었는데도 항산검문과 전쟁을 치를 여력은 남아 있었다.
 34|
 35|태원진가가 아니라 항산진가였다면 이미 오래전에 쪽박 차고 거리로 나앉았을 거다.
 36|
 37|
 38|
 39|‘태원진가의 땅을 밟지 않고서는 태원을 지나갈 수 없다.’
 40|
 41|
 42|
 43|언젠가 들었던 말을 떠올리는 내게 혁무진이 물었다.
 44|
 45|“무슨 생각을 그렇게 하세요?”
 46|
 47|“땅 투기가 좋긴 좋구나. 뭐 그런 생각.”
 48|
 49|“예?”
 50|
 51|“그런 게 있어. 넌…….”
 52|
 53|“몰라도 된다고요?”
 54|
 55|“잘 아네.”
 56|
 57|“그 말도 이제 지겹습니다.”
 58|
 59|“그래, 나도 너 지겹다.”
 60|
 61|“그럼 절 왜 데려오셨습니까?”
 62|
 63|“입은 비뚤어져도 말은 바로 하자. 내가 데려온 게 아니라 큰형님이 붙여 준 거야.”
 64|
 65|진위경은 내일 있을 산서 성주와의 오찬에 대비해 나를 먼저 보냈다. 아무래도 변덕이 심한 어린아이니 별다른 잡음 없이 최대한 맞춰 주려는 의도 같다.
 66|
 67|아무튼, 그 때문에 혁무진이 나와 동행했다. 태원 토박이인 녀석은 여러모로 수행원으로서 안성맞춤이었다.
 68|
 69|“그러고 보니까 여기가 네 고향 아니냐?”
 70|
 71|“고향이라, 그렇죠.”
 72|
 73|혁무진이 복잡한 눈빛으로 거리를 응시했다.
 74|
 75|“고작 오 년밖에 안 지났는데…… 참 많이 바뀌었네요.”
 76|
 77|“중간중간 몇 번은 들렀을 것 아냐.”
 78|
 79|“아뇨. 그동안 한 번도 안 들렀는데요.”
 80|
 81|뜻밖의 이야기에 깜짝 놀랐다.
 82|
 83|“오 년 동안 단 한 번도?”
 84|
 85|“제가 무공을 좀 늦게 시작했거든요. 다른 사람들을 따라잡으려면 별수 있겠습니까. 열 배, 스무 배로 노력하는 수밖에요.”
 86|
 87|“으음.”
 88|
 89|“이렇게 돌아올 줄은 몰랐습니다.”
 90|
 91|오랜만에 아니, 거의 처음 보는 진지한 모습이다.
 92|
 93|생각해 보면 혁무진 이 녀석은 매사에 실없이 굴어도 나름 한가락 하는 일류 고수였다. 워낙 주위에 괴물들이 득실거려서 그렇지, 결코 낮은 경지가 아니다.
 94|
 95|그만큼 피나는 노력이 뒷받침되었기에 가능한 일이었겠지. 거기에 더해서…….
 96|
 97|‘재능도 있는 편인 것 같고.’
 98|
 99|
100|
101|[Lv.48 혁무진]
102|
103|
104|
105|빠른 속도로 쑥쑥 올라가는 레벨이 그 증거다.
106|
107|이 녀석, 이러다가 갑자기 절정 고수라도 되는 거 아냐?
108|
109|내 새삼스러운 시선에도 오랜만에 고향을 방문한 혁무진은 감상에 젖어 있기 바빴다.
110|
111|“아, 저 아주머니 아직도 계시네.”
112|
113|반가우면서도 아련한 목소리다.
114|
115|혁무진이 손을 들어 가리킨 곳에는 머리가 희끗희끗한 중년 여인이 작은 좌판 앞에서 각종 군것질거리를 팔고 있었다.
116|
117|“혹시 빙당호로(冰糖葫芦) 좋아하세요?”
118|
119|평소였으면 헛소리 그만하고 갈 길이나 가자고 했겠지만 어째 분위기가 심상찮다. 나는 최대한 친절하게 대꾸했다.
120|
121|“태어나서 한 번도 안 먹어 봤어.”
122|
123|“어릴 때는 빙당호로가 그렇게 먹고 싶더라고요. 좌판 앞에 쭈그려 앉아서 손가락만 빨고 있으면 아주머니께서 한두 개씩 쥐여 주셨죠.”
124|
125|혁무진이 씁쓸하게 웃으며 말을 이었다.
126|
127|“그럴 때마다 다른 아이들이 얼마나 부러웠는지 모릅니다. 하나같이 부모님 손을 꼭 잡고 와서 빙당호로며 당과를 사서 저잣거리를 돌아다니던 그 모습…… 아직도 눈에 선해요.”
128|
129|이 분위기를 어떻게 해야 하나.
130|
131|어느 정도 사연이 있을 거라고는 생각했지만 이야기가 이렇게 흘러갈 거라고는 예상치 못했다.
132|
133|‘오 년 만에 왔다는 것부터 눈치챘어야 했는데.’
134|
135|이곳, 무림에는 유난히 고아가 많다. 당장 주변만 둘러봐도 저잣거리에 꾀죄죄한 누더기를 걸치고 돌아다니는 어린아이들을 쉽게 발견할 수 있으니까.
136|
137|‘아마 녀석도 비슷한 처지였겠지.’
138|
139|가족이 없으니 돌아올 이유도 없다. 와 봐야 빙당호로가 먹고 싶어 좌판 앞을 서성이던 어린 시절의 아픈 기억만 떠오를 뿐이다.
140|
141|그래서 수련으로 그 아픔을 잊으려 한 것일지도 모른다.
142|
143|녀석에게는 태원진가가 집이고 동료들이 가족이었던 거다.
144|
145|‘그것도 모르고…… 내가 그동안 너무 함부로 대했어.’
146|
147|젠장, 괜히 코끝이 찡해진다.
148|
149|이런 내 변화를 혁무진은 금방 알아차렸다.
150|
151|“왜 그러세요?”
152|
153|“아니, 그냥. 오늘 미세먼지가 심해서 그런가, 코가 간질간질하네.”
154|
155|“미세먼지요?”
156|
157|“그건 넘어가고, 빙당호로나 하나씩 먹을까?”
158|
159|“객잔부터 미리 들르는 게 좋을 것 같은데요. 해 떨어지기 전에 객실을 잡아 놓지 않으면 자리가 없어서.”
160|
161|“야, 저거 하나 먹는 데 뭐 얼마나 걸린다고 그래. 그렇게 비싼 것도 아니고. 어차피 경비도 넉넉하게 받았을 거 아냐?”
162|
163|“그건 그렇죠.”
164|
165|“이참에 먹고 싶은 거 다 먹고 실컷 놀다 가자. 너 어렸을 때 저 아주머니한테 얻어먹은 것도 갚을 겸 매상 잔뜩 올려 드려.”
166|
167|“필요한 곳에 쓰라고 주신 경비를 이렇게 써도 될지…….”
168|
169|“써, 다 써. 나중에 뭐라 하는 놈 있으면 나한테 데려와.”
170|
171|“이공자님이 뭐라고 하시면요?”
172|
173|“……그 인간은 빼고 데려와.”
174|
175|혁무진이 피식 웃더니 한층 밝아진 목소리로 말했다.
176|
177|“그럼 빙당호로나 하나씩 먹을까요?”
178|
179|“그래, 아까부터 보고 있으니까 침 고인다.”
180|
181|다분하게 혁무진을 의식한 말이다. 내일모레면 서른인데 과일 사탕 따위에 침이 고이긴 무슨.
182|
183|‘이렇게라도 기분이 좋아지면 된 거지.’
184|
185|저 녀석도 그동안 나 따라다니느라 고생 많았다. 틈만 나면 구박받고, 얻어맞고, 퀘스트만 했다 하면 괴물 같은 놈들만 만나는 바람에 죽을 고비도 여러 번 넘겼다.
186|
187|혁무진과의 첫 만남은 분명 악연이었지만 이제는 아니다.
188|
189|“야, 무진아.”
190|
191|막 좌판을 향해 걸어가려던 혁무진이 멈칫했다.
192|
193|“예? 왜요?”
194|
195|“그…….”
196|
197|앞으로도 잘 부탁한다는 말이 혀끝에서 맴돈다. 젠장, 시커먼 두 사내놈이 주고받기에는 너무 간질거리는 말이다.
198|
199|고민 끝에 결국 엉뚱한 소리만 툭 튀어나왔다.
200|
201|“각자 두 개씩 먹자. 큰 걸로.”
202|
203|“아, 예.”
204|
205|괜히 부끄러워서 먼 산을 바라보는 내 귓가로 혁무진과 중년 여인의 대화가 흘러들어 왔다.
206|
207|“어머! 너 무진이 아니니? 혁무진. 맞지?”
208|
209|“오랜만에 뵙습니다. 아주머니.”
210|
211|“세상에, 맞네. 맞아. 하마터면 못 알아볼 뻔했다, 얘.”
212|
213|“아주머니는 여전하신데요.”
214|
215|“호호호, 말이라도 고맙네. 무진이 너는 잘 지내고? 듣기로는 무인이 됐다던데.”
216|
217|“예. 태원진가 소속입니다. 곧 수문각주로 승진해요.”
218|
219|“태, 태원진가? 수문각주? 세상에, 세상에…….”
220|
221|수문각주로 승진할지 말지는 두고 봐야 알겠지만 절로 흐뭇한 미소가 지어지는 대화다.
222|
223|‘무슨 라디오 사연 같네.’
224|
225|늘 주위를 맴도는 고아 아이에게 빙당호로를 건네주곤 했던 맘씨 좋은 아주머니. 곤궁했던 어린 시절을 보낸 아이는 피나는 노력 끝에 마침내 성공하여 훌쩍 장성한 모습으로 돌아와 재회한다.
226|
227|어디선가 한 번쯤 들어 본 이야기지만 감동적이라는 사실은 변함이 없다.
228|
229|“크흠, 이거 참, 눈에 뭐가 들어갔나…….”
230|
231|이건 황사인가 미세먼지인가. 아직 공장은 안 세웠을 테니 황사겠지.
232|
233|나도 모르게 눈시울이 살짝 붉어진 그 순간이었다.
234|
235|“그래, 부모님은 찾아뵈었고?”
236|
237|“아직요. 오늘이나 내일쯤에 한 번 들러볼 생각입니다.”
238|
239|“빨리 가 봐라. 너희 집 이사 간 건 아니?”
240|
241|“이사요? 어디로요?”
242|
243|“저쪽 대로변에 큰 장원으로 갔다. 연못에 비단잉어도 풀어 놓고 키우더라.”
244|
245|“아, 그래요?”
246|
247|“……?”
248|
249|부모님? 이사? 커다란 장원에 비단잉어?
250|
251|잠깐. 이거 뭔가 이상한데. 황당해진 나는 빙당호로를 들고 돌아오는 혁무진에게 물었다.
252|
253|“무슨 소리야?”
254|
255|“예? 뭐가요?”
256|
257|“너희 부모님 살아 계셔?”
258|
259|혁무진이 나를 미친놈처럼 바라보았다.
260|
261|“멀쩡한 부모님을 왜 죽입니까?”
262|
263|“아니 그게 아니고…… 그럼 아까 했던 말은 뭔데.”
264|
265|“무슨 말이요?”
266|
267|“빙당호로. 그거 못 먹어서 맨날 손가락 쪽쪽 빨았다며?”
268|
269|“못 먹었죠. 부모님이 이빨 썩는다고 못 먹게 했어요. 여기 상인분들이야 저희 부모님 성격 극성인 거 다 아니까 일부러 저한테만 안 팔았는데, 저분만 몰래 하나씩 챙겨 주셨고.”
270|
271|“……부모님 손 잡고 다니는 애들 부러웠다는 건?”
272|
273|“저희 집 장사가 워낙 잘돼서 시간이 안 나시더라고요. 혼자 놀았죠, 뭐.”
274|
275|“그, 그럼 태원에 가족이 있으면서 오 년 동안 한 번도 안 왔다고?”
276|
277|“집 나왔어요. 가업 물려받기 싫어서 편지 한 통 남기고. 본가 수문각주님이 저희 아버지 불알친구라 제 근황은 다 알고 계셨을 겁니다.”
278|
279|“…….”
280|
281|“한 이 년 동안은 엄청 뭐라 하셨는데, 갑자기 막둥이가 태어나서 제가 가업을 이을 필요가 없어지니까 그 후부터는 별말씀 안 하시던데요?”
282|
283|목을 길게 빼고 두리번거리던 혁무진이 손을 들어 뭔가를 가리켰다.
284|
285|“아, 저기 있다. 보이시죠? 저 건물이 저희 부모님 건데…… 저 없는 동안 더 커졌네요.”
286|
287|나는 혁무진의 손가락을 따라 고개를 돌렸다.
288|
289|우뚝 솟은 거대한 5층짜리 전각과 커다란 글씨로 쓰인 현판이 눈에 들어온다.
290|
291|
292|
293|[혁가 포목점]
294|
295|
296|
297|혁무진은 뿌듯하게 웃었다.
298|
299|“태원에서 가장 큰 포목점입니다. 하남과 하북에 지점도 있어요.”
300|
301|이 새끼도 금수저구나…….
302|
303|이렇게 살벌한 동네에서 체인점까지 낼 정도면 말 다 했다.
304|
305|‘내가 뭘 한 거냐.’
306|
307|빙당호로가 먹고 싶어서 손가락 쪽쪽 빨던 어린 소년?
308|
309|실상은 성공한 사업가 부모님이 아들놈 치아 건강을 생각해서 못 먹게 한 거였다.
310|
311|‘아니 시벌, 이게 무슨.’
312|
313|입만 벌린 채 서 있는 내게 혁무진이 손에 든 빙당호로를 건넸다.
314|
315|“자, 하나 드세요. 제가 특별히 가장 크고 영롱한 걸로 골랐습니다. 이 근방에서는 저분이 파시는 빙당호로가 최고예요.”
316|
317|“이런 호로색…….”
318|
319|목구멍까지 솟구치는 욕을 꿀꺽 삼키고 빙당호로를 까드득 깨물었다.
320|
321|“이제 빨리 객실이나 잡으러 가자.”
322|
323|“벌써요? 이제 겨우 철전 몇 푼 썼는데…….”
324|
325|“마! 그게 네 돈이야? 필요할 때 쓰라고 준 경비잖아, 경비!”
326|
327|“아니, 방금은 실컷 쓰고 놀다 가자면서요?”
328|
329|“이 정도면 놀 만큼 놀았어. 해 떨어지면 객실 찬다며. 오늘 잠자리가 뒤숭숭해서 내일 오찬에 늦으면 네가 책임질래?”
330|
331|“…….”
332|
333|
334|
335|* * *
336|
337|
338|
339|홍화객잔.
340|
341|현판에 적힌 객잔 이름에서 알 수 있듯 이곳은 하오문의 손이 뻗친 곳 중 하나였다.
342|
343|‘밤에는 홍화루. 숙박은 홍화객잔이라.’
344|
345|거, 누구 생각인지 취객들 등골까지 뽑아 먹으려고 작정을 했구먼.
346|
347|“들어가자.”
348|
349|아까부터 주둥이가 댓 발 나온 혁무진을 데리고 객잔 입구를 향해 다가가려던 그때였다.
350|
351|“저어, 죄송합니다만.”
352|
353|그건 묘하게 신경을 잡아당기는 목소리였다. 꿈꾸는 듯 몽롱하고, 어린아이처럼 천진난만한 목소리의 주인은 서글서글한 인상의 청년이었다.
354|
355|‘이 느낌은…….’
356|
357|돌아서서 그의 맑은 눈동자를 마주 본 순간, 나도 모르게 숨이 막혔다.
358|
359|그건 진무경과는 다른 종류의 기세였다.
360|
361|
362|
363|[Lv.??? 청풍]
364|
365|
366|
367|또 다른 절정 고수의 등장. 긴장감 속에서 청년, 청풍의 입술이 열렸다.
368|
369|“실례가 안 된다면 빙당호로 하나만 먹어도 되겠습니까?”
370|
371|“……?”
372|
373|이건 또 뭐 하는 새끼냐.
```

## Assembled English

```markdown
[P1]
# Chapter 131

[P2]
“Fresh-killed pork, twenty coins per geun! Cheap, cheap!”

[P3]
“Oh my, that ring looks perfect on you. It’s normally one silver nyang, but since your fingers are so pretty, I’ll let you have it for half a nyang. What do you say?”

[P4]
“As for this pill, just one will clear your mind and fill you with strength…”

[P5]
The streets were packed with endless rows of stalls and the booming cries of merchants.

[P6]
When I saw the crowded streets of Taiyuan, I clicked my tongue in amazement.

[P7]
*There are a hell of a lot of people.*

[P8]
There was quite a variety among them, too. There were not only street vendors, but also quack medicine sellers, people dressed in smooth silk, and beggars whose poverty practically poured off them.

[P9]
Martial artists with swords at their waists were also a common sight, but no one paid them any particular attention. Everyone simply went about their business.

[P10]
*So this is the capital of Shanxi Province.*

[P11]
Shanxi Province had dozens of counties and towns, but Taiyuan held a special place among them.

[P12]
Thanks to its many advantages, it had once served as the capital of a dynasty in the distant past.

[P13]
That dynasty had fallen long ago, of course, but Taiyuan had continued to develop afterward…

[P14]
Or so Hyuk Mujin had told me.

[P15]
*That must be why the Jin Family of Taiyuan has managed to survive for three hundred years.*

[P16]
Abundant supplies and manpower. And economic power.

[P17]
Come to think of it, even after one worthless son raided the family coffers and blew it all at a pleasure house, they still had enough left to wage war against the Mount Heng Sword Sect.

[P18]
If they had been the Jin Family of Mount Heng instead of the Jin Family of Taiyuan, they would have gone bankrupt and ended up on the streets long ago.

[P19]
*You can’t pass through Taiyuan without setting foot on the Jin Family of Taiyuan’s land.*

[P20]
As I recalled the saying, Hyuk Mujin asked, “What are you thinking about so hard?”

[P21]
“Just that land speculation really pays off.”

[P22]
“What?”

[P23]
“It’s nothing. You…”

[P24]
“Don’t need to know?”

[P25]
“You catch on fast.”

[P26]
“I’m getting tired of hearing that.”

[P27]
“Yeah, I’m getting tired of you, too.”

[P28]
“Then why did you bring me?”

[P29]
“Let’s get the facts straight. I didn’t bring you. Eldest Brother assigned you to me.”

[P30]
Jin Wikyung had sent me ahead to prepare for tomorrow’s luncheon with Shanxi’s City Lord. The City Lord was a temperamental child, so Wikyung probably wanted us to accommodate him as much as possible and avoid any trouble.

[P31]
In any case, that was why Hyuk Mujin was traveling with me. As a native of Taiyuan, he was an ideal attendant in many ways.

[P32]
“Come to think of it, isn’t this your hometown?”

[P33]
“My hometown… Yes, it is.”

[P34]
Hyuk Mujin stared at the streets with a complicated look in his eyes.

[P35]
“It’s only been five years, but so much has changed.”

[P36]
“You must’ve stopped by a few times in between.”

[P37]
“No. I haven’t been back once.”

[P38]
His unexpected answer caught me by surprise.

[P39]
“Not even once in five years?”

[P40]
“I started learning martial arts rather late. If I wanted to catch up with everyone else, I had no choice but to work ten or twenty times harder.”

[P41]
“Hmm.”

[P42]
“I never thought I’d come back like this.”

[P43]
It was the first time in a long while—no, almost the first time ever—that I had seen him look so serious.

[P44]
Come to think of it, Hyuk Mujin might fool around constantly, but he was still a capable First Rate master. He only seemed unimpressive because he was surrounded by monsters. His realm was by no means low.

[P45]
He could never have reached it without working himself to the bone. And on top of that…

[P46]
*He seems to have some talent, too.*

[P47]
> **System**
>
> **Level:** 48  
> **Name:** Hyuk Mujin

[P48]
His rapidly rising Level was proof enough.

[P49]
*At this rate, is he going to become a Peak master before I know it?*

[P50]
Despite my newly appreciative gaze, Hyuk Mujin was too absorbed in the emotions of returning to his hometown after so long.

[P51]
“Ah, that auntie is still here.”

[P52]
His voice was happy, yet wistful.

[P53]
He pointed to a gray-streaked middle-aged woman selling all kinds of snacks from a small stall.

[P54]
“Do you like candied hawthorn skewers?”[^1]

[P55]
Normally, I would have told him to stop talking nonsense and keep moving, but the mood was unusual. I answered as kindly as I could.

[P56]
“I’ve never had one in my life.”

[P57]
“When I was little, I wanted them so badly. Whenever I crouched in front of her stall and sucked on my fingers, that auntie would give me one or two.”

[P58]
Hyuk Mujin continued with a bitter smile.

[P59]
“You have no idea how jealous I was of the other children. They’d come holding their parents’ hands, buy candied hawthorn and sweets, and wander around the market… I can still picture it.”

[P60]
What was I supposed to do with this mood?

[P61]
I had figured there must be a story behind him, but I hadn’t expected it to take this turn.

[P62]
*I should’ve known when he said he hadn’t come back in five years.*

[P63]
There were an unusually large number of orphans in the Murim. Even looking around us, it was easy to find children wandering through the market in filthy rags.

[P64]
*He must have been in a similar situation.*

[P65]
With no family, he had no reason to return. Coming back would only stir up painful memories of lingering outside the stall as a child, longing for candied hawthorn.

[P66]
Maybe that was why he had tried to forget his pain through training.

[P67]
For him, the Jin Family of Taiyuan had been home, and his companions had been his family.

[P68]
*And without knowing any of that… I’ve been treating him far too harshly.*

[P69]
Damn it. The tip of my nose was starting to sting for no reason.

[P70]
Hyuk Mujin immediately noticed the change in me.

[P71]
“What’s wrong?”

[P72]
“No, it’s nothing. Maybe the fine dust is especially bad today. My nose feels itchy.”

[P73]
“Fine dust?”

[P74]
“Never mind that. Why don’t we get a candied hawthorn skewer each?”

[P75]
“Wouldn’t it be better to find an inn first? If we don’t get a room before the sun goes down, there may not be any left.”

[P76]
“Hey, how long does it take to eat one of those? They’re not even that expensive. We were given plenty of travel expenses, weren’t we?”

[P77]
“That’s true.”

[P78]
“Let’s eat whatever we want and have all the fun we can before we leave. You can pay that auntie back for the treats she gave you by giving her plenty of business.”

[P79]
“I’m not sure we should spend money meant for necessities like this…”

[P80]
“Spend it. Spend all of it. If anyone complains later, bring them to me.”

[P81]
“What if the Second Young Master complains?”

[P82]
“…Bring me anyone except him.”

[P83]
Hyuk Mujin let out a short laugh before speaking in a much brighter voice.

[P84]
“Then shall we get a skewer each?”

[P85]
“Sure. I’ve been looking at them for a while, and they’re making my mouth water.”

[P86]
I said it entirely for Hyuk Mujin’s benefit. I was almost thirty. Why would fruit candy make my mouth water?

[P87]
*As long as it cheers him up.*

[P88]
That guy had suffered plenty while following me around. He was constantly berated and beaten, and every time we took on a Quest, we ended up meeting nothing but monsters. He had come close to dying more than once.

[P89]
My first meeting with Hyuk Mujin had certainly been an ill-fated one, but that was no longer true.

[P90]
“Hey, Mujin.”

[P91]
Hyuk Mujin, who had just started walking toward the stall, stopped short.

[P92]
“Yes? What is it?”

[P93]
“Well…”

[P94]
The words *I’m counting on you from here on out* hovered on the tip of my tongue. Damn it. That was much too sappy for two grown men to say to each other.

[P95]
After agonizing over it, I blurted out something completely different.

[P96]
“Let’s get two each. The big ones.”

[P97]
“Oh. Yes.”

[P98]
Too embarrassed to look at him, I gazed off at a distant mountain. Hyuk Mujin’s conversation with the middle-aged woman drifted to my ears.

[P99]
“Oh my! Aren’t you Mujin? Hyuk Mujin, right?”

[P100]
“It’s been a long time, Auntie.”

[P101]
“My goodness, it is you. It is! I almost didn’t recognize you, child.”

[P102]
“You haven’t changed at all, Auntie.”

[P103]
“Ho-ho-ho. That’s kind of you to say. Have you been well, Mujin? I heard you became a martial artist.”

[P104]
“Yes. I belong to the Jin Family of Taiyuan. I’ll be promoted to Master of the Gatekeeper Pavilion soon.”

[P105]
“T-the Jin Family of Taiyuan? Master of the Gatekeeper Pavilion? My goodness, my goodness…”

[P106]
Whether he would actually be promoted remained to be seen, but their conversation brought a pleased smile to my face.

[P107]
*This sounds like a radio call-in story.*

[P108]
A kindhearted auntie who used to give candied hawthorn to an orphan boy who lingered around her stall. After a childhood of hardship and years of grueling effort, the boy finally found success and returned as a strapping young man.

[P109]
It was a story I had heard somewhere before, but that didn’t make it any less moving.

[P110]
“Ahem. What is this? Did something get in my eye?”

[P111]
Was it yellow dust or fine dust? They couldn’t have built any factories yet, so it must have been yellow dust.

[P112]
That was when the rims of my eyes reddened slightly despite myself.

[P113]
“So, have you gone to see your parents?”

[P114]
“Not yet. I was thinking of stopping by today or tomorrow.”

[P115]
“Go see them soon. Didn’t your family move?”

[P116]
“Moved? Where?”

[P117]
“To a large estate along the main road over there. They even released koi into the pond and raised them.”

[P118]
“Oh, really?”

[P119]
“…?”

[P120]
Parents? Moving? A huge estate with koi?

[P121]
Wait. Something wasn’t right.

[P122]
I stared dumbfoundedly at Hyuk Mujin as he returned carrying the candied hawthorn skewers.

[P123]
“What was that about?”

[P124]
“Huh? About what?”

[P125]
“Your parents are alive?”

[P126]
Hyuk Mujin stared at me as though I were insane.

[P127]
“Why are you killing off my perfectly healthy parents?”

[P128]
“No, that’s not what I meant… Then what was all that stuff you said earlier?”

[P129]
“What stuff?”

[P130]
“The candied hawthorn. You said you couldn’t have any and spent every day sucking on your fingers.”

[P131]
“I couldn’t have any. My parents wouldn’t let me eat it because they said it would rot my teeth. Every merchant around here knew how overbearing my parents were, so they made a point of refusing to sell any to me. That lady was the only one who secretly slipped me some.”

[P132]
“…”

[P133]
“And what about being jealous of the children holding their parents’ hands?”

[P134]
“My family’s business was so successful that they never had any free time. I played by myself.”

[P135]
“Th-then you had family in Taiyuan, but you didn’t come back once in five years?”

[P136]
“I left home. I didn’t want to inherit the family business, so I left a single letter behind and ran away. The Master of the Gatekeeper Pavilion in our family is my father’s childhood best friend, so he probably knew everything about how I was doing.”

[P137]
“…”

[P138]
“For about two years, they gave me hell over it. Then my youngest sibling was suddenly born, so I no longer needed to inherit the family business. After that, they stopped saying much.”

[P139]
Hyuk Mujin craned his neck and looked around, then raised a hand and pointed.

[P140]
“Ah, there it is. See it? That building belongs to my parents… It got even bigger while I was away.”

[P141]
I followed Hyuk Mujin’s finger and turned my head.

[P142]
A huge, towering five-story pavilion and a signboard bearing enormous characters came into view.

[P143]
**Hyuk Family Textile Shop**

[P144]
Hyuk Mujin smiled proudly.

[P145]
“It’s the largest textile shop in Taiyuan. We have branches in Henan and Hebei, too.”

[P146]
*This bastard was born with a silver spoon, too…*

[P147]
You had to be pretty damn wealthy to open chain stores in a place this rough.

[P148]
*What the hell have I been doing?*

[P149]
A young boy who used to suck on his fingers because he wanted to eat candied hawthorn so badly?

[P150]
The truth was that his successful business-owner parents had forbidden him from eating it because they were worried about his teeth.

[P151]
*What the fuck is this?*

[P152]
As I stood there with my mouth hanging open, Hyuk Mujin held out one of the candied hawthorn skewers.

[P153]
“Here, have one. I specially chose the biggest and shiniest one. The ones that lady sells are the best in this area.”

[P154]
“You son of a…”

[P155]
I swallowed the curse that had surged up to my throat and bit down on the candied hawthorn with a loud crunch.

[P156]
“Let’s hurry up and find a room.”

[P157]
“Already? We’ve only spent a few iron coins…”

[P158]
“Hey! Is it your money? Those are travel expenses we were given to spend when necessary. Expenses!”

[P159]
“Didn’t you just say we should spend it all and have fun?”

[P160]
“We’ve had enough fun. You said the rooms would fill up after sunset. If we get a bad night’s sleep and end up late to tomorrow’s luncheon, are you going to take responsibility?”

[P161]
“…”

[P162]
* * *

[P163]
Honghwa Inn.

[P164]
As its signboard suggested, this was one of the establishments under the Lower District Sect’s influence.

[P165]
*Honghwaru at night. Honghwa Inn for lodging.*

[P166]
Whoever had come up with that arrangement was clearly determined to wring every last coin out of the drunks.

[P167]
“Let’s go in.”

[P168]
I was about to lead Hyuk Mujin, whose lower lip had been jutting out for some time, toward the inn’s entrance when someone spoke.

[P169]
“Excuse me. I’m sorry to bother you.”

[P170]
The voice strangely tugged at my nerves. Its owner was a young man with an affable expression and a dreamy, hazy voice as innocent as a child’s.

[P171]
*This feeling…*

[P172]
The moment I turned around and met his clear eyes, my breath caught despite myself.

[P173]
This was an aura different from Jin Mukyung’s.

[P174]
> **System**
>
> **Level:** ???  
> **Name:** Cheongpung

[P175]
Another Peak master had appeared.

[P176]
Amid the tension, the young man named Cheongpung opened his lips.

[P177]
“If you don’t mind, may I eat just one candied hawthorn skewer?”

[P178]
“…?”

[P179]
*What the hell is this guy?*

[P180]
[^1]: Candied hawthorn skewers are a traditional snack made by coating skewered fruit in hardened sugar.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source, RULES.md, or the exact
glossary requires the change. Exact glossary English wins over an older baseline
synonym for the same Korean key.

```markdown
[P1]
# Chapter 131

[P2]
“Fresh-killed pork, twenty coins per geun! Cheap, cheap!”

[P3]
“Oh my, what should I do? That ring suits you perfectly. It’s normally one nyang of silver, but you have such pretty fingers, so I’ll give it to you for half a nyang. What do you say?”

[P4]
“If I may say so, this pill will clear your mind and fill you with strength after just one dose…”

[P5]
The streets were filled with endless rows of stalls and the booming cries of market merchants.

[P6]
When I saw the crowded streets of Taiyuan, I clicked my tongue in amazement.

[P7]
*There are a hell of a lot of people.*

[P8]
There was quite a variety among them, too. There were not only street vendors, but also quack medicine sellers, people dressed in smooth silk, and beggars whose poverty practically poured off them.

[P9]
Martial artists wearing swords at their waists were easy enough to spot, but no one paid them any particular attention. Everyone simply continued with whatever they were doing.

[P10]
*So this is the capital of Shanxi Province.*

[P11]
Shanxi Province had dozens of counties and towns, but Taiyuan held a particularly important position among them.

[P12]
Thanks to its many advantages, it had once served as the capital of a dynasty in the distant past.

[P13]
That dynasty had fallen long ago, of course, but Taiyuan had continued to develop afterward…

[P14]
At least, that was what Hyuk Mujin had told me.

[P15]
*That must be why the Jin Family of Taiyuan has managed to survive for three hundred years.*

[P16]
Abundant supplies and manpower. And economic power.

[P17]
Come to think of it, even after some worthless son had plundered the family treasury and dumped all of it into a pleasure house, they had still possessed enough strength to go to war with the Mount Heng Sword Sect.

[P18]
If they had been the Jin Family of Mount Heng instead of the Jin Family of Taiyuan, they would have gone bankrupt and ended up on the streets long ago.

[P19]
*You can’t pass through Taiyuan without setting foot on the Jin Family of Taiyuan’s land.*

[P20]
As I recalled something I had heard long ago, Hyuk Mujin asked,

[P21]
“What are you thinking about so seriously?”

[P22]
“Land speculation is pretty great. That’s what I was thinking.”

[P23]
“What?”

[P24]
“It’s nothing. You…”

[P25]
“I don’t need to know?”

[P26]
“You catch on quickly.”

[P27]
“I’m getting tired of hearing that.”

[P28]
“Yeah, I’m getting tired of you, too.”

[P29]
“Then why did you bring me along?”

[P30]
“Let’s at least get the facts straight. I didn’t bring you. The eldest brother assigned you to me.”

[P31]
Jin Wikyung had sent me ahead in preparation for tomorrow’s luncheon with Shanxi’s City Lord. I assumed he wanted to accommodate the capricious child as much as possible without causing any trouble.

[P32]
In any case, that was why Hyuk Mujin was traveling with me. As a native of Taiyuan, he was an ideal attendant in many ways.

[P33]
“Come to think of it, isn’t this your hometown?”

[P34]
“My hometown… Yes, it is.”

[P35]
Hyuk Mujin stared at the streets with complicated emotions in his eyes.

[P36]
“It’s only been five years, but so much has changed.”

[P37]
“You must have stopped by a few times in between.”

[P38]
“No. I haven’t visited even once during that time.”

[P39]
I was startled by the unexpected answer.

[P40]
“Not even once in five years?”

[P41]
“I started learning martial arts rather late. If I wanted to catch up with everyone else, I had no choice but to work ten or twenty times harder.”

[P42]
“Hmm.”

[P43]
“I never thought I’d return like this.”

[P44]
It was the first time in a long while—no, almost the first time ever—that I had seen him look so serious.

[P45]
Come to think of it, Hyuk Mujin was a First Rate master who had quite a bit of skill, even though he acted foolishly about everything. It was just that he happened to be surrounded by monsters. His realm was by no means low.

[P46]
He could only have reached that level through tremendous effort. And on top of that…

[P47]
*He seems to have some talent, too.*

[P48]
> **System**
>
> **Level:** 48  
> **Name:** Hyuk Mujin

[P49]
The rapidly rising Level was proof of that.

[P50]
*Is this guy going to suddenly become a Peak master one of these days?*

[P51]
Despite my newly appreciative gaze, Hyuk Mujin was too absorbed in the emotions of returning to his hometown after so long.

[P52]
“Ah, that auntie is still here.”

[P53]
His voice was happy, yet wistful.

[P54]
The middle-aged woman he pointed toward had streaks of gray in her hair and was selling various snacks from a small stall.

[P55]
“Do you like candied hawthorn skewers?”[^1]

[P56]
Under normal circumstances, I would have told him to stop talking nonsense and keep moving, but the atmosphere was unusual. I answered as kindly as possible.

[P57]
“I’ve never eaten one in my life.”

[P58]
“When I was young, I wanted one so badly. Whenever I crouched in front of the stall and sucked on my fingers, that auntie would give me one or two.”

[P59]
Hyuk Mujin continued with a bitter smile.

[P60]
“You have no idea how envious I was of the other children. They would come holding tightly to their parents’ hands, buy candied hawthorn and sweets, and walk around the market… I can still see it clearly.”

[P61]
What was I supposed to do with this atmosphere?

[P62]
I had assumed there would be some sort of story behind him, but I hadn’t expected it to go in this direction.

[P63]
*I should have realized something when he said he hadn’t come back for five years.*

[P64]
There were an unusually large number of orphans in the Murim. Even looking around us, it was easy to find children wandering through the market in filthy rags.

[P65]
*He must have been in a similar situation.*

[P66]
If he had no family, he had no reason to return. Coming back would only remind him of the painful memories of standing around the stall as a child, wanting to eat candied hawthorn.

[P67]
Maybe that was why he had tried to forget his pain through training.

[P68]
For him, the Jin Family of Taiyuan had been home, and his companions had been his family.

[P69]
*And without knowing any of that… I’ve been treating him far too harshly.*

[P70]
Damn it. The tip of my nose was starting to sting for no reason.

[P71]
Hyuk Mujin immediately noticed the change in me.

[P72]
“What’s wrong?”

[P73]
“No, it’s nothing. Maybe the fine dust is especially bad today. My nose feels itchy.”

[P74]
“Fine dust?”

[P75]
“Forget that. Why don’t we each get a candied hawthorn skewer?”

[P76]
“Wouldn’t it be better to find an inn first? If we don’t get a room before the sun goes down, there may not be any left.”

[P77]
“Hey, how long does it take to eat one of those? They’re not even that expensive. We were given plenty of travel expenses, weren’t we?”

[P78]
“That’s true.”

[P79]
“Let’s eat whatever we want and have as much fun as we can before we leave. You can raise that auntie’s sales while paying her back for all the candied hawthorn she gave you when you were young.”

[P80]
“I’m not sure it’s right to spend the money we were given for things we need on this…”

[P81]
“Spend it. Spend every bit of it. If anyone complains later, bring them to me.”

[P82]
“What if the Second Young Master complains?”

[P83]
“...Bring anyone but him.”

[P84]
Hyuk Mujin let out a short laugh before speaking in a much brighter voice.

[P85]
“Then shall we each get a candied hawthorn skewer?”

[P86]
“Sure. I’ve been looking at them for a while, and they’re making my mouth water.”

[P87]
I was saying that very deliberately for Hyuk Mujin’s sake. I was almost thirty. What kind of adult salivated over fruit candy?

[P88]
*As long as it makes him feel better.*

[P89]
That guy had suffered plenty while following me around. He was constantly berated and beaten, and every time we took on a Quest, we ended up meeting nothing but monsters. He had come close to dying more than once.

[P90]
My first meeting with Hyuk Mujin had certainly been an ill-fated one, but that was no longer true.

[P91]
“Hey, Mujin.”

[P92]
Hyuk Mujin, who had just started walking toward the stall, stopped short.

[P93]
“Yes? What is it?”

[P94]
“That…”

[P95]
The words *I’m counting on you from here on out* hovered at the tip of my tongue. Damn it. That was far too embarrassing for two grown men to say to each other.

[P96]
After agonizing over it, I ended up blurting out something completely different.

[P97]
“Let’s each have two. The big ones.”

[P98]
“Oh. Yes.”

[P99]
Too embarrassed to look at him, I stared off at a distant mountain. That was when I heard Hyuk Mujin speaking with the middle-aged woman.

[P100]
“Oh my! Aren’t you Mujin? Hyuk Mujin, right?”

[P101]
“It’s been a long time, Auntie.”

[P102]
“My goodness, it is you. It is! I almost didn’t recognize you, child.”

[P103]
“You haven’t changed at all, Auntie.”

[P104]
“Ho-ho-ho. That’s kind of you to say. Have you been well, Mujin? I heard you became a martial artist.”

[P105]
“Yes. I belong to the Jin Family of Taiyuan. I’ll be promoted to Master of the Gatekeeper Pavilion soon.”

[P106]
“T-Taiyuan Jin Family? Master of the Gatekeeper Pavilion? My goodness, my goodness…”

[P107]
Whether he would actually be promoted to Master of the Gatekeeper Pavilion remained to be seen, but the conversation brought a pleased smile to my face.

[P108]
*This sounds like a radio call-in story.*

[P109]
A kindhearted auntie who used to give candied hawthorn to the orphan child who was always lingering around her stall. After years of backbreaking effort, the child who had endured a difficult childhood finally succeeded and returned as a tall, grown man.

[P110]
It was a story I had heard somewhere before, but that didn’t make it any less moving.

[P111]
“Ahem. What is this? Did something get in my eye?”

[P112]
Was this the yellow dust or the fine dust? Factories couldn’t have been built yet, so it must have been yellow dust.

[P113]
That was when the rims of my eyes reddened slightly despite myself.

[P114]
“So, have you gone to see your parents?”

[P115]
“Not yet. I was thinking of stopping by today or tomorrow.”

[P116]
“Go see them soon. Didn’t your family move?”

[P117]
“Move? Where did they go?”

[P118]
“They moved into a large estate along the main road over there. They even released koi into the pond and raised them.”

[P119]
“Oh, really?”

[P120]
“...?”

[P121]
Parents? Moving? A huge estate with koi?

[P122]
Wait. Something was wrong here. I asked Hyuk Mujin, who was returning with the candied hawthorn skewers in his hands.

[P123]
“What were you talking about?”

[P124]
“Huh? About what?”

[P125]
“Are your parents still alive?”

[P126]
Hyuk Mujin stared at me as though I were insane.

[P127]
“Why would I kill my perfectly healthy parents?”

[P128]
“No, that’s not what I meant… Then what were you talking about earlier?”

[P129]
“What did I say?”

[P130]
“About the candied hawthorn. You said you couldn’t eat it and spent every day sucking your fingers.”

[P131]
“I couldn’t eat it. My parents wouldn’t let me because they said it would rot my teeth. All the merchants around here knew how overbearing my parents were, so they made a point of refusing to sell any to me specifically. That lady was the only one who would secretly slip me one.”

[P132]
“…”

[P133]
“And what about being jealous of the children who walked around holding their parents’ hands?”

[P134]
“My family’s business was so successful that they never had any free time. I played by myself.”

[P135]
“Th-then you had family in Taiyuan, and you didn’t visit even once in five years?”

[P136]
“I left home. I didn’t want to inherit the family business, so I left a single letter behind and ran away. The Master of the Gatekeeper Pavilion in our family is my father’s childhood best friend, so he probably knew everything about how I was doing.”

[P137]
“…”

[P138]
“For about two years, they gave me hell over it. Then my youngest sibling was suddenly born, so I no longer needed to inherit the family business. After that, they stopped saying much.”

[P139]
Hyuk Mujin stretched his neck and looked around before raising a hand to point at something.

[P140]
“Ah, there it is. Do you see it? That building belongs to my parents… It got even bigger while I was gone.”

[P141]
I followed Hyuk Mujin’s finger and turned my head.

[P142]
A huge, towering five-story pavilion and a signboard bearing enormous characters came into view.

[P143]
**Hyuk Family Textile Shop**

[P144]
Hyuk Mujin smiled proudly.

[P145]
“It’s the largest textile shop in Taiyuan. We have branches in Henan and Hebei, too.”

[P146]
*This bastard is a rich kid, too…*

[P147]
You had to be pretty damn wealthy to open chain stores in a place this rough.

[P148]
*What the hell have I been doing?*

[P149]
A young boy who used to suck on his fingers because he wanted to eat candied hawthorn so badly?

[P150]
In reality, his successful business-owner parents had forbidden him from eating it because they were worried about their son’s dental health.

[P151]
*What the fuck is this?*

[P152]
As I stood there with my mouth hanging open, Hyuk Mujin held out one of the candied hawthorn skewers.

[P153]
“Here, have one. I specially chose the biggest and shiniest one. The ones that lady sells are the best in this area.”

[P154]
“You son of a…”

[P155]
I swallowed the curse that had surged up to my throat and bit down on the candied hawthorn with a loud crunch.

[P156]
“Let’s hurry up and find a room.”

[P157]
“Already? We’ve only spent a few copper coins…”

[P158]
“Hey! Is it your money? It’s travel expenses they gave us to use when necessary. Expenses!”

[P159]
“Didn’t you just say we should spend it all and have fun?”

[P160]
“We’ve had enough fun. You said the rooms would fill up after sunset. If we get a bad night’s sleep and end up late to tomorrow’s luncheon, are you going to take responsibility?”

[P161]
“…”

[P162]
* * *

[P163]
Honghwa Inn.

[P164]
As could be guessed from the name written on its signboard, this was one of the places under the Lower District Sect’s influence.

[P165]
*Honghwaru at night. Honghwa Inn for lodging.*

[P166]
Whoever had come up with that arrangement had clearly intended to wring every last penny from drunken customers.

[P167]
“Let’s go in.”

[P168]
I was about to lead Hyuk Mujin, who had been pouting since earlier, toward the inn’s entrance when someone spoke.

[P169]
“Excuse me, I’m sorry to bother you.”

[P170]
The voice strangely tugged at my nerves. Its owner was a young man with an affable expression and a dreamy, hazy voice as innocent as a child’s.

[P171]
*This feeling…*

[P172]
The moment I turned around and met his clear eyes, I found it difficult to breathe.

[P173]
This was an aura different from Jin Mukyung’s.

[P174]
> **System**
>
> **Level:** ???  
> **Name:** Cheongpung

[P175]
Another Peak master had appeared.

[P176]
Amid the tension, the young man named Cheongpung opened his lips.

[P177]
“If you don’t mind, may I eat just one candied hawthorn skewer?”

[P178]
“...?”

[P179]
*What the hell is this guy?*

[P180]
[^1]: Candied hawthorn skewers are a traditional snack made by coating skewered fruit in hardened sugar.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 기루     | **pleasure house**                               |                                                       |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 131,
  "passed": true,
  "metrics": {
    "source_characters": 5950,
    "translation_characters": 13463,
    "length_ratio": 2.263,
    "source_paragraphs": 176,
    "translation_paragraphs": 180
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "주신",
        "preferred": "God of Drinking"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "전하",
        "preferred": "His Highness"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "수문각",
        "preferred": "Gate Guard Pavilion"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "호호호",
        "romanization": "hohoho"
      }
    }
  ]
}
```

## Binding editorial rules

# Translation Rules

## Fidelity

- Translate the Korean source—not the wiki, manhwa, fan translations, or expected plot.
- Semantic fidelity outranks elegance. Never improve rhythm, humor, or localization by changing a physical action, negation, relationship, hierarchy, mechanism, quantity, or causal detail.
- Preserve every fact, causal link, joke, emotional beat, repetition, and intentional omission. Add nothing.
- Preserve small action verbs and pragmatic cues exactly: nodding versus shaking one's head, pretending nothing happened, and mild or approachable impressions are characterization, not expendable texture.
- Preserve viewpoint and tense. Resolve omitted subjects only when context supports it; retain genuine ambiguity.
- Match each speaker's hierarchy, intimacy, humor, and profanity naturally. Do not mechanically retain every honorific or classical self-reference.
- Do not censor or soften content.

## Terminology

- `compendium.md` and `docs/NAMES.md` are binding for established names, titles, ranks, techniques, organizations, system terms, items, and locations. Profile headings and aliases join that ledger.
- Search only exact Korean terms already present in the current chapter; the compendium contains future-sensitive entries.
- Never re-romanize established names or invent grand names for uncertain terms. First use of an unlisted name or title almost always needs a footnote or a mapped ledger term.
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them. Preserve an established chapter-specific rendering such as `internal energy` when the exact glossary and surrounding Korean distinguish accumulated `공력` from resulting `기운`.
- In System panels, render `등급` as `**Grade:**` for quest, item, skill, and martial-art classifications. Reserve `rank` for Hunter classifications or ordinary prose; never replace a System `Grade` field with `Rank`.

## English and Markdown

- Use contemporary US English and natural action-comedy prose; avoid Korean syntax calques and generic cultivation MTL phrasing.
- File: `translations/NNNN.md`; heading: `# Chapter N`.
- Speech: curly double quotes. Direct thoughts: italics without quotes.
- Use em dashes without spaces, the ellipsis character `…`, and `* * *` for source scene breaks.
- Format each actual game System-message panel as one Markdown blockquote window headed `> **System**`. Keep all consecutive notices, fields, and lines inside that same blockquote; separate windows when prose intervenes. Do not enclose System notices or UI terms in square brackets; the `System` heading and framed blockquote identify the panel. Do not label manuals, ordinary quotations, warnings printed in a manual, or other non-System material as `System`; use a normal blockquote or a specific heading instead. Do not wrap each complete notice in outer `**`; retain bold only for meaningful labels or emphasis inside the panel.
- Keep the final file English-only reading copy: no audit notes, Korean text, summaries, or model metadata.

### Tone and Style

- Write like a polished commercial webnovel: brisk, vivid, accessible, and easy to read aloud.
- Preserve the series’ contrast between danger and comedy. Let absurdity, bad timing, blunt reactions, and grim situations create dark humor without adding jokes absent from the Korean.
- Jin Taekyung’s narration is conversational, observant, self-mocking, and occasionally profane. It may be irreverent even when the situation is serious.
- Keep deadpan punchlines short and well-timed. Do not explain a joke after delivering it.
- Preserve the source's level of explicitness. A euphemism may remain euphemistic even when its meaning is sexual or crude; do not replace it with more graphic English merely for impact.
- Make dialogue spontaneous and character-specific. Preserve hierarchy and intimacy through word choice, address, rhythm, and restraint—not archaic wuxia English.
- Use strong profanity when the Korean is strong, but neither intensify nor sanitize it. Do not make ordinary lines uniformly vulgar. Profanity should reveal mood or relationship.
- Keep action and injury vivid but clear rather than purple. Do not make violence funny unless the source’s framing does.
- Avoid stiff literalism, translator-added melodrama, dated internet slang, and quippy superhero-style banter.
- On the second pass, correct awkward English collocations and word choices without changing meaning or voice. Prefer ordinary, spoken English over stiff Latinate or ceremonial wording when the scene is brisk or comic: “goose bumps” rather than “gooseflesh,” and “laid into them” rather than “launched into a solemn denunciation.” Read the prose aloud and replace any phrase that sounds like a formal essay, legal document, or literal dictionary gloss unless the source deliberately calls for that register.

## Footnotes

Use `[^1]` Markdown footnotes when a brief, factual, spoiler-free explanation materially helps an English reader understand:

- a Korean institution, living arrangement, food, holiday, myth, historical reference, or local custom;
- a Korean word, phrase, idiom, wordplay, or culturally specific image that cannot be conveyed fully by the best natural English analogy;
- a deliberately literal rendering whose cultural or linguistic force would otherwise be lost.

For example, render `고시원` as “goshiwon” when the setting or connotations matter, with a concise footnote explaining that it is a very small, inexpensive room-for-rent housing arrangement. Prefer the best natural English analogy in the prose. Use a literal translation plus a concise footnote when the Korean wording itself matters. Define a term at its first meaningful occurrence and do not repeat the note unnecessarily. Footnotes must be rare, useful, and non-spoiling; do not footnote ordinary vocabulary, fully preserved jokes, or uncertainty. Record consequential uncertainty in `docs/STATE.md`.

## Spoilers and Scope

- Safe profiles contain only facts revealed through the latest completed chapter.
- Never read `characters/spoilers/` during drafting. Reviewers may consult one relevant sealed profile only for a specific unresolved continuity issue after the draft is complete.
- Future knowledge may prevent contradiction but may not add early names, pronouns, certainty, motives, or foreshadowing.
- Translate exactly one requested chapter unless the user explicitly requests a batch. Never modify Korean source files under `source/`.

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

The accepted baseline is also the project's style and terminology anchor. Do not
replace an established rendering, cultural term, System label, Markdown form, or
recurring phrase with a synonym merely because the synonym sounds smoother.
Make that change only when the Korean source, `RULES.md`, or the exact glossary
requires it. In particular, do not turn a source-specific image into a nearby
English image, or change a gold-spoon joke, item name, technique name, or UI
label into a different expression without source support.

## Fidelity constraints

Never invent, omit, explain away, generalize, intensify, soften, or reinterpret source-supported content. In particular, preserve:

- exact actions, subjects, objects, directionality, causality, quantities, and physical details;
- deliberate ambiguity, euphemism, implication, profanity level, repetition, and withheld information;
- jokes and comic specificity, even when a more generic English joke would sound smoother;
- hierarchy, kinship, forms of address, characterization, and speaker attitude;
- System mechanics, Murim concepts, names, ranks, techniques, items, organizations, and established terminology.
- chapter-level logical consistency: interpret labels, counters, notifications, and repeated facts from how they behave across the scene, not from an isolated surface gloss;
- idioms by their narrative function rather than their component words, and jokes with their setup, recognition, and punchline timing intact;
- cross-sentence implications: do not create a claim that contradicts “again,” an increasing value, an earlier action, or the explanation immediately around it;
- repeated terminology and formatting: once the baseline or glossary establishes a rendering, keep it consistent throughout the chapter unless the source clearly changes the sense;

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

Before returning the chapter, perform a silent continuity pass: trace every
counter, quantity, repeated System label, item or technique name, joke setup and
payoff, and physical cause-and-effect sequence from the Korean through the
finished English. Correct any local sentence that contradicts the sequence.

## Relationship to project files

`RULES.md` is binding. `POLISH.md` describes known translation-English failure modes and should guide the edit. Exact glossary matches are binding unless the packet explicitly marks them otherwise. Character/continuity material is context only and must never override the chapter's Korean source.

## Output

Return only the complete edited English Markdown chapter. Preserve the required chapter heading and project Markdown conventions. Do not provide commentary, a change log, explanations, or a Markdown code fence.
