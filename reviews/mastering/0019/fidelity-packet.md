# Fidelity Gate — Chapter 19

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
  1|＃19화
  2|
  3|
  4|
  5|퀘스트
  6|
  7|
  8|
  9|[전쟁]
 10|
 11|두 가문의 명운을 건 전쟁이 시작되었습니다.
 12|
 13|무림에서 자신을 증명하는 것은 오로지 힘! 살아남는 자가 강하고, 강한 자만이 살아남을 것입니다.
 14|
 15|당신의 무운을 빕니다.
 16|
 17|
 18|
 19|등급 : 메인 퀘스트
 20|
 21|제한 : 진태경
 22|
 23|임무 : 항산검문의 항복 또는 멸문 (미완료)
 24|
 25|보상 : ???
 26|
 27|실패 : ???
 28|
 29|
 30|
 31|
 32|
 33|뚫어져라 퀘스트창을 노려보는 내게, 진위경이 말했다.
 34|
 35|“많이 피곤한가 보구나.”
 36|
 37|피곤? 현재 내 심리 상태를 그렇게 간단한 단어로 정의할 수 있다는 사실에 놀랐다.
 38|
 39|나는 대답 대신 김이 모락모락 피어오르는 찻잔을 바라봤다.
 40|
 41|‘이미 엎질러진 물이다.’
 42|
 43|나름 노력했지만 전쟁을 막을 수는 없었다. 가로회의는 작전 회의로 바뀌었고, 대장로의 전폭적인 지지를 받은 진위경은 망설임 없이 지휘봉을 들었다.
 44|
 45|
 46|
 47|태원진가의 무사들은 지금 즉시 본가로 집결하라!
 48|
 49|
 50|
 51|동틀 무렵 수십 마리의 전서구가 하늘을 날았고, 전령은 말을 달렸다. 철저한 경계망이 그물처럼 펼쳐졌다.
 52|
 53|그렇게 바짝 긴장된 분위기에서 가로회의가 파하자 나와 진위경, 위팽은 소가주 집무실로 자리를 옮겼다.
 54|
 55|“언젠가 벌어질 일이었다. 태경이 네 탓이 아니야.”
 56|
 57|진위경의 따스한 말에 눈물이 날 것 같다. 감동해서가 아니라, 억울해서다.
 58|
 59|‘당연히 내 탓이 아니지!’
 60|
 61|그리고 말이 나왔으니 말인데, 그 ‘언젠가 벌어질 일’이 왜 하필 지금 벌어지냐고.
 62|
 63|내심 분통을 터트리고 있을 때 위팽이 불쑥 입을 열었다.
 64|
 65|“그런데 주군.”
 66|
 67|“왜 그러나?”
 68|
 69|“대장로 말입니다만…… 도무지 의중을 모르겠습니다.”
 70|
 71|대장로. 그 이름을 듣는 순간 다른 생각은 내팽개쳤다. 이 게임에서 만난 NPC 중 가장 꺼림칙한 인물이다.
 72|
 73|진심으로 가문을 위하는 것 같기도 하고, 자신의 이익을 위해 움직이는 정치인의 냄새도 풍기고.
 74|
 75|나는 조심스럽게 입을 열었다.
 76|
 77|“대장로는 어떤 사람이죠?”
 78|
 79|“높은 경지의 무인이면서 심계도 깊다. 무림에서 가장 위험한 부류라 할 수 있지.”
 80|
 81|“그 정도인가요?”
 82|
 83|진위경이 무겁게 고개를 끄덕였다.
 84|
 85|“다른 장로들조차 대장로의 수족에 불과하다. 그는 모습을 좀처럼 드러내지 않으면서도, 장로원이라는 손발을 이용해 중진들을 포섭하고 휘하로 끌어들였지. 그 세월이 수십 년이다.”
 86|
 87|“그럼 가로회의에서 우리 손을 들어 준 것도…….”
 88|
 89|“정확한 사실은 알 수 없지만 꿍꿍이가 있을 것이다. 분명해.”
 90|
 91|“다 죽였어야 했습니다.”
 92|
 93|위팽이 차가운 목소리로 불쑥 끼어들었다.
 94|
 95|“불충한 역도들입니다. 대장로가 그들을 죽이자고 제안했을 때, 저는 솔직히 주군께서 받아들이셨으면 했습니다.”
 96|
 97|나도 그랬다. 하지만 그것은 대장로의 교묘한 화법에 불과했다. 이 정도에서 물러나는 게 어떻겠냐는.
 98|
 99|만약 진위경이 미친 척 그 제안을 수락했다면 결과는 뻔하다.
