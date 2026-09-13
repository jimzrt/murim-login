# Fidelity Gate — Chapter 375

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.

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
  1|＃375화
  2|
  3|
  4|
  5|병문안에도 순서가 있는 법.
  6|
  7|가주이자 가문의 웃어른인 당사독이 깨어났다는 소식에, 당문의 식솔들은 만사를 제치고 달려왔다.
  8|
  9|그러나 백여 명이나 되는 인원 모두가 당사독을 볼 수 있는 것은 아니었다.
 10|
 11|“은인, 우린 언제쯤 당 할아버지를 뵐 수 있어요?”
 12|
 13|“글쎄. 앞에 사람들이 들어간 지 꽤 됐으니까 슬슬 나오지 않을까.”
 14|
 15|“아, 그렇구나.”
 16|
 17|내 대답에 청풍이 고개를 끄덕인다.
 18|
 19|아니, 잠깐만. 청풍?
 20|
 21|“뭐야, 언제 왔어?”
 22|
 23|“방금요.”
 24|
 25|너무 자연스럽게 끼어들어서 있는 줄도 몰랐다. 그런데 이놈이 여길 왜 찾아왔지?
 26|
 27|내 의문을 읽기라도 한 것처럼 청풍이 자신의 가슴팍을 가리키며 대답했다.
 28|
 29|“미미가 보고 싶다고 해서요.”
 30|
 31|“……?”
 32|
 33|내가 지금 도대체 뭘 들은 거지.
 34|
 35|이제는 하다 하다 의사소통까지 하다니. 이 자식 혹시 화산파가 아니라 슬리데린 출신인가.
 36|
 37|심상치 않은 내 시선에 청풍이 고개를 갸웃했다.
 38|
 39|“제 이마는 갑자기 왜 쳐다보세요? 뭐 묻었어요?”
 40|
 41|“그냥. 이마에 번개 모양 흉터라도 있나 확인해 봤어.”
 42|
 43|“네?”
 44|
 45|“그런 게 있다.”
 46|
 47|말이 끝난 그 순간.
 48|
 49|덜컥.
 50|
 51|굳게 닫혀 있던 의방의 문이 열리고 십여 명의 사람들이 모습을 드러냈다.
 52|
 53|그들은 몇 남지 않은 사천당문의 직계들로, 그중에는 일면식이 있는 당호룡 역시 포함되어 있었다.
 54|
 55|“후우…….”
 56|
 57|붉게 충혈된 눈으로 하늘을 올려다본 그가 이쪽을 향해 걸어왔다.
 58|
 59|“가주께서 뵙고자 하시오.”
 60|
 61|“기다리고 있었습니다.”
 62|
 63|고개를 끄덕인 진위경이 앞장서고, 나와 청풍이 그 뒤를 따라 의방으로 들어갔다.
 64|
 65|사방에서 진동하는 탕약 냄새를 맡으며 얼마나 걸었을까. 하얀 천으로 코와 입을 가린 의원이 안내해 준 의실로 들어서자, 마침내 낯익은 얼굴들과 마주할 수 있었다.
 66|
 67|“쿨럭, 왔는가.”
 68|
 69|힘겹게 잔기침을 내뱉는 당사독의 상태는 한눈에 보기에도 심각했다.
 70|
 71|부러진 팔다리와 내상으로 인해 불안정한 기운.
 72|
 73|상반신을 일으키려는 그를, 우리와 눈인사를 주고받은 신의(神醫)가 만류했다.
 74|
 75|“가주, 제가 움직이지 말라 하지 않았습니까.”
 76|
 77|“노부는 죄인일세. 죽어 마땅한 죄를 지었으니 벌을 청하는 것이 이치지.”
 78|
 79|창백한 얼굴로 고개를 저은 당사독이 나를 똑바로 응시하며 말을 이었다.
 80|
 81|“구차한 변명은 하지 않겠네. 서천마군이 지하 뇌옥으로 향한 것은, 노부가 알려 주었기 때문일세.”
 82|
 83|나는 비스듬히 팔짱을 꼈다.
 84|
 85|“아, 어쩐지.”
 86|
 87|“……?”
 88|
 89|“왜요.”
 90|
 91|당사독이 당황한 얼굴로 물었다.
 92|
 93|“아, 알고 있었나?”
 94|
 95|“당연히 처음에는 몰랐죠. 그때는 워낙 정신이 없기도 했고. 그런데 나중에 곰곰이 생각해 보니까 서천마군. 그 새끼가 어떻게 만독지환의 위치를 알았나 싶더라고요.”
 96|
 97|애당초 만독지환의 위치를 아는 사람은 극소수.
 98|
 99|청풍은 겉보기에는 꽃잎처럼 가벼워 보여도 나무뿌리처럼 단단한 놈이니, 발설할 만한 사람은 당사독 한 명밖에 없었다.
