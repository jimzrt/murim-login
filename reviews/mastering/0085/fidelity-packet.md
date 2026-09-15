# Fidelity Gate — Chapter 85

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
  1|＃85화
  2|
  3|
  4|
  5|“형. 괜찮으세요?”
  6|
  7|“안 다치셨어요?”
  8|
  9|팀원들의 말에 임창수가 이를 악물었다.
 10|
 11|“입 닥쳐, 이 새끼들아. 그동안 내가 해 준 게 얼만데 구경만 하고 있어?”
 12|
 13|“아니, 저 그게…….”
 14|
 15|“그때 상황이 좀 그랬어요. 죄송해요.”
 16|
 17|“의리 없는 새끼들.”
 18|
 19|팀원들과 의리로 묶인 관계는 아니지만 그래도 줄 건 주고, 받을 건 받았다고 생각했다. 훈련소 낙제생들을 억지로 길드에 꽂아 넣고, 차도 사 주고 용돈도 준 게 누군가.
 20|
 21|그 대가로 충성을 받았는데…… 가장 중요한 순간에 외면당하니 뒤통수가 얼얼했다.
 22|
 23|‘시발, 뭐 이런 엿 같은 경우가.’
 24|
 25|수십 억? 분명 큰돈이긴 하지만 임창수로서는 감당 못 할 금액은 아니었다. 그의 명의로 잡힌 건물 한두 개만 팔아도 충분히 지급할 수 있다.
 26|
 27|그러나 자존심이 짓밟힌 건 도저히 용납할 수 없었다.
 28|
 29|‘쳐 죽일 놈.’
 30|
 31|임창수가 부릅뜬 눈으로 한 사람의 등을 노려봤다.
 32|
 33|검은 가죽 갑옷을 입고 있는 저놈, 진태경이 모든 일의 원흉이다.
 34|
 35|‘어디서 뭐 하다 온 놈인지는 모르겠지만…… 이 치욕은 반드시 갚아 주마.’
 36|
 37|놈의 정체가 뭔지는 아직 정확히 모르겠다. 확실한 건 결코 평범한 C급 헌터는 아니라는 거다.
 38|
 39|B급 몬스터 여덟 마리를 정면 승부로 박살 낼 수 있는 C급 헌터는 세상 어디에도 없으니까.
 40|
 41|‘정체는 왜 숨긴 거지? 혹시 도피 중인 범죄자? 아니면 부정 등록자? 일단 게이트에서 나가기만 하면 싹 다 털어 주마.’
 42|
 43|임창수가 은밀히 복수심을 불태우고 있던 그때였다.
 44|
 45|휙!
 46|
 47|돌연 그쪽으로 고개를 돌린 진태경이 눈을 가늘게 떴다. 먹이를 바라보는 포식자의 눈빛에 임창수의 가슴이 덜컥 내려앉았다.
 48|
 49|“야.”
 50|
 51|“예, 예?”
 52|
 53|“너 방금 내 욕 했지.”
 54|
 55|“아, 아, 아닌데요.”
 56|
 57|“아니긴. 말 더듬는 것만 봐도 사이즈 나오는데. 어쩐지 아까부터 뒤통수가 따끔따끔하더라.”
 58|
 59|임창수는 대격변 시대의 헌터이자 전쟁 영웅인 아버지의 말씀을 떠올렸다. 위험한 상황일수록 의연하게 대처해라.
 60|
 61|“진짜 아닙니다.”
 62|
 63|“내 관심법은 네가 거짓말을 하고 있다고 알려 주는데?”
 64|
 65|“관심법이라니, 그런 게 어디 있어요?”
 66|
 67|“마법도 있는데 관심법이 왜 없어. 구태의연한 사고방식을 버려.”
 68|
 69|“어쨌든 맹세코 아닙니다.”
 70|
 71|“아냐. 맹세코 맞아. 그리고 너도 한 대 맞아.”
 72|
 73|빡!
 74|
 75|눈물이 핑 돌았다. 스무 살 이후로는 아버지한테도 맞아 본 적이 없는 꿀밤이다. 그런데 기껏해야 또래로 보이는 놈한테, 그것도 팀원들과 여자들 앞에서 이런 굴욕을 당하다니.
 76|
 77|“제법 손맛이 있네. 딱 혁무진 때릴 때 느낌인데, 이거. 아무튼 조심해라. 응?”
 78|
 79|혁무진이 누군지는 모르겠지만 어쨌든 임창수는 고개를 푹 숙였다.
 80|
 81|“……예.”
 82|
 83|“근데 이놈의 미로는 끝도 없네. 야, 여기 보스 존 얼마나 남았어?”
 84|
 85|“저도 몰라요. 미로라서.”
 86|
 87|“몬스터도 더 이상 안 나오고. 심심해 죽겠다.”
 88|
 89|“…….”
 90|
 91|보이는 족족 때려잡으니까 안 나오지!
 92|
 93|임창수와 팀원들이 나설 필요도 없었다. 저 다섯 명만으로도 충분, 아니 진태경 한 명으로도 충분했다.
 94|
 95|‘괴물 같은 놈. 진짜 A급 헌터라도 되나?’
 96|
 97|진태경 혼자서만 서른 마리는 넘게 쓰러트린 것 같다. 좀 지쳤나 싶다가도 어느 순간을 기점으로는 또 펄펄 날아다녔다.
 98|
 99|‘레이드 속도가 더 빨라지고 있어.’
