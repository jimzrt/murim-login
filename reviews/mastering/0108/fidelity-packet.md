# Fidelity Gate — Chapter 108

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
  1|＃108화
  2|
  3|
  4|
  5|‘사냥꾼?’
  6|
  7|월화의 짐작은 절반만 맞았다. 사냥꾼은 사냥꾼인데, 불청객들의 정체는 조금 더 특별하고 훨씬 더 악랄했다.
  8|
  9|“빨리빨리 걸어라, 이놈들아.”
 10|
 11|“사내라는 것들이 이렇게 비리비리해서 어디다 써?”
 12|
 13|머릿수는 총 열 명. 하나같이 험상궂은 얼굴에, 병장기로 무장까지 했다. 그들의 선두에선 굴비처럼 밧줄로 묶인 포로들이 비틀거리고 있었다.
 14|
 15|퍽, 퍽퍽!
 16|
 17|“아이고, 대혀업!”
 18|
 19|“갑니다, 가고 있으니까 제발 그만 좀…….”
 20|
 21|“허, 그만? 이놈들이 아직도 정신이 덜 들었구나.”
 22|
 23|“어허, 적당히 때려. 어디 한 군데 부러지기라도 하면 값 떨어진다. 가뜩이나 조그마한 놈들이라 제값도 못 받게 생겼구먼.”
 24|
 25|“곡마단(曲馬團)에 팔아먹으면 그럭저럭 받겠지. 후딱 들어가서 화주나 한잔하자고.”
 26|
 27|“아따, 생각만 해도 침이…… 근데 저건 뭐여?”
 28|
 29|인간 사냥꾼들의 발걸음이 우뚝 멈췄다. 사당 앞에 세워져 있는 사두마차를 응시하던 눈동자들이 스르륵 옆으로 옮겨 간다.
 30|
 31|그들의 시선 끝에 나와 월화가 있었다.
 32|
 33|“……누구쇼?”
 34|
 35|우두머리로 보이는 놈의 질문에 내가 나섰다.
 36|
 37|“지나가던 과객.”
 38|
 39|“과객이라. 요즘 같은 시기에 돌아다니면 위험한데.”
 40|
 41|번들거리는 눈빛이 스스로가 위험한 놈이란 걸 말해 준다.
 42|
 43|물론 그래 봤자 겨우 25레벨이라 내게는 위험 축에도 못 끼지만.
 44|
 45|“이야, 사두마차에 기막힌 미녀까지. 있는 집 공자님이신가 봐?”
 46|
 47|가까이 다가가서 확인했다면 마차에 새겨진 태원진가의 문장을 확인할 수 있었겠지만, 지금은 시커먼 밤이었고 놈은 뛰어난 안력(眼力)의 소유자가 아니었다.
 48|
 49|“없는 집 자식은 아니지.”
 50|
 51|“거참. 아까부터 말씀이 짧으시네.”
 52|
 53|우두머리가 갈라진 입술을 핥았다. 슬슬 열이 오르는 모양이지만 아직은 나에 대한 경계를 풀지 않고 있다.
 54|
 55|“뭐, 됐고. 이곳은 우리가 며칠 전부터 머무르던 곳인데…… 어쩌겠소?”
 56|
 57|“뭘?”
 58|
 59|“뭐긴, 약간의 성의를 보여 주면 자리를 내어 드릴 수 있다는 거지.”
 60|
 61|“누가 들으면 이 사당이 그쪽 건 줄 알겠네.”
 62|
 63|“버려진 곳이니 먼저 차지하는 사람이 임자 아닌가?”
 64|
 65|“그럼 부동산 내용 증명서 떼 와.”
 66|
 67|“뭐?”
 68|
 69|우두머리가 어리둥절한 얼굴로 수하들을 돌아봤다. 생전 처음 듣는 용어일 테니 당연한 일이다. 하지만 아는 놈이 있을 리가 있나.
 70|
 71|부동산 내용 증명서에 관해 수군거리는 놈들을 향해 쯧쯧 혀를 찼다.
 72|
 73|“증명 못 하겠으면 곱게 돌아가라. 거기 잡아 둔 사람들은 풀어 주고.”
 74|
 75|“……선을 넘는군. 호위무사라도 기다리나?”
 76|
 77|“그런 거 없어.”
 78|
 79|“그럼 뭘 믿고?”
 80|
 81|“나.”
 82|
 83|우두머리의 시선이 내 텅 빈 두 손을 향한다.
 84|
 85|“병장기도 없이?”
 86|
 87|“너희 정도야 주먹으로 충분하니까.”
 88|
 89|“도련님이 어디서 한 수 배우긴 했나 본데…… 무림을 너무 우습게 보는 거 아닌가?”
 90|
 91|“무림은 안 우습지. 그냥 너희가 우스운 거야.”
 92|
 93|말과 함께 환하게 밝혀진 횃불을 향해 발을 내디딘 그 순간, 얌전히 잡혀 있던 포로들이 괴성을 내질렀다.
 94|
 95|“어, 어어어?”
 96|
 97|“으어어어! 대형! 대형!”
 98|
 99|“이 자식들이 미쳤나. 다들 입 안 닥쳐!”