100|
101|“왜 그랬습니까?”
102|
103|“……만독지환의 위치를 알려 주면 가문의 명맥을 보존해 주겠다 하더군.”
104|
105|“그걸 믿었어요?”
106|
107|“노부가 어리석었네. 잠시 판단력이 흐려져, 해서는 안 될 일을 저질렀지.”
108|
109|“알고는 계시네요.”
110|
111|나를 바라보는 당사독의 눈빛이 파르르 떨렸다.
112|
113|“이 늙은이가 목숨을 건사할 수 있었던 것은, 자네들에게 사죄하고 벌을 받으라는 하늘의 뜻이겠지.”
114|
115|“그럼 가주께서는 어떤 벌을 원하십니까.”
116|
117|불쑥 들려온 차가운 목소리의 주인은 아무 말 없이 대화를 듣고 있던 진위경이었다.
118|
119|“태원진가의 소가주 되시는가.”
120|
121|“예. 두 아우를 자식처럼 키운 형이기도 하지요.”
122|
123|깊게 가라앉은 진위경의 눈동자에서 숨길 수 없는 분노가 진득하게 묻어나왔다.
124|
125|“정도(正道)를 걷는 이라면 해서는 안 될 짓이었습니다.”
126|
127|“알고 있네. 아니, 알고 있소. 그렇기에 죄를 청하는 것이오.”
128|
129|“자결하라 한다면 어쩌시겠습니까.”
130|
131|“……!”
132|
133|나를 포함한 모두가 놀란 눈빛으로 진위경을 바라봤다.
134|
135|그러나 한 사람, 당사독만은 예외였다.
136|
137|그는 담담하기 그지없는 표정으로 입을 열었다.
138|
139|“나는 도의(道義)를 저버렸으나, 그대들이 목숨을 내놓고 싸워 준 덕분에 본가의 명맥을 이을 수 있게 되었소. 이 보잘것없는 늙은이의 목숨으로 사죄를 대신할 수 있다면, 흔쾌히 그리하리다.”
140|
141|짧은 침묵 뒤에 이어진 것은 진위경의 한숨이었다.
142|
143|“후우…….”
144|
145|복잡한 눈빛으로 당사독을 바라보던 그가 나를 향해 고개를 돌렸다.
146|
147|“어찌하겠느냐?”
148|
149|“……뭘요. 자결?”
150|
151|“그 무엇이든.”
152|
153|갑자기 손에 칼자루가 쥐어지니 심장이 쫀득해지는 기분이다.
154|
155|더군다나 그 칼자루 끝에 달린 것이 사천당문 가주의 목숨이라고 하니 더더욱 그랬다.
156|
157|‘갑자기 분위기 싸해진 것 보소.’
158|
159|물론 허허 웃고 넘어갈 일은 아니다. 내가 무슨 공명정대하고 속 넓은 인의대협도 아니고, 솔직히 사건의 전말을 깨달았을 때는 슬그머니 분노가 솟구치기도 했다.
160|
161|당시에는 나뿐만 아니라 모두의 목숨이 걸려 있는 상황이었으니까.
162|
163|하지만…….
164|
165|“됐습니다. 그렇게까지 하고 싶지는 않네요.”
166|
167|그래, 한편으로는 당사독의 입장을 이해한다.
168|
169|얼굴 몇 번 본 것이 고작인 외부인과 일가의 가주로서 목숨 걸고 지켜야 할 혈육을 저울에 올려 둔다면 나 역시 그와 같은 선택을 했을 것 같았다.
170|
171|‘그전에 빚도 있었고.’
172|
173|적천강이 깨어날 수 있었던 것에는 당사독의 도움도 크게 한몫했다.
174|
175|비록 모종의 거래가 있었다고는 하나, 한 핏줄에게도 알리지 않은 신물을 빌려준 사람 역시 당사독이었다.
176|
177|“그러니까 이걸로 쌤쌤. 퉁 치죠. 아니, 그건 너무 나갔고 이번 일로 사천당문이 저희에게 큰 빚을 진 것으로 하자고요.”
178|
179|내 말이 끝나자 청풍과 신의가 입을 열었다.
180|
181|“은인이 위험해졌던 건 분명히 당 할아버지의 잘못이지만…… 저도 은인의 뜻에 따를래요.”
182|
183|“전 이미 잊었습니다. 다만 의원으로서 바라는 것이 있다면 가주께서 하루빨리 쾌차하는 것이지요. 아직 살아남은 식솔들이 있지 않습니다.”
184|
185|마지막으로 입을 연 것은 진위경이었다. 처음과 달리 그에게서는 더 이상 어떤 분노도 느껴지지 않았다.
186|
187|아니, 어쩌면 진위경은 처음부터 내 대답을 알고 있었을지도 모르겠다.
188|
189|“그렇다는군요. 가주의 생각은 어떠하십니까.”
190|
191|“……!”
192|
193|우리를 바라보는 당사독의 눈동자가 격동으로 떨렸다.
194|
195|짧은 침묵이 흐른 뒤, 갈라진 목소리가 그의 입술 사이로 흘러나왔다.
196|
197|“노부가, 사천당문이 그대들에게 큰 은혜를 입었구려.”
198|
199|당사독이 진심을 담아 고개를 숙인 바로 그 순간이었다.
200|
201|띠링. 띠링. 띠링.
202|
203|
204|
205|- 자신의 죄를 고백하는 것은 어렵지만, 그보다 더 큰 용기를 필요로 하는 것이 있습니다. 바로 용서입니다.
206|
207|- 히든 퀘스트, [사죄와 용서]를 성공적으로 완료했습니다!
208|
209|- [Lv.115 당사독]이 당신들의 호의에 깊은 감사를 표합니다. 그와 [사천당문]은 결코 오늘의 호의와 도움을 잊지 않을 것이며, [사천당문]의 사람들은 당신을 은인으로 기억할 것입니다!
210|
211|- 칭호, [당문의 은인]을 획득했습니다!
212|
213|- 히든 퀘스트 완료 보상으로 막대한 경험치와 명성을 얻었습니다!
214|
215|- 레벨 업!
216|
217|
218|
219|뭐야, 이거. 갑자기 히든 퀘스트라니.
220|
221|내가 뜬금없이 울려 퍼진 시스템 알림에 얼떨떨해하던 그때, 차가운 무언가가 다리 사이를 스치며 지나갔다.
222|
223|취릭, 취리리릭.
224|
225|“미미, 이 녀석.”
226|
227|오랜만에 해후하는 미미와 당사독의 모습에, 잠시 깜빡하고 있던 물건 하나가 떠올랐다.
228|
229|“아, 그러고 보니 만독지환 말인데요. 다행히 제가 지금까지 잘 갖고 있었…….”
230|
231|“그런가?”
232|
233|내가 미처 말을 끝맺기도 전에, 불쑥 입을 연 당사독이 말을 이었다.
234|
235|“그럼 계속 갖고 있으시게.”
236|
237|“예, 그럼 제가 계속…… 예?”
238|
239|“자네에게 본가의 신물을 맡기겠네. 은인에 대한 증표이니 부디 거절하지 말아 주게.”
240|
241|띠링.
242|
243|
244|
245|- 소유자의 뜻에 따라 [만독지환]이 당신에게 양도되었습니다!
246|
247|- 새로운 아이템이 당신에게 종속됩니다!
248|
249|- 현재 보유 중인 종속 아이템 : [백염], [만독지환], [???].
250|
251|- 아직 이름이 정해지지 않은 종속 아이템이 있습니다. 새로운 이름을 부여해 주십시오.
252|
253|
254|
255|아니, 오늘 무슨 날이야?
256|
257|도대체 앞으로 어떤 개 같은 일들이 벌어지려고 이렇게 퍼 주나 싶어 불안하기까지 할 지경이다.
258|
259|금붕어처럼 입만 벙긋거리는 내 모습에, 당사독이 희미한 미소를 머금었다.
260|
261|“다들 원하는 것들이 있다면 말씀하시구려. 본가의 역량이 닿는 한 무엇이든 들어드리리다.”
262|
263|신의가 따라 웃으며 대답했다.
264|
265|“원하는 것이라면, 그저 병자들이 하루빨리 낫길 바랄 뿐입니다.”
266|
267|“허어.”
268|
269|과연 신의다운 대답이다. 아니, 이제는 동봉이라고 해야 하나.
270|
271|하지만 한 가지 확실한 것은, 그 역시 또 다른 한 사람의 신의(神醫)라는 사실이었다.
272|
273|“자네는 무엇을 원하는가?”
274|
275|갑작스러운 질문에 청풍이 화들짝 놀랐다.
276|
277|“저, 저요?”
278|
279|당사독이 고개를 끄덕이자 청풍이 손발을 배배 꼬며 대답했다.
280|
281|“저어는…… 그러니까요. 으음. 없어요.”
282|
283|“정말인가?”
284|
285|“네에. 없는 것 같아요.”
286|
287|“…….”
288|
289|“…….”
290|
291|야, 이 자식아. 미미쨩한테서 눈이나 떼고 얘기해.
292|
293|거울을 가져와서 보여 주고 싶다. 지금 청풍의 눈동자에는 미미쨩을 향한 애절함과 갈망이 떠올라 있었다.
294|
295|저러다가 뱀 가죽이 뚫리겠다 싶던 그때, 당사독이 입을 열었다.
296|
297|“이 녀석은 내 오랜 친우일세. 지난 수십 년 동안, 노부가 아무에게도 드러내지 못했던 희로애락(喜怒哀樂)을 나눌 수 있었던 유일한 존재였지.”
298|
299|청풍이 측은해진 눈빛으로 당사독을 바라봤다.
300|
301|“당 할아버지께서는 다른 친구가 없으시군요.”
302|
303|“만들지 않았다네. 노부에게 당문의 가주란 그런 자리였으니까.”
304|
305|“그래서 친구가 없으시군요.”
306|
307|“없던 게 아니라. 만들 수 있었는데…….”
308|
309|“친구 하나 없었군요. 불쌍해라.”
310|
311|“…….”
312|
313|신의가 다급하게 당사독의 어깨를 붙잡았다.
314|
315|“가주. 진정하십시오. 호흡이 너무 가파릅니다!”
316|
317|“후욱, 후우욱.”
318|
319|“크고 천천히 호흡하십시오. 자, 저를 따라서 하나, 둘…….”
320|
321|“후우우우욱…….”
322|
323|잠시 후, 간신히 고혈압의 위기에서 벗어난 당사독이 청풍을 바라보며 입을 열었다.
324|
325|“하지만 자네에게 미미를…….”
326|
327|청풍이 두 손으로 입을 틀어막았다.
328|
329|“아니에요. 당 할아버지. 할아버지의 유일한 친구를 데려갈 수는 없어요.”
330|
331|“……아직 맡기겠다고 하지 않았는데.”
332|
333|“앗. 아앗.”
334|
335|당사독이 한숨을 푹 내쉬었다. 잠깐이었지만 저런 놈한테 미미쨩을 맡겨도 되나, 하는 생각을 했음이 틀림없었다.
336|
337|“그래, 자네의 짐작대로일세. 향후 본가의 향방이 어떻게 될지 모르는바, 노부는 자네에게 미미를 맡기고자 하네. 물론 임시로.”
338|
339|“와아!”
340|
341|“마지막에 했던 말 들었나? 임시일세.”
342|
343|“와아아!”
344|
345|못 들었다에 혁무진 오른손 손목을 건다.
346|
347|미미의 임시보호자가 된 청풍은 기뻐서 어쩔 줄을 몰라 했다.
348|
349|“걱정 마세요. 잘 돌볼게요!”
350|
351|“지난번에 본 바에 의하면 미미가 자네를 잘 따르는 것 같긴 하지만, 녀석은 본래 성정이 까다롭고 낯을 많이 가리니…….”
352|
353|“미미. 회오리치기 후 뱅글뱅글 돌고 인사하기!”
354|
355|취리리릭!
356|
357|“오메, 시벌.”
358|
359|여기서 신기술을 써 버리네.
360|
361|생전 처음 보는 광경에 반쯤 넋이 나가 있던 진위경이 얼빠진 목소리로 중얼거렸다.
362|
363|“가주께서 걱정하시는 일은 없을 것 같군요.”
364|
365|당사독의 눈동자에 지진이 일어났다.
366|
367|당사독은 진위경과 긴히 나눌 말이 있다며 따로 자리를 청했고, 나와 청풍은 먼저 방을 빠져나왔다.
368|
369|아니, 지금 막 한 사람이 추가되었다.
370|
371|“진 소협. 잠시 이 늙은이에게 시간을 내어줄 수 있겠소?”
372|
373|“저요?”
374|
375|신의가 잔잔한 웃음과 함께 고개를 끄덕였다.
376|
377|“떠나기 전에 꼭 부탁하고 싶은 것이 있소.”
```

## Assembled English

```markdown
[P1]
# Chapter 375