100|
101|보통은 레이드의 끝으로 갈수록 피로 축적으로 느려지는 게 정상이다.
102|
103|그런데도 같은 몬스터를 상대하는데 레이드 속도가 빨라진다는 건…….
104|
105|‘계속해서 강해진다?’
106|
107|임창수는 순간 떠오른 생각을 애써 부정했다.
108|
109|무슨 게임 캐릭터가 레벨 업 하는 것도 아니고 그게 말이 되나. 꿀밤을 맞더니 머리가 고장 난 기분이다.
110|
111|“후우.”
112|
113|깊은 한숨을 내쉬는 그에게 팀원들이 우물쭈물 다가왔다.
114|
115|“창수 형…….”
116|
117|“오빠, 괜찮아? 어떡해. 이마에 혹 났어.”
118|
119|“기분 안 좋으니까 다 꺼져. 너희는 나가기만 하면 싹 다 모가지야. 알아?”
120|
121|아무리 체면을 구겨도, 이빨이 뽑혀도 호랑이는 호랑이다.
122|
123|임창수의 으름장에 팀원들이 숨을 삼켰다.
124|
125|‘할부 안 끝났는데.’
126|
127|‘상동 길드 나가면 어디에서 받아 주나.’
128|
129|‘이번 달 카드값이…….’
130|
131|이제껏 풍족한 생활을 영위할 수 있었던 이유는 임창수의 원조 덕분이다. 그들 모두 헌터니만큼 굶어 죽을 일은 없겠지만 어디를 가도 지금 같은 대우는 기대하기 어렵다.
132|
133|“거기서 끝낼 줄 알아? 기대해. 어딜 가더라도 상동 길드 이름으로 전화 한 통씩 꼭 넣어 줄 테니까. 이 바닥 좁은 거 알지?”
134|
135|쫓아내는 것도 모자라 앞길까지 방해한다는 말에 팀원들의 얼굴이 급변했다.
136|
137|“창수 형, 그건 좀.”
138|
139|“형? 너 좋을 때만 형이냐?”
140|
141|“오빠, 꼭 그렇게까지 해야겠어?”
142|
143|“그러니까 이 자식들아. 사람 잘 보고 줄을 댔어야지.”
144|
145|당장 모두 뺨이라도 한 대씩 올려붙이고 싶었지만 꾹 참았다.
146|
147|큰 소리를 냈다가는 언제 또 진태경이 돌아볼지 모르기 때문이다.
148|
149|‘시발, 내가 어쩌다가…….’
150|
151|꿀밤이 무서워서 화도 마음대로 못 내는 꼴이라니. 임창수가 바닥에 침을 탁 뱉고 돌아선 그때였다.
152|
153|덥석.
154|
155|“창수 형. 아니 임 팀장님, 이러시면 어떡해요.”
156|
157|“한 번만 다시 생각해 줘, 오빠. 응?”
158|
159|“놔라. 두 번 말하기 싫다.”
160|
161|“이번엔 진짜. 진짜로 시키는 거 다 할게요. 예?”
162|
163|“……시키는 거 다 한다고?”
164|
165|동료의 손을 뿌리치려던 임창수가 문득 동작을 멈췄다.
166|
167|힐끗 고개를 돌리니 길드원들과 실랑이를 벌이는 사이 거리가 벌어져 저 멀리 앞서가는 진태경 일행이 보인다.
168|
169|멀리서도 눈에 띄는 송송이의 환상적인 뒤태도.
170|
171|‘잠깐. 방법이 있을 것 같기도 한데.’
172|
173|그의 눈에 비친 진태경은 괴물이지만 딱 한 가지 약점이 있어 보였다. 송송이라는 여자.
174|
175|‘아까 보니까 완전 뻑이 갔던데.’
176|
177|눈치채고 말고 할 것도 없다. 누구나 한 번 본 것만으로도 그가 송송이를 마음에 품고 있다는 사실을 알아차릴 수 있을 정도니까.
178|
179|‘분명 C급 힐러라고 했지.’
180|
181|힐러를 제압하는 것은 닭목 비트는 것보다 쉽다. 좋아하는 여자가 붙잡혀 있다면 진태경도 쉽게 손을 쓸 수 없을 것이다.
182|
183|‘그럼 끝이지.’
184|
185|진태경을 제외하면 나머지 셋은 큰 걱정거리가 아니다.
186|
187|길드장이라는 노인네는 B급이지만 마법사라 근접전은 쥐약일 테고, E급 탱커인 아저씨는 논할 가치도 없다.
188|
189|약간 마음에 걸리는 사람이 있다면 최민우. 그놈인데…….
190|
191|“방금 그 말, 믿어도 되냐?”
192|
193|“물론입니다.”
194|
195|“저희만 믿으세요.”
196|
197|“오빠, 사람을 왜 이렇게 못 믿어? 우리가 이 정도 사이밖에 안 돼?”
198|
199|그에겐 명령에 복종할 B급 헌터 넷과 C급 헌터 다섯으로 이루어진 레이드 팀이 있다. 모두 임창수가 주는 먹이만 먹도록 길들여진 녀석들이다.
200|
201|“좋아. 그럼 지금부터 내가 하는 말 똑똑히 들어…….”
202|
203|짤막한, 그리고 간단한 설명이 끝나자 팀원들은 긴장된 기색을 숨기지 못했다.
204|
205|“될까요?”
206|
207|“가능성 있어 보이기는 하는데.”
208|
209|“오빠, 설마 내가 생각하는 그거, 아니지? 사람 죽이는 거면 나는 좀.”
210|
211|“시키는 대로 다 한다고 하지 않았냐?”
212|
213|“그래도 그건 좀…….”
214|
215|“됐어. 마음 같아서는 그러고 싶지만 내가 그 정도로 막 나가는 놈은 아니야. 일단 카메라 뺏고, 저 빌어먹을 놈한테 씻지 못할 굴욕을 안겨 줘야지.”
216|
217|“휴우. 다행이다. 그럼 난 무조건 오빠 편이지.”
218|
219|“잘해. 이번에 망설이거나 조금이라도 뒤로 빼는 놈 있으면 알지?”
220|
221|“당연하죠.”
222|
223|“저희만 믿으십쇼, 팀장님. 아니, 형님. 헤헤.”
224|
225|임창수의 입가에 비릿한 미소가 맺혔다.
226|
227|‘내 자존심을 짓밟았으면 그만한 대가를 치러야지.’
228|
229|곧 나오는 보스 존(Boss Zone)에서 겁도 없이 누굴 건드렸는지 똑똑히 깨닫게 해 줄 생각이었다.
230|
231|마침 진태경에게 대적할 만한 몬스터도 그곳에 있다.
232|
233|‘미노타우로스 대전사.’
234|
235|이곳, ‘미노타우로스의 미로’의 보스 몬스터.
236|
237|B급 몬스터 주제에 육체 능력만큼은 A급에 맞먹는다는 괴물 같은 놈이다.
238|
239|‘대전사가 놈의 힘을 소진시키면 그때 결행한다.’
240|
241|이이제이(以夷制夷).
242|
243|오랑캐는 오랑캐로. 괴물은 괴물로 물리친다.
244|
245|양쪽 모두 지친 그때가 바로 기회다. 어이없이 잃게 될 돈도, 땅에 떨어진 자존심도 한 번에 회복할 수 있다.
246|
247|“야, 빨리 와! 보스 존이잖아!”
248|
249|다음 순간 진태경의 외침이 들려왔다. 임창수가 활짝 웃었다.
250|
251|“예! 갑니다!”
252|
253|보스 존을 향해 걸어가는 그의 발걸음은 경쾌하기 그지없었다.
254|
255|
256|
257|* * *
258|
259|
260|
261|“일섬(一殲).”
262|
263|콰아아아.
264|
265|창날 끝에서 하늘이 쪼개지는 소리가 났다. 닿는 모든 것을 찢고 집어삼키는 백색 와류가 근육질의 가슴에 닿았다.
266|
267|- 모오?
268|
269|콰드드득.
270|
271|살았는지, 죽었는지 굳이 확인할 필요도 없었다.
272|
273|놈의 가슴에서 창을 뽑아낸 순간 시스템 알림이 울렸으니까.
274|
275|띠링.
276|
277|
278|
279|- [Lv.70 미노타우로스 대전사]를 처치했습니다!
280|
281|- 레벨 업!
282|
283|- 퀘스트, [B급 게이트 클리어]를 완료했습니다!
284|
285|- 당신의 기여도를 계산 중입니다…… 완료되었습니다!
286|
287|- 퀘스트 성공 보상이 인벤토리로 지급됩니다!
288|
289|
290|
291|“휴우.”
292|
293|역시 마지막은 큰 거 한 방이지. 몸이 엄청 피곤하긴 하지만. 나는 창에 묻은 피를 털며 돌아섰다.
294|
295|“빨리 부산물 챙겨서 나가죠. 배고파 죽겠…… 다들 왜 그러세요?”
296|
297|임꺽정이 대표로 입을 열었다.
298|
299|“그걸 몰라서 묻냐?”
300|
301|그가 죽은 보스 몬스터의 사체와 나를 번갈아 바라봤다.
302|
303|한 방에 B급 보스 몬스터를 끝장냈으니 무슨 변명이라도 해보라는 눈빛이다.
304|
305|“음, 운이 좋았던 걸로 해 두죠.”
306|
307|“운?”
308|
309|“네, 운.”
310|
311|정말 운이 좋아서다.
312|
313|내가 고시원에 살았던 것도, 고시원 앞에 캡슐이 버려진 것도. 전부 다.
314|
315|“허허, 기가 차서 말도 안 나오는구먼. 됐다.”
316|
317|다른 사람들도 임꺽정과 비슷한 반응이다. 이미 나와 레이드를 경험한 적 있는 최 팀장도 어안이 벙벙한 표정으로 한마디를 건넸다.
318|
319|“이 정도일 줄은 몰랐습니다만.”
320|
321|“지금 알면 됐죠.”
322|
323|“이에 관해 대화를 나눌 수 있을까요?”
324|
325|“물론입니다.”
326|
327|지금은 아니고, 나중에. 더 중요한 볼일이 남았거든.
328|
329|나는 최대한 매력적인 미소를 지으며 한 사람에게 다가갔다.
330|
331|“송이 씨, 저 힐 좀 부탁드려도 될…… 너희들은 거기서 뭐 하냐?”
332|
333|“아.”
334|
335|“뭐냐고. 왜 여기 있어?”
336|
337|“그냥, 그냥 있는데요.”
338|
339|“저, 저는 언니가 너무 예쁘셔서.”
340|
341|송이 씨 옆에 붙어 있던 상동 길드원들이 화들짝 놀라며 아무 말 대잔치를 시작한다.
342|
343|‘뭐야, 이것들.’
344|
345|나랑 송이 씨 사이에서 방해되니까 꺼지란 소리였는데. 내가 그렇게 무섭게 보이나?
346|
347|“임창수 어디 있어?”
348|
349|한마디에 상동 길드원들이 홍해처럼 쫙 갈라졌다. 임창수가 백지장처럼 하얀 얼굴로 대답했다.
350|
351|“여기 있습니다.”
352|
353|“너 얼굴 왜 그래? 어디 아파?”
354|
355|“모, 몸살 기운이 조금.”
356|
357|“쯧쯧. 포션도 챙겨 먹고 그래, 인마. 너 집에 돈 많잖아.”
358|
359|“…….”
360|
361|“어쨌든 빨리 부산물 수거하고 가자. 피곤하다.”
362|
363|“네, 넵.”
364|
365|임창수가 방해꾼들을 데리고 사라지자 기다렸던 순간이 찾아왔다. 나는 송이 씨를 향해 활짝 웃어 보였다.
366|
367|“배고프시죠? 저녁으로 근사한 레스토랑에서 스테이크 어떠세요?”
368|
369|송이 씨도 나를 따라 웃었다.
370|
371|“죄송하지만 제가 채식주의자라.”
372|
373|“이상하네. 어제 고기 잘 드셨던 것 같은데. 그럼 샐러드 바 가실래요?”
374|
375|“제가 육식주의자라.”
376|
377|“…….”
378|
379|이거 까인 거 맞지?
```

## Assembled English

```markdown
[P1]
# Chapter 85

