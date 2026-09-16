# Fidelity Gate — Chapter 107

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
  1|＃107화
  2|
  3|
  4|
  5|사두마차는 목적지를 향해 부드럽게 이동했다. 어제와 같은 말, 같은 마차임에도 승차감은 차원이 달랐다. 마부가 교체되었기 때문이다.
  6|
  7|겨우 마부석을 벗어나 내 옆자리에 앉은 혁무진이 속 편한 얼굴로 말했다.
  8|
  9|“역시 사람은 각자 타고나는 게 있나 봐요. 전 마차 모는 건 영 젬병이라.”
 10|
 11|젬병 같은 소리 하네.
 12|
 13|하오문 산서지부장인 월화가 데려온 사람이다. 당연히 평범한 마부일 리가 없다.
 14|
 15|묵묵하게 말고삐를 잡고 있는 그는 50레벨의 일류 무인이었다. 마부 겸 호위무사, 딱 그림이 나온다.
 16|
 17|“무진아.”
 18|
 19|“네?”
 20|
 21|“제발 조용히 좀 가자. 그럼 중간이라도 간다.”
 22|
 23|“……맨날 나만 갖고 뭐라 하셔.”
 24|
 25|“네가 맨날 헛소리만 하니까 그렇지, 인마.”
 26|
 27|맞은편에 앉아 우리를 지켜보던 월화가 실소를 흘렸다.
 28|
 29|“두 사람, 격의 없는 모습이 보기 좋네요.”
 30|
 31|“저놈이 싸가지가 없는 겁니다.”
 32|
 33|“싸가지라뇨. 이런 말까지는 안 하려고 했는데, 제가 조장보다 두 살이나 더 많습니다. 제 친구들은 애도 있어요.”
 34|
 35|“넌 없잖아.”
 36|
 37|“아니, 뭐. 그렇긴 한데요.”
 38|
 39|“그리고 네가 스물둘이어도 나보다 어려. 아무튼, 어려.”
 40|
 41|“그게 무슨 소립니까. 조장님이 이제 겨우 약관인 건 산서성 똥개들도 다 아는 사실인데.”
 42|
 43|“못 믿겠으면 한판 붙든가.”
 44|
 45|“……다른 분들도 계시니까 여기까지만 하겠습니다.”
 46|
 47|혁무진의 추한 변명에 월화가 활짝 웃었다.
 48|
 49|“어머, 난 괜찮은데? 여기 진 소협은 어떨지 모르겠지만.”
 50|
 51|자연스럽게 모두의 시선이 한 사람을 향해 쏠린다.
 52|
 53|아까부터 입을 꾹 다물고 있던 진무경이 움찔하더니 입을 열었다.
 54|
 55|“나, 난 상관없소.”
 56|
 57|“……?”
 58|
 59|뭐야, 저놈 지금 말 더듬은 거야?
 60|
 61|예상치 못한 반응에 눈을 동그랗게 뜨고 바라보자 진무경이 슬쩍 시선을 회피했다.
 62|
 63|‘어어, 점점.’
 64|
 65|원래 저런 캐릭터가 아닌데. 평소 같았으면 뭘 쳐다보냐고 눈을 부라릴 녀석인데.
 66|
 67|나는 진심을 담아 물었다.
 68|
 69|“어디 아파?”
 70|
 71|“……전혀.”
 72|
 73|“대화할 때는 사람 눈을 보고 해야지.”
 74|
 75|“……시끄럽다. 말 걸지 마.”
 76|
 77|오늘따라 참 요상하네, 진짜.
 78|
 79|절정 고수씩이나 되는 인간이 마차 멀미에 걸렸을 리는 없고.
 80|
 81|아침까지만 해도 팔팔하더니 어째 상태가 영 아니다.
 82|
 83|‘그러고 보니까 마차 타고 나서부터 저렇게 된 것 같은데.’
 84|
 85|눈을 가늘게 뜨고 진무경을 바라보던 그때.
 86|
 87|쿡쿡.
 88|
 89|슬쩍 옆구리를 찌른 혁무진이 내게만 들릴 정도로 작은 목소리로 속삭였다.
 90|
 91|“이공자님 좀 보세요.”
 92|
 93|“뭐가…… 아.”
 94|
 95|혁무진의 말을 들은 후에야 이상한 광경이 눈에 띄었다.
 96|
 97|어떻게 지금까지 눈치채지 못했나 싶을 정도다.
 98|
 99|‘뭐지?’