100|
101|“혈사가 일어났겠지.”
102|
103|“압니다. 그래서 참은 거고요.”
104|
105|태원진가의 수뇌부가 반으로 갈라져 죽고 죽이는 싸움을 계속할 것이다. 지면 죽음이고, 이겨도 큰 피해를 입었을 것이다.
106|
107|‘어쩌면 그게 대장로가 바랐던 결과일지도.’
108|
109|대장로. 보이지 않는 손. 문득 떠오른 생각에 등골이 오싹했다. 마침 내가 느낀 대장로의 이미지와도 딱 맞아떨어진다.
110|
111|한발 물러나 때를 기다리는 하이에나 같은 정치인.
112|
113|진위경이 찻잔을 기울였다.
114|
115|“하지만 어디까지나 짐작일 뿐. 대장로의 의중이 무엇인지는 모르는 것이다. 아직 그는 본가의 어른이며 강력한 아군이다. 주의는 하되 적대하지 말거라. 지금은 사람을 경계하기보다 상황을 헤쳐 나가야 할 때야.”
116|
117|나무가 아니라 숲을 보라는 이야기다.
118|
119|문제는 그 숲도 썩 좋은 상황이 아니라는 거지.
120|
121|내 생각을 읽은 것처럼 위팽이 그에 관련된 이야기를 꺼냈다.
122|
123|“상황도 좋지 않습니다. 외부 소식통에 의하면 이소군이 독살당했다는 소문이 퍼지면서 본가의 평판이 추락하고 있답니다.”
124|
125|“고작 반나절 만에?”
126|
127|“예. 산서성 전체가 그 얘기로 들썩거리고 있습니다.”
128|
129|진위경의 얼굴에 근심이 서렸다.
130|
131|“빠르군. 소문이 빨라도 너무 빨라. 확실히 뒤에 누군가 있어.”
132|
133|여기에 인터넷이 있는 것도 아니고, 이 넓은 땅덩어리에 벌써 소문이 퍼졌다는 것은 확실히 이상한 일이다.
134|
135|‘보이지 않는 적이라.’
136|
137|도대체 누굴까. 제삼의 세력? 항산검문의 자작극?
138|
139|나는 가급적 후자이기를 바랐다. 드러나지 않는 적만큼 위험한 건 없으니까.
140|
141|“민심은 아직까지 반신반의하는 모양이지만 다른 문파들은…….”
142|
143|“아직도 답이 없나?”
144|
145|위팽은 대답 대신 고개를 숙였다.
146|
147|진위경은 이소군의 독살 정보를 입수한 직후 곧장 산서성의 다른 중소 문파들에게 지원 요청을 했다. 하지만 빠짐없이 수포로 돌아간 모양이었다.
148|
149|‘갈수록 최악인데 이건.’
150|
151|진짜 도망쳐야 되나.
152|
153|그런 생각을 하며 창밖을 바라보고 있을 때였다. 푸드득. 홰치는 소리와 함께 비둘기 한 마리가 창가에 내려앉았다.
154|
155|“……답장, 온 것 같은데요?”
156|
157|
158|
159|* * *
160|
161|
162|
163|태원진가.
164|
165|웅장한 필체로 적힌 현판, 그리고 삼엄한 기세로 정문을 지킨 무사들이 가까워지자 마부는 고삐를 느슨하게 늘어트렸다.
166|
167|“정지. 신원과 목적을 밝히시오!”
168|
169|수문위사가 크게 외치며 마차를 가로막았다. 상황이 상황인지라 그의 목소리에는 긴장감이 배어 있었다.
170|
171|더군다나.
172|
173|‘범상치 않다.’
174|
175|고삐를 쥔 마부에게서는 단련된 무인의 냄새가 물씬 풍겼고, 네 마리 준마가 끄는 사두마차는 화려함과 동시에 기품이 있다.
176|
177|‘그런데 왠지 낯이 익은데?’
178|
179|마부도 그렇고. 마차도 그렇고. 어디서 봤더라?
180|
181|잠깐 떠오른 의문은 마부의 날카로운 눈매를 보는 순간 잊혔다. 저 기세, 눈빛. 역시 범상치 않은 손님이다.
182|
183|꿀꺽 침을 삼킨 수문위사가 재차 입을 열었다.
184|
185|“신원과 목적을 밝혀 주십시오.”
186|
187|마차의 문이 열리고, 붉은색 비단신이 사뿐히 내려앉았다.
188|
189|그리고 봄바람처럼 살랑거리는 목소리가 수문위사의 귓가에 내려앉았다.
190|
191|“홍화루에서 왔어요. 이름은 비밀.”
192|
193|목소리와 함께 드러나는 얼굴.
194|
195|수문위사의 눈이 몽롱하게 풀어졌다. 비단 그 혼자만의 일이 아니었다. 여인의 얼굴을 확인한 모두가 같은 반응이었다.
196|
197|수문위사의 입에서 넋 나간 목소리가 흘러나왔다.
198|
199|“아, 비밀…… 그럼 어떤 용무로 오셨는지.”
200|
201|여인, 월화는 매혹적인 미소와 함께 대답했다.
202|
203|“음. 외상값 받으러?”
204|
205|
206|
207|* * *
208|
209|
210|
211|“잘 지냈어요? 나 안 보고 싶었고?”
212|
213|나는 엉거주춤 일어선 채로 굳어 버렸다.
214|
215|잊을 수 없는 얼굴. 그리고 여기 있어서는 안 되는 얼굴이다.
216|
217|“월화?”
218|
219|이 게임에서 처음 만난 NPC. 홍화루의 기녀이자 나, 진태경의 새끼손가락. 그거.
220|
221|누나가 왜 거기서 나와……?
222|
223|“역시 기억하시네. 우리 진 공자님.”
224|
225|월화가 까르르 웃는다. 얘는 얼굴도 예쁜데 웃음소리도 예쁘고, 예쁜 애가 웃으니까 더 예뻐…… 아니, 지금 이럴 때가 아닌데.
226|
227|나는 잔뜩 숨죽인 목소리로 속삭였다.
228|
229|“여긴 어쩐 일로 왔어요. 아, 됐고. 나가요. 나가.”
230|
231|팔꿈치로 슬쩍슬쩍 월화의 몸을 밀었다. 와, 진짜 미치겠다.
232|
233|하필이면 이런 분위기에 나타나다니.
234|
235|가문 전체에 비상 경계령이 떨어졌는데 기녀 불렀다고 소문이라도 나 봐라. 내 평판이 어떻게 될지 상상만 해도 눈앞이 아찔하다.
236|
237|“찌르지 마요. 간지럽잖아.”
238|
239|“알겠으니까 빨리 나가요. 여기 지금 다른 사람들도 있는데 갑자기 와서 뭐 하자는 겁니까? 중요한 손님도 오시기로 했는데.”
240|
241|타이밍도 참 더럽게 안 좋다. 나는 소가주 집무실에서 하오문이라는 문파의 손님을 기다리는 중이었다.
242|
243|당연하게도 진위경, 위팽과 함께였다.
244|
245|“태경아.”
246|
247|진위경의 부름. 나는 뒤도 돌아보지 않고 황급히 손을 내저었다.
248|
249|“아, 생각하시는 그런 거 아닙니다. 저 안 불렀어요. 이분도 이제 가실 거래요. 그렇죠?”
250|
251|월화의 웃음소리가 높아졌다.
252|
253|“우리 진 공자님은 여전히 귀여우셔. 근데 잘못 짚었어. 나 여기 볼일 있어서 온 거거든.”
254|
255|“어허, 우리 진 공자는 무슨. 나 오늘부터 순결하게 살 거예요. 이제 그쪽 볼일 없으니까 빨리 나가요.”
256|
257|“음. 싫은데?”
258|
259|그럼 어쩔 수 없지. 힘으로 옮기는 수밖에. 나는 절박한 심정으로 월화의 허리를 붙잡고 번쩍 들어서…….
260|
261|“응?”
262|
263|뭐야, 이거. 왜 안 들려. 월화가 겉보기에는 늘씬하지만 통뼈라 무게가 많이 나가나?
264|
265|‘개소리지.’
266|
267|내 힘 스탯이 몇인데. 단순 근력으로만 해도 돌멩이를 가루로 만들어 버릴 수 있다. 그런데 내가 여자 NPC 하나 못 든다는 건…….
268|
269|“저, 태경아?”
270|
271|진위경의 두 번째 부름은 무시한 나는 슬그머니 손을 풀었다. 그리고 [기감]을 끌어올렸다.
272|
273|“아하하하하! 미치겠다, 진짜.”
274|
275|웃겨 죽는 월화의 머리 위로 레벨창이 뜸과 동시에, 진위경의 세 번째 부름이 들려왔다.
276|
277|
278|
279|[Lv.50 은소월]
280|
281|
282|
283|“태경아, 인사드려라. 하오문 산서 지부장님이시다…….”
284|
285|아아. 아아아.
286|
287|죽고 싶다.
288|
289|
290|
291|* * *
292|
293|
294|
295|“인사 올립니다. 하오문 산서 지부장, 월화입니다.”
296|
297|은소월. 아니, 일단은 월화라고 해 두자. 그녀는 지금까지의 모습과는 달랐다. 동작 하나하나에 귀부인 같은 기품과 우아함이 묻어 나왔다.
298|
299|“태원진가의 진위경이오.”
300|
301|“위팽입니다.”
302|
303|“…….”
304|
305|벙어리 삼룡이마냥 입을 다물고 있는 내게 월화가 씩 웃어 보였다. 불길한 웃음이다.
306|
307|‘안 돼. 웃지 마.’
308|
309|말 걸지도 마. 제발 그러지 마.
310|
311|“한 분 소개를 못 들은 것 같은데요.”
312|
313|시선이 따갑다. 탁자 아래로 누군가 내 발을 밟았다.
314|
315|나는 피를 토하는 심정으로 입을 열었다.
316|
317|“……진태경입니다.”
318|
319|“네에. 저도 잘 부탁드려요. 진 공자님.”
320|
321|커흠. 진위경이 헛기침과 함께 힐끔 나를 살폈다.
322|
323|“내 동생과 친분이 있는 줄은 몰랐소만.”
324|
325|“저희 가게 단골이시거든요. 태원에 있는 홍화루. 본 문의 산서지부이기도 하지요.”
326|
327|“아, 단골…….”
328|
329|나는 사람들의 시선을 회피했다. 풉, 웃음을 터트린 월화가 본론을 꺼내 들었다.
330|
331|“이제 일 얘기를 해 볼까요?”
332|
333|여러 번 느끼는 거지만 역시 시원시원한 여자다. 진위경과 위팽도 내게서 시선을 떼고 대화에 임했다.
334|
335|“우선 하오문의 도움에 진심 어린 감사를 표하오.”
336|
337|“별말씀을요.”
338|
339|“한데, 본가를 도우려는 이유를 알 수 있겠소?”
340|
341|진위경의 말에 월화가 싱긋 웃었다.
342|
343|“이유라…… 필요하다면 말씀드리지요. 우선 첫째, 본 문의 이득을 위해서입니다.”
344|
345|“이득이라. 구체적으로 어떤 보상을 원하시오?”
346|
347|“항산검문이 소유한 점포와 재화의 절반.”
348|
349|“좋소.”
350|
351|“주군!”
352|
353|위팽이 황급히 나섰지만 진위경은 아랑곳하지 않았다.
354|
355|월화도 살짝 놀란 기색이었다.
356|
357|“결정이 빠르시군요.”
358|
359|“가문의 모든 걸 걸었으니까.”
360|
361|“이미 합의된 내용인가요?”
362|
363|“나는 소가주고, 아버님이 안 계신 지금 가주 대행의 권한을 갖고 있소.”
364|
365|“내부의 반발이 꽤 거센 걸로 아는데요. 예를 들면 장로원이라든가?”
366|
367|“역시 하오문. 정보가 빠르군.”
368|
369|“어쩔 수 없지요. 이 삭막한 무림에서 살아남으려면 정보가 필수인데. 이런 수완이라도 있어야 먹고살지 않겠어요?”
370|
371|월화의 웃음을 보면서, 문득 한 가지 생각이 들었다.
372|
373|‘저 정보. 혹시 내가, 아니 진태경이 흘린 건가?’
374|
375|하오문, 그 이름을 어디서 들어봤나 했더니 무협 소설에서 단골로 등장하는 정보 문파다. 즉, 지부장인 월화는 베테랑 정보 상인인 셈이고.
376|
377|거기에 더해 50레벨의 출중한 무인이기도 하다. 저런 여자가 기녀로 위장해서 진태경 같은 놈을 만나?
378|
379|‘개가 웃을 소리지.’
380|
381|나는 월화를 응시했다. 여신이 내려왔나 싶을 정도로 눈부신 외모다. 그녀가 웃을 때마다 장미가 생각났다. 그 화려함에 숨겨진 날카로운 가시가 이제야 보인다.
382|
383|진위경이 굳은 얼굴로 말했다.
384|
385|“그럼 이제 두 번째 이유를 말하시오.”
386|
387|월화가 예의 화사한 미소를 지으며 대답했다.
388|
389|“진 공자가 마음에 들어서요.”
390|
391|“예?”
392|
393|“어린 데다가 얼굴 잘생겼고, 몸 좋고, 성격도 귀엽고.”
394|
395|“…….”
396|
397|“…….”
398|
399|도대체 어디까지가 진심이고 농담이야?
```

## Assembled English

```markdown
[P1]
# Chapter 19

