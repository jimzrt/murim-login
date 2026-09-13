# Fidelity Gate — Chapter 14

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
  1|＃14화
  2|
  3|
  4|
  5|“따라 나와라, 네놈이 저지른 짓의 대가를 치르게 해 주마!”
  6|
  7|이소군이 분노에 가득 찬 고함을 내지른 그 순간이었다.
  8|
  9|띠링.
 10|
 11|
 12|
 13|퀘스트
 14|
 15|
 16|
 17|[비무]
 18|
 19|당신의 방탕함이 드디어 일을 냈습니다!
 20|
 21|자신의 일은 스스로 해결해야 하는 법. 쥐꼬리만큼 남은 명예와 항산검문의 분노를 피하기 위해서 남은 방법은 하나뿐입니다.
 22|
 23|
 24|
 25|종류 : 돌발 퀘스트
 26|
 27|등급 : 일류
 28|
 29|제한 : 진태경
 30|
 31|임무 : 비무에서 승리 (미완료)
 32|
 33|보상 : 칭호, [승부사]
 34|
 35| 대량의 경험치
 36|
 37| 명성 50
 38|
 39|실패 : 칭호, [색마]
 40|
 41| 부상
 42|
 43|
 44|
 45|[비무] 퀘스트를 수락하시겠습니까?
 46|
 47|수락    /    거절
 48|
 49|
 50|
 51|“…….”
 52|
 53|아니, 고등학교 이후로 연애도 해 본 적 없는 내가 색마 소리까지 들어야 하나?
 54|
 55|하루 절반을 레이드 뛰고 고시원에서 쓰러져 자는 게 일상인데 이제는 게임에서 내가 싸지도 않은 똥을 치워야 한다.
 56|
 57|‘퀘스트나 좀 잘 주든가.’
 58|
 59|30레벨인 이소군을 무슨 수로 상대하란 말인가.
 60|
 61|‘이런 미친, 레벨 차이가 두 배가 넘어가는데…….’
 62|
 63|이건 절대 하면 안 되는 싸움이다.
 64|
 65|나는 퀘스트를 거절했다. 아니, 거절하려고 했다. 하지만 이소군이 한발 빨랐다.
 66|
 67|“만약 이 자리에서 도망친다면…… 태원진가는 합당한 대가를 치르게 될 것이다.”
 68|
 69|띠링.
 70|
 71|
 72|
 73|- 퀘스트 정보가 갱신되었습니다.
 74|
 75|- 퀘스트 거부 시, [항산검문]이 [태원진가]에 선전포고합니다. 또한 [진태경]을 문파 공적으로 지목합니다.
 76|
 77|
 78|
 79|……내 이럴 줄 알았다. 웬일로 선택권을 주나 했지.
 80|
 81|내가 한숨을 푹 내쉴 때, 회의장은 숯불 위 가마솥처럼 끓어오르는 중이었다.
 82|
 83|“무례하다!”
 84|
 85|“어린놈이 가문의 위세를 업고 못 하는 말이 없구나!”
 86|
 87|“아무리 삼공자가 개만도 못한 짓을 했어도 그렇지, 본가를 업신여기다니!”
 88|
 89|“…….”
 90|
 91|다 좋은데 마지막 누구냐.
 92|
 93|분위기가 험악해지자 소가주인 진위경이 나섰다.
 94|
 95|“모두 진정하시지요. 이 소협도 그만하게. 이번 한 번은 말실수로 생각하고 넘어가지.”
 96|
 97|가장 상석에 앉아 낮은 목소리로 경고하는데, 포스가 장난이 아니다. 뿌리 있는 명문가의 차기 가주답다고나 할까.
 98|
 99|이소군도 기세에 눌렸는지 확연히 줄어든 목소리로 대답했다.
