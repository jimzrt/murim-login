# Fidelity Gate — Chapter 124

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
  1|＃124화
  2|
  3|
  4|
  5|나도 사람인지라 이틀 전 밤 이소월이 내민 세 권의 무공 비급 앞에선 마음이 흔들릴 수밖에 없었다.
  6|
  7|자그마치 초절정 무공이다. 진가창법과 진무보법을 대성한 지금, 안 그래도 새로운 무공의 필요성을 느끼고 있던 차에 눈앞에 들이밀어진 달콤한 유혹.
  8|
  9|‘이대로는 안 돼.’
 10|
 11|풍양과의 싸움은 처절했다. 조필에게서 얻은 [이름 없는 검]이 아니었다면 목숨이 두 개라 해도 살아남지 못했을 것이다.
 12|
 13|이젠 더 많은 무공을 익혀서 새로운 경지에 들어야 할 때다.
 14|
 15|‘절정 고수.’
 16|
 17|혈랑검법과 혈랑보법, 그리고 수라멸권은 이미 검증된 절정 무공이다. 그 높다는 절정의 벽을 허물어트릴 수 있을 만큼 단단한 망치인 것이다. 하지만…….
 18|
 19|‘저게 망치면, 이건 포클레인이지.’
 20|
 21|나는 손에 들린 낡은 서책을 뿌듯하게 바라봤다.
 22|
 23|이 한 권의 무공 비급이 바로 별 미련 없이 이소월의 제안을 거절할 수 있는 이유다.
 24|
 25|“화, 화, 화, 화…….”
 26|
 27|한참 동안 버퍼링이 걸려 있던 진무경이 마침내 한 단어를 토해 냈다.
 28|
 29|“화염신장!”
 30|
 31|“오, 아네? 정답.”
 32|
 33|200년 전의 천하십대권법도 꿰고 있는 진무경이니 화염신장을 알고 있는 건 어쩜 당연했다. 이건 그보다 훨씬 더 대단한 무공이니까.
 34|
 35|‘아이템 확인.’
 36|
 37|띠링.
 38|
 39|
 40|
 41|아이템창
 42|
 43|
 44|
 45|[화염신장]
 46|
 47|종류 : 무공 비급
 48|
 49|등급 : 초절정
 50|
 51|제한 : 열양지기의 소유자
 52|
 53|설명 : 열화문(熱火門)의 비전절기 중 하나. 강력한 화기를 바탕으로 한 무공이다.
 54|
 55|효과 : [화염신장]의 습득
 56|
 57|
 58|
 59|
 60|
 61|진무경이 믿기지 않는다는 얼굴로 물었다.
 62|
 63|“네가 이걸 어떻게…….”
 64|
 65|“어떤 고마우신 분이 주고 가셨지.”
 66|
 67|“주고 갔다고?”
 68|
 69|“응.”
 70|
 71|이걸 주고 하늘나라로 훨훨 날아가셨다.
 72|
 73|호신강기도 파괴하는 만년한철로 만들어진 [이름 없는 검], 30년의 열양지기를 얻을 수 있는 [열화신단].
 74|
 75|마지막으로 초절정 무공인 [화염신장]까지.
 76|
 77|나는 아낌없이 주고 떠난 조필을 생각하며 창 너머 푸른 하늘을 바라보았다.
 78|
 79|‘잘 지내니.’
 80|
 81|그때 진무경이 불쑥 끼어들었다.
 82|
 83|“이제 헛소리 그만하고 사실대로 말해라. 열화문(熱火門)의 비전절기가 어떻게 네 손에 있는 거지?”
 84|
 85|“말했잖아. 누가 주고 갔다니까.”
 86|
 87|“지금 네가 뭘 착각하는 모양인데…….”
 88|
 89|진무경이 심각한 얼굴로 말을 이었다.
 90|
 91|“농으로 얼버무릴 상황이 아니다.”
 92|
 93|“왜?”
 94|
 95|“네가 타 문파의 무공을 훔친 도둑놈이 될 수도 있으니까. 자칫하면 본가가 천하 무림의 질타를 받게 된다.”
 96|
 97|미처 생각지 못한 문제다.
 98|
 99|무공은 곧 문파의 근간이자 역사다. 초절정 무공인 동시에 열화문의 비전절기라는 화염신장이야 말할 것도 없다.