100|
101|포로들의 격한 반응에 뒤에 선 놈들이 단검을 뽑아 목에 가져다 댔다. 우두머리가 경계심 어린 눈빛으로 나를 응시했다.
102|
103|“아는 놈들인가?”
104|
105|“아니, 태어나서 처음 보는데.”
106|
107|반응이 너무 갑작스러워서 나까지 당황할 정도다. 그리고 갑자기 대형이라니?
108|
109|“대혀어엉! 접니다! 저흽니다!”
110|
111|“이놈들은 그쪽을 아는 것 같은데?”
112|
113|“그거야 그냥 구해 달라고…… 어라?”
114|
115|나는 포로들을 유심히 바라봤다. 어린애처럼 작은 키에 하나같이 못생긴 얼굴. 어디서 본 것 같기도 하다.
116|
117|‘체형이 고블린을 닮아서 낯이 익은 건가?’
118|
119|잠깐만. 고블린?
120|
121|문득 오래전의 기억이 떠오른다. 아니, 사실 그리 오래된 기억도 아니다. 불과 몇 달 전 튜토리얼 퀘스트에서 있었던 일이니까.
122|
123|“설마 그, 천력부랑 같이 있었던?”
124|
125|포로들, 아니 천력부 장삼의 부하였던 오색귀(五色鬼)가 미친 듯이 고개를 끄덕였다.
126|
127|“맞습니다, 저흽니다!”
128|
129|“대형! 살려 주십시오!”
130|
131|이놈들을 여기서 보게 될 줄이야. 황당해하는 내게 뒤에서 상황을 지켜보던 월화가 물었다.
132|
133|“진 공자가 아는 사람들이에요?”
134|
135|“일단은 구면이네요.”
136|
137|인신매매범과 산적이라. 우열을 가릴 수 없는 조합이다.
138|
139|방금까지는 구해 줄 생각이었는데 지금은 살짝 고민되네.
140|
141|“대혀어어엉!”
142|
143|“저흴 버리실 생각이십니까!”
144|
145|“그날 이후 산적질도 그만두고 착하게 살았습니다!”
146|
147|“…….”
148|
149|눈치 하나는 귀신이다. 하긴, 천력부가 죽었을 때도 바로 항복해 버린 놈들이니 오죽할까.
150|
151|“구해 줄 건가요?”
152|
153|“쓰읍. 일단 구하긴 해야 할 것 같아요.”
154|
155|그날 이후 새사람이 됐다는데 이대로 보내기에는 영 찝찝하다. 무엇보다 현직 인신매매범보다는 전직 산적이 훨씬 낫지.
156|
157|그러자 우리의 대화를 들은 우두머리가 으르렁거리는 목소리로 끼어들었다.
158|
159|“구해? 네놈이?”
160|
161|“다 들어 놓고 뭘 또 물어봐. 너 인생 피곤하게 사는구나?”
162|
163|“이 애새끼가 보자 보자 하니까…….”
164|
165|차차창!
166|
167|우두머리가 창을 겨누자 수하들도 무기를 빼 들었다. 월화가 짐짓 겁먹은 얼굴로 내 옆구리에 달라붙는다.
168|
169|“어머, 무서워. 나 꼭 지켜 줘야 해요?”
170|
171|보호 본능을 불러일으키는 촉촉한 눈망울. 간절한 표정.
172|
173|월화의 실체를 아는 나로서는 기가 차는 광경이지만 놈들은 침을 꿀꺽 삼켰다.
174|
175|“널 죽여야 하는 이유가 하나 더 늘었군.”
176|
177|우두머리의 끈적끈적한 눈빛에 월화가 꺅, 비명을 질렀다.
178|
179|“어떡해, 어떡해! 소녀, 너무 무서워요!”
180|
181|“허허, 너무 겁먹지 말거라. 내 비록 일평생 거칠게 살았어도 마음만은 비단결처럼 고운 사내라는 걸 알게 될 테니. 잠시 후에 몸으로 대화를 나눠 보자꾸나.”
182|
183|“어, 그전에 나 좀 보자.”
184|
185|더러운 주둥이를 찢어 놔야 다시는 저딴 소리를 못 하지.
186|
187|놈을 향해 성큼성큼 걸어가다가 문득 발걸음을 멈췄다. 그런 내 모습을 본 우두머리가 껄껄 웃었다.
188|
189|“왜, 막상 싸우려니까 겁이 나나? 하지만 이미 늦었어.”
190|
191|“그러게. 너, 진짜 큰일 났다.”
192|
193|“……뭐?”
194|
195|나는 어리둥절해하는 놈을 향해 활짝 웃어 주었다.
196|
197|“좆 됐다고. 인마.”
198|
199|말이 끝난 그 순간, 땅이 울림과 동시에 강력한 바람이 휘몰아쳤다.
200|
201|쿵, 쐐애애액!
202|
203|말 그대로 찰나에 불과한 시간.
204|
205|무서운 속도로 나와 월화를 스쳐 간 그것은 어느새 우두머리의 앞에 서 있었다.
206|
207|“다시 한번 말해 봐라.”
208|
209|진무경. 그의 전신에서 뿜어져 나온 어마어마한 기파(氣波)가 장내를 짓눌렀다. 우두머리가 파랗게 질린 얼굴로 손을 덜덜 떨었다.
210|
211|“요, 용서. 제발…….”
212|
213|차가운 목소리가 대답했다.
214|
215|“한참 늦었어.”
216|
217|
218|
219|* * *
220|
221|
222|
223|어쩌면 진무경은 우리 중 최고의 비폭력주의자일지도 모른다. 불과 십여 초 만에 이어질 모든 불필요한 싸움을 종결지었으니까.
224|
225|“하, 항복, 항복하겠습니다.”
226|
227|“제발 살려 주십시오. 제발 목숨만은…….”
228|
229|공포에 질린 얼굴. 모두 다리가 풀려 자리에 주저앉았고, 누군가가 지린 소변은 언덕 아래로 흘렀다.
230|
231|그건 오색귀도 마찬가지였다.
232|
233|“시끄럽다.”
234|
235|진무경이 얼굴에 묻은 피를 닦아 내며 툭 던진 한마디에 죽음 같은 침묵이 내리깔린다. 눈 한쪽이 시퍼렇게 멍든 혁무진이 내게 속삭였다.
236|
237|“저 지금 살아 있는 거 맞습니까?”
238|
239|“어, 귓가에 숨결 닿는 거 소름 돋으니까 좀 떨어져.”
240|
241|“아까 전만 해도 이렇게 개처럼 맞을 수가 있나, 하는 생각이었는데 지금은…….”
242|
243|꿀꺽, 마른침을 삼키는 혁무진의 시선은 쓰러진 우두머리를 향해 고정되어 있었다.
244|
245|“흐윽, 흐으윽.”
246|
247|사지가 부러지고 단전(丹田)이 파괴당한 그는 힘겹게 숨을 몰아쉬는 중이었다. 잘만 요양하면 다시 걸어 다닐 수는 있겠지만 무인으로서의 생명은 끝장이다.
248|
249|기감으로 파악한 레벨창이 그 증거였다.
250|
251|
252|
253|[Lv.2 이삼]
254|
255|
256|
257|감시자들이 패밀리어로 쓰던 똥파리가 1레벨이었지, 아마.
258|
259|한때 일류에 근접했던 25레벨의 무인을 산송장으로 만들어 버린 범인은 아까부터 계속 이쪽을 힐끗거리고 있다.
260|
261|“조장님, 저 좀 살려 주세요. 이공자님께서 피가 부족하신가 봐요.”
262|
263|“헛소리하지 말고 쟤나 좀 적당한 곳에 옮겨 놔. 저러다가 죽겠다.”
264|
265|“죽어도 싼 놈 아닙니까? 멀쩡한 양민들 팔아먹던 놈들이잖아요.”
266|
267|“그래도 옮겨. 아직 살아 있잖아.”
268|
269|내가 무림과 현대를 오가며 느낀 가장 큰 괴리감 중 하나가 바로 살인(殺人)에 관한 문제였다.
270|
271|27년간, 법과 질서가 존재하는 사회에서 살았던 나다.
272|
273|날붙이로 적을 죽이는 법을 단련해 왔지만 그 대상은 몬스터였지, 살아 있는 인간이 아니었다.
274|
275|‘분명히 그랬는데…….’
276|
277|이제는 몇 명을 죽였는지 기억도 안 난다. 지금까지 내 손에 죽어 나간 적들이 NPC가 아닌 진짜 사람일지도 모른다는 걸 깨달았을 때도 큰 죄책감은 들지 않았다.
278|
279|‘적이었으니까. 저들도 날 죽이려고 했으니까.’
280|
281|헌터로 살아왔기 때문인지, 무림의 방식에 익숙해진 건지는 잘 모르겠다. 다만 무덤덤한 마음과 단순한 자기 합리화에 스스로 놀랐을 뿐.
282|
283|‘지금은 이 정도로도 괜찮겠지.’
284|
285|나는 전혀 다른 두 세계를 살아가는 중이다. 어설픈 불자(佛子) 흉내를 낼 정도로 여유로운 상황이 아니다.
286|
287|들러붙는 생각을 떨쳐 내며 주저앉아 있는 놈들을 향해 다가갔다.
288|
289|“히익!”
290|
291|“흐아악, 살려 주십쇼, 대형!”
292|
293|“이 자식들은 구해 주려고 해도 난리네. 가만히 있어 봐.”
294|
295|밧줄을 풀어 주자 자유의 몸이 된 오색귀가 후들거리는 다리로 일어났다.
296|
297|“가, 감사합니다.”
298|
299|“평생 은인으로 모시겠습니다!”
300|
301|“은인으로 모시긴 개뿔이. 그나저나 어쩌다가 이런 놈들한테 잡힌 거냐? 그것도 다섯 명이 한꺼번에.”
302|
303|오색귀 놈들이 체구가 작긴 해도 명색이 성인 남자다. 천력부를 따라 산적질 할 정도의 수준은 된다.
304|
305|“아니, 저 그게.”
306|
307|“……?”
308|
309|뭐지, 이놈들.
310|
311|머뭇거리는 태도에 이상함을 감지한 나는 가장 가까이 있는 인신매매범의 멱살을 붙잡고 끌어올렸다.
312|
313|“이놈들 어떻게 붙잡았어?”
314|
315|“저, 저잣거리에서 저희 전낭을 슬쩍 하려던 걸 붙잡았습니다.”
316|
317|“…….”
318|
319|이런 십색귀들을 봤나. 산적 관두고 농사라도 짓나 했더니 직종을 바꾼 거였어?
320|
321|“변명해 봐.”
322|
323|날카로운 내 시선에 다섯 놈이 눈알을 뒤룩뒤룩 굴렸다.
324|
325|“그, 그러니까.”
326|
327|“대형, 저희 같은 놈들은 배운 게 그런 것뿐이라.”
328|
329|“그, 그래도 시작한 지 얼마 안 됐습니다!”
330|
331|“착실하게 일하려고 했는데 영 신통치가 않아서…… 딱 한탕만 치고 빠지자 했던 게 그만.”
332|
333|“마적단 놈들인 줄 알았으면 건드리지도 않았죠. 저희도 피해잡니다. 대형, 제발 한 번만 용서해 주십쇼!”
334|
335|이놈들을 어떻게 처리해야 하나 고민하던 나는 익숙한 단어에 잠시 멈칫했다.
336|
337|“뭐라고?”
338|
339|“진짜 딱 한 번만 더 용서해 주시면 착실하게 살겠습니다!”
340|
341|“아니, 그거 말고. 저놈들이 뭐라고?”
342|
343|“아, 마적단 말씀이십니까요?”
344|
345|“그래, 그거.”
346|
347|“저희도 잡힌 후에야 들었습니다. 웬 왈패 무리가 기루에서 은자를 뿌리며 다니기에 따라붙었는데…… 마적들 사이에서도 흉악하기로 소문난 적풍단(赤風團) 놈들이었지 뭡니까.”
348|
349|“적풍단? 확실해?”
350|
351|“예. 제 귀로 똑똑히 들었습니다. 맞지?”
352|
353|다른 놈들도 앞다퉈 한 마디씩 보태기 시작했다.
354|
355|“내일 날이 밝자마자 떠날 거라고도 했습니다.”
356|
357|“산음(山陰)까지 가려면 쉬지 않고 달려야 한다고. 괜히 늦었다가 목 달아나는 거 아니냐고 걱정까지 하던데요.”
358|
359|“그렇단 말이지.”
360|
361|어제, 그리고 오늘. 이틀 연속으로 만난 마적이 하필이면 적풍단 소속인 것도 공교로운데, 산음은 항산검문의 본거지가 있는 응현(應現)과 가까운 곳이다.
362|
363|“이 녀석들 말이 모두 사실이냐?”
364|
365|내 오른손에 멱살이 붙잡혀 있던 인신매매범, 아니 적풍단의 마적이 덜덜 떨며 고개를 끄덕인 그 순간이었다.
366|
367|삐이익!
368|
369|날카로운 울음소리와 함께 한 마리의 매가 사당 앞에 내려앉았다. 발목에 묶인 자그마한 원통이 눈에 들어온다.
370|
371|‘전서응.’
372|
373|이거 어째 분위기가 묘하게 돌아가는데.
```

## Assembled English

```markdown
[P1]
# Chapter 108