[P2]
> **System**
>
> **Quest**
>
> **War**
>
> A war that will decide the fate of two families has begun.
>
> In Murim, the only way to prove yourself is through strength! Those who survive are strong, and only the strong will survive.
>
> May fortune favor you in battle.
>
> **Grade:** Main Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Surrender or destruction of the Mount Heng Sword Sect (Incomplete)  
> **Reward:** ???  
> **Failure:** ???

[P3]
Jin Wikyung spoke to me as I stared fixedly at the Quest Window.

[P4]
“You look very tired.”

[P5]
Tired? I was amazed that my current state of mind could be summed up in such a simple word.

[P6]
Instead of answering, I looked at the steaming teacup.

[P7]
*The water’s already been spilled.*

[P8]
I had done my best, but I couldn’t stop the war. The family council had turned into a war council, and with the Head Elder’s full support, Jin Wikyung had taken command without hesitation.

[P9]
> Martial artists of the Jin Family of Taiyuan, assemble at the main family residence immediately!

[P10]
Around dawn, dozens of messenger pigeons took to the sky while messengers rode hard on horseback. A tight security net spread across the entire area.

[P11]
When the family council finally adjourned in that tense atmosphere, Jin Wikyung, Wipeng, and I moved to the Lesser Family Head’s office.

[P12]
“It was bound to happen someday. This isn’t your fault, Taekyung.”