100|
101|“아, 젠장.”
102|
103|“다시 한번 물어보마. 화염신장의 비급을 어디서, 어떻게 얻었느냐?”
104|
105|나는 한숨을 푹 내쉬며 대답했다.
106|
107|“조필한테서.”
108|
109|“조필? 내가 알고 있는 일문일살 조필?”
110|
111|“맞아. 조필을 쓰러트리고 전리품으로 얻은 거지.”
112|
113|“그놈이 어떻게 화염신장의 비급을 갖고 있었는지 알고 있느냐?”
114|
115|“글쎄…….”
116|
117|곰곰이 생각한 끝에 그때 조필이 했던 말을 기억해 낼 수 있었다.
118|
119|“자기 입으로는 본인이 화염신장의 십구 대 계승자라던데.”
120|
121|“조필 같은 놈이 어찌…… 잘못 들은 건 아니냐?”
122|
123|“아냐, 확실해. 거짓말하는 것 같아 보이지도 않았고.”
124|
125|당시 조필은 선천지기를 끌어 올린 상태였고, 이미 빠르게 죽어 가고 있었다. 죽음을 목전에 둔 사람의 입에서 나오는 말은 대부분 진실에 가깝다.
126|
127|‘물론 조필이 거짓말을 쳤을 가능성도 염두에 둬야겠지.’
128|
129|그때 골똘히 생각에 잠겨 있던 진무경이 이해가 안 간다는 얼굴로 입을 열었다.
130|
131|“화염신장의 계승자라는 놈이 왜 너 같은 놈한테 져?”
132|
133|“…….”
134|
135|음, 기분은 더럽지만 일리가 있군.
136|
137|초절정 무공을 익힌 조필이 낭인 짓을 하고 있다는 것부터가 수상하긴 하다.
138|
139|‘그러고 보니 검기도 제대로 못 쓰는 놈이었고.’
140|
141|만나는 놈들마다 검기는 기본이요, 옵션으로 호신강기까지 달고 나오는 요즘이다. 일문일살 조필은 지금까지 내가 상대한 절정 고수 중 가장 약한 축에 속했다.
142|
143|“화염신장, 이거 생각보다 약한 무공인가?”
144|
145|“뭐? 화염신장이 약해?”
146|
147|진무경이 별 미친놈 다 보겠다는 눈빛으로 말했다.
148|
149|“정신 나간 놈. 화왕(火王)의 독문무공을 약하다고 하는 놈은 천하에 너 하나뿐일 거다.”
150|
151|“화왕이 누군데.”
152|
153|“장난칠 기분 아니다.”
154|
155|“나돈데?”
156|
157|“그만해라. 재미없으니까.”
158|
159|“응. 그래서 화왕이 누구냐고.”
160|
161|이번 침묵은 좀 길었다. 금붕어처럼 입만 벙긋거리던 진무경이 깊은 한숨을 뱉어 냈다.
162|
163|“네 손, 발가락을 합해 봐라. 모두 몇 개냐?”
164|
165|“스무 개.”
166|
167|“그래, 화왕은 천하를 거꾸로 들어서 탈탈 털어도 그 안에 들어가는 고수다.”
168|
169|“……오우야.”
170|
171|“일신(一神), 삼성(三星), 십왕(十王). 몰라? 정말 이걸 모른다고?”
172|
173|이거 아주 못 들어 봤다고 하면 모가지를 비틀어 버릴 기세다.
174|
175|진무경의 고리눈에 나는 조심스럽게 입을 열었다.
176|
177|“삼성은 들어 봤는데…….”
178|
179|“그나마 다행이군.”
180|
181|이 삼성이 그 삼성이 아니지만 어쨌든.
182|
183|지금 중요한 건 그게 아니다.
184|
185|“그럼 내가 화염신장을 갖고 있다는 사실을 화왕이 알게 된다면…….”
186|
187|“별로 상상하고 싶지 않은 상황이 벌어지겠지.”
188|
189|젠장, 천하를 통틀어 스무 손가락 안에 든다는 초절정 고수라니. 화왕이 이 사실을 알고 찾아온다면 태원진가 전체가 덤벼도 이길 수 없을 거다.
190|
191|‘어떻게 얻은 무공인데…….’
192|
193|익히지도 못하고 넘겨줘야 한다는 사실에 속이 쓰리던 그때였다.
194|
195|나와 마찬가지로 화염신장의 비급을 안타까운 얼굴로 바라보던 진무경이 한마디를 보탰다.
196|
197|“화왕이 아직까지 살아 있다면 말이다.”
198|
199|“뭐?”
200|
201|“화왕이 마지막으로 모습을 드러낸 것은 사십 년 전이 마지막이다.”
202|
203|“사십 년 전?”
204|
205|“처음 무림에 모습을 나타냈을 당시에도 화왕은 이미 노인이었다. 정마대전이 아니었다면 평생 은거기인으로 살았을지도 모르지.”
206|
207|진무경의 말이 이어졌다.
208|
209|“남궁세가를 패퇴시키고 안휘성(安徽城)을 점령한 마교의 사기는 하늘을 찔렀다. 수많은 약탈과 살인, 방화가 이뤄졌는데 그 과정에서 구화산(九華山)에 불을 지른 것이 화왕의 심기를 건드렸다더군.”
210|
211|“그래서?”
212|
213|“나흘 밤낮 동안 천 명이 죽었고, 구화산 깊숙한 곳에 은거해 있던 노인은 화왕이라는 이름을 얻었다.”
214|
215|“……천 명?”
216|
217|“그래. 구화산에서 입은 피해가 너무 컸던 탓에 마교는 얼마 버티지 못하고 안휘성에서 물러나야 했다.”
218|
219|천 명이란 말이지…….
220|
221|나는 신중한 고민 끝에 입을 열었다.
222|
223|“이거, 돌려주자.”
224|
225|오래 살고 싶다. 내 인생에 단신으로 천 명을 죽였다는 미친 노인네를 만나는 이벤트는 끼워 넣고 싶지 않다.
226|
227|“당장 출발해야겠네. 안휘성? 아직도 거기 사신대?”
228|
229|“아무도 모른다. 화왕은 그것으로 분이 안 풀렸는지 일 년 동안 눈에 보이는 마교도들을 전부 박살 내고 다시 은거했으니까.”
230|
231|“열화문! 열화문에 가면 볼 수 있겠네.”
232|
233|“열화문은 일인전승(一人傳承)이다. 철 대협과 비슷한 경우지.”
234|
235|“…….”
236|
237|돌려주고 싶어도 줄 수가 없네.
238|
239|그나마 화왕과 가장 가까웠던 인물이라면 조필인데, 이미 죽고 없으니 찾을 방법이 없다.
240|
241|‘가장 좋은 상황은 화왕이 이미 죽고 없는 건데…….’
242|
243|사십 년 전 이미 노인이었다고 하니 충분히 가능성이 있다.
244|
245|반대로 초절정 고수인 만큼 엄청나게 장수하고 있을 수도 있고.
246|
247|“쓰읍.”
248|
249|엄청난 보물인지, 아니면 계륵인지. 갈등 어린 눈빛으로 화염신장을 바라보는 내게 진무경이 말했다.
250|
251|“만약 화왕이 죽었다면…… 네가 바로 열화문의 주인이다.”
252|
253|
254|
255|* * *
256|
257|
258|
259|진무경은 빠르게 회복했다. 풍양으로부터 상당한 내상을 입은 탓에 완전히 회복하기까지는 어느 정도 시간이 필요하겠지만, 태원진가로 복귀할 수 있을 만한 기력은 충분했다.
260|
261|“드디어 돌아가네요.”
262|
263|혁무진이 감회 어린 얼굴로 중얼거렸다.
264|
265|“집 나오면 고생이라더니. 앞으로는 절대, 무조건! 본가 밖으로는 나오지 않을 겁니다.”
266|
267|“……누가 보면 네가 제일 고생한 줄 알겠다, 인마.”
268|
269|“왜 이러세요? 저도 나름의 고충이 있는 법입니다.”
270|
271|“너 뒤에 있는 사람한테 똑같이 말해 봐.”
272|
273|아직도 붕대를 풀지 못한 진무경이 나는 듯이 달려와 혁무진의 뒤통수를 갈겼다.
274|
275|빡!
276|
277|“컥!”
278|
279|“헛소리 그만하고 말이나 몰아.”
280|
281|“마부가 있는데 왜 제가…….”
282|
283|혁무진의 말마따나 마부는 따로 있었다. 월화가 따로 붙여 준 하오문 소속의 문도.
284|
285|그녀는 우리를 배웅하기 위해 먼저 나와 있었다.
286|
287|“잘 가요. 막상 헤어지려니까 아쉽네?”
288|
289|“그럼 지금이라도 같이 가실래요?”
290|
291|나를 향해 눈을 찡긋하는 그녀에게 농담처럼 말을 건넸다. 아직 경계심은 남아 있지만 지난 여정으로 농담 정도는 건넬 수 있는 사이가 됐다.
292|
293|“어머, 나야 그러고 싶긴 한데…… 이참에 산서 북부를 한번 쭉 돌아볼 생각이라.”
294|
295|지금까지 항산검문이 철저히 통제하고 있던 산서 북부는 열린 시장이 됐다. 산서성의 총지부장인 월화가 바빠지는 것은 당연한 결과다.
296|
297|“항산검문과의 일이 잘 풀렸나 보죠?”
298|
299|“비밀. 명색이 총지부장인데, 제가 본문의 대외비를 외인에게 떠들고 다닐 수는 없죠.”
300|
301|말은 저렇게 해도 시원시원하게 웃는 모습이 대답을 대신해 주었다.
302|
303|꼬리 아홉 개가 달려 있어도 이상하지 않은 여인이니 충분히 만족스러운 결과를 얻어 냈을 것이다.
304|
305|“다음에는 태원진가에서 만나겠네요.”
306|
307|“아, 혹시?”
308|
309|“그래도 전(前) 동맹인데, 앞으로도 계속 돈독한 관계를 유지해야 서로 좋지 않겠어요?”
310|
311|새치름하게 웃은 월화가 치맛자락을 살짝 들어 올렸다.
312|
313|“그때 꼭 다시 봐요. 그럼 이만.”
314|
315|그녀가 미리 대기하고 있던 마차에 오르자 곧장 마부가 채찍을 휘둘렀다. 빠르게 멀어져 가는 마차를 하염없이 바라보는 두 쌍의 시선이 있었다.
316|
317|“쩝. 조금만 더 있다 가시지.”
318|
319|“음, 으으음.”
320|
321|혁무진이야 그렇다 치고, 진무경은 도대체 왜?
322|
323|아쉬움이 듬뿍 묻어 나오는 녀석의 눈빛을 바라보던 내게 문득 떠오르는 생각이 있었다.
324|
325|‘저 자식, 설마…….’
326|
327|월화한테 관심이 있나?
328|
329|세상에, 이럴 수가. 저 무공밖에 모르는 놈이 여자한테 관심을 보이다니.
330|
331|이 어마어마한 빅뉴스를 혼자만 알고 있을 수는 없다. 나는 개미만 한 목소리로 혁무진에게 바싹 가까이 다가가 아주 작게 속삭였다.
332|
333|“야, 무진아.”
334|
335|“아, 깜짝아. 왜요?”
336|
337|“쉿. 놀라지 말고 들어라. 티 하나도 내지 마. 이건 무덤까지 안고 가야 할 비밀이야.”
338|
339|혁무진이 바짝 굳은 목소리로 대답했다.
340|
341|“헙, 네. 말씀하세요.”
342|
343|“저 인간…… 월화 소저한테 관심 있는 것 같아.”
344|
345|“…….”
346|
347|“아무한테도 말하지 마라. 이거 진짜 나만 아는 비밀인데, 너한테만 알려 주는 거야.”
348|
349|나의 진지한 속삭임에도 혁무진은 썩은 얼굴로 대꾸했다.
350|
351|“아, 네. 감사합니다. 정말 너무 감사해서 몸 둘 바를 모르겠네요.”
352|
353|아니, 이 새끼가?
354|
355|저 싸가지 없는 말투를 어떻게 교정시켜 줘야 할까 고민하던 그때였다.
356|
357|“은공.”
358|
359|나는 천천히 돌아섰다. 눈처럼 흰 궁장을 차려입은 이소월이 그곳에 있었다.
```

## Assembled English

```markdown
[P1]
# Chapter 124