100|
101|태원진가에서 가져온 사두마차는 상당히 호화롭다. 어지간한 방 하나 크기라 좌석도 넓었다. 지금 인원의 두 배를 태워도 무리가 없을 정도다.
102|
103|그런데…….
104|
105|‘쟤는 왜 저러고 있어.’
106|
107|현재 진무경은 넓은 좌석을 두고 마차 끄트머리 구석에 몸을 구겨 넣고 있었다. 아니, 저 정도면 거의 압축 수준이다.
108|
109|‘9와 4분의 3 승강장이야, 뭐야.’
110|
111|천무학관이 아니라 마법 학교를 다니고 있는 건가.
112|
113|한편 저 괴상한 짓거리를 지켜보고 있는 것은 나와 혁무진만이 아니었다.
114|
115|“진 소협. 많이 불편해 보이는데 이쪽으로 좀 오세요. 자리 많이 남아요.”
116|
117|월화의 고혹적인 목소리에 덜컥 굳는 진무경의 신형.
118|
119|삐걱거리는 대답이 흘러나온 건 잠시 후였다.
120|
121|“괘, 괜찮소.”
122|
123|“…….”
124|
125|하나도 안 괜찮아 보이는데. 나와 비슷한 표정을 짓고 있는 혁무진에게 조용히 속삭였다.
126|
127|“네가 봐도 이상하지?”
128|
129|“이상한 정도가 아닌데요.”
130|
131|“그래, 나도 비슷한 생각이야.”
132|
133|우리는 의미심장한 눈빛을 주고받았다.
134|
135|“세상에, 누가 상상이나 했겠습니까.”
136|
137|“그러게. 천하의 진천검이 저렇게 낯가림이 심할 줄이야.”
138|
139|“제 말이 그 말…… 예?”
140|
141|“반응이 왜 그래? 사람 성격 가지고 뭐라 하면 안 돼. 나처럼 낯짝 두꺼운 놈이 있으면 소심한 사람도 있는 거야.”
142|
143|“아니, 잠시만. 잠시만요.”
144|
145|혁무진이 더듬거리며 말을 이었다.
146|
147|“지금 무슨 말씀을 하시는 거예요?”
148|
149|“그야 당연히 진무경…….”
150|
151|으스스한 목소리가 불쑥 끼어들었다.
152|
153|“입 다물어.”
154|
155|아무리 넓어 봤자 마차 안이니 다 들린다. 진무경의 찢어 죽일 듯한 눈빛에 나와 혁무진이 동시에 입을 다물었다.
156|
157|살벌한 분위기를 환기시킨 건 월화였다.
158|
159|“내 정신 좀 봐, 아직 정식으로 인사드린 적이 없네요. 하오문 산서지부장 월화라고 합니다.”
160|
161|“……태원진가의 진무경이오.”
162|
163|“반응이 영 심심하네요. 저기 진 공자는 처음 제 신분을 듣고 엄청나게 놀랐는데.”
164|
165|“저 녀석에게 대충 들어서 알고는 있었소. 본가를 위해 큰일을 해 주셨다는 이야기도.”
166|
167|진무경이 정중하게 포권을 취했다.
168|
169|“늦었지만 감사를 표하오.”
170|
171|“별말씀을. 정당한 거래였어요.”
172|
173|월화가 매끄럽게 한 마디를 덧붙였다.
174|
175|“아직 적절한 보상은 못 받았지만요.”
176|
177|“본가는 하오문의 호의를 잊지 않을 거요.”
178|
179|아직도 어색하기 짝이 없는 행동과 말투지만 그래도 처음보다는 썩 나아진 모습이다.
180|
181|미남과 미녀의 그림 같은 투샷에 혁무진이 감탄사를 토했다.
182|
183|“촉망받는 젊은 고수와 절세의 미녀라…… 크으, 보기만 해도 가슴이 뛰는군요. 안 그렇습니까?”
184|
185|나는 못 들은 척 고개를 돌렸다.
186|
187|피부가 따끔거릴 정도로 살기 어린 시선을 보아하니, 혁무진의 가슴이 뛸 시간은 얼마 남지 않은 게 분명했다.
188|
189|
190|
191|* * *
192|
193|
194|
195|겨울의 낮은 성미가 급하다.
196|
197|산길을 따라 얼마나 이동했을까, 금세 해가 지고 어둠이 찾아왔다. 마차가 멈춘 것은 그로부터 두 시진이 지난 후, 자정 무렵이었다.
198|
199|“도착했습니다.”
200|
201|마차에서 내리자마자 보이는 것은 적당한 크기의 목제 건물이었다.
202|
203|안으로 발을 내딛자마자 느껴지는 싸늘한 공기. 사람을 본뜬 동상은 위엄 있게 우리를 내려다보고 있었다. 이런 곳을 뭐라고 하더라?
204|
205|‘아, 그래. 사당(祠堂).’
206|
207|죽은 이의 위패를 모시고 제사를 지내는 장소라고 들었다.
208|
209|무협 소설에서 심심하면 등장하는 관제묘(關帝廟)가 떠올라 동상을 살펴봤지만 누군지는 알 수 없었다.
210|
211|“수년 전 기근 이후로 버려진 사당인데, 지금도 간혹 인근 양민들이 오는 모양이에요.”
212|
213|월화의 말처럼 사당 내부는 휑했지만 아직 사람의 흔적이 남아 있었다. 이를테면 먼지 쌓인 바닥 위로 찍혀 있는 사람의 발자국이라든가.
214|
215|“자리를 준비하겠습니다.”
216|
217|하오문도로 짐작되는 마부 겸 호위무사의 말에 우리는 사당 밖으로 나왔다. 아니, 정확히 말하면 한 명은 누군가에 의해 끌려 나왔다고 해야 맞겠다.
218|
219|“따라와라.”
220|
221|“으헉, 조장님, 조장님!”
222|
223|진무경에게 멱살을 잡힌 채 질질 끌려가는 혁무진을 외면하고 하늘을 바라봤다. 음, 오늘은 달이 참 밝구나.
224|
225|“뭐 해요?”
226|
227|“뭐, 보시는 대로죠.”
228|
229|월화가 싱긋 웃었다.
230|
231|“경치 구경하는 거 좋아하나 봐요?”
232|
233|“요즘 들어서 좋아지고 있어요.”
234|
235|현대에서 볼 수 있는 경치라고 해 봐야 높은 곳에서 내려다보이는 야경이다. 그마저도 직장인들의 야근이 만들어 낸 슬픈 불빛들이고.
236|
237|‘이런 게 진짜 경치지.’
238|
239|빽빽한 빌딩 숲도, 아파트 단지와 공장 부지도 없다.
240|
241|아스팔트 도로 대신 축축한 흙길과 청량한 공기가 온 세상에 가득하다.
242|
243|‘이런 곳에서 살면 힐링 제대로 될 텐데.’
244|
245|문제는 킬링 당하기도 쉬운 동네라는 거다. 어떻게 된 게 여기는 몬스터보다 사람이 더 무섭다.
246|
247|굳이 대장로나 조필까지 갈 필요도 없이, 바로 어제 봉황객잔에서 있었던 일만 해도 그렇다.
248|
249|“아, 맞다. 그놈들은 어떻게 됐어요?”
250|
251|“적풍단(赤風團)의 마적들을 말하는 거라면 구금해 뒀어요. 물론 그 전에 의원을 불러야 했죠.”
252|
253|그 정도로 개박살을 내 줬으니 치료가 필요하긴 했을 거다.
254|
255|그러나 그보다 관심을 끄는 단어가 있었다.
256|
257|“적풍단이요?”
258|
259|“고원에서 떠오르는 신흥 강자예요. 규모도 제법 크고, 무엇보다 우두머리인 적풍단주의 무공이 고강하다고 알려져 있어요.”
260|
261|북부 고원. 항산검문과의 전쟁 당시 지도를 통해 처음으로 알게 된 지명이다.
262|
263|한 가지 의아한 점은, 봉황객잔이 있는 혼주와 고원의 거리가 상당하다는 것이었다. 밤낮으로 말을 달려도 일주일 이상이 소요되는 걸로 알고 있는데…….
264|
265|“그런 놈들이 어떻게 여기까지 흘러들어온 겁니까?”
266|
267|“이천백은 전쟁 말미에 수많은 낭인과 마적단들을 고용했어요. 그중 상당수는 팔천협에서 뼈를 묻었지만, 일부는 살아남아 도망쳤죠.”
268|
269|“그중에 적풍단이 있었다?”
270|
271|월화가 고개를 저었다.
272|
273|“적풍단주…… 생각 이상으로 머리 회전이 빠른 자더군요.”
274|
275|“그럼?”
276|
277|“그는 마지막까지 사태를 지켜봤어요. 불과 두 시진 떨어진 거리에서 팔천협을 예의 주시하다가 전투 결과를 듣고 말 머리를 돌렸죠. 자신을 따르는 이백 명의 수하와 함께.”
278|
279|자그마치 이백 명.
280|
281|만약 그날 팔천협에서 적풍단이 가세했다면 어떻게 되었을까? 엄청난 사상자가 나오는 건 물론이고 전투의 승패에도 영향을 끼쳤을지도 모른다.
282|
283|“우리로서는 행운이었네요.”
284|
285|“그렇죠. 항산검문 입장에서는 엄청난 불운이었고.”
286|
287|월화가 곰방대에 담뱃잎을 꾹꾹 눌러 담으며 말을 이었다.
288|
289|“적풍단은 그 길로 북상했어요. 대부분의 병력이 빠져나간 항산검문의 본진을 노린 거죠.”
290|
291|“……허.”
292|
293|그야말로 타고난 약탈자다.
294|
295|전쟁의 승기가 한쪽으로 기울자마자 북상, 대부분의 주력이 빠져나간 항산검문의 목덜미를 물어뜯은 것이다.
296|
297|전투에 참여하지 않은 덕분에 병력을 보존한 건 물론이고 충분한 휴식도 취했을 테니, 컨디션은 최상이었겠지.
298|
299|“결과는 진 공자도 들어서 알죠?”
300|
301|“네.”
302|
303|이틀 동안 이어진 치열한 전투는 결국 항산검문의 승리로 막을 내렸다. 아버지를 뒤를 이어야 할 소문주의 죽음을 남기고.
304|
305|“그런데 제가 들은 소문으로는 낭인과 마적들이 섞여 있었다고 하던데요.”
306|
307|“호랑이가 이빨이 빠졌다고 해서 개라고 부르진 않는 법. 적풍단주가 끌어들인 낭인들도 제법 되죠. 방패막이로 사용하기에는 딱 좋았을 테니까.”
308|
309|탁, 탁.
310|
311|화섭자를 꺼내 불을 붙인 그녀가 곰방대를 빨아들였다.
312|
313|“진 공자가 쓰러트린 마적들은 아마도 그때 도망친 자들일 거예요. 적풍단이 마적단치고 제법 규율이 강하긴 해도 탈영병이 아예 없진 않으니까. 혼주에서 뭘 하고 있었는지는 잘 모르겠지만요.”
314|
315|“탈영병이라…….”
316|
317|“그것 때문에 근래 들어 이 근방이 어수선해요. 낭인, 산적, 마적, 심지어는 흑도들까지 슬쩍 고개를 들고 있는데 항산검문의 힘은 형편없이 줄어들었으니까.”
318|
319|“우리의 제안을 받아들일 수밖에 없겠네요.”
320|
321|월화가 새치름하게 웃어 보였다.
322|
323|“정확히 말하면 우리, 가 아니라 태원진가겠죠? 뭐, 내 입장에서도 신임 문주를 핍박하기 좋은 때라는 건 맞지만.”
324|
325|“저기, 그런데요.”
326|
327|“응?”
328|
329|“이런 날씨에도 사당에 오는 양민들이 있습니까?”
330|
331|“그럴 리가요. 사냥꾼들이라면 몰라도. 그런데 갑자기 그건 왜?”
332|
333|나는 산길을 가리켰다. 어느새 휘날리기 시작한 엷은 눈보라 사이로, 이쪽을 향해 올라오는 횃불들이 보였다.
```

## Assembled English

```markdown
[P1]
# Chapter 107