[P13]
Jin Wikyung’s warm words almost brought tears to my eyes. Not because I was moved, but because it felt so unfair.

[P14]
*Of course it wasn’t my fault!*

[P15]
And since we were on the subject, why the hell did that “bound to happen someday” have to happen now?

[P16]
While I was fuming inwardly, Wipeng suddenly spoke.

[P17]
“My lord.”

[P18]
“What is it?”

[P19]
“The Head Elder… I simply cannot figure out what he’s thinking.”

[P20]
The Head Elder. The moment I heard that name, I abandoned all other thoughts. He was the most unsettling person among the NPCs I had encountered in this game.

[P21]
He seemed genuinely devoted to the family, yet he also gave off the unmistakable air of a politician maneuvering for his own benefit.

[P22]
I cautiously asked, “What kind of person is the Head Elder?”

[P23]
“He is a martial artist of a high realm, and his schemes run deep. You could call him one of the most dangerous types of people in Murim.”

[P24]
“That dangerous?”

[P25]
Jin Wikyung nodded gravely.

[P26]
“Even the other Elders are little more than the Head Elder’s hands and feet. He rarely shows himself, yet he has used the Elder Council as his limbs to win over influential members and bring them under his command. He has been doing so for decades.”

[P27]
“Then his supporting us at the family council…”

[P28]
“We cannot know the exact truth, but he must have an ulterior motive. Of that, I am certain.”

[P29]
“We should have killed them all.”

[P30]
Wipeng cut in abruptly, his voice cold.

[P31]
“They are disloyal rebels. When the Head Elder proposed killing them, I honestly hoped you would accept.”

[P32]
So had I. But that had merely been the Head Elder’s clever way of speaking—a suggestion that perhaps we should back down at this point.

[P33]
If Jin Wikyung had thrown caution to the wind and accepted that proposal, the result would have been obvious.

[P34]
“A bloodbath would have broken out.”

[P35]
“I know. That’s why I held back.”

[P36]
The leadership of the Jin Family of Taiyuan would have split in two and kept killing one another. Defeat would have meant death, and even victory would have come at a terrible cost.

[P37]
*Maybe that was exactly what the Head Elder wanted.*

[P38]
The Head Elder. An invisible hand.

[P39]
A chill ran down my spine at the thought. It fit the image I had formed of him perfectly.

[P40]
A hyena of a politician, stepping back and waiting for his moment.

[P41]
Jin Wikyung tilted his teacup.

[P42]
“But that is only a guess. We do not know what the Head Elder truly intends. He is still one of the family’s elders, and a powerful ally. Be wary of him, but do not make an enemy of him. For now, we need to overcome the situation rather than distrust everyone around us.”

[P43]
He was telling me to look at the forest, not the trees.

[P44]
The problem was that the forest itself wasn’t exactly in good shape, either.

[P45]
As if he had read my thoughts, Wipeng brought up the subject.

[P46]
“The situation is not good, either. According to our outside sources, rumors that Lee Seogeun had been poisoned to death have begun spreading, and our family’s reputation is plummeting.”

[P47]
“In only half a day?”

[P48]
“Yes. All of Shanxi is in an uproar over it.”

[P49]
Concern clouded Jin Wikyung’s face.

[P50]
“That is fast. Far too fast. Someone is definitely behind this.”

[P51]
There was no internet here, and yet rumors had already spread across this vast land. It was certainly strange.

[P52]
*An invisible enemy.*

[P53]
Who could it be? A third faction? A staged act by the Mount Heng Sword Sect?

[P54]
I hoped it was the latter if possible. Nothing was more dangerous than an enemy who remained unseen.

[P55]
“The common people still seem unsure what to believe, but the other sects…”

[P56]
“Still no replies?”

[P57]
Wipeng lowered his head instead of answering.

[P58]
As soon as Jin Wikyung learned that Lee Seogeun had been poisoned to death, he had sent requests for aid to the other small and mid-sized sects in Shanxi. It seemed every one of them had come to nothing.

[P59]
*This just keeps getting worse.*

[P60]
*Do I really need to run?*

[P61]
I was looking out the window, thinking that, when—

[P62]
Flap, flap.

[P63]
A pigeon landed on the windowsill with the sound of beating wings.

[P64]
“…It looks like a reply has arrived?”

[P65]
* * *