[P2]
I was only human, so I couldn’t help wavering when Lee Seowol presented me with three martial arts manuals two nights ago.

[P3]
They were Supreme Peak martial arts, no less. Now that I had mastered the Jin Family’s Spear Technique and Jin Family’s Manoeuvre Technique, I had already been feeling the need to learn something new. Then someone dangled such a tempting offer right in front of me.

[P4]
*I can’t go on like this.*

[P5]
My fight with Pung Yang had been brutal. If not for the Unnamed Sword I’d obtained from Jopil, even two lives wouldn’t have been enough to survive.

[P6]
It was time to learn more martial arts and reach a new realm.

[P7]
*Peak master.*

[P8]
The Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist were all proven Peak martial arts—sturdy hammers capable of breaking through the supposedly insurmountable wall of the Peak realm. But…

[P9]
*If those are hammers, then this is an excavator.*

[P10]
I gazed proudly at the old book in my hand.

[P11]
This single martial arts manual was why I could reject Lee Seowol’s proposal without much regret.

[P12]
“Fl, fl, fl, fl…”

[P13]
After buffering for quite some time, Jin Mukyung finally managed to spit out a single word.

[P14]
“Flame Divine Palm!”

[P15]
“Oh, you know it? Correct.”

[P16]
Jin Mukyung even knew the ten greatest fist techniques in the world from two hundred years ago, so perhaps it was only natural that he knew about the Flame Divine Palm. This martial art was even more incredible than those.