[P2]
“Changsoo hyung, are you okay?”

[P3]
“Are you hurt?”

[P4]
At his team members’ questions, Im Changsoo clenched his teeth.

[P5]
“Shut up, you bastards. After everything I’ve done for you, you just stood there and watched?”

[P6]
“No, it’s just…”

[P7]
“Things were a little complicated back there. I’m sorry.”

[P8]
“You disloyal bastards.”

[P9]
They weren’t bound together by loyalty, but Im Changsoo had always thought he gave them what they were due and received what he was owed in return. Who had forced those training-camp washouts into the Guild, bought them cars, and given them spending money?

[P10]
He had received their loyalty in exchange…but being abandoned at the most important moment felt like a stinging blow to the back of the head.

[P11]
*Fuck, what kind of bullshit is this?*

[P12]
Several billion won? It was certainly a lot of money, but not more than Im Changsoo could afford. Selling one or two of the buildings in his name would be enough to cover it.

[P13]
But he could never tolerate having his pride trampled.

[P14]
*That bastard deserves to be beaten to death.*

[P15]
Im Changsoo glared at one person’s back, his eyes wide.

[P16]
That bastard in the black leather armor—Jin Taekyung—was the root cause of everything.

[P17]
*I don’t know where he came from or what he was doing before this…but I’ll make him pay for this humiliation.*