[P66]
The Jin Family of Taiyuan.

[P67]
As the carriage approached the grand plaque bearing those words in magnificent calligraphy and the martial artists guarding the main gate with a stern aura, the coachman slackened the reins.

[P68]
“Stop! State your identity and purpose!”

[P69]
The gate guard shouted as he blocked the carriage. Given the circumstances, his voice was tense.

[P70]
What was more—

[P71]
*This isn’t ordinary.*

[P72]
The coachman holding the reins gave off the unmistakable air of a trained martial artist, while the carriage drawn by four fine horses combined splendor with dignity.

[P73]
*But why do they look familiar?*

[P74]
The coachman, too. The carriage, too. Where had he seen them?

[P75]
The question vanished the moment he saw the coachman’s sharp eyes. That aura, that gaze. This was certainly no ordinary visitor.

[P76]
The gate guard swallowed and spoke again.

[P77]
“Please state your identity and purpose.”

[P78]
The carriage door opened, and a red silk slipper alighted lightly onto the ground.

[P79]
Then a voice as gentle as a spring breeze drifted into the guard’s ear.

[P80]
“I’m from Honghwaru. My name is a secret.”

[P81]
Her face appeared along with her voice.

[P82]
The gate guard’s eyes grew dazed. He wasn’t the only one. Everyone who saw the woman reacted the same way.

[P83]
A vacant voice escaped the gate guard’s mouth.

[P84]
“Ah, a secret… Then what brings you here?”

[P85]
The woman—Wolhwa—answered with an enchanting smile.

[P86]
“Hmm. I’m here to collect an unpaid tab?”

[P87]
* * *

[P88]
“How have you been? Didn’t you miss me?”

[P89]
I froze halfway to my feet.

[P90]
A face I could never forget. And a face that had no business being here.

[P91]
“Wolhwa?”

[P92]
The first NPC I had met in this game. A courtesan at Honghwaru—and Jin Taekyung’s precious little finger. That thing.

[P93]
*Why is noona coming out of there…?*

[P94]
“You remember me after all. Our Young Master Jin.”

[P95]
Wolhwa giggled. She was beautiful, her laugh was beautiful, and when a beautiful woman laughed, she became even more beautiful…

[P96]
*No, this is not the time for that.*

[P97]
I whispered in a tightly restrained voice.

[P98]
“What brings you here? No, never mind. Leave. Get out.”

[P99]
I kept nudging Wolhwa with my elbow.

[P100]
*This is driving me insane.*

[P101]
Of all times, she had to show up in this atmosphere.

[P102]
The entire family was on high alert. If word got out that I had called for a courtesan, just imagining what would happen to my reputation made my vision swim.

[P103]
“Don’t poke me. That tickles.”

[P104]
“I get it, so hurry up and leave. There are other people here. What are you trying to pull, barging in like this? We’re expecting an important guest, too.”

[P105]
The timing was damn awful, too. I was in the Lesser Family Head’s office waiting for a guest from a sect called the Lower District Sect.

[P106]
Naturally, Jin Wikyung and Wipeng were there with me.

[P107]
“Taekyung.”

[P108]
Jin Wikyung called my name. Without even turning around, I hurriedly waved my hands.

[P109]
“Ah, it’s not what you think. I didn’t call her. She says she’s leaving now, too. Right?”

[P110]
Wolhwa’s laughter rose in pitch.

[P111]
“Our Young Master Jin is still so adorable. But you guessed wrong. I’m here on business.”

[P112]
“Don’t call me ‘our Young Master Jin.’ I’m going to live chastely from today onward. I don’t have any business with you anymore, so hurry up and leave.”

[P113]
“Hmm. I don’t want to.”

[P114]
Then there was no helping it. I would have to move her by force.

[P115]
In desperation, I grabbed Wolhwa around the waist and hoisted her up—

[P116]
“Huh?”

[P117]
What the hell? Why won’t she lift?

[P118]
Wolhwa looked slender, but was she so big-boned that she weighed a lot?

[P119]
*That’s bullshit.*

[P120]
Just how high was my Strength stat? With raw physical strength alone, I could grind a rock into powder. And yet I couldn’t lift a single female NPC, which meant—

[P121]
“Taekyung?”

[P122]
I ignored Jin Wikyung’s second call and furtively let go. Then I heightened my Qi Sense.

[P123]
“Ahahahahaha! This is driving me insane!”

[P124]
As Wolhwa laughed herself to death, a Level Window appeared above her head. At the same time, I heard Jin Wikyung call my name for the third time.

[P125]
> **System**
>
> **Lv. 50 Eun Sowol**

[P126]
“Taekyung, greet her. She is the Branch Leader of the Lower District Sect’s Shanxi branch…”

[P127]
Ah. Ahhh.

[P128]
*I want to die.*

[P129]
* * *

[P130]
“Greetings. I am Wolhwa, Branch Leader of the Lower District Sect’s Shanxi branch.”

[P131]
Eun Sowol.

[P132]
No, for now, let’s just call her Wolhwa.

[P133]
She was different from how she had acted until now. Every movement carried the grace and elegance of a noblewoman.

[P134]
“I am Jin Wikyung of the Jin Family of Taiyuan.”

[P135]
“I’m Wipeng.”

[P136]
I kept my mouth shut like Mute Samryong,[^1] and Wolhwa flashed me a grin.

[P137]
It was an ominous grin.

[P138]
*Don’t. Don’t smile.*

[P139]
*Don’t talk to me. Please don’t.*

[P140]
“It seems there’s one person I haven’t been introduced to.”

[P141]
I felt eyes boring into me. Someone stepped on my foot beneath the table.

[P142]
Feeling as though I were coughing up blood, I forced myself to speak.

[P143]
“…I’m Jin Taekyung.”

[P144]
“Yeees. I hope we get along too, Young Master Jin.”

[P145]
“Ahem.”

[P146]
With a cough, Jin Wikyung glanced at me.

[P147]
“I didn’t realize you were acquainted with my younger brother.”

