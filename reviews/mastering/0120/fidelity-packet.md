# Fidelity Gate — Chapter 120

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
  1|＃120화
  2|
  3|
  4|
  5|쉭!
  6|
  7|느리지만 힘차게 찔러 들어오는 검 한 자루.
  8|
  9|짧은 순간, 풍양의 입가에 비웃음이 떠올랐다.
 10|
 11|‘그래, 이럴 줄 알았지.’
 12|
 13|온갖 암수가 난무하는 고원에서 수십 년을 살았다. 같은 수법에 두 번이나 걸려들 만큼 어리석었다면 진즉 들개 밥이 되었을 것이다.
 14|
 15|‘그런데 저 검은 어디서 튀어나온 거지?’
 16|
 17|비수도 아니고 저만한 길이의 장검을 어디에 숨겨 놨던 걸까? 풍양은 가벼운 의문과 함께 호신강기를 끌어 올렸다.
 18|
 19|스스스스.
 20|
 21|예상했던 일이었기에 대처도 빨랐다. 순식간에 솟구쳐 오른 붉은 기가 빈틈없이 몸을 감싼다.
 22|
 23|호신강기는 강력한 검기(劍氣)가 아닌 이상 생채기 하나 낼 수 없는 무적의 갑옷. 어린놈의 헛된 발악이 우습기만 했다.
 24|
 25|‘지긋지긋한 놈. 이제 그만 죽어라.’
 26|
 27|단숨에 진태경의 목을 꺾어 버리려던 그 순간이었다.
 28|
 29|푹-!
 30|
 31|“……어?”
 32|
 33|몸 안을 파고드는 서늘한 냉기, 그리고 그 뒤를 잇는 뜨거운 통증. 풍양은 부릅뜬 눈으로 가슴을 관통한 검을 바라봤다.
 34|
 35|‘이게 무슨.’
 36|
 37|호신강기가 사라졌다. 아니, 파괴됐다.
 38|
 39|진태경의 검은 호신강기를 두부 가르듯 베어 버리고 그의 가슴마저 꿰뚫었다.
 40|
 41|피 한 방울 묻지 않은 투명한 검신을 내려다보던 풍양이 신음처럼 내뱉었다.
 42|
 43|“만년한철……?”
 44|
 45|들어 본 적이 있다. 천하의 그 무엇도 자르고 부술 수 있다는 신병이기(神兵利器)에 관한 이야기를.
 46|
 47|“이걸 네놈이 어떻게.”
 48|
 49|풍양은 일그러진 얼굴로 검의 주인을 바라봤다. 태원진가의 어린놈은 천진난만하게 눈을 깜빡이더니 입을 열었다.
 50|
 51|“와, 이게 되네.”
 52|
 53|“이런 개새끼가……!”
 54|
 55|당장 목을 꺾어 버리고 싶었지만, 순간 눈앞이 아득해지며 손아귀에서 힘이 풀렸다. 몸 안에 가득 차 있던 힘이 썰물처럼 사라지고 무력감이 차오른다.
 56|
 57|‘하필 이럴 때 잠력단의 효력이.’
 58|
 59|비틀비틀 물러나는 풍양의 칠공(七空)에서 피가 흘러나왔다.
 60|
 61|지금까지 입은 크고 작은 부상과 호신강기가 흩어지며 역류한 공력이 빠르게 그를 죽음으로 몰아가기 시작했다.
 62|
 63|‘이대로, 이대로 죽을 수는 없어.’
 64|
 65|풍양은 황급히 품을 더듬었다.
 66|
 67|아직 잠력단 한 알이 남아 있다. 그것만 먹으면 놈들을 단매에 쳐 죽이고 이 자리를 뜰 수 있다. 잃은 것이 적진 않지만 몸을 추스른 다음 다시 무림에 나오면 되는 거다.
 68|
 69|그래, 잠력단을 먹기만 하면…….
 70|
 71|툭.
 72|
 73|제기랄, 마음이 너무 급했다.
 74|
 75|풍양의 다급한 손길에 떨어진 목곽이 땅에 부딪치며 활짝 열렸다. 피처럼 붉은빛이 도는 단환이 또르르 굴러가더니 누군가의 발아래에 멈춘다.
 76|
 77|“아, 이게 잠력단이야?”
 78|
 79|신기한 듯 잠력단을 주워 살펴보는 진태경을 향해 풍양이 외쳤다.
 80|
 81|“내, 내놔라, 어서!”
 82|
 83|“여기서 문제, 그런다고 내가 줄까?”
 84|
 85|“놈!”
 86|
 87|있는 힘을 다해 달려들었지만 이미 망가진 신체는 한계에 달해 있었다. 진태경에게 닿기도 전에 힘이 풀린 다리가 풀썩 주저앉았다.
 88|
 89|이제 풍양에게 남은 길은 하나밖에 없었다.
 90|
 91|“제발 부탁이다. 내게, 내게 그걸 다오.”
 92|
 93|“만약에 준다면?”
 94|
 95|풍양이 간절하게 외쳤다.
 96|
 97|“다시는 네 눈에 띄지 않으마. 아니, 앞으로 네게 충성을 다하겠다!”
 98|
 99|“오, 절정 고수 수하라. 그거 괜찮은데.”