[P18]
He still didn’t know exactly who Taekyung was. The one thing he knew for certain was that Taekyung was no ordinary C-rank Hunter.

[P19]
There wasn’t a single C-rank Hunter in the world who could crush eight B-rank monsters in a head-on fight.

[P20]
*Why is he hiding his identity? Is he a fugitive? Or someone with a fraudulent registration? The moment we get out of this Gate, I’ll dig up every last thing about him.*

[P21]
Just as Im Changsoo was quietly stoking his thirst for revenge—

[P22]
Whoosh!

[P23]
Jin Taekyung suddenly turned toward him and narrowed his eyes. The gaze of a predator staring down its prey made Im Changsoo’s heart drop.

[P24]
“Hey.”

[P25]
“Y-yes?”

[P26]
“You were just cursing me in your head, weren’t you?”

[P27]
“N-no, I wasn’t.”

[P28]
“Don’t give me that. The stammering says it all. No wonder the back of my head has been prickling this whole time.”

[P29]
Im Changsoo recalled the words of his father, a Hunter and war hero from the Great Cataclysm era.

[P30]
*The more dangerous the situation, the more calmly you must respond.*

[P31]
“I really wasn’t.”

[P32]
“My mind-reading technique says you’re lying.”

[P33]
“Mind-reading? There’s no such thing.”

[P34]
“There’s magic, so why can’t there be mind-reading? Let go of your hidebound thinking.”

[P35]
“Either way, I swear I wasn’t.”

[P36]
“No, I swear you were. And you’ve got one coming too.”

[P37]
Bonk!

[P38]
Tears sprang to Im Changsoo’s eyes.

[P39]
It was a sharp rap on the forehead. Even his father hadn’t hit him since he turned twenty. Yet here he was, suffering this humiliation at the hands of someone barely his own age—and in front of his team members and several women, no less.

[P40]
“Not bad. Feels just like hitting Hyuk Mujin. Anyway, watch yourself, okay?”

[P41]
Im Changsoo had no idea who Hyuk Mujin was, but he lowered his head anyway.

[P42]
“…Yes.”

[P43]
“But this damn labyrinth never ends. Hey, how much farther is it to the Boss Zone?”

[P44]
“I don’t know. It’s a labyrinth.”

[P45]
“And no more monsters are coming out. I’m bored to death.”

[P46]
“…”

[P47]
*Of course they aren’t! You beat down every single one you see!*

[P48]
Im Changsoo and his team hadn’t even needed to step in. Those five were more than enough. No, Jin Taekyung alone was enough.

[P49]
*What a monster. Is he really an A-rank Hunter?*

[P50]
Taekyung alone seemed to have brought down more than thirty monsters. Just when he appeared to be tiring, he would suddenly start tearing through them again.

[P51]
*The raid is getting faster.*

[P52]
Normally, a raid slowed toward the end as fatigue accumulated.

[P53]
But the raid was getting faster even though they were fighting the same monsters…

[P54]
*Is he getting stronger the whole time?*

[P55]
Im Changsoo desperately rejected the thought that had flashed through his mind.

[P56]
*What is he, a game character leveling up? How could that make any sense?*

[P57]
Getting hit on the forehead must have broken his brain.

[P58]
“Hoo.”

[P59]
As Im Changsoo let out a deep sigh, his team members approached him hesitantly.

[P60]
“Changsoo hyung…”

[P61]
“Oppa, are you okay? Oh no, you’ve got a bump on your forehead.”

[P62]
“I’m in a bad mood, so get lost. The moment you leave, you’re all fired. Got it?”

[P63]
No matter how badly his dignity had been crushed, even a tiger with its teeth pulled was still a tiger.

[P64]
His team members swallowed nervously at Im Changsoo’s threat.

[P65]
*I haven’t even finished paying off my car.*

[P66]
*Who’ll take me if I leave Sangdong Guild?*

[P67]
*My credit-card bill this month…*

[P68]
They had been able to live so comfortably thanks to Im Changsoo’s support. They were all Hunters, so they wouldn’t starve, but they couldn’t expect the same treatment anywhere else.

[P69]
“You think it ends with getting fired? Just wait. Wherever you go, I’ll make sure to place a call in Sangdong Guild’s name. You know this field is small, right?”

[P70]
Their expressions changed completely at the threat that he would not only drive them out but ruin their futures as well.