[P2]
Even visiting the sick had a proper order.

[P3]
When word spread that Tang Sadok—the Family Head and elder of the clan—had awakened, the members of the Tang household dropped everything and came running.

[P4]
But not all hundred-plus people could see him.

[P5]
“Benefactor, when can we see Grandpa Tang?”

[P6]
“I don’t know. The people ahead of us have been in there for a while, so they should be coming out soon.”

[P7]
“Oh, I see.”

[P8]
Cheongpung nodded at my answer.

[P9]
Wait. Cheongpung?

[P10]
“What are you doing here? When did you get here?”

[P11]
“Just now.”

[P12]
He had slipped into the conversation so naturally that I hadn’t even noticed him. But why had this guy come here?

[P13]
As though he had read my thoughts, Cheongpung pointed to his chest.

[P14]
“Mimi said she wanted to see him.”

[P15]
“……?”

[P16]
*What the hell did I just hear?*

[P17]
Now they could even communicate. Was this bastard from Slytherin instead of Huashan?

[P18]
At my suspicious gaze, Cheongpung tilted his head.

[P19]
“Why are you suddenly staring at my forehead? Is there something on it?”

[P20]
“I was just checking whether you had a lightning-shaped scar.”

[P21]
“What?”

[P22]
“It’s a thing.”