100|
101|“그, 그렇지? 그러니 어서 내게 잠력단을 다오!”
102|
103|“일단 내 물건부터 돌려받고.”
104|
105|“물건?”
106|
107|그의 의문은 곧 풀렸다. 다가온 진태경이 가슴 한복판에 박혀 있던 검을 쑥 뽑은 것이다.
108|
109|아찔한 고통과 함께 피가 폭포수처럼 흘렀다.
110|
111|“쿠에에에엑!”
112|
113|풍양은 자신이 토해 낸 핏물에 내장 조각이 섞인 것도 눈치채지 못했다.
114|
115|단지 시야가 점점 어두워지고 소리가 아득히 멀어지는 것을 느꼈을 뿐이다.
116|
117|그는 죽어 가고 있었고, 간절함에 반쯤 미쳐 있었다.
118|
119|‘살고 싶다.’
120|
121|일평생을 무자비한 약탈자로 살아온 풍양이다.
122|
123|지금껏 무수히 많은 이들의 재물을, 혹은 목숨을 빼앗았지만, 자신이 이런 최후를 맞이할 것이라고는 꿈에도 생각하지 못했다.
124|
125|“이제, 이제 제발 잠력단을…….”
126|
127|흐릿한 시선 속, 고개를 가로젓는 진태경의 모습에 그가 애처롭게 중얼거렸다.
128|
129|“왜? 어째서?”
130|
131|그러나 대답은 다른 곳에서 들려왔다.
132|
133|“뭐라? 어째서?”
134|
135|“저 찢어 죽여도 시원찮을 놈이……!”
136|
137|살아남은 항산검문의 무인들이 살기 어린 눈빛으로 각자의 병장기를 움켜쥐었다.
138|
139|이소월 역시 입술을 깨물며 풍양에게로 활을 겨눴지만 진태경이 황급히 만류했다.
140|
141|“막타 자제 좀…… 아니, 편안하게 죽이기에는 너무 악랄한 놈입니다. 저렇게 천천히 죽어 가도록 두는 게 나아요.”
142|
143|짧은 시간, 이소월은 결국 수많은 갈등 끝에 활을 내렸다. 그러자 진태경이 풍양에게로 다가가 귓가에 작은 목소리로 속삭였다.
144|
145|“나도 슬슬 힘들다. 이제 죽자.”
146|
147|무슨 소리인지는 모르겠지만 하나는 확실하다.
148|
149|죽음. 풍양은 자신의 죽음이 코앞으로 성큼 다가왔음을 깨달았다.
150|
151|“원귀가 되어서라도 복수해 주마.”
152|
153|“아멘. 부디 다음 생에는 비아그라 정도로 만족해라.”
154|
155|풍양은 헛웃음을 터트렸다. 마지막 순간까지 저놈의 뜻 모를 헛소리를 들어야 하는 자신의 처지가 우습기 짝이 없었다.
156|
157|‘제기랄. 날씨 하고는.’
158|
159|고개를 들어 바라본 하늘은 온통 붉었다. 그리고 이내 암흑으로 물들었다.
160|
161|
162|
163|* * *
164|
165|
166|
167|스르륵.
168|
169|풍양의 고개가 꺾임과 동시에 허공에서 축포가 터졌다.
170|
171|띠링. 띠링. 띠링!
172|
173|
174|
175|- [Lv.85 풍양]을 처치했습니다!
176|
177|- [잠력단] 퀘스트를 성공적으로 완료했습니다!
178|
179|- 막대한 경험치와 명성을 얻었습니다!
180|
181|- 레벨 업!
182|
183|- 레벨 업!
184|
185|.
186|
187|.
188|
189|
190|
191|자그마치 다섯 번의 레벨 업과 명성치 상승을 알리던 시스템창은 이윽고 더 반가운 소식을 전해 주었다.
192|
193|
194|
195|- 퀘스트 성공 보상이 인벤토리에 지급되었습니다!
196|
197|- 퀘스트 성공 보상으로 [완전 회복]이 즉각 적용됩니다!
198|
199|
200|
201|‘완전 회복?’
202|
203|즉각 적용이라더니, 그 말대로 변화는 순식간에 일어났다.
204|
205|금이 가고 부러졌던 뼈가 붙고, 베이거나 찔린 상처는 씻은 듯이 아물었다. 변화는 외관에서 그치지 않았다.
206|
207|‘내상이…….’
208|
209|신체 내부에서도 보이지 않는 회복이 이루어졌다. 모든 내상이 낫는 것까지는 예상했지만 생각한 것 이상의 소득도 있었다.
210|
211|
212|
213|- [내상]이 모두 회복됩니다!
214|
215|- 안정된 신체가 새로운 기운을 받아들입니다!
216|
217|- [열화신단]을 완전히 흡수했습니다!
218|
219|- [공력]이 45년으로 상승합니다!
220|
221|- [공력-열양지기]의 특성이 부여됩니다!
222|
223|
224|
225|열화신단의 완전한 흡수. 그리고 비약적으로 상승한 공력.
226|
227|사지백해에 가득 찬 힘이 느껴진다. 용암처럼 내 몸을 태우던 열양지기는 어느새 따뜻한 봄바람이 되어 있었다.
228|
229|‘해냈구나.’
230|
231|레벨 업을 해서 몸이 어느 정도 회복되면 바로 운기조식으로 열양지기를 다스릴 생각이었는데…… 시스템 덕분에 어려운 일을 손쉽게 해치웠다.
232|
233|‘세상에, 45년이면 얼마야.’
234|
235|원래 가지고 있던 것에 비해 세 배, 자그마치 반 갑자(30년)의 공력이 추가로 늘어난 것이다.
236|
237|‘반 갑자라.’
238|
239|평범한 상황이었다면 열화신단을 복용하는 것은 뒤로 미뤄졌을 것이다. 그러나 도박처럼 시도했던 일이 신의 한 수가 되어 돌아왔다.
240|
241|‘천운이 따라 주지 않았다면 죽었겠지만.’
242|
243|두 번의 천운. 그중 하나는 열화신단이고, 다른 하나는 지금 내 손에 들려 있는 [이름 없는 검]이다.
244|
245|모두 몇 달 전 조필을 쓰러트리고 얻은 전리품들.
246|
247|‘이게 아니었으면 정말 큰일 날 뻔했어.’
248|
249|그저 다른 검들보다 조금 더 날카롭고 단단한 검이라고 생각했는데, 이게 사실은 만년한철이고, 그런 효능이 있는 줄은 꿈에도 몰랐다.
250|
251|그런 의미에서 오늘의 내게는 운칠기삼(運七技三)이 아니라 운구기일(運九氣一)이라는 말이 더 어울린다.
252|
253|‘이걸 운이 좋다고 해야 할지는 모르겠지만.’
254|
255|나는 천천히 주위를 둘러보았다. 거꾸로 꽂힌 병장기의 무덤, 누군가는 한가득 고인 피 웅덩이에 얼굴을 처박은 채로 죽었고 누군가는 부릅뜬 눈으로 여명이 밝아 오는 하늘을 바라보고 있다. 그런 시신들이 무려 수백에 이른다.
256|
257|“여기 생존자가 있다!”
258|
259|“춘삼아! 정신 좀 차려 보거라!”
260|
261|그 참혹한 광경 속에서 부지런히 움직이는 항산검문의 무인들. 몇 안 되는 생존자들을 일사불란하게 구해 내는 그들을 보고 있는데 문득 알 수 없는 위화감에 휩싸였다.
262|
263|‘뭐지?’
264|
265|뭔가 중요한 사실 하나를 잊은 것 같은데…….
266|
267|눈살을 찌푸리던 그때, 죽은 듯이 누워 있던 시체 하나가 상반신을 일으켰다.
268|
269|“크으으으.”
270|
271|“아.”
272|
273|그래, 반갑다 무경아.
274|
275|
276|
277|* * *
278|
279|
280|
281|장장 두 시진에 걸친 수색 작업이 끝났을 때쯤, 이소월의 몸은 핏물로 흠뻑 젖어 있었다.
282|
283|“생존자는?”
284|
285|“문주님을 포함…… 스물다섯입니다.”
286|
287|“몇 명이라고?”
288|
289|“스물다섯 명입니다. 그중 다섯은 오늘을 넘기기 힘들 것 같습니다.”
290|
291|물어본 이소월도, 대답한 무인도 입을 다물었다.
292|
293|한때 태원진가와 함께 산서성을 양분하던 항산검문은 이제 더 이상 존재하지 않는다. 남은 것은 부상자들과 약관도 되지 않은 어린 문주뿐이다.
294|
295|‘이곳을 버리고 도망쳤다면, 처음부터 풍양의 혼인 제안을 받아들였다면 그들을 살릴 수 있었을까?’
296|
297|후회는 언제나 부질없다. 그러나 이소월은 후회해야 했다.
298|
299|비록 얼마 남지 않았지만, 그녀는 여전히 일문(一門)의 문주였다. 뼈에 사무치게 고민하고 후회해야 이후에 같은 실수를 하지 않는다.
300|
301|그것이 오늘 죽은 이들을 위한 속죄고 남은 이들을 위한 노력이다.
302|
303|‘항산검문은 반드시 살아남는다. 본문을 위해 목숨을 바친 그대들을 위해서라도.’
304|
305|이소월은 주먹을 움켜쥐었다. 활시위를 당기며 깨진 손톱이 살을 파고들며 피가 배어 나왔지만 고통도 느끼지 못했다.
306|
307|“다른 사람들은?”
308|
309|“모두 대전에 있습니다. 태원진가 측에 제법 의술을 아는 여인이 있어 그녀가 부상자들을 돌보는 중입니다만…….”
310|
311|무인의 낯빛이 어두워졌다. 그만큼 몇몇 부상자들의 상태가 안 좋다는 증거다. 이소월은 더 이상 묻지 않고 대전을 향해 걸음을 옮겼다.
312|
313|‘추스르기도 전에 또다시 떠나보내는구나.’
314|
315|참을 수 없는 피로가 전신을 짓눌렀지만 정신력으로 버텼다. 적어도 떠나는 이들의 마지막은 지켜야 하지 않겠는가.
316|
317|끼이이익.
318|
319|대전으로 들어서자 태원진가에서 온 이들은 보이지 않았고, 누워 있는 부상자들이 곧장 눈에 띄었다.
320|
321|항산호 철무백과 십수 명의 무인들이 그녀를 발견하고 말을 건넸다.
322|
323|“아, 소월이 왔느냐?”
324|
325|“오셨습니까. 문주님!”
326|
327|“문주님을 뵙습니다!”
328|
329|“……?”
330|
331|기분 탓인가. 어쩐지 죽어 가는 것치고는 다들 활기가 넘친다. 한동안 말없이 그들을 바라보던 이소월은 활기의 정체를 깨달았다.
332|
333|“회광반조(回光返照)…….”
334|
335|그제야 저들의 얼굴 위에 짙게 드리운 죽음의 그림자가 보인다. 그녀가 터지려는 울음을 참으며 황급히 돌아선 그 순간이었다.
336|
337|쿵!
338|
339|뭔가 단단한 것에 이마를 부딪친 이소월이 비틀거렸다. 쓰러지려는 그녀의 어깨를 크고 단단한 손바닥이 감쌌다.
340|
341|“아이고, 조심 좀 하시지. 괜찮아요?”
342|
343|“아, 네.”
344|
345|“그럼 됐고.”
346|
347|이소월을 내려다보던 진태경이 피식 웃었다.
348|
349|
350|
351|* * *
352|
353|
354|
355|‘회광반조는 무슨.’
356|
357|새어 나오려는 실소를 간신히 참았다. 철무백과 다른 부상자들은 다들 팔팔하게 살아나는 중이다.
358|
359|아, 물론 진무경도 마찬가지고.
360|
361|‘나 아니었으면 어쩔 뻔했나.’
362|
363|정확히 말하면 퀘스트 보상이 아니었으면 저들 중 절반은 초상을 치렀을지도 모르겠다.
364|
365|각각 서른 개씩이나 보상으로 지급받은 [뛰어난 금창약]과 [십년하수오]는 외상과 내상 치유에 뛰어난 효과가 있었다.
366|
367|‘만약을 대비해서 아낄까도 생각해 봤지만…….’
368|
369|사람이 죽어 가는데 모른 척할 정도로 모진 놈은 아니다. 물론 수량이 많았던 것도 한몫했다.
370|
371|“안 들어가요?”
372|
373|“네?”
374|
375|“안 들어가실 거면 나 먼저 들어가고.”
376|
377|어쩐지 멍한 채로 선 이소월을 지나치려다가 문득 잊고 있던 게 생각났다. 가만있자, 그걸 어디 뒀더라?
378|
379|“아, 여기 있다.”
380|
381|품을 뒤지는 척하면서 인벤토리에서 죽간 하나를 꺼냈다.
382|
383|“여기요. 우리 형…… 아니, 소가주님이 보내시는 거.”
384|
385|이소월이 얼떨떨한 얼굴로 죽간을 받아 들기가 무섭게 시스템 알림이 울렸다.
386|
387|띠링.
388|
389|
390|
391|- 초대장 전달을 완료했습니다.
392|
393|- 퀘스트, [어제의 적, 오늘의 동지]를 완수했습니다!
394|
395|
396|
397|초대장 전달. 두 번 했다가는 사람 잡겠다.
```

## Assembled English

```markdown
[P1]
# Chapter 120