[P2]
The four-horse carriage rolled smoothly toward our destination. Though the horses and carriage were the same as yesterday, the difference in ride quality was night and day.

[P3]
We had a new driver.

[P4]
Having finally escaped the driver’s seat and settled beside me, Hyuk Mujin said with a carefree expression, “I guess everyone has their own natural talents. I’m hopeless at driving a carriage.”

[P5]
*Hopeless, my ass.*

[P6]
This was a man Wolhwa, the Lower District Sect’s Shanxi Branch Leader, had brought with her. Naturally, he was no ordinary coachman.

[P7]
The man silently holding the reins was a Level 50 First Rate martial artist. A coachman and a bodyguard—the picture fit perfectly.

[P8]
“Mujin.”

[P9]
“Yes?”

[P10]
“Please, just keep quiet. Then you’ll at least do okay.”

[P11]
“……Why am I always the one you pick on?”

[P12]
“Because you’re always spouting nonsense, you idiot.”

[P13]
Wolhwa, who was sitting across from us and watching, let out a quiet laugh.

[P14]
“It’s nice to see how comfortable you two are with each other.”

[P15]
“He just has no respect.”

[P16]
“No respect? I wasn’t going to bring this up, but I’m two years older than you, Captain. Some of my friends already have children.”

[P17]
“You don’t.”