[P2]
*Hunters?*

[P3]
Wolhwa’s guess was only half right. They were hunters, all right—but the uninvited guests were something more special and far more vicious.

[P4]
“Move it, you bastards.”

[P5]
“What good are grown men this scrawny?”

[P6]
There were ten of them in all, every one of them rough-faced and armed. Ahead of them staggered a line of prisoners strung together with rope like dried fish.

[P7]
*Thud! Thud-thud!*

[P8]
“Ugh, Boss!”

[P9]
“We’re moving! We’re moving, so please stop…”

[P10]
“Hah, stop? You bastards still haven’t learned your lesson.”

[P11]
“Hey, don’t hit them too hard. If something breaks, their price drops. They’re already so small we probably won’t get full value for them.”

[P12]
“We should get a decent price if we sell them to a circus troupe. Let’s hurry inside and have a drink.”

[P13]
“Ah, my mouth’s watering just thinking about it… But what’s that?”

[P14]
The human hunters stopped dead. Their eyes lingered on the four-horse carriage parked before the shrine, then slowly shifted aside.

[P15]
Their gazes came to rest on Wolhwa and me.

[P16]
“…Who are you?”

[P17]
I stepped forward when the apparent leader spoke.

[P18]
“Just a traveler passing through.”

[P19]
“A traveler, huh? Dangerous time to be wandering around.”