[P2]
*Shwick!*

[P3]
A sword thrust forward—slowly, but with tremendous force.

[P4]
For the briefest moment, a mocking smile appeared at the corner of Pung Yang’s mouth.

[P5]
*I knew this was coming.*

[P6]
He had spent decades living in Gaoyuan, where every kind of underhanded trick ran rampant. If he had been foolish enough to fall for the same trick twice, he would have become wild-dog food long ago.

[P7]
*But where did that sword come from?*

[P8]
It wasn’t a dagger. Where had the brat hidden a longsword that size?

[P9]
With that slight question in mind, Pung Yang drew up his Body-Protecting Qi.

[P10]
*Fssssss.*

[P11]
He had expected this, so his response was quick. Red qi surged up in an instant and wrapped tightly around his body.

[P12]
Body-Protecting Qi was invincible armor that nothing short of powerful Sword Energy could so much as scratch. The young brat’s futile struggle was laughable.

[P13]
*What an annoying bastard. Just die already.*

[P14]
He was about to snap Jin Taekyung’s neck in a single motion when—

[P15]
*Thud!*

[P16]
“…Huh?”

[P17]
A cold chill pierced his body, followed by searing pain. Pung Yang stared wide-eyed at the sword that had pierced straight through his chest.

[P18]
*What the hell?*