[P17]
*Check item.*

[P18]
*Ding.*

[P19]
> **System**
>
> **Item Window**
>
> **Flame Divine Palm**
>
> **Type:** Martial arts manual  
> **Grade:** Supreme Peak  
> **Restriction:** Owner of Scorching Yang Qi  
> **Description:** One of the Fire Gate Clan’s secret techniques. A martial art based on powerful fire qi.  
> **Effect:** Acquisition of Flame Divine Palm.

[P20]
Jin Mukyung asked in disbelief.

[P21]
“How did you get this…?”

[P22]
“Some generous soul gave it to me before he left.”

[P23]
“He gave it to you?”

[P24]
“Yeah.”

[P25]
He gave it to me and then flew away to heaven.

[P26]
The Unnamed Sword, made of Ten-Thousand-Year Cold Iron capable of destroying even Body-Protecting Qi. The Blazing Flame Divine Pill, which could grant thirty years of Scorching Yang Qi.

[P27]
And finally, the Flame Divine Palm, a Supreme Peak martial art.

[P28]
Thinking of Jopil, who had given me so much before leaving this world, I gazed at the blue sky beyond the window.

[P29]
*Hope you’re doing well.*

[P30]
That was when Jin Mukyung abruptly cut in.

[P31]
“Enough nonsense. Tell me the truth. How did a secret technique of the Fire Gate Clan end up in your hands?”

[P32]
“I told you. Someone gave it to me before he left.”

[P33]
“You seem to be misunderstanding something…”

[P34]
Jin Mukyung continued with a serious expression.

[P35]
“This isn’t a situation you can gloss over with a joke.”

[P36]
“Why not?”

[P37]
“Because you could be branded a thief who stole another sect’s martial art. If this goes badly, our family could face condemnation from the entire Murim.”

[P38]
That was a problem I hadn’t considered.

[P39]
A sect’s martial arts were its foundation and its history. The Flame Divine Palm was not only a Supreme Peak martial art but also a secret technique of the Fire Gate Clan. That went without saying.

[P40]
“Ah, damn it.”

[P41]
“I’ll ask you one more time. Where and how did you acquire the Flame Divine Palm manual?”

[P42]
I let out a deep sigh before answering.

[P43]
“From Jopil.”

[P44]
“Jopil? The One Question, One Kill Jopil I know?”

[P45]
“That’s right. I defeated him and took it as spoils.”

[P46]
“Do you know how that bastard came to possess the Flame Divine Palm manual?”

[P47]
“Not really…”

[P48]
After thinking carefully, I remembered what Jopil had said at the time.

[P49]
“He claimed he was the nineteenth-generation successor to the Flame Divine Palm.”

[P50]
“How could someone like Jopil… Are you sure you didn’t mishear him?”

[P51]
“No, I’m sure. He didn’t look like he was lying, either.”

[P52]
At the time, Jopil had been drawing on his innate qi and was already dying fast. Most words spoken by someone on the brink of death were close to the truth.

[P53]
*Of course, I have to consider the possibility that Jopil was lying.*

[P54]
Jin Mukyung, who had been lost in thought, spoke with a look of bafflement.

[P55]
“If he was the successor to the Flame Divine Palm, how did he lose to someone like you?”

[P56]
“…”

[P57]
Well, that pissed me off, but he had a point.

[P58]
It was suspicious enough that Jopil had been living as a wandering martial artist despite having learned a Supreme Peak martial art.

[P59]
*Come to think of it, he couldn’t even use Sword Energy properly.*

[P60]
These days, every martial artist I met came with Sword Energy as standard and Body-Protecting Qi as an optional extra. One Question, One Kill Jopil had been among the weakest Peak masters I had fought so far.

[P61]
“Is the Flame Divine Palm weaker than I thought?”

[P62]
“What? The Flame Divine Palm is weak?”

[P63]
Jin Mukyung looked at me as if I were the craziest person he had ever seen.

[P64]
“You lunatic. You’re probably the only person under heaven who would call the Fire King’s signature martial art weak.”

[P65]
“Who’s the Fire King?”

[P66]
“I’m not in the mood for jokes.”

[P67]
“Neither am I.”

[P68]
“Stop it. It isn’t funny.”

[P69]
“Okay. So who’s the Fire King?”

[P70]
This silence lasted a little longer. Jin Mukyung opened and closed his mouth like a goldfish before letting out a deep sigh.

[P71]
“Count your fingers and toes. How many are there altogether?”

[P72]
“Twenty.”

[P73]
“Right. Even if you turned the whole world upside down and shook it out, the Fire King would still rank among its twenty greatest masters.”

[P74]
“…Whoa.”