[P23]
The moment the words left my mouth—

[P24]
Clunk.

[P25]
The tightly shut door of the medical ward opened, and more than ten people emerged.

[P26]
They were among the few remaining direct descendants of the Sichuan Tang Clan. Tang Horyong, whom I had met before, was among them.

[P27]
“Hoo……”

[P28]
He looked up at the sky with bloodshot eyes, then walked toward us.

[P29]
“The Family Head wishes to see you.”

[P30]
“We’ve been waiting.”

[P31]
Jin Wikyung nodded and led the way. Cheongpung and I followed him into the medical ward.

[P32]
Who knew how long we walked through the pervasive smell of medicinal decoctions? At last, a physician with his nose and mouth covered by white cloth led us into a treatment room, where we came face-to-face with several familiar faces.

[P33]
“Cough. You’ve come.”

[P34]
One glance was enough to tell that Tang Sadok, laboring through a faint cough, was in serious condition.

[P35]
His limbs were broken, and his internal injuries had left his qi unstable.

[P36]
He tried to sit up, but the Divine Physician, who had exchanged nods with us, stopped him.

[P37]
“Family Head, didn’t I tell you not to move?”

[P38]
“This old man is a sinner. I committed a crime deserving of death, so it is only right that I ask for punishment.”

[P39]
Pale-faced, Tang Sadok shook his head, stared straight at me, and continued.

[P40]
“I will make no pathetic excuses. The Western Heaven Demon Lord went to the underground prison because I told him about it.”

[P41]
I crossed my arms at a slant.

[P42]
“Ah. That explains it.”

[P43]
“……?”

[P44]
“Why?”

[P45]
Tang Sadok asked, looking bewildered.

[P46]
“Ah, you knew?”

[P47]
“Of course I didn’t know at first. There was too much going on at the time. But later, when I thought about it carefully, I started wondering how that bastard, the Western Heaven Demon Lord, had known the location of the Myriad Poison Ring.”

[P48]
Only a handful of people knew its location in the first place.

[P49]
Cheongpung might look as light as a flower petal, but he was as solid as a tree root. That left Tang Sadok as the only person who could have revealed it.

[P50]
“Why did you do it?”

[P51]
“He said he would preserve our family line if I told him where the Myriad Poison Ring was.”

[P52]
“And you believed him?”

[P53]
“This old man was foolish. My judgment was clouded for a moment, and I did something I never should have done.”

[P54]
“At least you know that.”

[P55]
Tang Sadok’s eyes trembled as he looked at me.

[P56]
“Surely heaven spared this old man so that I might apologize to all of you and receive my punishment.”

[P57]
“What punishment do you want, then?”

[P58]
The cold voice that suddenly rang out belonged to Jin Wikyung, who had been listening in silence.

[P59]
“Are you the Lesser Family Head of the Jin Family of Taiyuan?”

[P60]
“Yes. I am also the older brother who raised my two younger brothers as though they were my own children.”

[P61]
Unconcealed anger clung heavily to Jin Wikyung’s deeply sunken eyes.

[P62]
“It was something no one who walks the righteous path should ever have done.”

[P63]
“I know. No—I understand. That is why I ask to be punished.”

[P64]
“What would you do if I told you to take your own life?”

[P65]
“……!”

[P66]
Everyone, myself included, looked at Jin Wikyung in surprise.

[P67]
Everyone except Tang Sadok.

[P68]
With an utterly calm expression, he spoke.

[P69]
“I abandoned righteousness, but because all of you risked your lives to fight for us, my family line will endure. If this worthless old man’s life can serve as an apology, I will gladly give it.”

[P70]
After a brief silence, Jin Wikyung sighed.

[P71]
“Hoo……”

[P72]
He regarded Tang Sadok with a complicated look, then turned to me.

[P73]
“What will you do?”

[P74]
“……About what? His suicide?”

[P75]
“Whatever you wish.”