100|
101|“알겠습니다. 하지만…….”
102|
103|“하지만?”
104|
105|“말실수가 아닙니다. 제가 개인의 자격으로 오늘 이 자리에 왔다고 생각하십니까?”
106|
107|그 말에 진위경은 물론이고 사람들의 안색이 굳어진다.
108|
109|맞다. 이소군은 항산검문이 정식으로 보낸 사자(使者)다.
110|
111|“아버님, 아니 문주께서 제게 모든 권한을 일임하셨습니다.”
112|
113|“……그래서 원하는 게 뭔가?”
114|
115|“이미 말씀드렸다시피 삼공자와의 비무를 원합니다.”
116|
117|아니. 그건 내가 싫은데.
118|
119|돌아가는 상황을 보아하니 항산검문 이 자식들, 작정하고 시비 털러 온 거다.
120|
121|이 일로 얻을 수 있는 건 최대한 얻고, 그게 실패하더라도 나 하나 정도는 작살내 버리겠다는 것 같은데…… 이렇게 노골적으로 저격당하니 등골이 서늘하다.
122|
123|“다른 길도 있겠지. 정말 원하는 걸 말해 보게.”
124|
125|“태원을 제외한 모든 군현(郡縣)에서 철수. 이 정도면 제 누이의 혼삿길을 막은 대가로 적절하지요.”
126|
127|말이 끝나기가 무섭게 회의장에 고함이 빗발쳤다.
128|
129|드문드문 들리는 말로는, 한마디로 속옷 빼고 다 벗겨 먹겠다는 소리였다. 소가주인 진위경의 선택은 보나 마나다.
130|
131|“불가.”
132|
133|“하면 비무를…….”
134|
135|“그 또한 거절하겠네.”
136|
137|막냇동생에게는 껌뻑 죽는 진위경이다. 척 봐도 위험한 비무에 나를 밀어 넣을 리 없었다.
138|
139|진위경의 대답에 이소군은 득의양양한 미소를 지어 보였다.
140|
141|“그럼 남은 길은 하나뿐이군요.”
142|
143|전쟁.
144|
145|그 단어를 떠올린 것은 나뿐만이 아니었다. 전쟁이 주는 무게감에 회의장은 침묵에 휩싸였다.
146|
147|그 침묵 사이에서, 나는 허공을 바라봤다.
148|
149|
150|
151|퀘스트를 수락하시겠습니까?
152|
153|수락    /    거절
154|
155|
156|
157|- 퀘스트 거절 시, [항산검문]이 [태원진가]에 선전포고합니다. 또한 [진태경]을 문파 공적으로 지목합니다.
158|
159|
160|
161|시스템 메시지 읽고, 땅 보고. 하늘 보고. 그리고 다시 읽고.
162|
163|‘씨바…….’
164|
165|어쩔 수 없다. 방법은 하나뿐이다.
166|
167|“하겠습니다.”
168|
169|이번만큼은 모든 이들의 반응이 일치했다. 부릅뜬 눈, 벌어진 입. 비무를 제안한 이소군, 거절한 진위경. 회의실 모두가 자신의 귀를 의심하고 있었다.
170|
171|“자, 잠깐만. 태경아?”
172|
173|황급히 만류하려는 진위경을 뒤로하고, 이소군에게 말했다.
174|
175|“나와. 한판 붙자.”
176|
177|이소군의 입꼬리가 잔인하게 올라갔다.
178|
179|
180|
181|* * *
182|
183|
184|
185|겨울바람이 차갑다. 구름 낀 하늘을 바라보며 심호흡했다.
186|
187|“후우.”
188|
189|이소군과 마주 선 이곳은 태원진가의 대연무장이다. 멀찍이 떨어진 오십여 명의 사람들은 자리에 앉아 우리를 바라보고 있었다.
190|
191|태원진가 사람들은 저 새끼가 뭘 잘못 먹었나, 하는 얼굴이고, 항산검문 똘마니들은 손에 팝콘만 없지 아주 놀러 온 모양새다.
192|
193|아. 전음을 보내는 사람도 있다.
194|
195|- 막내야. 심호흡해. 심호흡. 후. 하. 후. 하…….
196|
197|하고 있어. 이 양반아.
198|
199|근엄한 얼굴을 하고선 똥 마려운 강아지처럼 엉덩이를 들썩거린다. 위팽이 어깨를 누르고 있지 않았다면 당장이라도 난입했을 기세다.
200|
201|- 걱정 마라. 위험하다 싶으면 이 큰형님이. 막. 어? 저놈이 우리 막내한테 손만 댔다 하면 콱, 씨! 어? 알겠지? 흥분하지 말고 천천히, 안전하게. 할 수 있다. 진태경!
202|
203|……알겠으니까 진정 좀.
204|
205|아까 회의장에서는 포스가 철철 흘러넘치더니, 역시 기대를 저버리지 않는 진위경이다.
206|
207|‘그래도 없는 것보다는 백배 낫지.’
208|
209|최소한 반병신이 되기 전에는 구해 줄 사람이 있으니까.
210|
211|진위경에 위팽까지 하면 생명 보험이 두 개다. 좋아.
212|
213|그렇게 한결 가벼워진 마음으로 이소군을 바라봤을 때, 나는 곧바로 생각을 철회했다.
214|
215|‘좋긴 뭐가 좋아. 시발.’
216|
217|항산검문 놈들이 왜 그렇게 자신만만했는지 알겠다.
218|
219|난데없이 상의를 훌렁훌렁 벗어 던지는데, 연체동물처럼 꿈틀거리는 근육에 숨이 턱 막히고…….
220|
221|
222|
223|[Lv.30 이소군]
224|
225|
226|
227|피처럼 붉은 레벨창에 손발이 저려 온다.
228|
229|자그마치 16레벨 차이. 압도적이다. 그 사실을 알려 주듯이 시스템창이 울렸다.
230|
231|
232|
233|- 상태 이상 [위축]에 걸렸습니다!
234|
235|
236|
237|‘누가 구해 주기 전에 세 번은 죽겠다.’
238|
239|이런 내 반응을 눈치챘는지 이소군이 잔인한 미소를 지어 보였다.
240|
241|“이제 상황 파악이 되나? 숨이 턱 막히고 손발이 저려 오지?”
242|
243|이제는 관심법까지 쓰네. 하지만 싸움은 기세가 반이다.
244|
245|나는 짐짓 표정을 가다듬고 대답했다.
246|
247|“헛소리.”
248|
249|“목소리가 떨리는군. 당연히 겁먹었겠지. 좋아, 내가 하는 질문에 성실하게 답변한다면 살살 해 주마.”
250|
251|……솔직히 살짝 흔들릴 뻔했다.
252|
253|“헛소리는 집어치워.”
254|
255|“오, 주제에 무가의 자제라 이건가?”
256|
257|이소군이 가소롭다는 듯이 웃었다.
258|
259|“하나만 묻자. 무슨 자신감으로 비무를 받아들였나? 무공도 보잘것없고 겁쟁이로 소문난 네놈이. 그 이유가 듣고 싶다.”
260|
261|“이유?”
262|
263|아무리 생각해도 방법은 이것 하나뿐이었다. 전쟁이 일어나면 나는 항산검문의 문파 공적이 된다.
264|
265|사냥? 레벨 업? 꿈도 못 꾼다. 태원진가라는 울타리를 벗어난 순간 냄새를 맡은 암살자들이 득달같이 달려들 거다.
266|
267|‘목숨이라도 붙어 있으면 다음 기회가 있다.’
268|
269|내게는 마법이 있다. 레벨 업이라는 회복 마법이.
270|
271|마음이 조금 편안해졌다.
272|
273|“너 정도면 해 볼 만한 것 같아서.”
274|
275|“푸핫! 하룻강아지 같은 놈.”
276|
277|가벼운 도발인데 역시 먹히지 않는다. 본인의 실력에 자신이 있는지 여유가 제법이다.
278|
279|“이제 내가 질문할 차롄가?”
280|
281|“대답해 준다는 말은 없었는데…… 유언인 셈 치고 들어 주마.”
282|
283|“이번 일. 너희들이 조작한 거지?”
284|
285|예상치 못한 질문이었는지 이소군의 얼굴이 어색하게 굳어졌다.
286|
287|그 표정이 내게는 충분한 대답이었다.
288|
289|‘맞네.’
290|
291|혹시나 했는데, 역시다. 어쩐지 처음부터 끝까지 구린내가 진동을 하더라.
292|
293|“어이구, 이 치졸한 새끼들. 차라리 선전포고를 하지.”
294|
295|“……그 아가리를 찢어 주마.”
296|
297|이소군이 거대한 대검을 들어 보이며 음산하게 중얼거렸다.
298|
299|나도 미리 꺼내 둔 [예리한 창]을 곧추세웠다.
300|
301|‘그래, 해 보자.’
302|
303|나도 무공을 익혔다. 7년간 실전으로 다져진 감각도 있다.
304|
305|F급 헌터 겸 이류 무림인. 투잡으로 갈고닦은 실력을 무시하지 마라!
306|
307|“크아아아압!”
308|
309|이소군은 상상 이상으로 민첩했다. 순식간에 거리를 좁히고 수직으로 내리꽂히는 대검을 창대로 막아 냈다.
310|
311|카가가각.
312|
313|“큭.”
314|
315|그대로 양단되면 어쩌나 했는데, 예리한 창은 통짜 강철답게 튼튼했다. 그러나 대검에 실린 힘에 의해 두 발이 땅을 파고들기 시작했다.
316|
317|“죽어라, 이 벌레 같은 놈!”
318|
319|“흡!”
320|
321|가까이서 마주하니 더욱 숨 막히는 기세다. 몬스터의 피어(Fear)가 이럴까.
322|
323|“지금이라도 무릎을 꿇고 용서를 빌어라! 그럼 팔 하나 정도로 끝내 주지!”
324|
325|- 막내야!
326|
327|이소군의 어깨 너머로 벌떡 일어난 진위경이 보인다. 항산검문 놈들은 킬킬거리며 지켜보고, 태원진가 사람들은 차마 못 보겠다는 듯 고개를 돌리고 있다.
328|
329|‘버텨야 해.’
330|
331|적어도 진위경이 올 때까지만이라도!
332|
333|“크아압!”
334|
335|종횡무진. 사방에서 이소군의 대검이 연달아 작렬했다. 분명 철끼리 부딪치는데, 내 귀에는 대포 소리가 들린다.
336|
337|쾅! 쾅! 쾅! 막았다.
338|
339|“크아아!”
340|
341|“하압!”
342|
343|쾅! 쾅! 다시 막았다.
344|
345|“크아아아!”
346|
347|“하아아압!”
348|
349|쾅! 또 막았다.
350|
351|“크아아압…….”
352|
353|“하아앗…….”
354|
355|“……?”
356|
357|“……?”
358|
359|다음 순간, 이소군과 시선이 부딪쳤다.
360|
361|그 얼떨떨하고 당황해하는 눈빛을 보는 순간, 녀석이 나와 똑같은 생각을 하고 있음을 알 수 있었다.
362|
363|‘뭐여, 이게.’
364|
365|이소군은 강하다. 대형 몬스터를 연상시키는 괴력에, 근육에 맞지 않게 민첩하며, 무지막지한 대검을 성냥개비처럼 휘두른다.
366|
367|그뿐인가, 방귀 좀 뀐다는 항산검문의 자제다. 펼치는 무공도 제법 높은 수준일 것이다.
368|
369|그런데…….
370|
371|‘할 만한데?’
372|
373|나는 지금도 끊임없이 휘둘러지는 대검을 하나하나 막아 내고 있었다. 20회가 넘어가는 공격. 그리고 방어.
374|
375|보인다. 보여서 막을 수 있는 거다. 어느새 발목까지 파묻힌 다리를 슬며시 들어 보였다. 쑥 뽑힌다.
376|
377|‘이거 혹시…….’
378|
379|에이, 설마. 아니겠지.
380|
381|쐐액-!
382|
383|그 순간, 허리를 노리고 날아든 대검을 창간으로 흘렸다. 그리고 나도 모르게 순간적으로 텅 빈 이소군의 가슴을 걷어찼다.
384|
385|빠악!
386|
387|“컥!”
388|
389|……응?
390|
391|주르륵, 복부를 부여잡고 대여섯 발자국을 밀려난 이소군이 아무 일도 없었다는 듯 콧잔등을 슥 문질렀다.
392|
393|“제법이군. 쓰레기답지 않게 한 수 재간은 있어.”
394|
395|“…….”
396|
397|“후후. 양보도 여기까지다.”
398|
399|“……야.”
400|
401|“다음 일격에 네놈의 머리통을…… 왜?”
402|
403|나는 떨떠름한 얼굴로 손을 들어 녀석의 입을 가리켰다.
404|
405|“너, 피 나.”
406|
407|주륵. 한 박자 늦게 피 한 줄기가 이소군의 입가를 타고 흐른다. 저거 아무래도 혀 깨물었나 본데. 아프겠다.
408|
409|“앗! 잉! 엑! 훅!”
410|
411|뭔 개 같은 추임새를 넣으며 피를 닦아 내는 이소군에게, 내가 말했다.
412|
413|“닦지 마. 놔둬.”
414|
415|“……?”
416|
417|“이따 한 번에 닦는 게 편해.”
418|
419|왜냐하면 지금부터 나한테 존나 맞아야 하거든.
420|
421|
422|
423|- 상태 이상, [위축]이 해제됩니다!
```

## Assembled English

```markdown
[P1]
# Chapter 14