[P19]
His Body-Protecting Qi had vanished.

[P20]
No—it had been destroyed.

[P21]
Jin Taekyung’s sword sliced through it as easily as cutting tofu, then pierced Pung Yang’s chest as well.

[P22]
Pung Yang looked down at the transparent blade, unstained by even a drop of blood, and muttered like he was groaning.

[P23]
“Ten-Thousand-Year Cold Iron…?”

[P24]
He had heard of it before. Stories about a divine weapon said to be capable of cutting and breaking anything in the world.

[P25]
“How did you get this?”

[P26]
Pung Yang glared at the sword’s owner with a twisted expression. The young brat from the Jin Family of Taiyuan blinked innocently.

[P27]
“Wow. This actually worked.”

[P28]
“You fucking bastard…!”

[P29]
He wanted to snap the brat’s neck right away, but his vision suddenly went hazy, and the strength drained from his grip. The power that had filled his body vanished like the outgoing tide, leaving only helplessness in its wake.

[P30]
*The Temporary Strength Pill had to wear off now of all times.*

[P31]
Blood streamed from the seven openings in Pung Yang’s face as he staggered backward.

[P32]
The injuries he had suffered, both great and small, combined with the dispersal of his Body-Protecting Qi. The internal energy surging backward through his body began driving him rapidly toward death.

[P33]
*I can’t die like this. I can’t.*

[P34]
Pung Yang hurriedly searched inside his robes.

[P35]
He still had one Temporary Strength Pill left. If he took it, he could beat these bastards to death in a single stroke and leave this place. He had lost plenty, but he could recover and return to Murim afterward.

[P36]
Yes. All he had to do was take the Temporary Strength Pill…

[P37]
*Clatter.*

[P38]
Damn it. He was in too much of a hurry.

[P39]
The wooden box slipped from Pung Yang’s frantic hand, struck the ground, and sprang open. A pill tinged with a blood-red color rolled across the ground before coming to a stop beneath someone’s foot.

[P40]
“Oh, so this is the Temporary Strength Pill?”

[P41]
Jin Taekyung picked it up and examined it curiously. Pung Yang shouted at him.

[P42]
“G-Give it to me! Hurry!”

[P43]
“Here’s a question. Do you really think I’ll give it to you just because you ask?”

[P44]
“You bastard!”

[P45]
Pung Yang lunged forward with all his remaining strength, but his ruined body had already reached its limit. His legs gave out before he could reach Jin Taekyung, and he crumpled to the ground.

[P46]
Only one path remained to Pung Yang now.

[P47]
“Please. I’m begging you. Give it to me. Give it to me!”

[P48]
“What if I do?”

[P49]
Pung Yang cried out desperately.

[P50]
“You’ll never see me again. No—I’ll swear my loyalty to you from this day forward!”

[P51]
“Oh, a Peak master as my subordinate. That sounds pretty good.”

[P52]
“R-Really? Then hurry and give me the Temporary Strength Pill!”

[P53]
“First, I’m taking my property back.”

[P54]
“Your property?”

[P55]
His question was answered a moment later when Jin Taekyung approached and yanked the sword from the center of his chest.

[P56]
Blood poured out like a waterfall, accompanied by dizzying pain.

[P57]
“Gueeeeegh!”

[P58]
Pung Yang didn’t even notice the pieces of internal organs mixed with the blood he vomited.

[P59]
All he felt was his vision gradually darkening and the sounds around him receding into the distance.

[P60]
He was dying, and desperation had driven him half-mad.

[P61]
*I want to live.*

[P62]
Pung Yang had spent his entire life as a ruthless marauder.

[P63]
He had stolen the wealth—and sometimes the lives—of countless people, but never in his wildest dreams had he imagined meeting an end like this.

[P64]
“Now… now, please give me the Temporary Strength Pill…”

[P65]
Through his blurred vision, he saw Jin Taekyung shake his head. Pung Yang mumbled piteously.

[P66]
“Why? Why not?”

[P67]
But the answer came from somewhere else.

[P68]
“What? Why?”

[P69]
“That bastard deserves to be torn limb from limb!”

[P70]
The surviving martial artists of the Mount Heng Sword Sect gripped their weapons, their eyes brimming with killing intent.

[P71]
Lee Seowol also bit her lip and aimed her bow at Pung Yang, but Jin Taekyung hurriedly stopped her.

[P72]
“Let’s hold off on the finishing blow… No, he’s too vicious to let him die comfortably. Better to leave him there and let him die slowly.”

[P73]
Lee Seowol wrestled with the decision for a moment before finally lowering her bow. Jin Taekyung approached Pung Yang and whispered into his ear.

[P74]
“I’m starting to get tired too. Let’s just die now.”

[P75]
Pung Yang didn’t understand what he meant, but one thing was certain.

[P76]
Death.

[P77]
Pung Yang realized that his own death was almost upon him.

[P78]
“Even if I become a vengeful ghost, I’ll have my revenge.”

[P79]
“Amen. In your next life, be satisfied with Viagra.”