[P75]
“One God, Three Saints, Ten Kings. You’ve never heard of them? You seriously don’t know?”

[P76]
He looked ready to twist my neck if I said I had never heard of any of them.

[P77]
Faced with Jin Mukyung’s wide-eyed stare, I cautiously opened my mouth.

[P78]
“I’ve heard of the Three Saints, at least…”

[P79]
“That’s something.”

[P80]
I meant Samsung,[^1] not the Three Saints, but whatever.

[P81]
That wasn’t important right now.

[P82]
“Then if the Fire King finds out I have the Flame Divine Palm…”

[P83]
“Something you’d rather not imagine will probably happen.”

[P84]
Damn it. A Supreme Peak master ranked among the twenty greatest experts in the entire world. If the Fire King learned about this and came looking for me, the entire Jin Family of Taiyuan could attack him together and still lose.

[P85]
*After everything it took to get this martial art…*

[P86]
My gut twisted at the thought of handing it over without even learning it.

[P87]
At that moment, Jin Mukyung, who had been gazing at the Flame Divine Palm manual just as regretfully as I was, added,

[P88]
“If the Fire King is still alive, that is.”

[P89]
“What?”

[P90]
“The Fire King last appeared forty years ago.”

[P91]
“Forty years ago?”

[P92]
“He was already an old man when he first appeared in the Murim. If not for the Great Faction War, he might have spent his entire life as a secluded eccentric.”

[P93]
Jin Mukyung continued.

[P94]
“The Demonic Cult’s morale soared after it defeated the Nangong Family and occupied Anhui Province. Its members looted, murdered, and committed arson on a massive scale. Apparently, setting fire to Mount Jiuhua was what finally provoked the Fire King.”

[P95]
“And then?”

[P96]
“A thousand people died over four days and nights, and the old man who had been living in seclusion deep within Mount Jiuhua gained the name Fire King.”

[P97]
“…A thousand people?”

[P98]
“Yes. The Demonic Cult suffered such heavy losses at Mount Jiuhua that it could not hold out for long and had to withdraw from Anhui Province.”

[P99]
A thousand people, huh…

[P100]
After careful consideration, I spoke.

[P101]
“Let’s give it back.”

[P102]
I wanted to live a long life. I didn’t want an event involving some insane old man who had single-handedly killed a thousand people added to my life.

[P103]
“We should leave right away. Anhui Province? Do people still say he lives there?”

[P104]
“No one knows. Perhaps that still hadn’t been enough to quell the Fire King’s anger. He spent an entire year crushing every Demonic Cult member he could find before disappearing into seclusion again.”

[P105]
“The Fire Gate Clan! We can find him if we go to the Fire Gate Clan.”

[P106]
“The Fire Gate Clan has only one successor at a time. It’s similar to Great Hero Cheol’s situation.”

[P107]
“…”

[P108]
So even if I wanted to return it, there was no one to give it to.

[P109]
Jopil had probably been the person closest to the Fire King, but he was already dead. I had no way to find the man.

[P110]
*The best-case scenario is that the Fire King is already dead…*

[P111]
He had already been an old man forty years ago, so it was entirely possible.

[P112]
On the other hand, as a Supreme Peak master, he might have lived an extraordinarily long life.

[P113]
“Hmm.”

[P114]
Was this a priceless treasure or a useless burden? As I stared at the Flame Divine Palm with a conflicted expression, Jin Mukyung said,

[P115]
“If the Fire King is dead… then you’re the master of the Fire Gate Clan now.”

[P116]
* * *

[P117]
Jin Mukyung recovered quickly. He had suffered considerable internal injuries from Pung Yang, so a full recovery would still take some time, but he had enough strength to return to the Jin Family of Taiyuan.

[P118]
“We’re finally going home.”

[P119]
Hyuk Mujin muttered with a deeply moved expression.

[P120]
“They say leaving home means hardship. From now on, I will never, ever leave the family grounds again!”

[P121]
“…Anyone listening would think you suffered the most, you punk.”

[P122]
“What are you talking about? I have my own hardships, you know.”

[P123]
“Try saying that to the person behind you.”

[P124]
Jin Mukyung, who still hadn’t been able to remove his bandages, came flying over and smacked Hyuk Mujin on the back of the head.

[P125]
*Whack!*

[P126]
“Urk!”

[P127]
“Enough nonsense. Drive the carriage.”

[P128]
“There’s a coachman. Why do I have to…?”

[P129]
Just as Hyuk Mujin said, we had a separate coachman—a member of the Lower District Sect whom Wolhwa had assigned to us.

[P130]
Wolhwa had come out ahead of time to see us off.

[P131]
“Goodbye. It’s a shame to part now that the time has come, isn’t it?”

[P132]
“Then would you like to come with us now?”

[P133]
I spoke jokingly to her as she winked at me. I was still wary of her, but after our journey together, we had become close enough to exchange jokes.

[P134]
“Oh my, I’d love to, but… I’m planning to take this opportunity to tour all of northern Shanxi.”

[P135]
Northern Shanxi, which the Mount Heng Sword Sect had kept under tight control until now, had become an open market. Naturally, Wolhwa—the Lower District Sect’s Chief Branch Leader for Shanxi Province—would be busy.

[P136]
“Things must have gone well with the Mount Heng Sword Sect?”

[P137]
“Secret. I may be the Chief Branch Leader, but I can’t go around telling outsiders our sect’s confidential information.”

[P138]
Her words said one thing, but her bright, carefree smile was answer enough.

[P139]
She was the sort of woman who could have nine tails and no one would find it strange, so she had probably obtained a more than satisfactory result.

[P140]
“I suppose we’ll meet at the Jin Family of Taiyuan next time.”

[P141]
“Oh, really?”

[P142]
“We were allies once. Wouldn’t it be better for both of us if we continued to maintain a close relationship?”