[P2]
“Come out with me, you bastard! I’ll make you pay for what you’ve done!”

[P3]
The instant Lee Seogeun shouted those words in fury—

[P4]
Ding.

[P5]
> **System**
>
> **Quest**
>
> **Duel**
>
> Your debauchery has finally caught up with you!
>
> A man must deal with his own mess. To protect the tiny scrap of honor you have left and avoid the wrath of the Mount Heng Sword Sect, only one option remains.
>
> **Type:** Sudden Quest  
> **Grade:** First Rate  
> **Restriction:** Jin Taekyung  
> **Mission:** Win the duel (Incomplete)
>
> **Reward:** Title: **Gambler**
>
> - A large amount of EXP
> - Fame 50
>
> **Failure:** Title: **Sex Fiend**
>
> - Injury
>
> Would you like to accept the **Duel** Quest?
>
> **Accept** / **Decline**

[P6]
“……”

[P7]
Seriously? I hadn’t even dated anyone since high school, and now I had to be called a sex fiend?

[P8]
I spent half my day running raids and collapsed asleep in my goshiwon every night. Now I had to clean up a mess I hadn’t even made in a game.

[P9]
*At least give me a decent Quest.*

[P10]
How was I supposed to fight Lee Seogeun when he was Level 30?

[P11]
*This is insane. He’s more than twice my Level…*