[P76]
Having the hilt of a knife suddenly thrust into my hand made my heart feel strangely taut.

[P77]
Especially when the life hanging from the other end belonged to the Family Head of the Sichuan Tang Clan.

[P78]
*Would you look at how suddenly the mood turned cold.*

[P79]
Of course, this wasn’t something I could laugh off. I wasn’t some fair-minded, magnanimous Great Hero of benevolence and righteousness. To be honest, when I realized the full truth of what had happened, anger had quietly welled up inside me.

[P80]
After all, everyone’s lives had been on the line at the time—not just mine.

[P81]
But……

[P82]
“That’s enough. I don’t want to take it that far.”

[P83]
That was right. On the other hand, I could understand Tang Sadok’s position.

[P84]
If, as the head of a family, I had to weigh outsiders I’d met only a few times against blood relatives I was duty-bound to protect with my life, I probably would’ve made the same choice.

[P85]
*Besides, I owed him.*

[P86]
Tang Sadok’s help had played a major role in allowing Jeok Cheongang to wake up.

[P87]
There may have been some sort of deal involved, but Tang Sadok had still lent us a sacred artifact whose existence he hadn’t revealed even to his own blood relatives.

[P88]
“So let’s call it even. We’ll let it slide. No, that’s going too far—let’s say the Sichuan Tang Clan owes us a huge debt over this.”

[P89]
When I finished, Cheongpung and the Divine Physician spoke up.

[P90]
“It was definitely Grandpa Tang’s fault that Benefactor was put in danger, but… I’ll follow Benefactor’s wishes too.”

[P91]
“I have already forgotten the matter. But if I have one wish as a physician, it is that the Family Head recover as soon as possible. After all, there are still surviving members of his household.”

[P92]
Jin Wikyung spoke last. Unlike before, there was no anger left in him.

[P93]
No—perhaps he had known what my answer would be from the very beginning.

[P94]
“So that is their decision. What do you think, Family Head?”

[P95]
“……!”

[P96]
Tang Sadok’s eyes trembled with emotion as he looked at us.

[P97]
After a short silence, a hoarse voice slipped between his lips.

[P98]
“This old man—and the Sichuan Tang Clan—owe all of you a great debt of gratitude.”

[P99]
The instant Tang Sadok bowed his head with genuine sincerity—

[P100]
> **System**
>
> Confessing one’s sins is difficult, but there is something that requires even greater courage. That is forgiveness.
>
> **Hidden Quest:** **Apology and Forgiveness** successfully completed!
>
> **Level 115 Tang Sadok** expresses his deep gratitude for your kindness. He and the **Sichuan Tang Clan** will never forget the kindness and assistance you showed them today, and the people of the **Sichuan Tang Clan** will remember you as their **Benefactor**!
>
> **Title Acquired:** **Benefactor of the Tang Clan**
>
> You have gained a tremendous amount of EXP and Fame as a reward for completing the Hidden Quest!
>
> **Level Up!**

[P101]
*What was this? A Hidden Quest, all of a sudden?*

[P102]
As I stood there dumbfounded by the System notification that had suddenly rung out, something cold brushed between my legs.

[P103]
Sssrik. Sssriririk.

[P104]
“Mimi, you little……”

[P105]
At the sight of Mimi and Tang Sadok reunited after so long, I remembered something I had momentarily forgotten.

[P106]
“Ah, now that I think about it, the Myriad Poison Ring. Thankfully, I’ve been keeping it safe all this time……”

[P107]
“Is that so?”

[P108]
Tang Sadok cut in before I could finish.

[P109]
“Then continue to keep it.”

[P110]
“Yes, then I’ll keep—what?”

[P111]
“I am entrusting our family’s sacred artifact to you. It is a token of gratitude for our Benefactor, so please do not refuse.”

[P112]
> **System**
>
> According to the owner’s wishes, **Myriad Poison Ring** has been transferred to you!
>
> A new item is now bound to you!
>
> **Currently bound items:** **White Flame**, **Myriad Poison Ring**, **???**
>
> You have a bound item that has not yet been named. Please give it a new name.

[P113]
*What kind of day was today?*

[P114]
I was getting downright nervous, wondering what kind of shitty things were about to happen for them to be giving so much away like this.

[P115]
At the sight of me opening and closing my mouth like a goldfish, Tang Sadok smiled faintly.

[P116]
“If any of you desire something, speak. I will grant anything within our family’s power.”

[P117]
The Divine Physician smiled along with him.

[P118]
“If there is something I desire, it is simply for the patients to recover as soon as possible.”

[P119]
“Good heavens.”

[P120]
That was certainly an answer worthy of the Divine Physician. No, should I be calling him Dongbong now?

[P121]
But one thing was certain: he, too, was another Divine Physician.

[P122]
“What do you want?”

[P123]
Cheongpung jumped at the sudden question.

[P124]
“M-Me?”

[P125]
Tang Sadok nodded, and Cheongpung answered while fidgeting with his hands and feet.

[P126]
“Well, I… Let me think. Um. Nothing.”

[P127]
“Are you sure?”

[P128]
“Yeees. I don’t think there’s anything.”

[P129]
“……”

[P130]
“……”

[P131]
*Hey, you idiot. Take your eyes off Mimi-chan and talk.*

[P132]
I wanted to bring him a mirror and show him his own face. His eyes brimmed with aching longing and desire for Mimi-chan.

[P133]
*At this rate, he’s going to stare a hole through the snake’s hide.*

[P134]
Just then, Tang Sadok spoke.

[P135]
“This creature is an old friend of mine. For the past several decades, she has been the only one with whom this old man could share the joy, anger, sorrow, and pleasure he could reveal to no one else.”

[P136]
Cheongpung looked at Tang Sadok with pity.

[P137]
“So you don’t have any other friends, Grandpa Tang.”