[P80]
Pung Yang gave a hollow laugh. It was absurd that he had to listen to that bastard’s incomprehensible nonsense until the very end.

[P81]
*Damn it. What terrible weather.*

[P82]
He raised his head and looked at the sky. It was entirely red.

[P83]
Then darkness swallowed it.

[P84]
* * *

[P85]
As Pung Yang’s head lolled to the side, celebratory fireworks burst overhead.

[P86]
*Ding. Ding. Ding!*

[P87]
> **System**
> - Defeated **Lv. 85 Pung Yang**!
> - Successfully completed the **Temporary Strength Pill** Quest!
> - Obtained a massive amount of **EXP** and **Fame**!
> - Level Up!
> - Level Up!
> - …

[P88]
After announcing five level-ups and an increase in Fame, the System window delivered even better news.

[P89]
> **System**
> - The Quest success reward has been delivered to your **Inventory**!
> - **Full Recovery** has taken effect immediately as the Quest success reward!

[P90]
*Full Recovery?*

[P91]
It said the effect would be immediate, and the change happened exactly as promised.

[P92]
Cracked and broken bones knitted together. Cuts and puncture wounds healed without a trace. And the changes didn’t stop at the surface.

[P93]
*My Internal Injuries…*

[P94]
Invisible healing took place inside my body as well. I had expected all my Internal Injuries to heal, but there was an even greater benefit than I had imagined.

[P95]
> **System**
> - All **Internal Injuries** have healed!
> - Your stabilized body accepts new qi!
> - The **Blazing Flame Divine Pill** has been fully absorbed!
> - Your **internal energy** has risen to 45 years!
> - Your **internal energy** has gained the **Scorching Yang Qi** attribute!

[P96]
The Blazing Flame Divine Pill had been completely absorbed.

[P97]
And my internal energy had risen dramatically.

[P98]
I could feel power filling every limb and bone. The Scorching Yang Qi that had burned through my body like lava had somehow become a warm spring breeze.

[P99]
*I did it.*

[P100]
I had planned to circulate my qi and control the Scorching Yang Qi once my body recovered somewhat from the level-ups, but thanks to the System, I had handled the difficult part with ease.

[P101]
*Forty-five years? Just how much is that?*

[P102]
It was three times what I’d originally possessed—an increase of half a jiazi, a full thirty years of internal energy.

[P103]
*Half a jiazi.*

[P104]
Under normal circumstances, I would have put off taking the Blazing Flame Divine Pill. But the gamble had turned out to be a masterstroke.

[P105]
*I would have died if luck hadn’t been on my side, though.*

[P106]
Two strokes of heavenly luck.

[P107]
One was the Blazing Flame Divine Pill. The other was the **Unnamed Sword** in my hand.

[P108]
Both were loot I had obtained after defeating Jopil several months ago.

[P109]
*Without this, I really would’ve been screwed.*

[P110]
I’d thought it was merely a little sharper and harder than other swords. Never in my wildest dreams had I imagined it was actually Ten-Thousand-Year Cold Iron—or that it had such an ability.

[P111]
In that sense, *seven parts luck and three parts skill* didn’t suit me today. *Nine parts luck and one part qi* was much more appropriate.[^1]

[P112]
*Though I’m not sure this really counts as good luck.*

[P113]
I slowly looked around.

[P114]
A graveyard of weapons stood with their hilts buried in the ground. Some people had died with their faces planted in pools of blood. Others stared wide-eyed at the sky as dawn began to break.

[P115]
There were hundreds of corpses like that.

[P116]
“There’s a survivor here!”

[P117]
“Chunsam! Wake up!”

[P118]
Amid that horrific scene, the martial artists of the Mount Heng Sword Sect moved tirelessly. As I watched them rescue the few survivors with disciplined efficiency, I was suddenly seized by an inexplicable sense of wrongness.

[P119]
*What is it?*

[P120]
It felt like I’d forgotten something important…

[P121]
Just as I was frowning, one of the corpses that had been lying motionless sat up.

[P122]
“Guuuuuh.”

[P123]
“Oh.”

[P124]
Right. Good to see you, Mukyung.

[P125]
* * *

[P126]
By the time the two-shichen search was over, Lee Seowol was soaked in blood.

[P127]
“How many survivors?”

[P128]
“Twenty-five, including you, Sect Leader.”

[P129]
“How many did you say?”

[P130]
“Twenty-five. Five of them probably won’t make it through today.”

[P131]
Both Lee Seowol, who had asked the question, and the martial artist who answered it fell silent.

[P132]
The Mount Heng Sword Sect, which had once divided Shanxi Province with the Jin Family of Taiyuan, no longer existed. All that remained were the wounded and a young Sect Leader who wasn’t even twenty years old.

[P133]
*If I had abandoned this place and fled, if I had accepted Pung Yang’s marriage proposal from the beginning, could I have saved them?*

[P134]
Regret was always futile.

[P135]
But Lee Seowol had to regret.

[P136]
Although few remained, she was still the Sect Leader of a sect. Only by agonizing over her mistakes and regretting them to the bone could she avoid making the same mistakes again.

[P137]
That was her atonement to those who had died today and her effort on behalf of those who remained.

[P138]
*The Mount Heng Sword Sect will survive. If only for those who gave their lives for our sect.*

[P139]
Lee Seowol clenched her fist. Her fingernails, broken from drawing the bowstring, dug into her flesh. Blood seeped out, but she felt no pain.

[P140]
“What about the others?”

[P141]
“They’re all in the main hall. A woman from the Jin Family of Taiyuan knows a fair amount about medicine and is treating the wounded, but…”

[P142]
The martial artist’s expression darkened. It was proof of just how bad the condition of some of the wounded was.

[P143]
Lee Seowol asked no more questions and headed toward the main hall.

[P144]
*We haven’t even had time to collect ourselves, and already I’m sending them off again.*

[P145]
Unbearable fatigue pressed down on her entire body, but she held on through sheer willpower.

[P146]
At the very least, she had to be there for their final moments.

[P147]
*Creeeeak.*

[P148]
When Lee Seowol entered the main hall, the people from the Jin Family of Taiyuan were nowhere in sight. The wounded lying on the floor immediately caught her eye.

[P149]
The Tiger of Mount Heng, Cheol Mubaek, and more than a dozen martial artists noticed her and called out.