[P12]
This was a fight I absolutely couldn’t take.

[P13]
I declined the Quest. Or tried to. But Lee Seogeun beat me to it.

[P14]
“If you run away from this place… the Jin Family of Taiyuan will pay the appropriate price.”

[P15]
Ding.

[P16]
> **System**
>
> - Quest information has been updated.
>
> - If the Quest is declined, the **Mount Heng Sword Sect** will declare war on the **Jin Family of Taiyuan**. In addition, **Jin Taekyung** will be designated a public enemy of the sect.

[P17]
*…I knew it.*

[P18]
I had wondered why the System was giving me a choice for once.

[P19]
As I let out a deep sigh, the assembly hall was boiling like a cauldron over charcoal.

[P20]
“How dare you!”

[P21]
“That young punk thinks he can say whatever he wants because he has his family’s backing!”

[P22]
“Even if the Third Young Master did something lower than a dog, how dare he look down on our family!”

[P23]
“……”

[P24]
The first two were fine, but who the hell was that last guy?

[P25]
As the atmosphere turned hostile, Jin Wikyung, the Lesser Family Head, stepped in.

[P26]
“Everyone, calm yourselves. And you, Young Hero, that is enough. Let us consider this a slip of the tongue and overlook it this once.”

[P27]
Seated in the place of honor, he issued the warning in a low voice. His presence was no joke. He really did have the bearing of the next Family Head of a prestigious house with deep roots.

[P28]
Perhaps cowed by his aura, Lee Seogeun answered in a noticeably quieter voice.

[P29]
“Understood. However…”

[P30]
“However?”

[P31]
“It was not a slip of the tongue. Do you think I came here in a personal capacity?”

[P32]
At those words, Jin Wikyung’s expression hardened, along with everyone else’s.

[P33]
Right. Lee Seogeun was an envoy officially sent by the Mount Heng Sword Sect.

[P34]
“My father—no, the Sect Leader—has entrusted me with full authority.”

[P35]
“……Then what is it you want?”

[P36]
“As I already said, I want a duel with the Third Young Master.”

[P37]
*No. I don’t want that.*

[P38]
Judging by how things were unfolding, those bastards from the Mount Heng Sword Sect had come here looking for a fight.

[P39]
They intended to get as much as possible out of this incident, and even if that failed, they were going to wreck me, at least. Being targeted so blatantly sent a chill down my spine.

[P40]
“There must be another way. Tell me what you truly want.”

[P41]
“Withdraw from every commandery and county except Taiyuan. That should be an appropriate price for ruining my sister’s marriage prospects.”

[P42]
The instant he finished speaking, shouts erupted throughout the assembly hall.

[P43]
From the bits and pieces I could make out, he was basically saying they intended to strip us of everything but our underwear. Jin Wikyung’s answer was obvious.

[P44]
“Impossible.”

[P45]
“Then accept the duel—”

[P46]
“That too, I must refuse.”

[P47]
Jin Wikyung was a complete pushover when it came to his youngest brother. There was no way he would push me into a duel that was obviously dangerous.

[P48]
At Jin Wikyung’s answer, Lee Seogeun smiled triumphantly.

[P49]
“Then there is only one path left.”

[P50]
War.

[P51]
I wasn’t the only one who thought of that word. The assembly hall fell silent beneath its weight.

[P52]
Amid that silence, I looked up at the empty air.

[P53]
> **System**
>
> Would you like to accept the Quest?
>
> **Accept** / **Decline**
>
> - If the Quest is declined, the **Mount Heng Sword Sect** will declare war on the **Jin Family of Taiyuan**. In addition, **Jin Taekyung** will be designated a public enemy of the sect.

[P54]
I read the System message, looked at the floor, looked at the ceiling, and then read it again.

[P55]
*Fuck…*

[P56]
There was no choice. Only one way remained.

[P57]
“I’ll do it.”

[P58]
For once, everyone reacted the same way. Wide eyes. Open mouths. Lee Seogeun, who had proposed the duel. Jin Wikyung, who had refused it. Every person in the assembly hall looked as though they couldn’t believe their ears.

[P59]
“W-wait. Taekyung?”

[P60]
Ignoring Jin Wikyung’s frantic attempt to stop me, I spoke to Lee Seogeun.

[P61]
“Come out. Let’s fight.”

[P62]
The corners of Lee Seogeun’s mouth curled into a cruel smile.

[P63]
* * *

[P64]
The winter wind was cold. I took a deep breath as I looked up at the cloudy sky.

[P65]
“Whoo.”

[P66]
I stood facing Lee Seogeun on the Jin Family of Taiyuan’s main training ground. About fifty people sat some distance away, watching us.

[P67]
The Jin Family people looked like they were wondering what the hell had gotten into me, while the Mount Heng Sword Sect’s goons looked like they’d come out for a day of entertainment. All they were missing was popcorn.