[P18]
“Well, no. That’s true.”

[P19]
“And even if you were twenty-two, you’d still be younger than me. Anyway, you’re younger.”

[P20]
“What are you talking about? Even the stray dogs of Shanxi Province know you’ve only just turned twenty.”

[P21]
“If you don’t believe me, fight me.”

[P22]
“……Since we have company, I’ll leave it at that.”

[P23]
Wolhwa beamed at Hyuk Mujin’s ugly excuse.

[P24]
“Oh, I don’t mind. Though I can’t speak for Young Hero Jin over here.”

[P25]
Everyone’s eyes naturally turned toward one person.

[P26]
Jin Mukyung, who had kept his mouth firmly shut until now, flinched before speaking.

[P27]
“I-I don’t mind.”

[P28]
“……?”

[P29]
*What the hell? Did he just stutter?*

[P30]
My eyes widened at the unexpected response, and Jin Mukyung subtly looked away.

[P31]
*Oh, this is getting worse.*

[P32]
He wasn’t usually like this. Normally, he would have glared and demanded to know what I was staring at.

[P33]
I asked him sincerely, “Are you sick?”

[P34]
“……Not at all.”

[P35]
“You should look people in the eye when you talk to them.”

[P36]
“……Shut up. Don’t talk to me.”

[P37]
He was acting really strange today.

[P38]
There was no way a Peak master like him had gotten motion sickness.

[P39]
He had been full of energy until this morning, but now he was clearly not himself.

[P40]
*Come to think of it, he seems to have been like this ever since we got into the carriage.*

[P41]
Just as I was narrowing my eyes and watching Jin Mukyung—

[P42]
*Poke, poke.*

[P43]
Hyuk Mujin nudged me in the side and whispered so quietly that only I could hear.

[P44]
“Look at the Second Young Master.”

[P45]
“What about him…? Ah.”

[P46]
Only after hearing Hyuk Mujin did I notice the bizarre sight.

[P47]
I couldn’t believe I had missed it until now.

[P48]
*What is he doing?*

[P49]
The four-horse carriage brought from the Jin Family of Taiyuan was quite luxurious. The interior was about the size of an ordinary room, with seats spacious enough to accommodate twice our number without trouble.

[P50]
And yet…

[P51]
*Why is he sitting like that?*

[P52]
Despite all the available space, Jin Mukyung had crammed himself into the farthest corner of the carriage. No, *crammed* didn’t quite cover it. He was practically compressed.

[P53]
*What is this, Platform Nine and Three-Quarters?*

[P54]
Was he attending a magic school instead of Heaven’s Gate Temple?

[P55]
Hyuk Mujin and I weren’t the only ones watching his strange behavior.

[P56]
“Young Hero Jin, you look very uncomfortable. Why don’t you come over here? There’s plenty of room.”

[P57]
Jin Mukyung went rigid at the sound of Wolhwa’s alluring voice.

[P58]
His creaking reply came a moment later.

[P59]
“I-I’m fine.”

[P60]
“……”

[P61]
He didn’t look fine at all.

[P62]
I quietly whispered to Hyuk Mujin, who wore an expression much like mine.

[P63]
“You think he’s acting strange too, right?”

[P64]
“This goes beyond strange.”

[P65]
“Yeah, that’s what I thought.”

[P66]
We exchanged meaningful glances.

[P67]
“My goodness. Who would’ve imagined?”

[P68]
“Exactly. Who knew the great Heaven Shaking Sword was so shy around strangers?”

[P69]
“That’s exactly what I—huh?”

[P70]
“Why are you reacting like that? You shouldn’t criticize someone for their personality. If there are thick-skinned bastards like me, there can be timid people too.”

[P71]
“No, wait. Just wait a moment.”

[P72]
Hyuk Mujin stumbled over his words.

[P73]
“What exactly are you talking about?”

[P74]
“Obviously, Jin Mukyung…”

[P75]
An eerie voice suddenly cut in.

[P76]
“Shut up.”

[P77]
No matter how spacious it was, we were still inside a carriage. Everyone could hear us.

[P78]
Faced with Jin Mukyung’s murderous glare, Hyuk Mujin and I shut our mouths at the same time.