[P20]
The oily gleam in his eyes said he himself was one of those dangers.

[P21]
Of course, at a mere Level 25, he didn’t even qualify as a threat to me.

[P22]
“Would you look at that. A four-horse carriage and a stunning beauty. You must be the Young Master of some wealthy family.”

[P23]
If he had come closer to inspect it, he could have seen the crest of the Jin Family of Taiyuan carved into the carriage. But it was pitch-black outside, and he didn’t possess particularly sharp eyesight.

[P24]
“I’m not from a poor one.”

[P25]
“Well now. You’ve been awfully informal with me from the start.”

[P26]
The leader licked his cracked lips. He seemed to be getting irritated, but he still hadn’t let down his guard around me.

[P27]
“Whatever. We’ve been staying here for the past few days… So what are you going to do?”

[P28]
“About what?”

[P29]
“What do you think? If you show us a little sincerity, we might let you have the place.”

[P30]
“Anyone listening would think you owned this shrine.”

[P31]
“It’s abandoned. Doesn’t that mean whoever claims it first owns it?”

[P32]
“Then bring me a certified deed.”

[P33]
“What?”

[P34]
The leader turned to his men in bewilderment. Naturally, it was probably the first time any of them had heard the term. Not that his men were likely to know any better.

[P35]
I clicked my tongue as they whispered among themselves about certified deeds.

[P36]
“If you can’t prove you own it, leave quietly. And untie those people.”

[P37]
“…You’re crossing the line. Are you waiting for bodyguards?”

[P38]
“I don’t have any.”

[P39]
“Then what are you relying on?”

[P40]
“Me.”

[P41]
The leader’s gaze shifted to my two empty hands.

[P42]
“Without even a weapon?”

[P43]
“For the likes of you, my fists are enough.”

[P44]
“Looks like the Young Master learned a move or two somewhere… But aren’t you taking Murim a little too lightly?”

[P45]
“Murim isn’t a joke. You are.”

[P46]
The moment I stepped toward the brightly burning torch, the prisoners who had been quietly restrained began screaming.

[P47]
“Wh-what?”

[P48]
“Boss! Boss!”

[P49]
“Have you bastards lost your minds? Shut your mouths!”

[P50]
The men in the rear drew daggers and held them to the prisoners’ throats in response to their violent reaction. The leader stared at me with wary eyes.

[P51]
“You know them?”

[P52]
“No. Never seen them before in my life.”

[P53]
Their reaction was so sudden that even I was caught off guard. And why were they calling me Boss?

[P54]
“Bosss! It’s me! It’s us!”

[P55]
“These men seem to know you.”

[P56]
“They’re just asking me to save them… Huh?”

[P57]
I looked closely at the prisoners. They were all short as children and had uniformly ugly faces. They looked vaguely familiar.

[P58]
*Is it because they’re built like goblins?*

[P59]
Wait. Goblins?

[P60]
A distant memory suddenly surfaced. No, it wasn’t even that distant. It had happened only a few months earlier, during the tutorial Quest.

[P61]
“Don’t tell me… You were with the Heavenly Axe?”

[P62]
The prisoners—or rather, the Five-Colored Ghosts[^1], former subordinates of Jang Sam the Heavenly Axe—nodded frantically.

[P63]
“That’s us!”

[P64]
“Boss! Please save us!”

[P65]
I never expected to run into these bastards here. While I stood dumbfounded, Wolhwa, who had been watching from behind, asked,

[P66]
“Are they acquaintances of yours, Young Master Jin?”

[P67]
“We’ve met before, at least.”

[P68]
Human traffickers and bandits. It was hard to say which was worse.

[P69]
A moment ago, I’d been planning to save them. Now I was having second thoughts.