[P68]
Ah. Someone was sending me a Sound Transmission, too.

[P69]
- Little brother. Deep breaths. Deep breaths. In. Out. In. Out…

[P70]
*I’m doing it, man.*

[P71]
Jin Wikyung had a solemn expression, but he kept shifting his hips like a puppy that needed to poop. If Wipeng hadn’t been holding him down by the shoulder, he looked ready to charge into the training ground at any moment.

[P72]
- Don’t worry. If it looks dangerous, this eldest brother of yours will… You know? If that bastard so much as lays a hand on our youngest, I’ll—fuck! Got it? Don’t get worked up. Take it slow and stay safe. You can do it, Jin Taekyung!

[P73]
*……I get it, so calm down.*

[P74]
He had radiated such overwhelming force in the assembly hall, yet Jin Wikyung was once again living up to my expectations.

[P75]
*Still, he’s a hundred times better than having no one.*

[P76]
At least someone would save me before I ended up half crippled.

[P77]
With Jin Wikyung and Wipeng, I had two life insurance policies. Excellent.

[P78]
But the moment I looked at Lee Seogeun with a much lighter heart, I took that thought back.

[P79]
*What’s so excellent about this? Fuck.*

[P80]
Now I understood why the Mount Heng Sword Sect’s people had been so confident.

[P81]
Lee Seogeun suddenly stripped off his upper garments, and my breath caught at the muscles writhing like some kind of mollusk.

[P82]
> **System**
>
> **Lv. 30 Lee Seogeun**

[P83]
My hands and feet began to tingle at the sight of the blood-red Level window.

[P84]
A gap of sixteen Levels. It was overwhelming. As if to drive that fact home, the System chimed.

[P85]
Ding.

[P86]
> **System**
>
> - You have been afflicted with the Status Effect **Intimidation**!

[P87]
*I’ll die three times before anyone gets here to save me.*

[P88]
Perhaps he noticed my reaction, because Lee Seogeun gave me a cruel smile.

[P89]
“Do you understand the situation now? Your breath is caught, and your hands and feet are tingling, aren’t they?”

[P90]
He could read minds now, too?

[P91]
But momentum was half the battle.

[P92]
I deliberately composed my expression before answering.

[P93]
“Bullshit.”

[P94]
“Your voice is trembling. Of course you’re afraid. Fine. If you answer my questions honestly, I’ll go easy on you.”

[P95]
……To be honest, I almost wavered.

[P96]
“Cut the bullshit.”

[P97]
“Oh? Putting on airs because you’re the son of a martial family, are you?”

[P98]
Lee Seogeun laughed as if I were ridiculous.

[P99]
“Let me ask you one thing. What gave you the confidence to accept this duel? Your martial arts are pathetic, and you’re known as a coward. I want to hear your reason.”

[P100]
“My reason?”

[P101]
No matter how much I thought about it, this was the only way.

[P102]
If war broke out, I would become a public enemy of the Mount Heng Sword Sect.

[P103]
Hunting? Leveling up? I could forget about it. The moment I stepped outside the fence of the Jin Family of Taiyuan, assassins who caught my scent would come running.

[P104]
*As long as I stay alive, there’ll be another chance.*

[P105]
I had magic. The recovery magic called leveling up.

[P106]
My mind eased slightly.

[P107]
“I thought someone like you might be manageable.”

[P108]
“Pfft! You’re just a wet-behind-the-ears pup.”

[P109]
It was a mild provocation, but it didn’t work. He was confident in his abilities, and it showed in his relaxed manner.

[P110]
“Is it my turn to ask a question now?”

[P111]
“I never said I’d answer them… but I’ll indulge you as if they were your last words.”

[P112]
“This incident. You fabricated it, didn’t you?”

[P113]
Perhaps the question caught him off guard, because Lee Seogeun’s expression stiffened awkwardly.

[P114]
That expression was answer enough.

[P115]
*So I was right.*

[P116]
I had wondered if that was the case, but sure enough. No wonder the whole thing had smelled rotten from beginning to end.

[P117]
“You petty bastards. You should’ve just declared war.”

[P118]
“……I’ll tear that mouth apart.”

[P119]
Lee Seogeun lifted his massive greatsword and muttered ominously.

[P120]
I raised the Sharp Spear I had taken out beforehand.

[P121]
*All right. Let’s do this.*

[P122]
I had learned martial arts. I also had instincts honed through seven years of real combat.

[P123]
An F-rank Hunter and a Second Rate Murim martial artist. Don’t underestimate the skills I’d honed working two jobs!

[P124]
“Graaah!”

[P125]
Lee Seogeun was more agile than I’d imagined. He closed the distance in an instant, and I blocked the greatsword crashing straight down with the shaft of my spear.

[P126]
Kra-kra-kraang.

[P127]
“Urgh.”

[P128]
I’d worried the Sharp Spear might be cut clean in half, but it was sturdy, as befitted a solid piece of steel. Even so, the force behind the greatsword began driving both my feet into the ground.

[P129]
“Die, you insect!”

[P130]
“Hup!”

[P131]
Up close, his aura was even more suffocating. Was this what a monster’s Fear felt like?

[P132]
“Kneel and beg for forgiveness now! Then I’ll let you off with one arm!”

[P133]
- Little brother!

[P134]
Over Lee Seogeun’s shoulder, I saw Jin Wikyung spring to his feet. The Mount Heng Sword Sect’s people watched while snickering, and the Jin Family people turned their heads away as if they couldn’t bear to watch.

[P135]
*I have to hold out.*

[P136]
At least until Jin Wikyung gets here!

[P137]
“Graaah!”

[P138]
Lee Seogeun’s greatsword struck from every direction in a relentless barrage. The weapons were clearly clashing, iron against iron, but all I could hear was cannon fire.

[P139]
Boom! Boom! Boom! I blocked them.