[P138]
“I never made any. Being the Family Head of the Tang Clan was that kind of position.”

[P139]
“So you have no friends.”

[P140]
“It wasn’t that I had none. I could have made them, but……”

[P141]
“You didn’t have a single friend. How pitiful.”

[P142]
“……”

[P143]
The Divine Physician hurriedly grabbed Tang Sadok by the shoulders.

[P144]
“Family Head, calm down. You’re breathing too quickly!”

[P145]
“Huuk, hoo-oo.”

[P146]
“Take deep, slow breaths. Come on, follow me. One, two……”

[P147]
“Huooooo……”

[P148]
A little while later, after narrowly escaping a hypertensive crisis, Tang Sadok looked at Cheongpung and spoke again.

[P149]
“But as for Mimi, perhaps you……”

[P150]
Cheongpung covered his mouth with both hands.

[P151]
“No, Grandpa Tang. I can’t take away your only friend.”

[P152]
“……I haven’t said I’m entrusting her to you yet.”

[P153]
“Oh. Oh!”

[P154]
Tang Sadok let out a deep sigh. It had only been for a moment, but he had undoubtedly wondered whether he could entrust Mimi-chan to someone like that.

[P155]
“Yes, just as you guessed. Since we do not know what path our family will take from here on, I wish to entrust Mimi to you. Temporarily, of course.”

[P156]
“Yaaay!”

[P157]
“Did you hear the last part? Temporarily.”

[P158]
“Yaaay!”

[P159]
*I’ll bet Hyuk Mujin’s right wrist that he didn’t.*

[P160]
Now Mimi’s temporary guardian, Cheongpung was beside himself with joy.

[P161]
“Don’t worry. I’ll take good care of her!”

[P162]
“From what I saw last time, Mimi does seem fond of you, but she is temperamental by nature and extremely wary of strangers, so……”

[P163]
“Mimi. Do Whirlwind, then spin round and round and say hello!”

[P164]
Sssriririk!

[P165]
“Holy shit.”

[P166]
*He busted out a new trick right here.*

[P167]
Jin Wikyung, half stunned by the sight he was seeing for the first time in his life, muttered in a dazed voice.

[P168]
“It seems you have nothing to worry about, Family Head.”

[P169]
An earthquake shook Tang Sadok’s eyes.

[P170]
Tang Sadok asked Jin Wikyung to stay behind for a private conversation, while Cheongpung and I left the room first.

[P171]
No, one person had just been added.

[P172]
“Young Hero Jin. Could you spare this old man a little of your time?”

[P173]
“Me?”

[P174]
The Divine Physician nodded with a gentle smile.

[P175]
“There is something I very much wish to ask of you before you leave.”
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 375

[P2]
Even hospital visits had a proper order.

[P3]
When word spread that Tang Sadok—the Family Head and elder of the clan—had awakened, the members of the Tang household dropped everything and came running.

[P4]
However, not all of the more than one hundred people could see Tang Sadok.

[P5]
“Benefactor, when can we see Grandpa Tang?”

[P6]
“I don’t know. It’s been quite a while since the people in front of us went in, so they should be coming out soon.”

[P7]
“Oh, I see.”

[P8]
Cheongpung nodded at my answer.

[P9]
Wait. Cheongpung?

[P10]
“What are you doing here? When did you get here?”

[P11]
“Just now.”

[P12]
He had joined the conversation so naturally that I hadn’t even noticed he was there. But why had this guy come here?

[P13]
As though he had read my thoughts, Cheongpung pointed to his chest and answered.

[P14]
“Because Mimi said she wanted to visit.”

[P15]
“……?”

[P16]
*What did I just hear?*

[P17]
Now Mimi was communicating with him, too. Was this bastard from Slytherin instead of Huashan?

[P18]
At my suspicious gaze, Cheongpung tilted his head.

[P19]
“Why are you suddenly staring at my forehead? Is there something on it?”

[P20]
“I was just checking whether you had a lightning-shaped scar on your forehead.”

[P21]
“What?”

[P22]
“Never mind.”

[P23]
The moment the words left my mouth—

[P24]
Clunk.

[P25]
The tightly closed door of the medical ward opened, and more than ten people emerged.

[P26]
They were among the few remaining direct-line members of the Sichuan Tang Clan. Tang Horyong was among them, and I had met him before.

[P27]
“Hoo……”

[P28]
After looking up at the sky with bloodshot eyes, he walked toward us.

[P29]
“The Family Head wishes to see you.”

[P30]
“We’ve been waiting.”

[P31]
Jin Wikyung nodded and led the way. Cheongpung and I followed him into the medical ward.

[P32]
Who knew how long we walked through the pervasive smell of medicinal decoctions? At last, the physician whose nose and mouth were covered with white cloth led us into a treatment room, where we came face-to-face with several familiar faces.

[P33]
“Cough, cough. You’ve come.”

[P34]
Tang Sadok’s condition was visibly serious. His limbs were broken, and his internal injuries had left his qi unstable.

[P35]
As he tried to raise his upper body, the Divine Physician who had exchanged a nod with us stopped him.

[P36]
“Family Head, didn’t I tell you not to move?”

[P37]
“This old man is a sinner. I committed a crime deserving of death, so it is only right that I ask for punishment.”

[P38]
Pale-faced, Tang Sadok shook his head, stared straight at me, and continued.

[P39]
“I will not make any pathetic excuses. The reason the Western Heaven Demon Lord headed for the underground prison was because I told him about it.”

[P40]
I folded my arms at an angle.

[P41]
“Ah. That explains it.”

[P42]
“……?”

[P43]
“Why are you looking at me like that?”

[P44]
“Ah, you knew?”

[P45]
“Of course I didn’t know at first. There was too much going on at the time. But later, when I thought about it carefully, I started wondering how that bastard, the Western Heaven Demon Lord, had known the location of the Myriad Poison Ring.”