[P143]
Wolhwa smiled coyly and lifted the hem of her skirt slightly.

[P144]
“Make sure you come see me again then. Well, I’ll be off.”

[P145]
As soon as she climbed into the waiting carriage, the coachman cracked his whip. Two pairs of eyes gazed blankly after the carriage as it rapidly receded into the distance.

[P146]
“Tsk. She could’ve stayed a little longer.”

[P147]
“Hmm. Mmm…”

[P148]
Hyuk Mujin was one thing, but what was Jin Mukyung’s deal?

[P149]
As I watched the wistful look in his eyes, a thought suddenly occurred to me.

[P150]
*Could that bastard possibly…?*

[P151]
Was he interested in Wolhwa?

[P152]
Good heavens. I couldn’t believe it. The man who knew nothing but martial arts was showing an interest in a woman.

[P153]
I couldn’t keep this earth-shattering news to myself. I moved close to Hyuk Mujin and whispered in a voice as small as an ant.

[P154]
“Hey, Mujin.”

[P155]
“Ah! You startled me. What is it?”

[P156]
“Shh. Listen, but don’t be surprised. Don’t show even the slightest reaction. This is a secret we have to take to our graves.”

[P157]
Hyuk Mujin answered in a stiff voice.

[P158]
“Gasp. Yes. Go ahead.”

[P159]
“I think that guy… is interested in Young Lady Wolhwa.”

[P160]
“…”

[P161]
“Don’t tell anyone. This is a secret only I know, and I’m telling you alone.”

[P162]
Despite my serious whisper, Hyuk Mujin replied with a sour expression.

[P163]
“Oh, yes. Thank you. I’m so grateful I don’t know what to do with myself.”

[P164]
*Why, this little shit…*

[P165]
I was wondering how to correct that rude tone when—

[P166]
“Benefactor.”

[P167]
I slowly turned around.

[P168]
Lee Seowol stood there in a snow-white palace robe.

[P169]
[^1]: The Korean name “Samsung” is pronounced *Samseong*, the same as the Korean term rendered here as “Three Saints.”
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
# Chapter 124

[P2]
I was only human, so I couldn’t help wavering when Lee Seowol presented me with three martial arts manuals two nights ago.

[P3]
They were Supreme Peak martial arts, no less. Now that I had mastered the Jin Family’s Spear Technique and Jin Family’s Manoeuvre Technique, I had already been feeling the need to learn something new. And then, right in front of me, someone had dangled such a tempting offer.

[P4]
*This won’t do.*

[P5]
My fight with Pung Yang had been brutal. If I hadn’t had the Unnamed Sword I’d obtained from Jopil, I wouldn’t have survived even if I’d had two lives.

[P6]
It was time to learn more martial arts and enter a new realm.

[P7]
*Peak master.*

[P8]
The Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist were all proven Peak martial arts. They were sturdy hammers, strong enough to break through that supposedly insurmountable wall of the Peak realm. But…

[P9]
*If those are hammers, then this is an excavator.*

[P10]
I gazed proudly at the old book in my hand.

[P11]
This one martial arts manual was the reason I could reject Lee Seowol’s proposal without much regret.

[P12]
“Fl, fl, fl, fl…”

[P13]
After buffering for quite some time, Jin Mukyung finally managed to spit out a single word.

[P14]
“Flame Divine Palm!”

[P15]
“Oh, you know it? Correct.”

[P16]
Jin Mukyung knew even the ten greatest fist techniques in the world from two hundred years ago, so perhaps it was only natural that he knew about the Flame Divine Palm. This martial art was even more incredible than those.

[P17]
*Check item.*

[P18]
*Ding.*

[P19]
> **System**
>
> **Item Window**
>
> **Flame Divine Palm**
>
> **Type:** Martial arts manual  
> **Grade:** Supreme Peak  
> **Restriction:** Owner of Scorching Yang Qi  
> **Description:** One of the secret techniques of the Fire Gate Clan. A martial art based on powerful fire energy.  
> **Effect:** Acquisition of Flame Divine Palm.

[P20]
Jin Mukyung asked with an expression of utter disbelief.

[P21]
“How did you get this…?”

[P22]
“Some generous soul gave it to me before he left.”

[P23]
“He gave it to you?”

[P24]
“Yeah.”

[P25]
He gave it to me and then flew away to heaven.

[P26]
The Unnamed Sword, made of Ten-Thousand-Year Cold Iron capable of destroying even Body-Protecting Qi. The Blazing Flame Divine Pill, which could grant me thirty years of Scorching Yang Qi.

[P27]
And finally, the Flame Divine Palm, a Supreme Peak martial art.

[P28]
Thinking of Jopil, who had given me so much before leaving this world, I gazed at the blue sky beyond the window.

[P29]
*I hope you’re doing well.*

[P30]
That was when Jin Mukyung abruptly cut in.

[P31]
“Stop spouting nonsense and tell me the truth. How did a secret technique of the Fire Gate Clan end up in your hands?”

[P32]
“I told you. Someone gave it to me before he left.”

[P33]
“It seems you’re under some kind of misunderstanding…”

[P34]
Jin Mukyung continued with a serious expression.

[P35]
“This isn’t a situation you can gloss over with a joke.”

[P36]
“Why not?”

[P37]
“Because you could end up branded a thief who stole another sect’s martial arts. If things go badly, the Jin Family could be condemned by the entire Murim.”

[P38]
That was a problem I hadn’t considered.

[P39]
Martial arts were the foundation and history of a sect. The Flame Divine Palm was not only a Supreme Peak martial art but also a secret technique of the Fire Gate Clan. That went without saying.

[P40]
“Damn it.”

[P41]
“I’ll ask you one more time. Where and how did you acquire the manual for the Flame Divine Palm?”