[P71]
“Changsoo hyung, that’s going too far.”

[P72]
“Hyung? I’m only your hyung when it suits you?”

[P73]
“Oppa, do you really have to take it that far?”

[P74]
“That’s why you bastards should’ve picked the right person to hitch your wagon to.”

[P75]
He wanted to slap every last one of them across the face, but he forced himself to hold back.

[P76]
If he raised his voice, there was no telling when Jin Taekyung might turn around again.

[P77]
*Fuck, how did I end up…*

[P78]
Too afraid of another rap on the forehead to even lose his temper properly. How pathetic could he get?

[P79]
Im Changsoo spat on the floor and turned away.

[P80]
That was when someone grabbed him.

[P81]
“Changsoo hyung. No, Team Leader Im, you can’t do this.”

[P82]
“Please think it over one more time, oppa. Okay?”

[P83]
“Let go. I don’t want to say it twice.”

[P84]
“This time, I mean it. I really will do anything you tell me. Okay?”

[P85]
“…Anything I tell you?”

[P86]
Im Changsoo stopped just as he was about to shake off his colleague’s hand.

[P87]
He glanced back. While he had been arguing with his Guild members, Jin Taekyung’s group had pulled far ahead.

[P88]
Even from that distance, Song Song’s stunning figure from behind was impossible to miss.

[P89]
*Wait. Maybe there is a way.*

[P90]
To Im Changsoo, Jin Taekyung looked like a monster—but he seemed to have one weakness.

[P91]
A woman named Song Song.

[P92]
*He was completely smitten earlier.*

[P93]
There was no need to be perceptive about it. Anyone could tell from a single glance that Jin Taekyung had feelings for Song Song.

[P94]
*She said she was a C-rank healer, right?*

[P95]
Subduing a healer would be easier than wringing a chicken’s neck. If the woman he liked were taken hostage, Jin Taekyung wouldn’t be able to move so freely.

[P96]
*Then it’s over.*

[P97]
Apart from Taekyung, the other three weren’t much of a concern.

[P98]
The old man who was supposedly their Guild Master was a B-rank Hunter, but he was a mage, so close combat would be his weakness. The middle-aged E-rank tank wasn’t even worth discussing.

[P99]
The only person who bothered Im Changsoo a little was Choi Minwoo. That guy…

[P100]
“Can I trust what you just said?”

[P101]
“Of course.”

[P102]
“Just trust us.”

[P103]
“Oppa, why don’t you trust people at all? Are we really only this close?”

[P104]
Im Changsoo had a raid team made up of four B-rank Hunters and five C-rank Hunters who would obey his commands. He had trained every one of them to eat only from his hand.

[P105]
“Fine. Then listen carefully to what I’m about to say…”

[P106]
After a short and simple explanation, the team members couldn’t hide their nervousness.

[P107]
“Will it work?”

[P108]
“It does seem possible.”

[P109]
“Oppa, you’re not suggesting what I think you are, right? If you mean killing someone, I don’t know if I can do that.”

[P110]
“Didn’t you just say you’d do anything I told you?”

[P111]
“Even so, that’s a little…”

[P112]
“Forget it. I’d like to, but I’m not reckless enough to go that far. First, we take the camera. Then we put that son of a bitch through a humiliation he’ll never live down.”

[P113]
“Whew. That’s a relief. Then I’m definitely on your side, oppa.”

[P114]
“Do it right. You know what happens if anyone hesitates this time or holds back even a little, right?”

[P115]
“Of course.”

[P116]
“Just trust us, Team Leader. No, hyungnim. Hehe.”

[P117]
A sinister smile spread across Im Changsoo’s lips.

[P118]
*If he trampled on my pride, he has to pay the price.*

[P119]
In the Boss Zone ahead, he would make Jin Taekyung understand exactly who he had dared to cross.

[P120]
There was even a monster there capable of standing against him.

[P121]
*The Minotaur Great Warrior.*

[P122]
The boss monster of **The Minotaur’s Labyrinth**.

[P123]
Despite being only a B-rank monster, it was a monstrous creature whose physical abilities rivaled those of an A-rank.

[P124]
*Once the Great Warrior wears him down, we’ll make our move.*

[P125]
Set a barbarian against a barbarian.

[P126]
Defeat a monster with a monster.

[P127]
The moment both sides were exhausted would be their chance. In one stroke, he could recover both the money he was about to lose for nothing and the pride that had been dragged through the dirt.

[P128]
“Hey, hurry up! It’s the Boss Zone!”

[P129]
Jin Taekyung’s shout rang out the next moment.

[P130]
Im Changsoo smiled broadly.

[P131]
“Yes! Coming!”

[P132]
His steps toward the Boss Zone were remarkably light.

[P133]
* * *

[P134]
“One Annihilation.”

[P135]
Kraaaaaash!

[P136]
The sound of the sky splitting erupted from the tip of my spear. A white vortex that tore apart and devoured everything it touched slammed into the Great Warrior’s muscular chest.

[P137]
—Moo?

[P138]
Crack-crack-crack!

[P139]
There was no need to check whether it was alive or dead.

[P140]
The moment I pulled my spear from its chest, the System notification rang out.

[P141]
Ding.

[P142]
> **System**
>
> - Defeated **Lv. 70 Minotaur Great Warrior**!
>
> - Level Up!
>
> - Quest, **B-rank Gate Clear**, completed!
>
> - Calculating your contribution… Complete!
>
> - The Quest Success Reward has been deposited into your Inventory!

[P143]
“Whew.”

[P144]
The last one should always end with one big hit.

[P145]
My body was incredibly tired, though.

[P146]
I shook the blood from my spear and turned around.

[P147]
“Let’s collect the byproducts and get out of here. I’m starving to dea—why are you all looking at me like that?”

[P148]
Im Kkeokjeong spoke for everyone.

[P149]
“You really have to ask?”

[P150]
He looked back and forth between the boss monster’s corpse and me.