[P148]
“He’s a regular at our establishment—the Honghwaru in Taiyuan. It also serves as our sect’s Shanxi branch.”

[P149]
“Ah. A regular…”

[P150]
I avoided everyone’s gaze. Wolhwa snorted with laughter, then got down to business.

[P151]
“Shall we talk business now?”

[P152]
I had felt it several times before, but she really was a refreshingly direct woman. Jin Wikyung and Wipeng also turned their attention away from me and joined the conversation.

[P153]
“First, allow me to offer my sincere thanks for the Lower District Sect’s assistance.”

[P154]
“Think nothing of it.”

[P155]
“But may I ask why you wish to help our family?”

[P156]
Wolhwa smiled sweetly at Jin Wikyung’s question.

[P157]
“The reason… I will tell you if necessary. First, we are doing this for our sect’s benefit.”

[P158]
“Benefit. What specific compensation do you want?”

[P159]
“Half of the shops and assets owned by the Mount Heng Sword Sect.”

[P160]
“Good.”

[P161]
“My lord!”

[P162]
Wipeng hurriedly stepped forward, but Jin Wikyung paid him no heed.

[P163]
Wolhwa also looked slightly surprised.

[P164]
“You decide quickly.”

[P165]
“Because I have staked everything the family has.”

[P166]
“Has this already been agreed upon?”

[P167]
“I am the Lesser Family Head, and with my father absent, I possess the authority of the acting Family Head.”

[P168]
“I hear the internal opposition is quite fierce. The Elder Council, for example?”

[P169]
“As expected of the Lower District Sect. You certainly get your information fast.”

[P170]
“It can’t be helped. Information is essential if you want to survive in this bleak Murim. We need at least that much resourcefulness to make a living, don’t we?”

[P171]
Watching Wolhwa smile, I suddenly had a thought.

[P172]
*That information. Did I—or rather, did Jin Taekyung—let it slip?*

[P173]
I had wondered where I had heard the name Lower District Sect before. It was an information-gathering sect that appeared regularly in martial-arts novels. In other words, Wolhwa, its Branch Leader, was a veteran information merchant.

[P174]
On top of that, she was an outstanding martial artist at Level 50. A woman like that had disguised herself as a courtesan to meet a guy like Jin Taekyung?

[P175]
*Even a dog would laugh at that.*

[P176]
I stared at Wolhwa.

[P177]
Her beauty was dazzling enough to make me wonder if a goddess had descended. Whenever she smiled, roses came to mind. Only now could I see the sharp thorns hidden beneath all that splendor.

[P178]
Jin Wikyung spoke with a stiff expression.

[P179]
“Then tell us the second reason.”

[P180]
Wolhwa answered with her usual radiant smile.

[P181]
“Because I like Young Master Jin.”

[P182]
“Excuse me?”

[P183]
“He’s young, handsome, well-built, and has such a cute personality.”

[P184]
“…”

[P185]
“…”

[P186]
*How much of that was sincere, and how much was a joke?*

[P187]
[^1]: Mute Samryong is the protagonist of a well-known Korean short story; his name literally means “Three Dragons.”
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 19

[P2]
> **System**
>
> **Quest**
>
> **War**
>
> A war that will decide the fate of two factions has begun.
>
> In Murim, the only way to prove yourself is through strength! Those who survive are strong, and only the strong will survive.
>
> May fortune favor you in battle.
>
> **Grade:** Main Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Surrender or destruction of the Mount Heng Sword Sect (Incomplete)  
> **Reward:** ???  
> **Failure:** ???

[P3]
Jin Wikyung spoke to me as I stared fixedly at the Quest Window.

[P4]
“You look very tired.”

[P5]
Tired? I was amazed that my current state of mind could be summed up in such a simple word.

[P6]
Instead of answering, I looked at the steaming teacup.

[P7]
*The water’s already been spilled.*

[P8]
I had done my best, but I couldn’t stop the war. The family council had turned into a war council, and with the Head Elder’s full support, Jin Wikyung had taken up command without hesitation.

[P9]
> Martial artists of the Jin Family of Taiyuan, assemble at the main family residence immediately!

[P10]
At dawn, dozens of messenger pigeons took to the sky while messengers rode hard on horseback. A tight security net was thrown over the entire area.

[P11]
When the family council finally broke up in that tense atmosphere, Jin Wikyung, Wipeng, and I moved to the Lesser Family Head’s office.

[P12]
“It was bound to happen someday. This isn’t your fault, Taekyung.”

[P13]
I felt like crying at Jin Wikyung’s warm words. Not because I was moved, but because it felt so unfair.

[P14]
*Of course it wasn’t my fault!*

[P15]
And since we were on the subject, why the hell did that “bound to happen someday” have to happen now?

[P16]
While I was fuming inwardly, Wipeng suddenly spoke.

[P17]
“My lord.”

[P18]
“Why?”

[P19]
“The Head Elder… I simply cannot figure out what he’s thinking.”

[P20]
The Head Elder. The moment I heard that name, I abandoned all other thoughts. He was the most unsettling person among the NPCs I had encountered in this game.

[P21]
He seemed genuinely devoted to the family, yet he also gave off the unmistakable air of a politician maneuvering for his own benefit.

[P22]
I cautiously opened my mouth.

[P23]
“What kind of person is the Head Elder?”

[P24]
“He is a martial artist of a high realm, and his schemes run deep. You could call him one of the most dangerous types of people in Murim.”

[P25]
“That dangerous?”

[P26]
Jin Wikyung nodded heavily.

[P27]
“Even the other Elders are little more than the Head Elder’s hands and feet. He rarely reveals himself, yet he has used the Elder Council to win over influential members and bring them under his command. He has been doing so for decades.”

[P28]
“Then his supporting us at the family council…”

[P29]
“We cannot know the exact truth, but he must have an ulterior motive. Of that, I am certain.”

[P30]
“We should have killed them all.”

[P31]
Wipeng cut in abruptly, his voice cold.