[P70]
“Bosssss!”

[P71]
“Are you going to abandon us?”

[P72]
“We quit being bandits after that day and have lived good lives ever since!”

[P73]
“…”

[P74]
Their ability to read the situation was almost supernatural. No wonder. They had surrendered immediately when the Heavenly Axe died, after all.

[P75]
“Are you going to save them?”

[P76]
“Tsk. I think we have to, at least.”

[P77]
They said they had turned over a new leaf after that day, and leaving them like this wouldn’t sit right with me. More importantly, former bandits were far better than active human traffickers.

[P78]
The leader overheard us and cut in with a growl.

[P79]
“Save them? You?”

[P80]
“You heard the whole thing. Why ask again? You sure know how to make life difficult for yourself.”

[P81]
“You little shit. I’ve let you run your mouth long enough…”

[P82]
*Clang!*

[P83]
The leader leveled his spear at me, and his men drew their weapons as well. Wolhwa clung to my side with a deliberately frightened expression.

[P84]
“Oh my, I’m scared. You have to protect me, don’t you?”

[P85]
Her moist eyes stirred a man’s protective instinct. Her expression was pleading.

[P86]
Knowing Wolhwa’s true nature, I found the sight ridiculous. The men, however, swallowed hard.

[P87]
“Now I have one more reason to kill you.”

[P88]
When the leader gave her a lecherous look, Wolhwa shrieked.

[P89]
“Oh no, oh no! This maiden is so scared!”

[P90]
“Ho ho, don’t be so frightened. Though I may have lived a rough life, you’ll soon learn that I’m a man with a heart as soft as silk. In a little while, we can have a conversation with our bodies.”

[P91]
“Hey, look at me first.”

[P92]
I needed to tear that filthy mouth open so he’d never say anything like that again.

[P93]
I strode toward him, then abruptly stopped. The leader saw me halt and burst into laughter.

[P94]
“What’s wrong? Lost your nerve now that it’s time to fight? Too late.”

[P95]
“Exactly. You’re in real trouble now.”

[P96]
“…What?”

[P97]
I gave the bewildered man a broad smile.

[P98]
“I said you’re fucked, asshole.”

[P99]
The moment I finished speaking, the ground shook, and a powerful wind whipped through the area.

[P100]
*Boom—whoosh!*

[P101]
It all happened in the blink of an eye.

[P102]
Something swept past Wolhwa and me at terrifying speed and was already standing in front of the leader.

[P103]
“Say that again.”

[P104]
Jin Mukyung.

[P105]
An overwhelming wave of qi poured from his entire body and crushed the entire scene. The leader’s face turned deathly pale, and his hands began to tremble.

[P106]
“F-forgive me. Please…”

[P107]
A cold voice answered.

[P108]
“You’re far too late.”

[P109]
* * *

[P110]
Perhaps Jin Mukyung was the greatest pacifist among us. In just over ten seconds, he had put an end to all the unnecessary fighting that would have followed.

[P111]
“S-surrender! We surrender!”

[P112]
“Please spare us! Please, just let us live…”

[P113]
Their faces were frozen with terror. Everyone’s legs gave out, and they collapsed where they stood. Someone’s urine trickled down the hill.

[P114]
The Five-Colored Ghosts were no different.

[P115]
“Quiet.”

[P116]
Jin Mukyung wiped the blood from his face and tossed out that single word. A deathly silence fell.

[P117]
Hyuk Mujin, one eye bruised deep blue, whispered to me,

[P118]
“Am I actually alive right now?”

[P119]
“Yeah. Your breath against my ear is giving me goose bumps, so move away.”

[P120]
“Just a moment ago, I was wondering how anyone could get beaten like a dog that badly, but now…”

[P121]
*Gulp.*

[P122]
Hyuk Mujin swallowed dryly, his gaze fixed on the fallen leader.

[P123]
“Hng… Hng…”

[P124]
With all four limbs broken and his dantian destroyed, the man struggled for breath. If he received proper care, he might be able to walk again, but his life as a martial artist was over.

[P125]
The Level window I sensed through Qi Sense was proof.

[P126]
> **System**
>
> **Level 2 — Lee Sam**

[P127]
*The dung flies those watchers used as Familiars were Level 1, if I remember right.*

[P128]
The culprit who had reduced a Level 25 martial artist—one who had once been close to First Rate—to a living corpse kept stealing glances in our direction.

[P129]
“Captain, please save me. I think the Second Young Master is still short on blood.”

[P130]
“Stop talking nonsense and move that guy somewhere suitable. He’ll die if you leave him like that.”

[P131]
“Doesn’t he deserve to die? They were selling perfectly innocent commoners.”

[P132]
“Move him anyway. He’s still alive.”

[P133]
One of the greatest sources of dissonance I had felt while moving between Murim and the modern world was the issue of killing people.

[P134]
For twenty-seven years, I had lived in a society governed by law and order.

[P135]
I had trained to kill enemies with bladed weapons, but my targets had been monsters, not living humans.

[P136]
*I was sure that was the case…*

[P137]
Now I couldn’t even remember how many people I had killed. Even after realizing that the enemies who had died by my hand might have been real people rather than NPCs, I hadn’t felt much guilt.

[P138]
*They were enemies. They were trying to kill me too.*

[P139]
I didn’t know whether it was because I had lived as a Hunter or because I had grown accustomed to Murim’s ways. I was only surprised by my own numbness and the simplicity of my self-justification.

[P140]
*For now, this much should be fine.*

[P141]
I was living in two completely different worlds. I couldn’t afford to play at being some half-baked Buddhist disciple.

[P142]
I shook off the thoughts clinging to me and approached the men cowering on the ground.

[P143]
“Eek!”

[P144]
“Uaaagh! Save me, Boss!”

[P145]
“You bastards make a fuss even when I’m trying to save you. Hold still.”

[P146]
I untied the ropes, and the Five-Colored Ghosts were free. They stood on trembling legs.