[P151]
His eyes demanded some kind of explanation for how I had finished off a B-rank boss monster with a single blow.

[P152]
“Hmm. Let’s just say I got lucky.”

[P153]
“Lucky?”

[P154]
“Yes. Lucky.”

[P155]
It really was because I had been lucky.

[P156]
Lucky that I had lived in a goshiwon.[^1] Lucky that a capsule had been discarded in front of it.

[P157]
All of it.

[P158]
“Good grief. I’m too dumbfounded to speak. Fine.”

[P159]
The others reacted much the same way as Im Kkeokjeong. Even Team Leader Choi, who had already been on a raid with me, looked stunned.

[P160]
“I didn’t realize you were this capable.”

[P161]
“If you know now, that’s enough.”

[P162]
“Could we discuss this?”

[P163]
“Of course.”

[P164]
Not now. Later.

[P165]
I still had something more important to take care of.

[P166]
With my most charming smile, I approached one person.

[P167]
“Miss Song, could I ask you for a heal—what are you guys doing over there?”

[P168]
“Ah.”

[P169]
“What are you doing? Why are you here?”

[P170]
“We’re just…just standing here.”

[P171]
“I-I just think she’s so beautiful.”

[P172]
The Sangdong Guild members clustered around Song Song jumped in surprise and began blurting out whatever came to mind.

[P173]
*What’s with these guys?*

[P174]
I only meant that they should get lost because they were getting in the way between me and Miss Song.

[P175]
*Do I really look that scary?*

[P176]
“Where’s Im Changsoo?”

[P177]
At a single word from me, the Sangdong Guild members split apart like the Red Sea.

[P178]
Im Changsoo answered from behind them, his face white as a sheet.

[P179]
“I’m here.”

[P180]
“What’s wrong with your face? Are you sick?”

[P181]
“I-I think I’m coming down with something.”

[P182]
“Tsk, tsk. Take a potion, you idiot. Your family’s rich.”

[P183]
“…”

[P184]
“Anyway, hurry up and collect the byproducts. Let’s go. I’m tired.”

[P185]
“Yes, yessir.”

[P186]
Once Im Changsoo disappeared with the nuisances, the moment I had been waiting for finally arrived.

[P187]
I flashed Song Song a bright smile.

[P188]
“You’re hungry, right? How about steak at a nice restaurant for dinner?”

[P189]
Song Song smiled back at me.

[P190]
“I’m sorry, but I’m a vegetarian.”

[P191]
“That’s strange. You seemed to eat meat just fine yesterday. How about a salad bar?”

[P192]
“I’m a carnivore.”

[P193]
“…”

[P194]
*I got rejected, right?*