[P79]
Wolhwa was the one who dispelled the grim atmosphere.

[P80]
“Where are my manners? I haven’t properly introduced myself yet. I’m Wolhwa, Shanxi Branch Leader of the Lower District Sect.”

[P81]
“……I am Jin Mukyung of the Jin Family of Taiyuan.”

[P82]
“What a dull reaction. Young Master Jin over there was extremely surprised when he first learned who I was.”

[P83]
“I heard the general details from him. I also heard that you rendered our family a great service.”

[P84]
Jin Mukyung politely clasped his hands.

[P85]
“Though it comes late, allow me to express my gratitude.”

[P86]
“Not at all. It was a fair transaction.”

[P87]
Wolhwa smoothly added, “Though I have yet to receive proper compensation.”

[P88]
“Our family will not forget the Lower District Sect’s goodwill.”

[P89]
His behavior and manner of speaking were still awkward beyond belief, but he was doing much better than when they had first met.

[P90]
Looking at the handsome man and beautiful woman sitting together like a picture, Hyuk Mujin exclaimed,

[P91]
“A promising young martial arts master and a peerless beauty… Whew, just looking at them makes my heart race. Don’t you agree?”

[P92]
I turned away and pretended not to hear him.

[P93]
Judging by the killing intent prickling my skin, Hyuk Mujin’s heart wouldn’t be racing much longer.

[P94]
* * *

[P95]
Winter days were short-tempered.

[P96]
How long had we traveled along the mountain road? The sun quickly set, and darkness descended. The carriage stopped two shichen later, around midnight.

[P97]
“We’ve arrived.”

[P98]
The first thing I saw upon stepping out of the carriage was a moderately sized wooden building.

[P99]
A chill greeted me the moment I entered. A statue in human form gazed solemnly down at us.

[P100]
*What did they call places like this again?*

[P101]
*Oh, right. A shrine.*

[P102]
I had heard they were places where the spirit tablets of the dead were enshrined and memorial rites performed.

[P103]
The Guandi Temples that appeared at the drop of a hat in martial arts novels came to mind. I examined the statue, but I couldn’t tell who it depicted.

[P104]
“This shrine was abandoned after a famine several years ago, but it seems the local commoners still visit from time to time.”

[P105]
Just as Wolhwa had said, the shrine’s interior was bare, but signs of human presence remained—footprints in the dust covering the floor, for instance.

[P106]
“I’ll prepare the place.”

[P107]
At the words of the coachman and bodyguard, whom I assumed to be a member of the Lower District Sect, we headed outside.

[P108]
More precisely, one of us was dragged out by someone.

[P109]
“Follow me.”

[P110]
“Gah! Captain! Captain!”

[P111]
I ignored Hyuk Mujin as Jin Mukyung dragged him away by the collar and looked up at the sky.

[P112]
*Hmm. The moon sure is bright tonight.*

[P113]
“What are you doing?”

[P114]
“As you can see.”

[P115]
Wolhwa smiled faintly.

[P116]
“You seem to enjoy looking at the scenery.”

[P117]
“I’ve been getting into it lately.”

[P118]
The only scenery to be found in the modern world was the nightscape seen from some high vantage point. Even that consisted of sad lights created by office workers working overtime.

[P119]
*Now this is real scenery.*

[P120]
There were no dense forests of skyscrapers, apartment complexes, or industrial sites.

[P121]
In place of asphalt roads, damp dirt paths and crisp air filled the entire world.

[P122]
*Living in a place like this would be genuinely healing.*

[P123]
The problem was that it was also an easy place to get killed.

[P124]
Somehow, people were more frightening here than monsters.

[P125]
I didn’t even need to go as far as the Head Elder or Jopil. What had happened at the Phoenix Inn just yesterday was enough.

[P126]
“Oh, right. What happened to those guys?”

[P127]
“If you mean the mounted bandits from the Red Wind Band, they’ve been detained. Of course, we had to call a physician first.”

[P128]
I’d beaten the shit out of them, so of course they’d needed treatment.

[P129]
But there was another word that caught my attention more than that.

[P130]
“The Red Wind Band?”

[P131]
They’re a rising power from Gaoyuan. They’re fairly large, and more than anything, the Red Wind Band Leader is said to possess formidable martial arts.

[P132]
Northern Gaoyuan.

[P133]
I had first learned of that place from a map during the war with the Mount Heng Sword Sect.

[P134]
One thing puzzled me. Gaoyuan was a considerable distance from Honju, where the Phoenix Inn was located. As far as I knew, the journey took more than a week even if you rode day and night.

[P135]
“How did people like that end up all the way here?”

[P136]
“Toward the end of the war, Lee Cheonbaek hired countless wandering martial artists and mounted-bandit groups. Many of them met their end at Eight Spring Gorge, but some survived and fled.”

[P137]
“So the Red Wind Band was among them?”

[P138]
Wolhwa shook her head.

[P139]
“The Red Wind Band Leader… He was quicker-witted than I expected.”

[P140]
“Then what happened?”

[P141]
“He watched the situation until the very end. He kept a close eye on Eight Spring Gorge from only two shichen away, then turned his horse around the moment he heard how the battle had ended—along with the two hundred men under his command.”

[P142]
Two hundred people.

[P143]
What would have happened if the Red Wind Band had joined the battle at Eight Spring Gorge that day? There would have been an enormous number of casualties, and it might even have affected the outcome of the battle.

[P144]
“We were lucky.”

[P145]
“We were. For the Mount Heng Sword Sect, it was incredibly unlucky.”

[P146]
Wolhwa continued as she firmly packed tobacco leaves into her long-stemmed pipe.