[P150]
“Ah, Seowol. You’ve come?”

[P151]
“You’re here, Sect Leader!”

[P152]
“We greet you, Sect Leader!”

[P153]
“…?”

[P154]
Was it just her imagination?

[P155]
For people on the verge of death, they seemed strangely full of energy. After staring at them in silence for a while, Lee Seowol realized what that energy meant.

[P156]
“A final rally…”

[P157]
Only then did she see the dark shadow of death hanging over their faces.

[P158]
Just as she hurriedly turned away to hold back her tears—

[P159]
*Bang!*

[P160]
Lee Seowol staggered after striking her forehead against something solid. As she began to fall, a large, firm hand caught her by the shoulder.

[P161]
“Oh, careful there. Are you all right?”

[P162]
“Ah, yes.”

[P163]
“Then we’re good.”

[P164]
Jin Taekyung looked down at Lee Seowol and let out a short laugh.

[P165]
* * *

[P166]
*Some final rally.*

[P167]
I barely held back a snort.

[P168]
Cheol Mubaek and the other wounded were all recovering vigorously.

[P169]
Of course, Jin Mukyung was no exception.

[P170]
*What would they have done without me?*

[P171]
More precisely, if not for the Quest rewards, half of them might have needed funerals.

[P172]
The thirty **Superior Wound Medicines** and thirty **Ten-Year He Shouwu** I’d received as rewards were remarkably effective at treating external wounds and Internal Injuries.

[P173]
*I did consider saving them for an emergency…*

[P174]
But I wasn’t heartless enough to ignore people dying right in front of me.

[P175]
Of course, the sheer quantity had played a part too.

[P176]
“Aren’t you coming in?”

[P177]
“What?”

[P178]
“If you’re not going in, I’ll go in first.”

[P179]
I was about to walk past Lee Seowol, who was standing there in a daze, when I suddenly remembered what I’d forgotten.

[P180]
*Wait. Where did I put that?*

[P181]
“Ah, here it is.”

[P182]
I pretended to rummage through my robes and pulled a bamboo slip from my Inventory.

[P183]
“Here. It’s from my hyung… no, from the Lesser Family Head.”

[P184]
Lee Seowol accepted the bamboo slip with a bewildered expression.

[P185]
The instant she took it, a System notification rang out.

[P186]
*Ding.*

[P187]
> **System**
> - Invitation delivery complete.
> - Quest **Yesterday’s Enemy, Today’s Ally** completed!

[P188]
Invitation delivery.

[P189]
If I had to do that twice, someone was going to die.

[P190]
[^1]: A playful variation on the Korean saying *seven parts luck, three parts skill*, replacing skill with *qi* and shifting the balance even further toward luck.
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
# Chapter 120

[P2]
*Shwick!*

[P3]
A sword thrust forward—slowly, but with tremendous force.

[P4]
For the briefest moment, a mocking smile appeared at the corner of Pung Yang’s mouth.

[P5]
*I knew this was coming.*

[P6]
He had spent decades living on a plateau where every kind of underhanded trick ran rampant. If he had been foolish enough to fall for the same trick twice, he would have become wild-dog food long ago.

[P7]
*But where did that sword come from?*

[P8]
It wasn’t a dagger. Where had the brat hidden a longsword that size?

[P9]
With that slight question in mind, Pung Yang drew up his Body-Protecting Qi.

[P10]
*Fssssss.*

[P11]
He had expected this, so his response was quick. Red qi surged upward in an instant and wrapped tightly around his body.

[P12]
Body-Protecting Qi was invincible armor that nothing short of powerful Sword Energy could put so much as a scratch on. The young brat’s futile struggle was nothing but laughable.

[P13]
*What an annoying bastard. Just die already.*

[P14]
He was about to snap Jin Taekyung’s neck in a single motion when—

[P15]
*Thud!*

[P16]
“……Huh?”

[P17]
A chilly coldness pierced into his body, followed by searing pain. Pung Yang stared wide-eyed at the sword that had pierced straight through his chest.

[P18]
*What the hell?*

[P19]
His Body-Protecting Qi had vanished.

[P20]
No—it had been destroyed.

[P21]
Jin Taekyung’s sword sliced through it as easily as cutting tofu, then pierced Pung Yang’s chest as well.

[P22]
Pung Yang looked down at the transparent blade, not a drop of blood staining it, and muttered like he was groaning.

[P23]
“Ten-Thousand-Year Cold Iron……?”

[P24]
He had heard of it before. Stories about a divine weapon said to be capable of cutting and breaking anything in the world.

[P25]
“How did you get this?”

[P26]
Pung Yang glared at the sword’s owner with a twisted expression. The young brat from the Jin Family of Taiyuan blinked innocently before opening his mouth.

[P27]
“Wow. This actually worked.”

[P28]
“You fucking bastard……!”

[P29]
He wanted to snap the brat’s neck right away, but his vision suddenly went hazy, and the strength drained from his fingers. The power that had filled his body vanished like the outgoing tide, leaving only helplessness in its wake.

[P30]
*The Temporary Strength Pill had to wear off now of all times.*

[P31]
Blood began flowing from the seven openings in Pung Yang’s face as he staggered backward.

[P32]
His various injuries, both great and small, combined with the dispersal of his Body-Protecting Qi. The internal energy surging backward through his body began driving him rapidly toward death.

[P33]
*I can’t die like this. I can’t.*

[P34]
Pung Yang hurriedly searched inside his robes.

[P35]
He still had one Temporary Strength Pill left. If he took it, he could beat the bastards to death in a single stroke and leave this place. He had lost quite a lot, but he could recover, then return to the Murim.

[P36]
Yes. If he just took the Temporary Strength Pill……

[P37]
*Clatter.*

[P38]
Damn it. He was too desperate.

[P39]
The wooden box slipped from Pung Yang’s frantic hand, struck the ground, and sprang open. A pill tinged with a blood-red color rolled across the ground before coming to a stop beneath someone’s foot.

[P40]
“Oh, is this the Temporary Strength Pill?”

[P41]
Jin Taekyung picked it up and examined it with curiosity. Pung Yang shouted at him.

[P42]
“G-Give it to me! Hurry!”

[P43]
“Here’s a question. Do you think I’ll give it to you just because you ask?”