[P32]
“They are disloyal rebels. When the Head Elder proposed killing them, I honestly hoped you would accept.”

[P33]
I had felt the same way. But that had merely been the Head Elder’s clever way of speaking—a suggestion that perhaps we should back down at this point.

[P34]
If Jin Wikyung had pretended to be insane and accepted that proposal, the result would have been obvious.

[P35]
“A bloodbath would have broken out.”

[P36]
“I know. That’s why I held back.”

[P37]
The Jin Family of Taiyuan’s leadership would have split in two and continued fighting until they killed one another. If we lost, we would die. Even if we won, we would suffer tremendous damage.

[P38]
*Maybe that was exactly what the Head Elder wanted.*

[P39]
The Head Elder. An invisible hand.

[P40]
A chill ran down my spine at the thought. It fit the image I had formed of him perfectly.

[P41]
A politician like a hyena, stepping back and waiting for his moment.

[P42]
Jin Wikyung tilted his teacup.

[P43]
“But that is only a guess. We do not know what the Head Elder truly intends. He is still one of the family’s elders, and a powerful ally. Be wary of him, but do not make an enemy of him. For now, we need to overcome the situation rather than distrust everyone around us.”

[P44]
He was telling me to look at the forest, not the trees.

[P45]
The problem was that the forest itself wasn’t exactly in good shape, either.

[P46]
As if he had read my thoughts, Wipeng brought up the subject.

[P47]
“The situation is not good, either. According to our outside sources, rumors that Lee Seogeun was poisoned have begun spreading, and the main family’s reputation is falling.”

[P48]
“In only half a day?”

[P49]
“Yes. All of Shanxi is in an uproar over it.”

[P50]
Concern clouded Jin Wikyung’s face.

[P51]
“That is fast. Far too fast. Someone is definitely behind this.”

[P52]
There was no internet here, and yet rumors had already spread across this vast land. It was certainly strange.

[P53]
*An invisible enemy.*

[P54]
Who could it be? A third faction? A staged act by the Mount Heng Sword Sect?

[P55]
I hoped it was the latter if possible. Nothing was more dangerous than an enemy who remained unseen.

[P56]
“The people are still taking the rumors with a grain of salt, but the other sects…”

[P57]
“Still no replies?”

[P58]
Wipeng lowered his head instead of answering.

[P59]
Immediately after obtaining the information about Lee Seogeun’s poisoning, Jin Wikyung had sent requests for support to the other small and mid-sized sects in Shanxi. But it seemed every one of them had failed.

[P60]
*This keeps getting worse.*

[P61]
*Do I really need to run?*

[P62]
I was looking out the window, thinking that, when—

[P63]
Flap, flap.

[P64]
A pigeon landed on the windowsill with the sound of beating wings.

[P65]
“…It looks like a reply has arrived?”

[P66]
* * *

[P67]
The Jin Family of Taiyuan.

[P68]
As the carriage approached the grand signboard written in magnificent calligraphy and the martial artists standing guard at the main gate with a stern aura, the coachman loosened the reins.

[P69]
“Stop. State your identity and purpose!”

[P70]
The gate guard called out loudly and blocked the carriage. Given the circumstances, there was tension in his voice.

[P71]
More than that—

[P72]
*This isn’t ordinary.*

[P73]
The coachman holding the reins gave off the unmistakable air of a trained martial artist, while the four-horse carriage had both luxury and dignity.

[P74]
*But why does he look familiar?*

[P75]
The coachman, too. The carriage, too. Where had he seen them?

[P76]
The question vanished the moment he saw the coachman’s sharp eyes. That aura, that gaze. This was certainly no ordinary visitor.

[P77]
The gate guard swallowed and spoke again.

[P78]
“Please state your identity and purpose.”

[P79]
The carriage door opened, and a red silk slipper stepped lightly onto the ground.

[P80]
Then a voice as gentle as a spring breeze drifted into the guard’s ear.

[P81]
“I’m from Honghwaru. My name is a secret.”

[P82]
Her face appeared along with her voice.

[P83]
The gate guard’s eyes grew dazed. He wasn’t the only one. Everyone who saw the woman reacted the same way.

[P84]
A vacant voice escaped the gate guard’s mouth.

[P85]
“Ah, a secret… Then what brings you here?”

[P86]
The woman, Wolhwa, answered with a charming smile.

[P87]
“Hmm. I’m here to collect an unpaid tab?”

[P88]
* * *

[P89]
“How have you been? Didn’t you miss me?”

[P90]
I froze halfway to standing.

[P91]
A face I could never forget. And a face that had no business being here.

[P92]
“Wolhwa?”

[P93]
The first NPC I had met in this game. A courtesan at Honghwaru—and my precious little finger. That thing.

[P94]
*Why is noona coming out of there…?*

[P95]
“You remember me after all. Our Young Master Jin.”

[P96]
Wolhwa giggled. She was beautiful, had a beautiful laugh, and when a beautiful woman laughed, she became even more beautiful…

[P97]
*No, this is not the time for that.*

[P98]
I whispered in a tightly restrained voice.

[P99]
“What brings you here? No, never mind. Leave. Get out.”

[P100]
I nudged Wolhwa with my elbow.

[P101]
*This is driving me insane.*

[P102]
Of all times, she had to show up in this atmosphere.

[P103]
The entire family was on high alert. If word got out that I had called for a courtesan, I couldn’t even imagine what would happen to my reputation. Just thinking about it made my vision swim.

[P104]
“Don’t poke me. That tickles.”

[P105]
“I know, so get out quickly. There are other people here. What are you trying to do by suddenly coming here? We’re expecting an important guest, too.”

[P106]
The timing was damn awful, too. I was waiting for a guest from a sect called the Lower District Sect in the Lesser Family Head’s office.

[P107]
Naturally, Jin Wikyung and Wipeng were there with me.

[P108]
“Taekyung.”

[P109]
Jin Wikyung called my name. Without even turning around, I hurriedly waved my hands.

[P110]
“Ah, it’s not what you think. I didn’t call her. She’s leaving now, too. Right?”