[P195]
[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often used by students and people on tight budgets.
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
# Chapter 85

[P2]
“Changsoo hyung. Are you okay?”

[P3]
“Were you hurt?”

[P4]
At his team members’ questions, Im Changsoo clenched his teeth.

[P5]
“Shut up, you bastards. After everything I’ve done for you, you’re just standing around watching?”

[P6]
“No, it’s just…”

[P7]
“The situation was a little complicated then. I’m sorry.”

[P8]
“You disloyal bastards.”

[P9]
They weren’t bound together by loyalty, but Im Changsoo thought he had given them what they were due and received what he was owed in return. Who had been the one to force the training-camp washouts into the Guild, buy them cars, and give them spending money?

[P10]
He had received their loyalty in exchange…but being abandoned at the most important moment felt like a stinging blow to the back of the head.

[P11]
*Fuck, what kind of bullshit is this?*

[P12]
Several billion won? It was certainly a large amount of money, but it wasn’t beyond Im Changsoo’s means. He could pay it in full by selling just one or two buildings registered under his name.

[P13]
But he couldn’t tolerate having his pride trampled.

[P14]
*That bastard deserves to be beaten to death.*

[P15]
Im Changsoo glared at one person’s back with wide-open eyes.

[P16]
That bastard in the black leather armor—Jin Taekyung—was the root cause of everything.

[P17]
*I don’t know where he came from or what he was doing before this…but I’ll make him pay for this humiliation.*

[P18]
He still didn’t know exactly what Taekyung’s identity was. The one thing he knew for certain was that Taekyung was no ordinary C-rank Hunter.

[P19]
There wasn’t a single C-rank Hunter in the world who could crush eight B-rank monsters in a head-on fight.

[P20]
*Why is he hiding his identity? Is he a fugitive criminal? Or someone with a fraudulent registration? The moment we get out of this Gate, I’ll dig up every last thing about him.*

[P21]
It was at that moment that Jin Taekyung suddenly turned his head toward him and narrowed his eyes.

[P22]
The predator’s gaze, fixed on its prey, made Im Changsoo’s heart drop.

[P23]
“Hey.”

[P24]
“Y-yes?”

[P25]
“You were just cursing me in your head, weren’t you?”

[P26]
“N-no, I didn’t.”

[P27]
“Don’t give me that. The way you stammered gives it away. No wonder the back of my head has been prickling since earlier.”

[P28]
Im Changsoo recalled the words of his father, a Hunter and war hero from the Great Cataclysm era.

[P29]
*The more dangerous the situation, the more calmly you have to deal with it.*

[P30]
“I really didn’t.”

[P31]
“My mind-reading technique says you’re lying.”

[P32]
“Mind-reading? There’s no such thing.”

[P33]
“There’s magic, so why not mind-reading? Let go of your hidebound thinking.”

[P34]
“Regardless, I swear I didn’t.”

[P35]
“No, I swear you did. And you’re getting one too.”

[P36]
Bonk!

[P37]
Tears sprang to Im Changsoo’s eyes.

[P38]
It was a forehead flick. He hadn’t even been hit by his father since turning twenty. And now, in front of his team members and several women, he had suffered this humiliation at the hands of someone who looked barely his age.

[P39]
“Not bad. The feel is exactly like when I hit Hyuk Mujin. Anyway, watch yourself, okay?”

[P40]
Im Changsoo didn’t know who Hyuk Mujin was, but he lowered his head anyway.

[P41]
“…Yes.”

[P42]
“But this damn labyrinth really doesn’t end. Hey, how much farther to the Boss Zone?”

[P43]
“I don’t know. It’s a labyrinth.”

[P44]
“And no more monsters are coming out. I’m bored to death.”

[P45]
“…”

[P46]
*Of course they aren’t coming out when you beat down every single one you see!*

[P47]
Im Changsoo and his team didn’t even need to step in. Those five were more than enough. No, Jin Taekyung alone was enough.

[P48]
*What a monster. Is he really an A-rank Hunter?*

[P49]
Taekyung alone seemed to have brought down more than thirty monsters. Just when it seemed like he was getting tired, he would suddenly start flying around again.

[P50]
*The raid is getting faster.*

[P51]
Normally, a raid slowed down toward the end as fatigue accumulated.

[P52]
But the raid was getting faster even though they were fighting the same monsters…

[P53]
*Is he getting stronger the whole time?*

[P54]
Im Changsoo desperately rejected the thought that had flashed through his mind.

[P55]
*What is he, a game character leveling up? How could that make any sense?*

[P56]
Getting hit on the forehead must have broken his brain.

[P57]
“Hoo.”

[P58]
As Im Changsoo let out a deep sigh, his team members approached him hesitantly.

[P59]
“Changsoo hyung…”

[P60]
“Oppa, are you okay? What do we do? You’ve got a bump on your forehead.”

[P61]
“I’m in a bad mood, so get lost. The moment you leave, you’re all fired. Got it?”

[P62]
No matter how badly his dignity had been crushed, even a tiger with its teeth pulled was still a tiger.

[P63]
His team members swallowed nervously at Im Changsoo’s threat.

[P64]
*My car payments aren’t even finished.*

[P65]
*Where will I get accepted if I leave Sangdong Guild?*

[P66]
*My credit-card bill this month…*

[P67]
The reason they had been able to enjoy such comfortable lives was Im Changsoo’s support. Since they were all Hunters, they weren’t going to starve to death, but wherever they went, it would be difficult to expect the same treatment.

[P68]
“You think you’re getting away with it just because you’re leaving? Just wait. Wherever you go, I’ll make sure to place a call in Sangdong Guild’s name. You know this field is small, right?”

[P69]
At the threat that he would not only drive them out but also ruin their futures, their expressions changed completely.

[P70]
“Changsoo hyung, that’s going too far.”

[P71]
“Hyung? I’m only hyung when things are going your way?”

[P72]
“Oppa, do you really have to take it that far?”

[P73]
“That’s why you bastards should’ve picked the right person to hitch your wagon to.”

[P74]
He wanted to slap every one of them across the face, but he forced himself to hold back.

[P75]
If he raised his voice again, there was no telling when Jin Taekyung might turn around.

[P76]
*Fuck, how did I end up…*

[P77]
What kind of pathetic situation was this, being too afraid of a forehead flick to even get angry properly?

[P78]
Im Changsoo spat on the floor and turned away.

[P79]
That was when someone grabbed him.

[P80]
“Changsoo hyung. No, Team Leader Im, you can’t do this.”

[P81]
“Think it over one more time, oppa. Please?”

[P82]
“Let go. I don’t want to say it twice.”

[P83]
“This time, for real. I’ll do everything you tell me. Okay?”

[P84]
“…Everything I tell you?”

[P85]
Im Changsoo, who had been about to pull away from his colleague’s hand, suddenly stopped.

[P86]
He glanced back and saw Jin Taekyung’s group far ahead of them. They had gotten some distance away while he was arguing with his Guild members.

[P87]
Even from that distance, Song Song’s stunning figure from behind was impossible to miss.

[P88]
*Wait. Maybe there is a way.*

[P89]
To Im Changsoo, Jin Taekyung looked like a monster—but he seemed to have one weakness.

[P90]
A woman named Song Song.

[P91]
*He was completely smitten earlier.*

[P92]
There was no need to be perceptive about it. Anyone could tell from a single glance that Jin Taekyung had feelings for Song Song.

[P93]
*She said she was a C-rank healer, right?*

[P94]
Subduing a healer was easier than twisting a chicken’s neck. If the woman he liked were being held hostage, Jin Taekyung wouldn’t be able to act freely.

[P95]
*Then it’s over.*

[P96]
Apart from Taekyung, the other three weren’t much of a concern.

[P97]
The old man who was supposedly the Guild Master was a B-rank Hunter, but he was a mage, so close combat would be his worst area. The middle-aged man who was an E-rank tank wasn’t even worth discussing.

[P98]
The only person who bothered Im Changsoo a little was Choi Minwoo. That guy…

[P99]
“Can I trust what you just said?”

[P100]
“Of course.”

[P101]
“Just trust us.”

[P102]
“Oppa, why don’t you trust people at all? Are we really only this close?”

[P103]
Im Changsoo had a raid team made up of four B-rank Hunters and five C-rank Hunters who would obey his commands. They were all people he had trained to live solely on the scraps he handed them.

[P104]
“Fine. Then listen carefully to what I’m about to say…”

[P105]
After a short and simple explanation, the team members couldn’t hide their nervousness.

[P106]
“Will it work?”

[P107]
“It does seem possible.”

[P108]
“Oppa, it’s not what I think it is, right? If you’re talking about killing someone, I’m not sure I can.”

[P109]
“Didn’t you say you’d do everything I told you?”

[P110]
“Even so, that’s a little…”

[P111]
“Forget it. I’d like to do that, but I’m not reckless enough to go that far. First, we take the camera. Then we give that son of a bitch a humiliation he’ll never live down.”

[P112]
“Whew. What a relief. Then I’m definitely on oppa’s side.”

[P113]
“Do your best. You know what happens if anyone hesitates this time or holds back even a little, right?”

[P114]
“Of course.”

[P115]
“Just trust us, Team Leader. No, hyungnim. Hehe.”

[P116]
A sinister smile spread across Im Changsoo’s lips.

[P117]
*If he trampled on my pride, he has to pay the price.*

[P118]
In the Boss Zone they were about to enter, Im Changsoo intended to make Jin Taekyung understand exactly whose toes he had stepped on.

[P119]
There was even a monster there capable of standing against Jin Taekyung.

[P120]
*The Minotaur Warrior.*

[P121]
The boss monster of **The Minotaur’s Labyrinth**.

[P122]
Despite being only a B-rank monster, it was a monstrous creature whose physical abilities rivaled those of an A-rank.

[P123]
*Once the Minotaur Warrior wears him down, we’ll make our move.*

[P124]
Set a barbarian against a barbarian.

[P125]
Defeat a monster with a monster.

[P126]
The moment both sides were exhausted would be their opportunity. He could recover both the money he was about to lose for no good reason and the pride that had been dragged through the dirt.

[P127]
“Hey, hurry up! This is the Boss Zone!”

[P128]
Jin Taekyung’s shout rang out the next moment.

[P129]
Im Changsoo smiled broadly.

[P130]
“Yes! Coming!”

[P131]
His steps toward the Boss Zone were remarkably light.

[P132]
* * *

[P133]
“One Annihilation.”

[P134]
Kraaaaaash!

[P135]
From the tip of the spear came the sound of the sky splitting apart.

[P136]
A white vortex that tore through and devoured everything it touched slammed into the muscular chest of the Minotaur Warrior.

[P137]
—Moo?

[P138]
Crack-crack-crack!

[P139]
There was no need to check whether it was alive or dead.

[P140]
The moment I pulled my spear from its chest, the System notification rang out.

[P141]
Ding.

[P142]
> **System**
>
> - Defeated **Lv. 70 Minotaur Warrior**!
>
> - Level Up!
>
> - Quest, **B-rank Gate Clear**, completed!
>
> - Calculating your contribution… Complete!
>
> - The Quest Success Reward has been deposited into your Inventory!

[P143]
“Whew.”

[P144]
The last one should always end with one big hit.

[P145]
My body was incredibly tired, though.

[P146]
I shook the blood from my spear and turned around.

[P147]
“Let’s collect the byproducts and get out of here. I’m starving to dea—why are you all looking at me like that?”

[P148]
Im Kkeokjeong spoke for everyone.

[P149]
“You really have to ask?”

[P150]
He looked back and forth between the dead boss monster’s corpse and me.

[P151]
His eyes demanded some kind of explanation for how I had finished a B-rank boss monster with a single blow.

[P152]
“Hmm. Let’s just say I got lucky.”

[P153]
“Lucky?”

[P154]
“Yes. Lucky.”

[P155]
It really was because I had been lucky.

[P156]
The fact that I had lived in a goshiwon.[^1] The fact that a capsule had been discarded in front of my goshiwon.

[P157]
All of it.

[P158]
“Good grief. I’m speechless. Fine.”

[P159]
The others reacted much the same way as Im Kkeokjeong. Even Team Leader Choi, who had already experienced a raid with me, addressed me with a stunned expression.

[P160]
“I didn’t expect you to be this capable.”

[P161]
“If you know now, that’s enough.”

[P162]
“Could we discuss this?”

[P163]
“Of course.”

[P164]
Not now. Later.

[P165]
I still had something more important to take care of.

[P166]
With my most charming smile, I approached one person.

[P167]
“Miss Song, could I ask you for a heal—what are you guys doing over there?”

[P168]
“Ah.”

[P169]
“What are you doing? Why are you here?”

[P170]
“We’re just… just standing here.”

[P171]
“I-I just think she’s so beautiful.”

[P172]
The Sangdong Guild members who had been standing next to Song Song jumped in surprise and began spouting all kinds of nonsense.

[P173]
*What’s wrong with these guys?*

[P174]
I only meant that they should get lost because they were getting in the way between me and Miss Song.

[P175]
*Do I really look that scary?*

[P176]
“Where’s Im Changsoo?”

[P177]
At a single word from me, the Sangdong Guild members split apart like the Red Sea.

[P178]
Im Changsoo answered from behind them, his face white as a sheet.

[P179]
“I’m here.”

[P180]
“What’s wrong with your face? Are you sick?”

[P181]
“I-I think I’m coming down with something.”

[P182]
“Tsk, tsk. Take a potion, you idiot. You’ve got plenty of money at home.”

[P183]
“…”

[P184]
“Anyway, hurry up and collect the byproducts. Let’s go. I’m tired.”

[P185]
“Yes, yessir.”

[P186]
Once Im Changsoo disappeared with the nuisances, the moment I had been waiting for finally arrived.

[P187]
I smiled brightly at Song Song.

[P188]
“You’re hungry, right? How about steak at a nice restaurant for dinner?”

[P189]
Song Song smiled back at me.

[P190]
“I’m sorry, but I’m a vegetarian.”

[P191]
“That’s strange. I thought you ate meat just fine yesterday. How about a salad bar?”

[P192]
“I’m a carnivore.”

[P193]
“…”

[P194]
*I got rejected, right?*

[P195]
[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often used by students and people on tight budgets.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 최민우    | **Choi Minwoo**   |
| 송송이    | **Song Song**     |
| 임창수    | **Im Changsoo**   |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 힐러      | **healer**            |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 85,
  "passed": true,
  "metrics": {
    "source_characters": 5584,
    "translation_characters": 12443,
    "length_ratio": 2.228,
    "source_paragraphs": 185,
    "translation_paragraphs": 195
  },
  "errors": [],
  "warnings": [
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "송이",
        "preferred": "Song-i"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "상동",
        "romanization": "sangdong"
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