[P147]
“Th-thank you.”

[P148]
“We’ll serve you as our Benefactor for the rest of our lives!”

[P149]
“Like hell you will. Anyway, how did you end up getting caught by men like these? All five of you at once?”

[P150]
The Five-Colored Ghosts were small, but they were grown men, at least in name. They had been strong enough to commit banditry alongside the Heavenly Axe.

[P151]
“Um, well…”

[P152]
“…?”

[P153]
What was wrong with these guys?

[P154]
Sensing something off in their hesitation, I grabbed the nearest human trafficker by the collar and hauled him up.

[P155]
“How did you catch them?”

[P156]
“We caught them trying to steal our money pouches in the marketplace.”

[P157]
“…”

[P158]
What the hell, these Ten-Colored Ghosts. I thought they had quit being bandits and might have taken up farming, but they had only changed occupations?

[P159]
“Explain yourselves.”

[P160]
Under my piercing stare, the five men’s eyes darted around.

[P161]
“W-well…”

[P162]
“Boss, this is the only kind of thing people like us ever learned to do.”

[P163]
“E-even so, we only started recently!”

[P164]
“We tried to work honestly, but nothing went right… We said we’d pull just one job and get out, but then…”

[P165]
“If we’d known they were mounted bandits, we never would’ve touched them. We’re victims too. Boss, please forgive us just this once!”

[P166]
As I wondered what to do with these men, a familiar word made me pause.

[P167]
“What did you say?”

[P168]
“We’ll live honestly if you forgive us just one more time!”

[P169]
“No, not that. What did they say?”

[P170]
“Ah, do you mean the mounted-bandit group?”

[P171]
“Yeah. That.”

[P172]
“We only found out after they caught us. Some ruffians were throwing silver around at a pleasure house, so we followed them… Turns out they were from the Red Wind Band, infamous for their viciousness even among mounted bandits.”

[P173]
“The Red Wind Band? Are you sure?”

[P174]
“Yes. I heard it clearly with my own ears. Right?”

[P175]
The others began eagerly adding their own pieces.

[P176]
“They also said they were leaving at first light tomorrow.”

[P177]
“They said they’d have to ride without stopping to reach Saneum. They were even worried they might lose their heads if they arrived late.”

[P178]
“So that’s how it is.”

[P179]
Yesterday, and now today.

[P180]
Running into mounted bandits from the Red Wind Band two days in a row was already an uncanny coincidence. On top of that, Saneum was close to Eung-hyeon, where the Mount Heng Sword Sect’s headquarters stood.

[P181]
“Are these men telling the truth?”

[P182]
The human trafficker whose collar I held in my right hand—or rather, the mounted bandit from the Red Wind Band—nodded, trembling.

[P183]
At that moment—

[P184]
*Shriek!*

[P185]
A hawk landed in front of the shrine with a sharp cry. A small cylinder tied to its ankle caught my eye.

[P186]
*A messenger eagle.*

[P187]
Things were taking a strange turn.

[P188]
[^1]: A nickname meaning “Five-Colored Ghosts.”
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
# Chapter 108

[P2]
*Hunters?*

[P3]
Wolhwa’s guess was only half right. They were hunters, all right—but the uninvited guests were something more special and far more vicious.

[P4]
“Move it, you bastards.”

[P5]
“Who can do anything with men as scrawny as you?”

[P6]
There were ten of them in all. Every one had a rough-looking face and was armed with a weapon. At the front of their group, prisoners tied together with rope like a string of dried fish staggered along.

[P7]
*Thud! Thud-thud!*

[P8]
“Ugh, Boss!”

[P9]
“We’re coming, we’re coming, so please stop already…”

[P10]
“Huh, stop? These bastards still haven’t come to their senses.”

[P11]
“Hey, take it easy. If you break something, their price drops. They’re small to begin with, so it looks like we won’t get full value for them.”

[P12]
“We should get a decent price if we sell them to a circus troupe. Let’s hurry inside and have a drink.”

[P13]
“Ah, my mouth waters just thinking about it… But what’s that?”

[P14]
The human hunters came to an abrupt stop. Their eyes, which had been fixed on the four-horse carriage parked in front of the shrine, slowly shifted to the side.

[P15]
At the end of their gazes stood Wolhwa and me.

[P16]
“…Who are you?”

[P17]
I stepped forward at the question from the man who appeared to be their leader.

[P18]
“Just a traveler passing through.”

[P19]
“A traveler. It’s dangerous to be wandering around at a time like this.”

[P20]
The gleam in his eyes told me he was a dangerous man.

[P21]
Of course, at Level 25, he didn’t even qualify as a threat to me.

[P22]
“Wow, a four-horse carriage and a gorgeous woman. You must be a Young Master from a wealthy family, huh?”

[P23]
If he had come closer to inspect it, he could have seen the crest of the Jin Family of Taiyuan carved into the carriage. But it was pitch-black outside, and he didn’t possess particularly sharp eyesight.

[P24]
“I’m not from a poor family.”

[P25]
“Well now. You’ve been awfully informal with me from the start.”

[P26]
The leader licked his split lips. He seemed to be getting irritated, but he still hadn’t let down his guard around me.

[P27]
“Whatever. This is a place we’ve been staying in for several days… What are you going to do?”

[P28]
“Do about what?”

[P29]
“What do you think? If you show us a little sincerity, we might let you have the place.”

[P30]
“Anyone listening would think you owned this shrine.”

[P31]
“It’s abandoned. Doesn’t that mean whoever claims it first owns it?”

[P32]
“Then go get a certified property document.”

[P33]
“What?”

[P34]
The leader turned toward his men with a bewildered expression. Naturally. They had probably never heard the term in their lives. But it wasn’t as though any of them would know what it meant.

[P35]
I clicked my tongue at the men whispering among themselves about the certified property document.

[P36]
“If you can’t prove it, then leave quietly. And release the people you’ve tied up.”