[P147]
“The Red Wind Band headed north immediately. They targeted the Mount Heng Sword Sect’s main base after most of its forces had withdrawn.”

[P148]
“……Huh.”

[P149]
They were natural-born plunderers.

[P150]
The moment the tide of the war turned, they headed north and sank their teeth into the Mount Heng Sword Sect’s throat while most of its main force was away.

[P151]
They had preserved their forces by staying out of the battle, and they must have been well-rested too. They would have been in peak condition.

[P152]
“Young Master Jin, you heard how it ended, didn’t you?”

[P153]
“Yes.”

[P154]
After two days of fierce fighting, the Mount Heng Sword Sect ultimately emerged victorious—but at the cost of the Young Sect Leader, who was supposed to succeed his father.

[P155]
“But the rumors I heard said that wandering martial artists and mounted bandits were mixed together.”

[P156]
“A tiger doesn’t become a dog just because it has lost its teeth. The Red Wind Band Leader had recruited quite a few wandering martial artists as well. They would have made excellent shields.”

[P157]
*Tap, tap.*

[P158]
Wolhwa took out a fire starter, lit it, and drew on her long-stemmed pipe.

[P159]
“The mounted bandits Young Master Jin defeated were probably the ones who fled at that time. Even if the Red Wind Band is unusually disciplined for a mounted-bandit group, it doesn’t mean they have no deserters at all. I’m not sure what they were doing in Honju, though.”

[P160]
“Deserters…”

[P161]
“That’s why the surrounding area has been so unsettled lately. Wandering martial artists, bandits, mounted bandits, even dark-path figures—they’re all starting to rear their heads now that the Mount Heng Sword Sect’s strength has been so badly diminished.”

[P162]
“They’ll have no choice but to accept our proposal.”

[P163]
Wolhwa gave me a prim smile.

[P164]
“Strictly speaking, it isn’t *our* proposal. It’s the Jin Family of Taiyuan’s, isn’t it? Still, from my perspective, this is certainly a good time to pressure the new Sect Leader.”

[P165]
“By the way…”

[P166]
“Yes?”

[P167]
“Do commoners really visit this shrine in weather like this?”

[P168]
“Of course not. Hunters, perhaps. Why do you ask all of a sudden?”

[P169]
I pointed toward the mountain path.

[P170]
Through the light snowstorm that had begun to swirl, I could see torches climbing toward us.
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
# Chapter 107

[P2]
The four-horse carriage moved smoothly toward its destination. Even though it was the same carriage pulled by the same horses as yesterday, the ride was on an entirely different level.

[P3]
The driver had been replaced.

[P4]
Hyuk Mujin, who had finally escaped the driver’s seat and settled beside me, said with a relaxed expression,

[P5]
“People really must be born with different talents. I’m hopeless at driving a carriage.”

[P6]
*What a load of crap.*

[P7]
He was someone Wolhwa, the Lower District Sect’s Shanxi Branch Leader, had brought with her. Naturally, there was no way he was an ordinary coachman.

[P8]
The man quietly holding the reins was a Level 50 First Rate martial artist. A coachman and a bodyguard. The picture fit perfectly.

[P9]
“Mujin.”

[P10]
“Yes?”

[P11]
“Please just travel quietly. Then you’ll at least do okay.”

[P12]
“……Why am I always the one you pick on?”

[P13]
“Because you’re always spouting nonsense, you idiot.”

[P14]
Wolhwa, who was sitting across from us and watching, let out a quiet laugh.

[P15]
“You two seem very comfortable with each other.”

[P16]
“He’s just rude.”

[P17]
“Rude? I wasn’t going to say this, but I’m two years older than the squad leader. My friends have children.”

[P18]
“You don’t.”

[P19]
“Well, no. That’s true.”

[P20]
“And even if you were twenty-two, you’d still be younger than me. Anyway, you’re younger.”

[P21]
“What are you talking about? Even the stray dogs of Shanxi Province know that the squad leader is barely twenty.”

[P22]
“If you don’t believe me, then let’s have a match.”

[P23]
“……Since there are other people here, I’ll stop at this point.”

[P24]
Wolhwa smiled brightly at Hyuk Mujin’s ugly excuse.

[P25]
“Oh, I don’t mind. Though I can’t speak for Young Hero Jin.”

[P26]
Everyone’s eyes naturally turned toward one person.

[P27]
Jin Mukyung, who had kept his mouth tightly shut until then, flinched and opened it.

[P28]
“I—I don’t mind.”

[P29]
“……?”

[P30]
*What the hell? Did he just stutter?*

[P31]
I stared at him with my eyes wide open at the unexpected response. Jin Mukyung subtly looked away.

[P32]
*Oh, this is getting worse.*

[P33]
He wasn’t usually like this. Normally, he would have glared and asked what I was staring at.

[P34]
I asked him sincerely,

[P35]
“Are you sick?”

[P36]
“……Not at all.”

[P37]
“When you’re talking to someone, you should look them in the eye.”

[P38]
“……Be quiet. Don’t talk to me.”

[P39]
He was acting really strange today.

[P40]
There was no way a Peak master like him had gotten motion sickness.

[P41]
He had been full of energy until this morning, but now he was clearly not himself.

[P42]
*Come to think of it, he seems to have been like this ever since we got into the carriage.*

[P43]
Just as I was narrowing my eyes and watching Jin Mukyung—

[P44]
*Poke, poke.*

[P45]
Hyuk Mujin nudged me in the side and whispered so quietly that only I could hear him.

[P46]
“Look at the Second Young Master.”