[P44]
“You bastard!”

[P45]
Pung Yang threw himself forward with all his remaining strength, but his ruined body had already reached its limit. Before he could reach Jin Taekyung, his legs gave out and he collapsed.

[P46]
Only one path remained to Pung Yang now.

[P47]
“Please. I’m begging you. Give it to me. Give it to me!”

[P48]
“What if I do?”

[P49]
Pung Yang cried out desperately.

[P50]
“You’ll never see me again. No—instead, I’ll swear my loyalty to you from now on!”

[P51]
“Oh, having a Peak master as a subordinate. That sounds pretty good.”

[P52]
“R-Really? Then hurry and give me the Temporary Strength Pill!”

[P53]
“First, I’m taking my property back.”

[P54]
“Your property?”

[P55]
His question was answered a moment later. Jin Taekyung approached and yanked the sword from the center of Pung Yang’s chest.

[P56]
Blood poured out like a waterfall, accompanied by dizzying pain.

[P57]
“Gueeeeegh!”

[P58]
Pung Yang did not even notice that chunks of his internal organs were mixed into the blood he vomited.

[P59]
All he felt was his vision gradually darkening and the sounds around him receding into the distance.

[P60]
He was dying, and desperation had driven him half-mad.

[P61]
*I want to live.*

[P62]
Pung Yang had spent his entire life as a ruthless marauder.

[P63]
He had stolen the wealth—and sometimes the lives—of countless people, but he had never once imagined that he would meet an end like this.

[P64]
“Now, now, please give me the Temporary Strength Pill……”

[P65]
Through his blurred vision, he saw Jin Taekyung shake his head. Pung Yang mumbled piteously.

[P66]
“Why? Why not?”

[P67]
But the answer came from somewhere else.

[P68]
“What? Why?”

[P69]
“That bastard deserves to be torn limb from limb!”

[P70]
The surviving martial artists of the Mount Heng Sword Sect gripped their weapons, their eyes brimming with killing intent.

[P71]
Lee Seowol also bit down on her lip and drew her bow toward Pung Yang, but Jin Taekyung hurriedly stopped her.

[P72]
“Let’s lay off the finishing blow for now…… No, he’s too vicious to let him die comfortably. It’s better to leave him there and let him die slowly.”

[P73]
For a brief while, Lee Seowol struggled with herself. In the end, she lowered her bow. Jin Taekyung approached Pung Yang and whispered softly into his ear.

[P74]
“I’m starting to get tired too. Let’s just die now.”

[P75]
Pung Yang didn’t know what he meant, but one thing was certain.

[P76]
Death.

[P77]
Pung Yang realized that his own death was almost upon him.

[P78]
“Even as a vengeful ghost, I’ll have my revenge.”

[P79]
“Amen. In your next life, be satisfied with Viagra.”

[P80]
Pung Yang gave a hollow laugh. It was absurd that he had to listen to that bastard’s incomprehensible nonsense until the very end.

[P81]
*Damn. What terrible weather.*

[P82]
He raised his head and looked at the sky. It was dyed entirely red.

[P83]
Then it was swallowed by darkness.

[P84]
* * *

[P85]
As Pung Yang’s head lolled to the side, celebratory fireworks burst overhead.

[P86]
*Ding. Ding. Ding!*

[P87]
> **System**
> - Defeated **Lv. 85 Pung Yang**!
> - Successfully completed the **Temporary Strength Pill** Quest!
> - Obtained a massive amount of **EXP** and **Fame**!
> - Level Up!
> - Level Up!
> - …

[P88]
After announcing five level-ups and an increase in Fame, the System window delivered even better news.

[P89]
> **System**
> - The Quest success reward has been delivered to your **Inventory**!
> - **Full Recovery** has taken effect immediately as the Quest success reward!

[P90]
*Full Recovery?*

[P91]
It said the effect would be immediate, and the change happened exactly as promised.

[P92]
Cracked and broken bones knitted back together. Cuts and punctures healed as if they had been washed clean. The changes did not stop at the surface.

[P93]
*The Internal Injuries……*

[P94]
Invisible healing took place inside my body as well. I had expected all my Internal Injuries to heal, but there was an even greater benefit than I had imagined.

[P95]
> **System**
> - All **Internal Injuries** have healed!
> - Your stabilized body accepts new qi!
> - The **Blazing Flame Divine Pill** has been fully absorbed!
> - Your **internal energy** has risen to 45 years!
> - Your **internal energy** has gained the **Scorching Yang Qi** attribute!

[P96]
The Blazing Flame Divine Pill had been completely absorbed.

[P97]
And my internal energy had risen explosively.

[P98]
I could feel power filling every limb and bone. The Scorching Yang Qi that had burned through my body like lava had somehow become a warm spring breeze.

[P99]
*I did it.*

[P100]
I had planned to circulate my qi and control the Scorching Yang Qi once my body recovered somewhat from the level-ups, but thanks to the System, I had handled the difficult part with ease.

[P101]
*Forty-five years? How much is that?*

[P102]
Compared to what I had originally possessed, it was three times as much—an additional half a jiazi, or thirty years, of internal energy.

[P103]
*A half jiazi.*

[P104]
Under normal circumstances, I would have put off taking the Blazing Flame Divine Pill. But the gamble I had taken had come back as a masterstroke.

[P105]
*I would have died if luck hadn’t been on my side, though.*

[P106]
Two strokes of heavenly luck.

[P107]
One was the Blazing Flame Divine Pill, and the other was the **Unnamed Sword** in my hand.

[P108]
Both were loot I had obtained after defeating Jopil several months ago.

[P109]
*I would have been in serious trouble without this.*

[P110]
I had thought it was merely a sword that was a little sharper and harder than other swords. I had never dreamed that it was actually Ten-Thousand-Year Cold Iron, or that it possessed such an ability.

[P111]
In that sense, the saying *seven parts luck and three parts skill* didn’t suit me today. *Nine parts luck and one part qi* was much more appropriate.[^1]

[P112]
*Though I’m not sure this can really be called good luck.*

[P113]
I slowly looked around.

[P114]
A graveyard of weapons stood with their hilts buried upside down. Some people had died with their faces planted in pools of blood. Others stared wide-eyed at the sky as dawn began to break.

[P115]
There were hundreds of corpses like that.