[P140]
“Graaah!”

[P141]
“Hup!”

[P142]
Boom! Boom! I blocked them again.

[P143]
“Graaah!”

[P144]
“Haaah!”

[P145]
Boom! I blocked another.

[P146]
“Graaah…”

[P147]
“Haaah…”

[P148]
“……?”

[P149]
“……?”

[P150]
The next moment, Lee Seogeun and I locked eyes.

[P151]
The instant I saw the bewilderment and confusion in his gaze, I knew he was thinking exactly what I was.

[P152]
*What the hell is this?*

[P153]
Lee Seogeun was strong. He had the brute strength of a giant monster, moved with surprising agility for someone so muscular, and swung his massive greatsword like a matchstick.

[P154]
And that wasn’t all. He was a Young Master of the Mount Heng Sword Sect—a sect that could actually throw its weight around. The martial arts he used had to be quite advanced.

[P155]
And yet…

[P156]
*This is… doable?*

[P157]
Even now, I was blocking each and every strike of the continuously swinging greatsword. More than twenty attacks. And more than twenty blocks.

[P158]
I could see them. That was why I could block them.

[P159]
I slowly lifted one of my legs, which had been buried in the ground up to the ankle.

[P160]
It came right out.

[P161]
*Could it be…*

[P162]
No way. Surely not.

[P163]
Ssshwip!

[P164]
At that moment, I deflected the greatsword flying toward my waist along the shaft of my spear. Then, without thinking, I kicked Lee Seogeun in his unguarded chest.

[P165]
Whack!

[P166]
“Urgh!”

[P167]
……Huh?

[P168]
Clutching his stomach, Lee Seogeun skidded back five or six steps. Then he casually rubbed the bridge of his nose as if nothing had happened.

[P169]
“Not bad. You’ve got a trick or two despite being trash.”

[P170]
“……”

[P171]
“Heh. I won’t hold back anymore.”

[P172]
“……Hey.”

[P173]
“With my next strike, I’ll smash your head—what?”

[P174]
I raised a hand, looking awkward, and pointed at his mouth.

[P175]
“You’re bleeding.”

[P176]
A beat later, a thin line of blood ran down from the corner of Lee Seogeun’s mouth. He had probably bitten his tongue. That had to hurt.

[P177]
“Ah! Eeng! Eek! Hup!”

[P178]
Lee Seogeun wiped away the blood with a series of ridiculous yelps.

[P179]
“Don’t wipe it. Leave it.”

[P180]
“……?”

[P181]
“It’ll be easier to wipe it all off at once later.”

[P182]
Because from now on, I was going to beat the absolute shit out of him.

[P183]
> **System**
>
> - The Status Effect **Intimidation** has been removed!
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 14

[P2]
“Come out with me, you bastard! I’ll make you pay for what you’ve done!”

[P3]
The instant Lee Seogeun shouted those words, filled with fury—

[P4]
Ding.

[P5]
> **System**
>
> **Quest**
>
> **Duel**
>
> Your debauchery has finally caught up with you!
>
> A man must deal with his own mess. To protect the tiny scrap of honor you have left and to avoid the anger of the Mount Heng Sword Sect, only one option remains.
>
> **Type:** Sudden Quest  
> **Grade:** First Rate  
> **Restriction:** Jin Taekyung  
> **Mission:** Win the duel (Incomplete)
>
> **Reward:** Title: **Gambler**
>
> - A large amount of EXP
> - Fame 50
>
> **Failure:** Title: **Sex Fiend**
>
> - Injury
>
> Would you like to accept the **Duel** Quest?
>
> **Accept** / **Decline**

[P6]
“……”

[P7]
Seriously? I hadn’t even dated anyone since high school, and I had to be called a sex fiend?

[P8]
I spent half my day on raids and collapsed asleep in my goshiwon every night. Now I had to clean up a mess I hadn’t even made in a game.

[P9]
*At least give me a decent Quest.*

[P10]
How was I supposed to fight a Level 30 like Lee Seogeun?

[P11]
*This is insane. The Level gap is more than twice mine…*

[P12]
This was a fight I couldn’t possibly take.

[P13]
I declined the Quest. Or I was going to. But Lee Seogeun beat me to it.

[P14]
“If you run away from this place… the Jin Family of Taiyuan will pay the appropriate price.”

[P15]
Ding.

[P16]
> **System**
>
> - Quest information has been updated.
>
> - If the Quest is declined, the **Mount Heng Sword Sect** will declare war on the **Jin Family of Taiyuan**. In addition, **Jin Taekyung** will be designated a public enemy of the sect.

[P17]
*…I knew it.*

[P18]
I had wondered why the System was giving me a choice for once.

[P19]
As I let out a deep sigh, the assembly hall was boiling like a cauldron over charcoal.

[P20]
“How dare you!”

[P21]
“That young punk thinks he can say anything because he has his family’s backing!”

[P22]
“Even if the Third Young Master did something lower than a dog, how dare he look down on our family!”

[P23]
“……”

[P24]
The first two were fine, but who the hell was that last guy?

[P25]
As the atmosphere turned hostile, Jin Wikyung, the Lesser Family Head, stepped forward.

[P26]
“Everyone, calm yourselves. And you, Young Hero, enough. Let us consider this a verbal slip and let it go this once.”

[P27]
Seated in the place of honor, he issued the warning in a low voice. His presence was no joke. He really did have the bearing of the next Family Head of a prestigious house with deep roots.

[P28]
Perhaps cowed by that aura, Lee Seogeun answered in a noticeably quieter voice.

[P29]
“Understood. However…”

[P30]
“However?”

[P31]
“It was not a verbal slip. Do you think I came here as a private individual?”

[P32]
At those words, Jin Wikyung’s expression hardened, and so did everyone else’s.

[P33]
Right. Lee Seogeun was an envoy officially sent by the Mount Heng Sword Sect.