[P46]
Only a handful of people knew where the Myriad Poison Ring was in the first place.

[P47]
Cheongpung might look as light as a flower petal, but he was as sturdy as a tree root. That left Tang Sadok as the only person who could have revealed it.

[P48]
“Why did you do it?”

[P49]
“He said that if I revealed the location of the Myriad Poison Ring, he would preserve the family line.”

[P50]
“And you believed him?”

[P51]
“This old man was foolish. My judgment was clouded for a moment, and I committed an act I should never have committed.”

[P52]
“At least you know that.”

[P53]
Tang Sadok’s eyes trembled as he looked at me.

[P54]
“The reason this old man was able to keep his life is surely heaven’s will. I must apologize to you all and accept my punishment.”

[P55]
“What punishment do you want, then?”

[P56]
The owner of the cold voice was Jin Wikyung, who had been listening to the conversation in silence.

[P57]
“Are you the Lesser Family Head of the Jin Family of Taiyuan?”

[P58]
“Yes. I am also an older brother who raised my two younger brothers as though they were my own children.”

[P59]
Unconcealed anger clung heavily to Jin Wikyung’s deeply sunken eyes.

[P60]
“It was something no one walking the righteous path should have done.”

[P61]
“I know. No—I understand. That is why I ask to be punished.”

[P62]
“What will you do if I tell you to take your own life?”

[P63]
“……!”

[P64]
Everyone, myself included, looked at Jin Wikyung in surprise.

[P65]
Everyone except Tang Sadok.

[P66]
He opened his mouth with an expression of utter calm.

[P67]
“I abandoned righteousness, but thanks to the fact that all of you fought while putting your lives on the line, my family will be able to continue. If this insignificant old man’s life can serve as an apology, I will gladly give it.”

[P68]
After a brief silence, Jin Wikyung sighed.

[P69]
“Hoo……”

[P70]
He stared at Tang Sadok with complicated emotions before turning to me.

[P71]
“What will you do?”

[P72]
“……About what? His suicide?”

[P73]
“Whatever you wish.”

[P74]
Having the hilt of a knife suddenly thrust into my hand made my heart feel strangely taut.

[P75]
Even more so when I was told that the life attached to the end of that hilt was the life of the Family Head of the Sichuan Tang Clan.

[P76]
*Look at how suddenly the mood turned cold.*

[P77]
Of course, this wasn’t something to laugh off. I wasn’t some impartial, broad-minded Great Hero. To be honest, when I realized the whole truth of what had happened, a quiet anger had risen inside me.

[P78]
After all, everyone’s lives had been on the line at the time—not just mine.

[P79]
But……

[P80]
“That’s enough. I don’t want to take things that far.”

[P81]
That was right. On the other hand, I could understand Tang Sadok’s position.

[P82]
If, as the head of a family, I had to weigh blood relatives I was duty-bound to protect with my life against outsiders I’d met only a few times, I probably would’ve made the same choice.

[P83]
*I had a debt to him, too.*

[P84]
Tang Sadok’s help had played a major role in Jeok Cheongang’s recovery.

[P85]
There may have been a transaction involved, but Tang Sadok had still lent us a sacred artifact without even telling his own blood relatives.

[P86]
“So let’s call it even. We’ll let it slide. No, that’s going too far—let’s say the Sichuan Tang Clan owes us a huge debt over this.”

[P87]
When I finished speaking, Cheongpung and the Divine Physician spoke up.

[P88]
“It was definitely Grandpa Tang’s fault that the Benefactor was put in danger, but… I’ll follow the Benefactor’s wishes, too.”

[P89]
“I’ve already forgotten about it. But if there is one thing I wish for as a physician, it is that the Family Head recovers as soon as possible. There are still surviving members of the household, after all.”

[P90]
The last person to speak was Jin Wikyung. Unlike before, there was no anger to be felt from him anymore.

[P91]
No—perhaps Jin Wikyung had known my answer from the very beginning.

[P92]
“So that is their decision. What do you think, Family Head?”

[P93]
“……!”

[P94]
Tang Sadok’s eyes trembled with emotion as he looked at us.

[P95]
After a short silence, a hoarse voice slipped between his lips.

[P96]
“This old man—and the Sichuan Tang Clan—have received a great kindness from you.”

[P97]
The instant Tang Sadok bowed his head with genuine sincerity—

[P98]
> **System**
>
> Confessing one's sins is difficult, but there is something that requires even greater courage. That is forgiveness.
>
> **Hidden Quest:** **Atonement and Forgiveness** successfully completed!
>
> **Level 115 Tang Sadok** expresses his deep gratitude for your kindness. He and the **Sichuan Tang Clan** will never forget the favor and assistance you showed them today, and the people of the **Sichuan Tang Clan** will remember you as their **Benefactor**!
>
> **Title Acquired:** **Benefactor of the Tang Clan**
>
> You have gained a tremendous amount of EXP and Fame as a reward for completing the Hidden Quest!
>
> **Level Up!**

[P99]
*What was this? A Hidden Quest, all of a sudden?*

[P100]
As I stood there dumbfounded by the System notification that had suddenly rung out, something cold brushed between my legs.

[P101]
Ssssk. Ssssss.

[P102]
“Mimi, you little……”

[P103]
At the sight of Mimi and Tang Sadok reunited after so long, I remembered something I had momentarily forgotten.

[P104]
“Ah, now that I think about it, the Myriad Poison Ring. Thankfully, I’ve been keeping it safe all this time……”

[P105]
“Is that so?”

[P106]
Before I could finish speaking, Tang Sadok interrupted.

[P107]
“Then continue to keep it.”

[P108]
“Yes, then I’ll keep—what?”