[P42]
I let out a deep sigh before answering.

[P43]
“From Jopil.”

[P44]
“Jopil? The One Question, One Kill Jopil I know?”

[P45]
“That’s right. I defeated Jopil and obtained it as spoils.”

[P46]
“Do you know how that bastard came to possess the Flame Divine Palm manual?”

[P47]
“Not really…”

[P48]
After thinking carefully, I remembered what Jopil had said at the time.

[P49]
“He claimed he was the nineteenth-generation successor of the Flame Divine Palm.”

[P50]
“How could someone like Jopil be… Are you sure you didn’t hear him wrong?”

[P51]
“No, I’m sure. He didn’t look like he was lying, either.”

[P52]
At the time, Jopil had been drawing on his innate qi, and he had already been dying rapidly. Words spoken by someone standing on the brink of death were usually close to the truth.

[P53]
*Of course, I have to consider the possibility that Jopil was lying.*

[P54]
Jin Mukyung had been lost in thought. Then he spoke with an expression of confusion.

[P55]
“If he was a successor of the Flame Divine Palm, how did he lose to someone like you?”

[P56]
“…”

[P57]
Well, that pissed me off, but he had a point.

[P58]
It was suspicious enough that Jopil had been living as a wandering martial artist despite having learned a Supreme Peak martial art.

[P59]
*Now that I think about it, he couldn’t even use Sword Energy properly.*

[P60]
These days, every martial artist I met came with Sword Energy as standard and Body-Protecting Qi as an optional extra. One Question, One Kill Jopil had been among the weakest Peak masters I had fought so far.

[P61]
“Is the Flame Divine Palm weaker than I thought?”

[P62]
“What? The Flame Divine Palm is weak?”

[P63]
Jin Mukyung looked at me as if I were the craziest person he had ever seen.

[P64]
“You lunatic. You’re probably the only person in the world who would call the Fire King’s signature martial art weak.”

[P65]
“Who’s the Fire King?”

[P66]
“I’m not in the mood for jokes.”

[P67]
“Neither am I.”

[P68]
“Stop it. You’re not funny.”

[P69]
“Okay. So who’s the Fire King?”

[P70]
This silence lasted a little longer. Jin Mukyung opened and closed his mouth like a goldfish before letting out a deep sigh.

[P71]
“Count your fingers and toes. How many are there altogether?”

[P72]
“Twenty.”

[P73]
“Right. Even if you turned the entire world upside down and shook it out, the Fire King would still be among the twenty greatest masters in it.”

[P74]
“…Whoa.”

[P75]
“One God, Three Saints, Ten Kings. You’ve never heard of them? You really don’t know?”

[P76]
He looked ready to twist my neck if I said I had never heard of any of them.

[P77]
Under Jin Mukyung’s ringed eyes, I cautiously opened my mouth.

[P78]
“I’ve heard of the Three Saints, at least…”

[P79]
“That’s something.”

[P80]
I meant Samsung,[^1] not the Three Saints, but whatever.

[P81]
[^1]: The Korean name “Samsung” is pronounced *Samseong*, the same as the Korean term rendered here as “Three Saints.”

[P82]
That wasn’t important right now.

[P83]
“Then if the Fire King finds out that I have the Flame Divine Palm…”

[P84]
“Something you won’t particularly want to imagine will happen.”

[P85]
Damn it. A Supreme Peak master ranked among the twenty greatest experts in the entire world. If the Fire King learned about this and came looking for me, the entire Jin Family of Taiyuan could attack him together and still lose.

[P86]
*After everything it took to obtain this martial art…*

[P87]
My gut twisted at the thought that I might have to hand it over without even learning it.

[P88]
At that moment, Jin Mukyung, who had been gazing sorrowfully at the Flame Divine Palm manual just as I was, added one more thing.

[P89]
“If the Fire King is still alive.”

[P90]
“What?”

[P91]
“The last time the Fire King appeared was forty years ago.”

[P92]
“Forty years ago?”

[P93]
“When he first appeared in the Murim, the Fire King was already an old man. If not for the Great Faction War, he might have lived his entire life as a secluded eccentric.”

[P94]
Jin Mukyung continued.

[P95]
“The Demonic Cult’s morale soared after it defeated the Nangong Family and occupied Anhui Province. They carried out countless acts of looting, murder, and arson, and apparently, setting fire to Mount Jiuhua was what finally provoked the Fire King.”

[P96]
“And then?”

[P97]
“A thousand people died over four days and nights, and the old man who had been living in seclusion deep within Mount Jiuhua gained the name Fire King.”

[P98]
“…A thousand people?”

[P99]
“Yes. The Demonic Cult suffered such heavy losses at Mount Jiuhua that it could not hold out for long and had to withdraw from Anhui Province.”

[P100]
A thousand people, huh…

[P101]
After careful consideration, I opened my mouth.

[P102]
“Let’s give it back.”

[P103]
I wanted to live a long life. I didn’t want an event involving some insane old man who had killed a thousand people by himself added to my life.

[P104]
“We should leave right away. Anhui Province? Do people still say he lives there?”

[P105]
“No one knows. Perhaps that still hadn’t been enough to quell the Fire King’s anger. He spent an entire year crushing every Demonic Cult member he could find before disappearing into seclusion again.”

[P106]
“The Fire Gate Clan! We can find him if we go to the Fire Gate Clan.”

[P107]
“The Fire Gate Clan has a single successor. It’s a situation similar to Great Hero Cheol’s.”

[P108]
“…”

[P109]
Even if I wanted to return it, I had no one to give it to.

[P110]
And the person who had probably been closest to the Fire King was Jopil, but he was already dead. There was no way to find him.

[P111]
*The best-case scenario would be that the Fire King is already dead…*