[P34]
“My father—no, the Sect Leader—has entrusted me with all authority.”

[P35]
“……Then what is it you want?”

[P36]
“As I already said, I want a duel with the Third Young Master.”

[P37]
*No. I don’t want that.*

[P38]
Judging by how things were unfolding, those bastards from the Mount Heng Sword Sect had come here looking for a fight.

[P39]
They intended to get as much as possible out of this incident, and even if that failed, they were going to wreck me, at least. Being targeted so blatantly sent a chill down my spine.

[P40]
“There must be another way. Tell me what you truly want.”

[P41]
“Withdraw from every commandery and county except Taiyuan. That should be an appropriate price for ruining my sister’s chances of marriage.”

[P42]
The instant he finished speaking, shouts erupted throughout the assembly hall.

[P43]
From the bits and pieces I could make out, he was basically saying they intended to strip us of everything but our underwear. Jin Wikyung’s answer was obvious.

[P44]
“Impossible.”

[P45]
“Then accept the duel—”

[P46]
“That too, I must refuse.”

[P47]
Jin Wikyung was a complete pushover when it came to his youngest brother. There was no way he would push me into a duel that was obviously dangerous.

[P48]
At Jin Wikyung’s answer, Lee Seogeun smiled triumphantly.

[P49]
“Then there is only one path left.”

[P50]
War.

[P51]
I wasn’t the only one who thought of that word. The assembly hall fell silent beneath the weight of it.

[P52]
Amid that silence, I looked up at the empty air.

[P53]
> **System**
>
> Would you like to accept the Quest?
>
> **Accept** / **Decline**
>
> - If the Quest is declined, the **Mount Heng Sword Sect** will declare war on the **Jin Family of Taiyuan**. In addition, **Jin Taekyung** will be designated a public enemy of the sect.

[P54]
I read the System message, looked at the floor, looked at the ceiling, and then read it again.

[P55]
*Fuck…*

[P56]
There was no choice. Only one way remained.

[P57]
“I’ll do it.”

[P58]
Everyone reacted the same way this time. Wide eyes. Open mouths. Lee Seogeun, who had proposed the duel. Jin Wikyung, who had refused it. Every person in the assembly hall looked as if they doubted their own ears.

[P59]
“W-wait. Taekyung?”

[P60]
I left Jin Wikyung’s frantic attempt to stop me behind me and spoke to Lee Seogeun.

[P61]
“Come out. Let’s have a go.”

[P62]
The corners of Lee Seogeun’s mouth rose cruelly.

[P63]
* * *

[P64]
The winter wind was cold. I took a deep breath while looking up at the cloudy sky.

[P65]
“Whoo.”

[P66]
I faced Lee Seogeun on the Jin Family of Taiyuan’s main training ground. About fifty people sat some distance away, watching us.

[P67]
The Jin Family people wore expressions that seemed to ask what the hell I had eaten, while the Mount Heng Sword Sect’s goons looked like they had come out for a day of entertainment. The only thing missing was popcorn.

[P68]
Ah. Someone was sending me Sound Transmission, too.

[P69]
- Little brother. Deep breaths. Deep breaths. In. Out. In. Out…

[P70]
*I’m doing it, man.*

[P71]
Jin Wikyung had a solemn expression, but he kept shifting his hips like a puppy that needed to poop. If Wipeng hadn’t been holding him down by the shoulder, he looked ready to charge into the training ground at any moment.

[P72]
- Don’t worry. If it looks dangerous, this eldest brother of yours will jump in. What? If that bastard so much as lays a hand on our youngest brother, I’ll—fuck! Got it? Don’t get worked up. Take it slow and stay safe. You can do it, Jin Taekyung!

[P73]
*……I get it, so calm down.*

[P74]
He had radiated such overwhelming force in the assembly hall, yet Jin Wikyung was once again living up to my expectations.

[P75]
*Still, he’s a hundred times better than having no one.*

[P76]
At least someone would save me before I became a half-crippled wreck.

[P77]
With Jin Wikyung and Wipeng, I had two life insurance policies. Excellent.

[P78]
But the moment I looked at Lee Seogeun with that slightly lighter feeling, I withdrew my thoughts.

[P79]
*What’s so excellent about this? Fuck.*

[P80]
Now I understood why the Mount Heng Sword Sect’s people had been so confident.

[P81]
Lee Seogeun suddenly stripped off his upper garments, and my breath caught at the muscles writhing like some kind of mollusk.

[P82]
> **System**
>
> **Lv. 30 Lee Seogeun**

[P83]
My hands and feet began to tingle at the sight of the blood-red Level window.

[P84]
The sixteen-Level gap was overwhelming. As if to drive that fact home, the System rang.

[P85]
Ding.

[P86]
> **System**
>
> - You have been afflicted with the Status Effect **Intimidation**!

[P87]
*I’ll die three times before anyone gets here to save me.*

[P88]
Perhaps he noticed my reaction, because Lee Seogeun gave me a cruel smile.

[P89]
“Do you understand the situation now? Your breath is caught, and your hands and feet are tingling, aren’t they?”

[P90]
He could read minds now, too?

[P91]
But momentum was half the fight.

[P92]
I deliberately composed my expression before answering.

[P93]
“Bullshit.”

[P94]
“Your voice is trembling. Of course you’re afraid. Fine. If you answer my questions honestly, I’ll go easy on you.”

[P95]
……To be honest, I almost wavered.

[P96]
“Cut the bullshit.”

[P97]
“Oh? Putting on the airs of a martial family’s son, are you?”

[P98]
Lee Seogeun laughed as if I were ridiculous.

[P99]
“Let me ask you one thing. What made you accept the duel? You, whose martial arts are pathetic and who is infamous for being a coward. I want to hear the reason.”

[P100]
“The reason?”

[P101]
No matter how much I thought about it, this was the only way.

[P102]
If war broke out, I would become a public enemy of the Mount Heng Sword Sect.