[P109]
“I am entrusting the sacred artifact of our family to you. It is a token of our gratitude to our Benefactor, so please do not refuse.”

[P110]
> **System**
>
> According to the owner's wishes, **Myriad Poison Ring** has been transferred to you!
>
> A new item is now bound to you!
>
> **Currently bound items:** **White Flame**, **Myriad Poison Ring**, **???**
>
> You have a bound item that has not yet been named. Please give it a new name.

[P111]
*What kind of day was today?*

[P112]
I was getting downright nervous, wondering what kind of shitty things were about to happen for them to be giving so much away like this.

[P113]
At the sight of me opening and closing my mouth like a goldfish, Tang Sadok smiled faintly.

[P114]
“If any of you have something you want, speak up. I will grant you anything within the limits of our family’s abilities.”

[P115]
The Divine Physician smiled along with him and answered.

[P116]
“If there is something I want, it is simply for the patients to recover as soon as possible.”

[P117]
“Good heavens.”

[P118]
That was certainly an answer worthy of the Divine Physician. No, should I be calling him Dongbong now?

[P119]
But one thing was certain: he, too, was another Divine Physician.

[P120]
“What do you want?”

[P121]
Cheongpung jumped at the sudden question.

[P122]
“M-Me?”

[P123]
Tang Sadok nodded, and Cheongpung answered while fidgeting with his hands and feet.

[P124]
“Well, I…… Let me think. Um. Nothing.”

[P125]
“Are you sure?”

[P126]
“Yeees. I don’t think there’s anything.”

[P127]
“……”

[P128]
“……”

[P129]
*Hey, you idiot. Take your eyes off Mimi-chan and talk.*

[P130]
I wanted to bring him a mirror and show him his face. Cheongpung’s eyes were filled with aching longing and desire for Mimi-chan.

[P131]
*At this rate, he’s going to stare a hole through the snake’s hide.*

[P132]
Just then, Tang Sadok spoke.

[P133]
“This creature is an old friend of mine. For the past several decades, it has been the only one with whom this old man could share the joys and sorrows he could reveal to no one else.”

[P134]
Cheongpung looked at Tang Sadok with pity.

[P135]
“So you don’t have any other friends, Grandpa Tang.”

[P136]
“I never made any. Being the Family Head of the Tang Clan was that kind of position.”

[P137]
“So you have no friends.”

[P138]
“It wasn’t that I had none. I could have made them, but……”

[P139]
“You didn’t have a single friend. How pitiful.”

[P140]
“……”

[P141]
The Divine Physician hurriedly grabbed Tang Sadok by the shoulders.

[P142]
“Family Head, please calm down. Your breathing is too rapid!”

[P143]
“Huuk, hoo-oo.”

[P144]
“Take deep, slow breaths. Come on, follow me. One, two……”

[P145]
“Huooooo……”

[P146]
A little while later, Tang Sadok barely managed to escape a hypertensive crisis before opening his mouth again.

[P147]
“But I could entrust Mimi to you……”

[P148]
Cheongpung covered his mouth with both hands.

[P149]
“No, Grandpa Tang. I can’t take away your only friend.”

[P150]
“……I haven’t even said I was going to entrust her to you yet.”

[P151]
“Oh. Oh!”

[P152]
Tang Sadok let out a deep sigh. It had only been for a moment, but he had undoubtedly wondered whether he could entrust Mimi-chan to someone like that.

[P153]
“Yes, just as you guessed. Since we do not know what path our family will take from here on, I wish to entrust Mimi to you. Temporarily, of course.”

[P154]
“Yaaay!”

[P155]
“Did you hear what I said at the end? Temporarily.”

[P156]
“Yaaay!”

[P157]
*I’ll bet Hyuk Mujin’s right wrist that he didn’t hear that.*

[P158]
Cheongpung, now Mimi’s temporary guardian, didn’t know what to do with his happiness.

[P159]
“Don’t worry. I’ll take good care of her!”

[P160]
“From what I saw last time, Mimi does seem to like you, but she has a rather difficult temperament and is very wary of strangers, so……”

[P161]
“Mimi. Do Whirlwind, then spin round and round and say hello!”

[P162]
Sssriririk!

[P163]
“Oh, for fuck’s sake.”

[P164]
*He’s using a new trick here.*

[P165]
Jin Wikyung had been half out of his mind at the sight he was seeing for the first time in his life. He muttered in a dazed voice.

[P166]
“It seems you have nothing to worry about, Family Head.”

[P167]
An earthquake struck Tang Sadok’s eyes.

[P168]
Tang Sadok asked Jin Wikyung to stay behind for a private conversation, while Cheongpung and I left the room first.

[P169]
No, one person had just been added.

[P170]
“Young Hero Jin. Could you spare this old man a little of your time?”

[P171]
“Me?”

[P172]
The Divine Physician nodded with a gentle smile.

[P173]
“There is something I would like to ask you before you leave.”
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 375,
  "passed": true,
  "metrics": {
    "source_characters": 5748,
    "translation_characters": 12105,
    "length_ratio": 2.106,
    "source_paragraphs": 184,
    "translation_paragraphs": 175
  },
  "errors": [],
  "warnings": [
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
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
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

## Chapter 374 Expedition

- This branch intentionally starts at Chapter 374. Chapters 65–370 have no accepted local English translation here; Chapters 371–373 are source-only bridge summaries.
- Treat `docs/EXPEDITION_SEED.md` and `summaries/0369-0373.md` as bounded orientation, not as a substitute for missing translations.
- When the current Korean source conflicts with bridge context, the current source wins. Preserve uncertainty instead of inventing skipped-range backstory.
- From Chapter 374 onward, the ordinary workflow update, names ledger, profiles, summaries, QA, hashes, and mastering artifacts are authoritative for this branch.

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