[P47]
“Look at what…… Ah.”

[P48]
Only after hearing Hyuk Mujin did I notice the bizarre sight.

[P49]
I couldn’t believe I hadn’t noticed it until now.

[P50]
*What is he doing?*

[P51]
The four-horse carriage brought from the Jin Family of Taiyuan was quite luxurious. The inside was about the size of an ordinary room, and the seats were spacious too. It could have carried twice as many people as we had without any trouble.

[P52]
And yet…

[P53]
*Why is he sitting like that?*

[P54]
Jin Mukyung had ignored the spacious seats and folded himself into the corner at the very end of the carriage.

[P55]
No, “folded” didn’t quite cover it. He was practically compressed.

[P56]
*What is this, Platform Nine and Three-Quarters?*

[P57]
Was he attending a magic school instead of Heaven’s Gate Temple?

[P58]
I wasn’t the only one watching this strange behavior.

[P59]
“Young Hero Jin, you look very uncomfortable. Why don’t you come over here? There’s plenty of room.”

[P60]
Jin Mukyung’s body went rigid at the sound of Wolhwa’s alluring voice.

[P61]
A creaking reply came a moment later.

[P62]
“I—I’m fine.”

[P63]
“……”

[P64]
He didn’t look fine at all.

[P65]
I whispered quietly to Hyuk Mujin, whose expression was similar to mine.

[P66]
“You think he’s acting strange too, right?”

[P67]
“It’s more than strange.”

[P68]
“Yeah. I thought so too.”

[P69]
We exchanged meaningful glances.

[P70]
“My goodness. Who could have imagined this?”

[P71]
“Exactly. Who knew the Heaven Shaking Sword was so shy around people?”

[P72]
“That’s exactly what I mean…… Huh?”

[P73]
“Why are you reacting like that? You shouldn’t criticize someone’s personality. If there are thick-skinned guys like me, then there can be timid people too.”

[P74]
“No, wait. Just wait a moment.”

[P75]
Hyuk Mujin stumbled over his words.

[P76]
“What exactly are you talking about?”

[P77]
“Obviously, Jin Mukyung……”

[P78]
An eerie voice suddenly cut in.

[P79]
“Shut up.”

[P80]
No matter how spacious the carriage was, everyone inside could hear everything.

[P81]
Under Jin Mukyung’s murderous glare, Hyuk Mujin and I shut our mouths at the same time.

[P82]
Wolhwa was the one who changed the grim atmosphere.

[P83]
“Where are my manners? I haven’t even properly introduced myself yet. I’m Wolhwa, Shanxi Branch Leader of the Lower District Sect.”

[P84]
“……I am Jin Mukyung of the Jin Family of Taiyuan.”

[P85]
“What a dull reaction. That Young Master Jin over there was extremely surprised when he first heard about my identity.”

[P86]
“I heard the general details from him. I also heard that you did a great deal for our family.”

[P87]
Jin Mukyung politely clasped his hands.

[P88]
“I realize this is late, but allow me to express my thanks.”

[P89]
“Not at all. It was a fair trade.”

[P90]
Wolhwa smoothly added,

[P91]
“Though I haven’t received the proper compensation yet.”

[P92]
“Our family will not forget the Lower District Sect’s goodwill.”

[P93]
His behavior and speech were still awkward beyond belief, but he was doing much better than when they had first met.

[P94]
Looking at the handsome man and beautiful woman sitting together like a picture, Hyuk Mujin exclaimed,

[P95]
“A promising young martial arts master and a peerless beauty… Whew, just looking at them makes my heart race. Don’t you agree?”

[P96]
I turned my head away and pretended not to hear him.

[P97]
Judging by the killing intent prickling my skin, Hyuk Mujin’s heart wouldn’t be racing for much longer.

[P98]
* * *

[P99]
Winter days were short-tempered.

[P100]
How long had we traveled along the mountain road? The sun quickly set, and darkness descended. The carriage stopped four hours later, around midnight.

[P101]
“We’ve arrived.”

[P102]
The first thing I saw after stepping out of the carriage was a moderately sized wooden building.

[P103]
The moment I stepped inside, I felt a chill in the air. A statue shaped in the likeness of a person looked down at us with solemn dignity.

[P104]
*What did they call places like this again?*

[P105]
*Oh, right. A shrine.*

[P106]
I had heard that it was a place where the spirit tablets of the dead were kept and memorial rites were performed.

[P107]
The Guandi Temples that appeared so often in martial arts novels came to mind. I looked closely at the statue, but I couldn’t tell who it represented.

[P108]
“It’s a shrine that was abandoned after a famine several years ago, though it seems local commoners still come here from time to time.”

[P109]
Just as Wolhwa had said, the inside of the shrine was empty, but traces of human presence remained. For example, there were footprints pressed into the dust-covered floor.

[P110]
“I’ll prepare the place.”

[P111]
At the words of the coachman and bodyguard, whom I assumed was a member of the Lower District Sect, we went outside the shrine.

[P112]
More precisely, one of us was dragged out by someone.

[P113]
“Follow me.”

[P114]
“Gah! Squad Leader! Squad Leader!”

[P115]
I ignored Hyuk Mujin as Jin Mukyung dragged him away by the collar and looked up at the sky.

[P116]
*The moon is awfully bright tonight.*

[P117]
“What are you doing?”

[P118]
“As you can see.”

[P119]
Wolhwa smiled faintly.

[P120]
“You seem to enjoy looking at the scenery.”

[P121]
“I’ve been starting to enjoy it lately.”