[P37]
“…You’re crossing the line. Are you waiting for bodyguards?”

[P38]
“I don’t have any.”

[P39]
“Then what are you relying on?”

[P40]
“Me.”

[P41]
The leader’s gaze shifted to my two empty hands.

[P42]
“Without even a weapon?”

[P43]
“People at your level? My fists are enough.”

[P44]
“Looks like the Young Master learned a move or two somewhere… But aren’t you taking Murim a little too lightly?”

[P45]
“Murim isn’t something to laugh at. You are.”

[P46]
The moment I stepped toward the brightly burning torch, the prisoners who had been quietly restrained began screaming.

[P47]
“Wh-what?”

[P48]
“Boss! Boss!”

[P49]
“You bastards gone crazy? Shut your mouths!”

[P50]
The men in the rear drew daggers and held them to the prisoners’ throats in response to their violent reaction. The leader stared at me with wary eyes.

[P51]
“Do you know them?”

[P52]
“No. I’m seeing them for the first time in my life.”

[P53]
Their sudden reaction had even caught me off guard. And why were they suddenly calling me Boss?

[P54]
“Bosss! It’s me! It’s us!”

[P55]
“These men seem to know you.”

[P56]
“They’re just asking me to save them… Huh?”

[P57]
I looked closely at the prisoners. They were all short as children and had uniformly ugly faces. They looked vaguely familiar.

[P58]
*Is it because their body shapes resemble goblins?*

[P59]
Wait. Goblins?

[P60]
A memory from long ago suddenly came to mind. No, it wasn’t actually that long ago. It had happened only a few months earlier, during the tutorial Quest.

[P61]
“Don’t tell me… You were with the Heavenly Axe?”

[P62]
The prisoners—or rather, the Five-Colored Ghosts[^1] who had once been Jang Sam the Heavenly Axe’s subordinates—nodded frantically.

[P63]
“That’s us!”

[P64]
“Boss! Please save us!”

[P65]
I never expected to run into these bastards here. As I stood there dumbfounded, Wolhwa, who had been watching the situation from behind, asked,

[P66]
“Are these people acquaintances of Young Master Jin?”

[P67]
“We’ve met before, at least.”

[P68]
Human traffickers and bandits. It was hard to say which was worse.

[P69]
Until a moment ago, I had been thinking of saving them. Now I was having second thoughts.

[P70]
“Bosssss!”

[P71]
“Are you planning to abandon us?”

[P72]
“We quit being bandits after that day and have lived good lives ever since!”

[P73]
“…”

[P74]
Their ability to read the situation was almost supernatural. No wonder. They had surrendered immediately when the Heavenly Axe died, after all.

[P75]
“Are you going to save them?”

[P76]
“Tsk. I think we have to, at least.”

[P77]
They said they had become new men after that day, and it felt wrong to leave them like this. More importantly, former bandits were far better than active human traffickers.

[P78]
The leader, who had overheard our conversation, interrupted with a growl.

[P79]
“Save them? You?”

[P80]
“You heard the whole thing. Why ask again? You must live a tiring life.”

[P81]
“You little shit, I’ve been letting you run your mouth, but…”

[P82]
*Clang!*

[P83]
The leader leveled his spear at me, and his men drew their weapons as well. Wolhwa clung to my side with a deliberately frightened expression.

[P84]
“Oh my, I’m scared. You have to protect me, don’t you?”

[P85]
Her moist eyes stirred a man’s protective instinct. Her expression was pleading.

[P86]
To someone who knew Wolhwa’s true nature, it was an absurd sight. But the men swallowed hard.

[P87]
“There’s one more reason I have to kill you.”

[P88]
At the leader’s lecherous gaze, Wolhwa let out a shriek.

[P89]
“Oh no, oh no! This maiden is so scared!”

[P90]
“Ho ho, don’t be so frightened. Though I may have lived a rough life, you’ll soon learn that I’m a man with a heart as soft as silk. In a little while, we can have a conversation with our bodies.”

[P91]
“Before that, deal with me.”

[P92]
I needed to rip that filthy mouth open so he would never say anything like that again.

[P93]
I strode toward him, then suddenly stopped. Seeing that, the leader burst out laughing.

[P94]
“What’s wrong? Are you scared now that we’re actually going to fight? But it’s already too late.”

[P95]
“Yeah. You’re really screwed.”

[P96]
“…What?”

[P97]
I gave the bewildered man a broad smile.

[P98]
“I said you’re fucked, asshole.”

[P99]
The moment I finished speaking, the ground shook, and a powerful wind whipped through the area.

[P100]
*Boom—whoosh!*

[P101]
It lasted no more than an instant.

[P102]
The figure that swept past Wolhwa and me at terrifying speed was already standing in front of the leader.

[P103]
“Say that again.”

[P104]
Jin Mukyung.

[P105]
An overwhelming wave of qi poured from his entire body and crushed the entire scene. The leader’s face turned deathly pale, and his hands began to tremble.

[P106]
“F-forgive me. Please…”

[P107]
The cold voice answered.

[P108]
“You’re far too late.”

[P109]
* * *

[P110]
Perhaps Jin Mukyung was the greatest pacifist among us. In just over ten seconds, he had put an end to all the unnecessary fighting that would have followed.

[P111]
“S-surrender! We surrender!”

[P112]
“Please spare us! Please, just spare our lives…”

[P113]
Their faces were frozen with terror. Everyone’s legs gave out, and they collapsed where they stood. Someone’s urine trickled down the hill.

[P114]
The Five-Colored Ghosts were no different.

[P115]
“Quiet.”

[P116]
Jin Mukyung wiped the blood from his face and tossed out a single word. A deathly silence descended.

[P117]
Hyuk Mujin, one eye bruised deep blue, whispered to me,

[P118]
“Am I actually alive right now?”

[P119]
“Yeah. Your breath against my ear is giving me goose bumps, so move away.”