[P111]
Wolhwa’s laughter rose in pitch.

[P112]
“Our Young Master Jin is still so adorable. But you guessed wrong. I came here because I have business to attend to.”

[P113]
“Don’t call me ‘our Young Master Jin.’ I’m going to live chastely from today onward. I don’t have any business with you anymore, so get out quickly.”

[P114]
“Hmm. No.”

[P115]
Then there was no helping it. I would have to move her by force.

[P116]
In desperation, I grabbed Wolhwa around the waist and hoisted her up—

[P117]
“Huh?”

[P118]
What the hell? Why won’t she lift?

[P119]
Wolhwa looked slender, but was she so big-boned that she weighed a lot?

[P120]
*That’s bullshit.*

[P121]
What was my Strength stat again? With pure physical strength alone, I could grind a rock into powder. And yet I couldn’t lift one female NPC, which meant—

[P122]
“Taekyung?”

[P123]
I ignored Jin Wikyung’s second call and furtively let go. Then I heightened my Qi Sense.

[P124]
“Ahahahahaha! This is driving me insane!”

[P125]
As Wolhwa laughed herself to death, a Level Window appeared above her head. At the same time, I heard Jin Wikyung call my name for the third time.

[P126]
> **System**
>
> **Lv. 50 Eun Sowol**

[P127]
“Taekyung, greet her. She is the Branch Leader of the Lower District Sect’s Shanxi branch…”

[P128]
Ah. Ahhh.

[P129]
*I want to die.*

[P130]
* * *

[P131]
“Greetings. I am Wolhwa, Branch Leader of the Lower District Sect’s Shanxi branch.”

[P132]
Eun Sowol.

[P133]
No, for now, let’s just call her Wolhwa.

[P134]
She was different from how she had acted until now. Every movement carried the grace and elegance of a noblewoman.

[P135]
“I am Jin Wikyung of the Jin Family of Taiyuan.”

[P136]
“I’m Wipeng.”

[P137]
I kept my mouth shut like mute Samryong,[^1] and Wolhwa flashed me a grin.

[P138]
It was an ominous grin.

[P139]
*Don’t. Don’t smile.*

[P140]
*Don’t talk to me. Please don’t.*

[P141]
“It seems I haven’t been introduced to one person.”

[P142]
Her gaze stung. Someone stepped on my foot beneath the table.

[P143]
I opened my mouth with a feeling like I was coughing up blood.

[P144]
“…I’m Jin Taekyung.”

[P145]
“Yes. I hope we get along too, Young Master Jin.”

[P146]
“Ahem.”

[P147]
With a cough, Jin Wikyung glanced at me.

[P148]
“I didn’t realize you were acquainted with my younger brother.”

[P149]
“He is a regular at our establishment—the Honghwaru in Taiyuan. It also serves as this sect’s Shanxi branch.”

[P150]
“Ah. A regular…”

[P151]
I avoided everyone’s gaze. Wolhwa let out a burst of laughter, then brought up the real subject.

[P152]
“Shall we talk business now?”

[P153]
I had felt it several times before, but she really was a refreshingly direct woman. Jin Wikyung and Wipeng also turned their attention away from me and joined the conversation.

[P154]
“First, allow me to offer my sincere thanks for the Lower District Sect’s assistance.”

[P155]
“Think nothing of it.”

[P156]
“But may I ask why you wish to help our family?”

[P157]
Wolhwa smiled sweetly at Jin Wikyung’s question.

[P158]
“The reason… I will tell you if necessary. First, we are doing this for our sect’s benefit.”

[P159]
“Benefit. What specific compensation do you want?”

[P160]
“Half of the shops and assets owned by the Mount Heng Sword Sect.”

[P161]
“Good.”

[P162]
“My lord!”

[P163]
Wipeng hurriedly stepped forward, but Jin Wikyung paid him no heed.

[P164]
Wolhwa also looked slightly surprised.

[P165]
“You decide quickly.”

[P166]
“Because I have staked everything the family has.”

[P167]
“Has this already been agreed upon?”

[P168]
“I am the Lesser Family Head, and with Father absent, I possess the authority of the acting Family Head.”

[P169]
“I hear the internal opposition is quite fierce. The Elder Council, for example?”

[P170]
“As expected of the Lower District Sect. Your information is fast.”

[P171]
“It cannot be helped. Information is essential for survival in this bleak Murim. We need skills like these to make a living, don’t we?”

[P172]
Watching Wolhwa smile, I suddenly had a thought.

[P173]
*That information. Did I—or rather, did Jin Taekyung—let it slip?*

[P174]
I had wondered where I had heard the name Lower District Sect before. It was an information-gathering sect that appeared regularly in martial-arts novels. In other words, Wolhwa, its Branch Leader, was a veteran information merchant.

[P175]
On top of that, she was an outstanding martial artist at Level 50. A woman like that had disguised herself as a courtesan to meet a guy like Jin Taekyung?

[P176]
*Even a dog would laugh at that.*

[P177]
I stared at Wolhwa.

[P178]
Her beauty was dazzling enough to make me wonder if a goddess had descended. Whenever she smiled, roses came to mind. Only now could I see the sharp thorns hidden beneath all that splendor.

[P179]
Jin Wikyung spoke with a stiff expression.

[P180]
“Then tell us the second reason.”

[P181]
Wolhwa answered with her usual radiant smile.

[P182]
“Because I like Young Master Jin.”

[P183]
“Excuse me?”

[P184]
“He’s young, handsome, well-built, and has such a cute personality.”

[P185]
“…”

[P186]
“…”

[P187]
*How much of that was sincere, and how much was a joke?*

[P188]
[^1]: Samryong is the mute protagonist of a well-known Korean short story; his name literally means “Three Dragons.”
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 19,
  "passed": true,
  "metrics": {
    "source_characters": 5866,
    "translation_characters": 13145,
    "length_ratio": 2.241,
    "source_paragraphs": 185,
    "translation_paragraphs": 187
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