[P103]
Hunting? Leveling up? I could forget about it. The moment I left the fence of the Jin Family of Taiyuan, assassins who caught my scent would come running.

[P104]
*As long as I stay alive, there will be another chance.*

[P105]
I had magic. The recovery magic of leveling up.

[P106]
My mind eased slightly.

[P107]
“I thought someone like you might be manageable.”

[P108]
“Pfft! You’re just a wet-behind-the-ears pup.”

[P109]
It was a mild provocation, but it didn’t work. He was confident in his own abilities, and it showed in his relaxed manner.

[P110]
“Is it my turn to ask questions now?”

[P111]
“I never said I’d answer them… but I’ll indulge you as if they were your last words.”

[P112]
“This incident. You fabricated it, didn’t you?”

[P113]
Perhaps the question was unexpected, because Lee Seogeun’s expression stiffened awkwardly.

[P114]
That expression was answer enough.

[P115]
*There it is.*

[P116]
I had wondered if that was the case, but sure enough. No wonder the whole thing had smelled rotten from beginning to end.

[P117]
“You petty bastards. You should have just declared war.”

[P118]
“……I’ll tear that mouth apart.”

[P119]
Lee Seogeun lifted a massive greatsword and muttered ominously.

[P120]
I raised the Sharp Spear I had drawn earlier.

[P121]
*All right. Let’s do this.*

[P122]
I had learned martial arts. I also had instincts honed by seven years of real combat.

[P123]
An F-rank Hunter and a second-rate Murim martial artist. Don’t underestimate the skills I had honed working two jobs!

[P124]
“Graaah!”

[P125]
Lee Seogeun was more agile than I had imagined. He closed the distance in an instant, and I blocked the greatsword crashing down vertically with the shaft of my spear.

[P126]
Kra-kra-kraang.

[P127]
“Urgh.”

[P128]
I had wondered if I would be split in two, but the Sharp Spear was sturdy as a solid piece of steel. However, the force behind the greatsword began driving both my feet into the ground.

[P129]
“Die, you insect!”

[P130]
“Hup!”

[P131]
Up close, his aura was even more suffocating. Was this what a monster’s Fear felt like?

[P132]
“Kneel and beg for forgiveness now! Then I’ll let you off with one arm!”

[P133]
- Little brother!

[P134]
Over Lee Seogeun’s shoulder, I saw Jin Wikyung spring to his feet. The Mount Heng Sword Sect’s people watched while snickering, and the Jin Family people turned their heads away as if they couldn’t bear to watch.

[P135]
*I have to hold out.*

[P136]
At least until Jin Wikyung got here!

[P137]
“Graaah!”

[P138]
Lee Seogeun’s greatsword struck from every direction in a blurring barrage. The weapons were clearly clashing, iron against iron, but all I could hear was the sound of cannons.

[P139]
Boom! Boom! Boom! I blocked them.

[P140]
“Graaah!”

[P141]
“Hup!”

[P142]
Boom! Boom! I blocked them again.

[P143]
“Graaah!”

[P144]
“Haaah!”

[P145]
Boom! I blocked another.

[P146]
“Graaah…”

[P147]
“Haaah…”

[P148]
“……?”

[P149]
“……?”

[P150]
The next moment, Lee Seogeun and I met each other’s eyes.

[P151]
The moment I saw the bewilderment and confusion in his gaze, I knew he was thinking exactly what I was.

[P152]
*What the hell is this?*

[P153]
Lee Seogeun was strong. He possessed the brute strength of a giant monster, moved with surprising agility for someone with that much muscle, and swung his massive greatsword like a matchstick.

[P154]
And that wasn’t all. He was a Young Master of the Mount Heng Sword Sect—a sect that could actually throw its weight around. The martial arts he used had to be quite advanced.

[P155]
And yet…

[P156]
*This is… doable?*

[P157]
Even now, I was blocking each and every strike of the continuously swinging greatsword. More than twenty attacks. And more than twenty blocks.

[P158]
I could see them. That was why I could block them.

[P159]
I slowly lifted one of my legs, which had been buried in the ground up to the ankle. It came free with ease.

[P160]
*Could this be…*

[P161]
No way. Surely not.

[P162]
Ssshwip!

[P163]
At that moment, I redirected the greatsword flying toward my waist along the shaft of my spear. Then, without thinking, I kicked Lee Seogeun in his unguarded chest.

[P164]
Whack!

[P165]
“Urgh!”

[P166]
……Huh?

[P167]
Lee Seogeun slid back five or six steps while clutching his chest. Then he casually rubbed the bridge of his nose as if nothing had happened.

[P168]
“You’re not bad. You’ve got a trick or two, despite being trash.”

[P169]
“……”

[P170]
“Heh. I won’t hold back anymore.”

[P171]
“……Hey.”

[P172]
“With my next strike, I’ll smash your head—what?”

[P173]
With a queasy look, I raised a hand and pointed at his mouth.

[P174]
“You’re bleeding.”

[P175]
A beat later, a thin line of blood ran down from the corner of Lee Seogeun’s mouth. He had probably bitten his tongue. That had to hurt.

[P176]
“Ah! Eeng! Eek! Hup!”

[P177]
Lee Seogeun wiped away the blood while letting out some ridiculous yelps.

[P178]
“Don’t wipe it. Leave it.”

[P179]
“……?”

[P180]
“It’ll be easier to wipe it all off at once later.”

[P181]
Because from now on, I was going to beat the absolute shit out of him.

[P182]
> **System**
>
> - The Status Effect **Intimidation** has been removed!
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 14,
  "passed": true,
  "metrics": {
    "source_characters": 5523,
    "translation_characters": 12743,
    "length_ratio": 2.307,
    "source_paragraphs": 194,
    "translation_paragraphs": 183
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "철수",
        "preferred": "Cheol Soo"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "심법",
        "preferred": "cultivation technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "일격",
        "preferred": "One Strike"
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