[P116]
“There’s a survivor here!”

[P117]
“Chunsam! Come around!”

[P118]
Amid that horrific scene, the martial artists of the Mount Heng Sword Sect moved tirelessly. As I watched them rescue the few survivors with disciplined efficiency, I was suddenly seized by an inexplicable sense of wrongness.

[P119]
*What is it?*

[P120]
It felt like I had forgotten something important……

[P121]
Just as I was frowning, one of the corpses that had been lying motionless raised its upper body.

[P122]
“Guuuuuh.”

[P123]
“Oh.”

[P124]
Right. Good to see you, Mukyung.

[P125]
* * *

[P126]
By the time the four-hour search was over, Lee Seowol’s body was soaked in blood.

[P127]
“How many survivors?”

[P128]
“Twenty-five, including you, Sect Leader.”

[P129]
“How many did you say?”

[P130]
“Twenty-five. Five of them probably won’t make it through today.”

[P131]
Both Lee Seowol, who had asked the question, and the martial artist who answered it fell silent.

[P132]
The Mount Heng Sword Sect, which had once divided control of Shanxi with the Jin Family of Taiyuan, no longer existed. All that remained were the injured and a young Sect Leader who was not even twenty years old.

[P133]
*If I had abandoned this place and fled, if I had accepted Pung Yang’s marriage proposal from the beginning, could I have saved them?*

[P134]
Regret was always pointless.

[P135]
But Lee Seowol had to regret.

[P136]
Although few remained, she was still the Sect Leader of a sect. Only by agonizing over her mistakes and regretting them to the bone could she avoid making the same mistakes again.

[P137]
That was her atonement to those who had died today and her effort on behalf of those who remained.

[P138]
*The Mount Heng Sword Sect will survive. If only for those who gave their lives for our sect.*

[P139]
Lee Seowol clenched her fist. Her fingernails, broken from drawing the bowstring, dug into her flesh as she clenched her fist. Blood seeped out, but she felt no pain.

[P140]
“What about the others?”

[P141]
“They’re all in the main hall. There’s a woman from the Jin Family of Taiyuan who knows a fair amount about medicine, and she’s treating the wounded, but……”

[P142]
The martial artist’s expression darkened. It was proof of just how bad the condition of some of the wounded was.

[P143]
Lee Seowol did not ask anything else and headed toward the main hall.

[P144]
*I’m sending them off again before we’ve even had time to recover.*

[P145]
Unbearable fatigue pressed down on her entire body, but she held on through sheer willpower.

[P146]
At the very least, she had to see off those who were leaving.

[P147]
*Creeeeak.*

[P148]
When Lee Seowol entered the main hall, the people from the Jin Family of Taiyuan were nowhere in sight. The wounded lying on the floor immediately caught her eye.

[P149]
The Tiger of Mount Heng, Cheol Mubaek, and more than a dozen martial artists noticed her and called out.

[P150]
“Ah, Seowol. You’ve come?”

[P151]
“You’re here, Sect Leader!”

[P152]
“We greet you, Sect Leader!”

[P153]
“……?”

[P154]
Was it just her imagination?

[P155]
For people who were supposedly dying, they seemed strangely full of energy. After silently staring at them for a while, Lee Seowol realized what that energy meant.

[P156]
“A final rally……”

[P157]
Only then did she see the dark shadow of death lying heavily across their faces.

[P158]
Just as she hurriedly turned away to hold back her tears—

[P159]
*Bang!*

[P160]
Lee Seowol staggered after striking her forehead against something solid. As she began to fall, a large, firm hand caught her shoulder.

[P161]
“Oh, careful there. Are you all right?”

[P162]
“Ah, yes.”

[P163]
“Then we’re good.”

[P164]
Jin Taekyung looked down at Lee Seowol and let out a short laugh.

[P165]
* * *

[P166]
*Some final rally.*

[P167]
I barely held back a snort.

[P168]
Cheol Mubaek and the other wounded were all recovering vigorously.

[P169]
Of course, Jin Mukyung was no exception.

[P170]
*What would they have done without me?*

[P171]
To be precise, if not for the Quest rewards, there might have been funerals for half of them.

[P172]
The thirty **Superior Wound Medicines** and thirty **Ten-Year He Shouwu** I had received as rewards each had remarkable effects on external and Internal Injury healing.

[P173]
*I did consider saving them in case of an emergency……*

[P174]
But I wasn’t heartless enough to ignore people dying right in front of me.

[P175]
Of course, the sheer quantity had played a part too.

[P176]
“Aren’t you coming in?”

[P177]
“What?”

[P178]
“If you’re not going in, I’ll go in first.”

[P179]
I was about to walk past Lee Seowol, who was standing there in a daze, when I suddenly remembered something I had forgotten.

[P180]
*Wait. Where did I put that?*

[P181]
“Ah, here it is.”

[P182]
I pretended to rummage around inside my robes and pulled a bamboo slip from my Inventory.

[P183]
“Here. It’s from my hyung…… no, from the Lesser Family Head.”

[P184]
Lee Seowol accepted the bamboo slip with a bewildered expression.

[P185]
The System notification rang the instant she took it.

[P186]
*Ding.*

[P187]
> **System**
> - Invitation delivery complete.
> - Quest **Yesterday’s Enemy, Today’s Ally** completed!

[P188]
Invitation delivery.

[P189]
If I had to do that twice, someone was going to die.

[P190]
[^1]: A playful variation on the Korean saying *seven parts luck, three parts skill*, replacing skill with *qi* and shifting the balance even further toward luck.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본문      | **our sect / this sect**                                        |
| 귀가      | **your family**                                                 |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 하수오 | **He Shou Wu** | Traditional medicinal herb; a thirty-year-old specimen is offered to Jang Taebo. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 120,
  "passed": true,
  "metrics": {
    "source_characters": 6009,
    "translation_characters": 13844,
    "length_ratio": 2.304,
    "source_paragraphs": 184,
    "translation_paragraphs": 190
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "운기조식",
        "preferred": "circulate one's qi"
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
        "korean": "귀가",
        "preferred": "your family"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "인도",
        "preferred": "Human Butcher"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진태",
        "preferred": "Jintae"
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
        "korean": "검신",
        "preferred": "Sword God"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "하수오",
        "preferred": "He Shou Wu"
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