[P120]
“Just a moment ago, I was thinking, *How can someone get beaten like a dog this badly?* But now…”

[P121]
*Gulp.*

[P122]
Hyuk Mujin swallowed dryly, his gaze fixed on the fallen leader.

[P123]
“Hng… Hng…”

[P124]
With all four limbs broken and his dantian destroyed, the man struggled for breath. If he received proper care, he might be able to walk again, but his life as a martial artist was over.

[P125]
The Level window I sensed through Qi Sense was proof.

[P126]
> **System**
>
> **Level 2 — Lee Sam**

[P127]
*The dung flies the watchers used as Familiars were Level 1, if I remember correctly.*

[P128]
The culprit who had turned a Level 25 martial artist who had once been close to First Rate into a living corpse had been sneaking glances in our direction for a while.

[P129]
“Captain, please save me. I think the Second Young Master is still short on blood.”

[P130]
“Stop talking nonsense and move that guy somewhere suitable. He’ll die if you leave him like that.”

[P131]
“Isn’t he a bastard who deserves to die? They were selling perfectly innocent commoners.”

[P132]
“Even so, move him. He’s still alive.”

[P133]
One of the greatest sources of dissonance I had felt while moving between Murim and the modern world was the issue of killing people.

[P134]
For twenty-seven years, I had lived in a society where law and order existed.

[P135]
I had trained to kill enemies with bladed weapons, but my targets had been monsters, not living humans.

[P136]
*I was sure that was the case…*

[P137]
Now I couldn’t even remember how many people I had killed. Even when I realized that the enemies who had died by my hand might have been real people rather than NPCs, I hadn’t felt particularly guilty.

[P138]
*They were enemies. They were trying to kill me too.*

[P139]
I didn’t know whether it was because I had lived as a Hunter or because I had grown accustomed to Murim’s ways. I was only surprised by my own numbness and the simplicity of my self-justification.

[P140]
*For now, maybe this much is okay.*

[P141]
I was living in two entirely different worlds. This wasn’t a situation where I had the leisure to put on an awkward act as a Buddhist.

[P142]
Shaking off the thoughts clinging to me, I approached the men cowering on the ground.

[P143]
“Eek!”

[P144]
“Uaaagh! Save me, Boss!”

[P145]
“These guys cause a commotion even when I’m trying to save them. Hold still.”

[P146]
I untied the ropes, and the Five-Colored Ghosts were free. They stood on trembling legs.

[P147]
“Th-thank you.”

[P148]
“We’ll regard you as our Benefactor for the rest of our lives!”

[P149]
“Like hell you will. Anyway, how did you end up getting caught by men like these? All five of you at once?”

[P150]
The Five-Colored Ghosts were small, but they were grown men, at least in name. They had been strong enough to commit banditry alongside the Heavenly Axe.

[P151]
“Um, well…”

[P152]
“…?”

[P153]
What was wrong with these guys?

[P154]
Sensing something strange in their hesitation, I grabbed the nearest human trafficker by the collar and hauled him up.

[P155]
“How did you catch these men?”

[P156]
“We caught them trying to steal our money pouches in the marketplace.”

[P157]
“…”

[P158]
What the hell, these Ten-Colored Ghosts. I thought they had quit being bandits and might have taken up farming, but they had only changed occupations?

[P159]
“Explain yourselves.”

[P160]
Under my sharp gaze, the five men rolled their eyes back and forth.

[P161]
“W-well…”

[P162]
“Boss, people like us only know how to do this.”

[P163]
“Even so, we only started recently!”

[P164]
“We tried to work honestly, but things didn’t go very well… We said we’d pull just one job and get out, but then…”

[P165]
“If we’d known they were mounted bandits, we wouldn’t have touched them. We’re victims too. Boss, please forgive us just this once!”

[P166]
As I wondered what to do with these men, a familiar word made me pause.

[P167]
“What did you say?”

[P168]
“We’ll live honestly if you forgive us just one more time!”

[P169]
“No, not that. What did they say?”

[P170]
“Ah, do you mean the mounted-bandit group?”

[P171]
“Yes. That.”

[P172]
“We only heard after we were captured. Some bunch of ruffians were throwing silver around at a pleasure house, so we followed them… But they turned out to be members of the Red Wind Band, infamous for their viciousness even among mounted bandits.”

[P173]
“The Red Wind Band? Are you sure?”

[P174]
“Yes. I heard it clearly with my own ears. Didn’t I?”

[P175]
The others began eagerly adding their own pieces.

[P176]
“They said they were leaving as soon as dawn broke tomorrow.”

[P177]
“They said they’d have to travel nonstop to reach Saneum. They were even worried that they might lose their heads if they arrived late.”

[P178]
“So that’s how it is.”

[P179]
Yesterday and today.

[P180]
It was already an uncanny coincidence that the mounted bandits I had encountered two days in a row happened to belong to the Red Wind Band. On top of that, Saneum was close to Eung-hyeon, where the Mount Heng Sword Sect’s headquarters was located.

[P181]
“Are these men telling the truth?”

[P182]
The human trafficker held by the collar in my right hand—or rather, the mounted bandit from the Red Wind Band—nodded with a trembling head.

[P183]
That was when it happened.

[P184]
*Shriek!*

[P185]
A hawk landed in front of the shrine with a sharp cry. A small cylinder tied to its ankle caught my eye.

[P186]
*A messenger hawk.*

[P187]
This was getting strange.

[P188]
[^1]: A nickname meaning “Five-Colored Ghosts.”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 월화     | **Wolhwa**         |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 마적     | **mounted bandits**                              |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 은자 | **silver nyang** | Silver currency unit. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 108,
  "passed": true,
  "metrics": {
    "source_characters": 5908,
    "translation_characters": 12571,
    "length_ratio": 2.128,
    "source_paragraphs": 182,
    "translation_paragraphs": 188
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "귀가",
        "preferred": "your family"
      }
    },
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
        "korean": "은자",
        "preferred": "silver nyang"
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