[P122]
The only scenery available in the modern world was a night view seen from some high place. Even that consisted of sad lights created by office workers working overtime.

[P123]
*This is real scenery.*

[P124]
There were no dense forests of skyscrapers, no apartment complexes, and no factories.

[P125]
In place of asphalt roads, damp dirt paths and crisp air filled the entire world.

[P126]
*Living in a place like this would be genuinely healing.*

[P127]
The problem was that it was also an easy place to get killed.

[P128]
Somehow, people were more frightening here than monsters.

[P129]
I didn’t even need to go as far as the Head Elder or Jopil. What had happened at the Phoenix Inn just yesterday was enough.

[P130]
“Oh, right. What happened to those guys?”

[P131]
“If you mean the mounted bandits from the Red Wind Band, they’ve been detained. Of course, we had to call a physician first.”

[P132]
I’d beaten the shit out of them, so of course they’d needed treatment.

[P133]
But there was another word that caught my attention more than that.

[P134]
“The Red Wind Band?”

[P135]
“They’re a rising power from the plateau. They’re fairly large, and more than anything, the leader of the Red Wind Band is said to possess formidable martial arts.”

[P136]
The Northern Plateau.

[P137]
I had first learned of that place through the map during the war with the Mount Heng Sword Sect.

[P138]
One thing struck me as strange: the plateau was a considerable distance from Honju, where the Phoenix Inn was located. As far as I knew, it took more than a week even if one rode day and night.

[P139]
“How did people like that end up all the way here?”

[P140]
“Toward the end of the war, Lee Cheonbaek hired countless wandering martial artists and mounted-bandit groups. Many of them met their end at Eight Spring Gorge, but some survived and fled.”

[P141]
“So the Red Wind Band was among them?”

[P142]
Wolhwa shook her head.

[P143]
“The leader of the Red Wind Band…… He was quicker-witted than I expected.”

[P144]
“What do you mean?”

[P145]
“He watched the situation until the very end. He kept a close eye on Eight Spring Gorge from only four hours away, then turned his horse around when he heard the outcome of the battle.”

[P146]
“With the two hundred subordinates who followed him.”

[P147]
Two hundred people.

[P148]
What would have happened if the Red Wind Band had joined the battle at Eight Spring Gorge that day? There would have been an enormous number of casualties, and it might even have affected the outcome of the battle.

[P149]
“We were lucky.”

[P150]
“We were. For the Mount Heng Sword Sect, it was incredibly unlucky.”

[P151]
Wolhwa continued as she packed tobacco into her long-stemmed pipe.

[P152]
“The Red Wind Band headed north immediately. They targeted the Mount Heng Sword Sect’s main base after most of its forces had withdrawn.”

[P153]
“……Huh.”

[P154]
They were natural-born plunderers.

[P155]
The moment the tide of the war turned, they headed north and bit into the throat of the Mount Heng Sword Sect, whose main forces had already withdrawn.

[P156]
They had preserved their forces by not participating in the battle, and they must have gotten plenty of rest as well. Their condition would have been at its peak.

[P157]
“Young Master Jin, you heard what happened, didn’t you?”

[P158]
“Yes.”

[P159]
The fierce battle that continued for two days ended with the Mount Heng Sword Sect’s victory.

[P160]
It also left behind the death of the Young Sect Leader, who was supposed to succeed his father.

[P161]
“But the rumors I heard said that wandering martial artists and mounted bandits were mixed together.”

[P162]
“A tiger doesn’t become a dog just because it has lost its teeth. The wandering martial artists the leader of the Red Wind Band drew in were fairly numerous as well. They would have been perfect for use as shields.”

[P163]
*Tap, tap.*

[P164]
Wolhwa took out a fire starter, lit it, and drew on her long-stemmed pipe.

[P165]
“The mounted bandits Young Master Jin defeated were probably the ones who fled at that time. Even if the Red Wind Band is unusually disciplined for a mounted-bandit group, it doesn’t mean they have no deserters at all. I’m not sure what they were doing in Honju, though.”

[P166]
“Deserters……”

[P167]
“That’s why things have been chaotic around here lately. Wandering martial artists, bandits, mounted bandits, and even dark-path figures are starting to raise their heads, while the Mount Heng Sword Sect’s strength has been reduced to almost nothing.”

[P168]
“They’ll have no choice but to accept our proposal.”

[P169]
Wolhwa smiled demurely.

[P170]
“To be precise, it isn’t *our* proposal. It’s the Jin Family of Taiyuan’s, isn’t it? Still, from my perspective, this is indeed a good time to pressure the new Sect Leader.”

[P171]
“By the way……”

[P172]
“Yes?”

[P173]
“Do commoners really come to this shrine in weather like this?”

[P174]
“Of course not. Hunters, perhaps. Why do you ask all of a sudden?”

[P175]
I pointed toward the mountain path.

[P176]
Through the thin snowstorm that had begun to swirl, I could see torches climbing toward us.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 천무학관   | **Heaven's Gate Temple**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 산서지부장  | **Shanxi Branch Leader**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 보상               | **Reward**                     |
| 몬스터     | **monster**           |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 혼주 | **Honju** | Shanxi location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 107,
  "passed": true,
  "metrics": {
    "source_characters": 5396,
    "translation_characters": 12095,
    "length_ratio": 2.241,
    "source_paragraphs": 164,
    "translation_paragraphs": 170
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "3"
        ]
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "천무학관",
        "preferred": "Heaven's Gate Temple"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "곰방대",
        "preferred": "long-stemmed tobacco pipe"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "상태",
        "preferred": "Status"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "보상",
        "preferred": "Reward"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
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