[P112]
He had already been an old man forty years ago, so it was certainly possible.

[P113]
On the other hand, as a Supreme Peak master, he might have lived an extraordinarily long life.

[P114]
“Hmm.”

[P115]
Was this a priceless treasure or a useless burden? As I stared at the Flame Divine Palm with a conflicted expression, Jin Mukyung said,

[P116]
“If the Fire King is dead… then you’re the master of the Fire Gate Clan now.”

[P117]
* * *

[P118]
Jin Mukyung recovered quickly. His Internal Injuries from Pung Yang had been considerable, so it would still take some time for him to recover completely, but he had enough strength to return to the Jin Family of Taiyuan.

[P119]
“We’re finally going home.”

[P120]
Hyuk Mujin muttered with deep emotion.

[P121]
“They say leaving home means hardship. From now on, I will never, ever leave the family grounds again!”

[P122]
“…Anyone listening to you would think you were the one who suffered the most, you punk.”

[P123]
“What are you talking about? I have my own hardships, you know.”

[P124]
“Try saying that to the person behind you.”

[P125]
Jin Mukyung, who still hadn’t been able to remove his bandages, came flying over and smacked Hyuk Mujin on the back of the head.

[P126]
*Whack!*

[P127]
“Urk!”

[P128]
“Stop spouting nonsense and drive the carriage.”

[P129]
“There’s a coachman. Why do I have to…?”

[P130]
Just as Hyuk Mujin said, we had a separate coachman—a member of the Lower District Sect whom Wolhwa had assigned to us.

[P131]
Wolhwa had come out ahead of time to see us off.

[P132]
“Goodbye. It’s a shame to part now that the time has come, isn’t it?”

[P133]
“Then would you like to come with us now?”

[P134]
I spoke jokingly to her as she winked at me. I was still wary of her, but after traveling together, we were close enough to exchange jokes.

[P135]
“Oh, I would like that, but… I’m planning to take this opportunity to make a full tour of northern Shanxi.”

[P136]
Northern Shanxi, which had been under the strict control of the Mount Heng Sword Sect until now, had become an open market. It was only natural that Wolhwa, the Lower District Sect’s Chief Branch Leader in Shanxi Province, would be busy.

[P137]
“Things must have gone well with the Mount Heng Sword Sect?”

[P138]
“Secret. I may be the Chief Branch Leader, but I can’t go around telling outsiders the sect’s confidential information.”

[P139]
Her words said one thing, but her bright, carefree smile was answer enough.

[P140]
She was the sort of woman who could have nine tails and no one would find it strange, so she had probably obtained a more than satisfactory result.

[P141]
“We’ll meet again at the Jin Family of Taiyuan next time.”

[P142]
“Oh, really?”

[P143]
“We were allies once. Wouldn’t it be better for both of us if we continued to maintain a close relationship?”

[P144]
Wolhwa gave a coy smile and lifted the hem of her skirt slightly.

[P145]
“Make sure you come see me again then. Well, I’ll be off.”

[P146]
As soon as she climbed into the carriage waiting nearby, the coachman cracked his whip. Two pairs of eyes gazed blankly at the carriage as it quickly disappeared into the distance.

[P147]
“Tsk. She could’ve stayed a little longer.”

[P148]
“Hmm. Mmm…”

[P149]
Hyuk Mujin was one thing, but why was Jin Mukyung doing that?

[P150]
As I watched his wistful gaze, a thought suddenly occurred to me.

[P151]
*Could that bastard possibly…?*

[P152]
Was he interested in Wolhwa?

[P153]
Good heavens. I couldn’t believe it. The man who knew nothing but martial arts was showing an interest in a woman.

[P154]
I couldn’t keep this earth-shattering news to myself. I moved close to Hyuk Mujin and whispered in a voice as small as an ant.

[P155]
“Hey, Mujin.”

[P156]
“Ah! You startled me. What is it?”

[P157]
“Shh. Listen, but don’t be surprised. Don’t show even the slightest reaction. This is a secret we have to take to our graves.”

[P158]
Hyuk Mujin answered in a stiff voice.

[P159]
“Gasp. Yes. Go ahead.”

[P160]
“I think that guy is interested in Young Lady Wolhwa.”

[P161]
“…”

[P162]
“Don’t tell anyone. This is a secret only I know, and I’m telling you alone.”

[P163]
Despite my serious whisper, Hyuk Mujin replied with a sour expression.

[P164]
“Oh, yes. Thank you. I’m so grateful I don’t know what to do with myself.”

[P165]
*Why, this little shit…*

[P166]
I was wondering how to correct that rude tone when—

[P167]
“Benefactor.”

[P168]
I slowly turned around.

[P169]
Lee Seowol stood there, dressed in a snow-white formal robe.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이소월    | **Lee Seowol**     |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 일신     | **One God**         |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 열화문    | **Fire Gate Clan**               |
| 남궁세가   | **Nangong Family**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 검법     | **sword technique**                              |                                                       |
| 권법     | **fist technique**                               |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 지부장    | **Branch Leader**                            |
| 진가창법   | **Jin Family's Spear Technique**       |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 습득               | **Acquired**                   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 안휘     | **Anhui**              |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 124,
  "passed": true,
  "metrics": {
    "source_characters": 5442,
    "translation_characters": 12480,
    "length_ratio": 2.293,
    "source_paragraphs": 173,
    "translation_paragraphs": 169
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기세",
        "preferred": "aura / momentum"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가창법",
        "preferred": "Jin Family's Spear Technique"
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
        "korean": "습득",
        "preferred": "Acquired"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "화산",
        "preferred": "Huashan"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "내상",
        "preferred": "Internal Injury"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진무보법",
        "preferred": "Jin Family's Manoeuvre Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "세가",
        "preferred": "great family"
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
