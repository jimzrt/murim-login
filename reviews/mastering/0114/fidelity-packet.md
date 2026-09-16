# Fidelity Gate — Chapter 114

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
  1|＃114화
  2|
  3|
  4|
  5|항산호 철무백은 철탑처럼 서 있었다.
  6|
  7|뻥 뚫린 입구는 마차 두 대가 지나가고도 남을 만큼 넓었지만 오십여 명의 적풍단은 아무도 발을 내딛지 못했다.
  8|
  9|앞서 나섰던 동료들이 어떻게 죽었는지 똑똑히 봤기 때문이다.
 10|
 11|머리가 터져 죽고, 복부를 뚫려 죽고, 사지가 꺾여서 죽었다. 철무백의 일권(一拳)이 언제, 어떻게 움직였는지 제대로 본 사람은 없었다.
 12|
 13|그렇게 죽은 이가 스물이 넘었다.
 14|
 15|“괴물…….”
 16|
 17|공포에 잠긴 그들을 구원한 것은 뒤에서 들려온 누군가의 중후한 목소리였다.
 18|
 19|“너희들은 이만 가 보거라. 여긴 내가 맡겠다.”
 20|
 21|목소리의 주인, 적풍단주 풍양의 등장에 마적들이 썰물처럼 물러났다. 두 절정 고수는 그제야 서로를 마주했다.
 22|
 23|“다시 뵙소, 철 선배.”
 24|
 25|“도적놈을 후배로 둔 기억은 없는데.”
 26|
 27|“까칠한 건 여전하시구려. 옷깃만 스쳐도 인연이라는데, 선배와 나는 손까지 섞은 사이 아니오?”
 28|
 29|“그랬지. 네놈은 뒤도 안 돌아보고 도망쳤고.”
 30|
 31|“전략적 후퇴라고 해 둡시다. 나도 거기서 철 선배가 등장하실 줄은 몰랐으니까.”
 32|
 33|“내상은 다 나았나?”
 34|
 35|“속이 뜨거워서 며칠 혼났지요. 그래도 죽을 정도는 아니라 염치 불고하고 다시 찾아온 것 아니겠소?”
 36|
 37|“오늘은 뜨거운 정도로 끝나지 않을 게다.”
 38|
 39|“저런, 대화로 푸는 건 어떻겠소? 연세도 꽤 지긋하신 분이 성격이 이리 불같아서야…….”
 40|
 41|풍양의 능청스러운 말에 철무백이 이를 갈았다.
 42|
 43|“대화? 네가 배신하지 않았더라면 천백, 그 친구는 살 수도 있었다.”
 44|
 45|“승산 없는 싸움에 끼어들 정도로 멍청한 놈은 아니라서 말이오.”
 46|
 47|“그것으로 부족해서 소광이마저 죽였느냐?”
 48|
 49|“주제도 모르고 덤비는 어린놈을 살려 줄 만큼 유한 성격도 아니고.”
 50|
 51|풍양이 부드럽게 웃으며 말을 이었다.
 52|
 53|“그 어린놈이 내 처남이 될 줄 알았다면 살려 뒀겠지만 말이오.”
 54|
 55|“이노옴!”
 56|
 57|철무백의 전신에서 용암 같은 기세가 끓어올랐다. 절정 고수의 강대한 열양지기에 지면을 덮은 눈이 녹아내리고 초목이 노랗게 물든다.
 58|
 59|그 광경에 풍양이 탄성을 토해 냈다.
 60|
 61|“역시 대단한 공력이오. 철 선배가 마음만 먹었다면 오늘 내가 상대하는 것은 항산권문(恒山拳門)이 되었겠군.”
 62|
 63|“네놈의 사지를 뽑아 주마.”
 64|
 65|“글쎄, 너무 자신하지 않는 게 좋을 거요.”
 66|
 67|“지난번 같은 요행은 바라지 마라. 오늘은 방패막이로 사용할 놈들도 없으니.”
 68|
 69|풍양이 빙긋 웃었다.
 70|
 71|“내가 수하들을 물린 이유가 뭐겠소?”
 72|
 73|“그건…….”
 74|
 75|철무백은 멈칫했다. 안 그래도 아까부터 풍양의 여유로운 태도가 마음에 걸리던 찰나였다.
 76|
 77|‘무슨 꿍꿍이지?’
 78|
 79|지난번에는 불과 백여 합 만에 내상을 입고 물러났던 풍양이다. 수하들을 방패 삼아 도망쳤던 그가 모두를 물리고 제 발로 찾아왔다는 것은 그만큼 자신이 있단 소린데…….
 80|
 81|“무슨 개수작이냐?”
 82|
 83|“개수작이라니, 호랑이에게 닭 잡는 칼을 쓸 수 없어 직접 나섰을 뿐이오.”
 84|
 85|“네깟 놈 혼자?”
 86|
 87|“안될 것 있겠소?”
 88|
 89|“그럴 리가. 나야 고마울 따름이지.”
 90|
 91|의구심 어린 눈빛으로 풍양을 노려보던 철무백이 주먹을 말아 쥐었다.
 92|
 93|“덕분에 일이 쉽게 끝나게 됐으니 말이다.”
 94|
 95|후우웅.
 96|
 97|말이 끝남과 동시에 뜨거운 열풍이 바로 앞으로 들이닥쳤다. 풍양은 숨을 삼키며 가슴을 노리고 날아드는 붉은 권기(拳氣)를 향해 곡도를 휘둘렀다.
 98|
 99|쾅! 쾅쾅!
100|
101|두 절정 고수의 격돌. 연달아 터지는 굉음과 함께 몰아친 바람이 눈 덮인 바닥을 휩쓸었다.
102|
103|높이 솟구친 눈 더미 아래, 한 사람이 비틀거리며 물러났다.
104|
105|“으음.”
106|
107|풍양이 침음을 삼키며 찢어진 손아귀를 바라봤다. 볼썽사납게 병장기를 놓치는 것은 면했으나 힘의 차이는 확실했다.
108|
109|“역시 강하구려.”
110|
111|철무백이 풍양을 향해 걸음을 내디디며 대답했다.
112|
113|“후회해도 늦었다.”
114|
115|“이하 동문이오.”
116|
117|“주둥이부터 찢어 놔야겠군.”
118|
119|쐐애애액!
120|
121|철무백은 호랑이 같은 몸놀림으로 달려들었다.
122|
123|오래전 실전되었다고 알려진 수라멸권(修羅滅拳)의 강맹한 초식들이 풍양을 향해 쏟아졌다.
124|
125|콰과광!
126|
127|
128|
129|* * *
130|
131|
132|
133|성벽에서는 치열한 혈투가 벌어지고 있었다. 자그마치 네 배에 달하는 병력의 차이가 있지만 항산검문의 무인들은 물러서지 않았다.
134|
135|“물러서면 죽음뿐이다!”
136|
137|“마적 놈들에게 고향을 뺏길 셈이냐!”
138|
139|“놈들에게 죽은 사형제들의 원수를 갚자!”
140|
141|서걱, 푹!
142|
143|“크아악!”
144|
145|“미, 밀지 마!”
146|
147|적풍단의 마적들은 혼란에 빠졌다. 앞서 당한 화공의 영향과 또 다른 함정이 있을지 모른다는 두려움이 발목을 잡았다.
148|
149|그들은 자신들과는 반대로 눈이 뒤집혀 달려드는 항산검문 무인들의 파죽지세에 속수무책으로 썰려 나갔다.
150|
151|“도망치지 마라!”
152|
153|“물러서는 놈들은 내 손에 뒈질 줄 알아!”
154|
155|조장 격인 마적들이 목청껏 외쳤지만 혼란을 수습하는 건 역부족이었다. 오히려 그들 또한 어디서 날아왔는지 모를 화살에 목숨을 헌납해야 했다.
156|
157|푸푹!
158|
159|“크륵. 커어어…….”
160|
161|“조, 조장!”
162|
163|이소월은 가장 높은 망루에 서서 쉼 없이 활시위를 당겼다.
164|
165|그녀의 곁에는 항산검문의 무인 중 가장 활을 잘 다루는 다섯 명의 궁수가 함께했다.
166|
167|퉁! 푹!
168|
169|시위가 당겨질 때마다 한 명의 마적들이 쓰러진다. 조장, 혹은 그 이상으로 보이는 자들이 최우선으로 노려야 할 표적이었다.
170|
171|‘한 놈이라도 더, 더.’
172|
173|그러나 전황은 생각 이상으로 어렵게 흘러가고 있었다.
174|
175|처음부터 적은 병력으로 전투에 임했던 항산검문의 무인들은 빠른 속도로 지쳐 갔고, 이내 하나둘씩 눈먼 칼날에 목숨을 잃고 있었다.
176|
177|반면 마적들은 점차 혼란에서 빠져나오는 중이었다.
178|
179|“정신 차려! 항산검문 놈들은 몇 안 돼!”
180|
181|“이놈들만 죽이면 우리의 승리다!”
182|
183|더 이상 잃을 게 없는 항산검문의 무인들 역시 불리한 전황에도 아랑곳하지 않고 필사적으로 맞섰다.
184|
185|“죽여라!”
186|
187|서걱, 서걱, 서걱!
188|
189|그러나 마적 하나를 베면 둘이, 둘을 베면 셋이 나타나 빈자리를 메웠다.
190|
191|“헉, 허억!”
192|
193|정신없이 검을 휘두르는 항산검문의 무인을, 사방에서 튀어나온 대여섯 개의 병장기가 난도질한다.
194|
195|서걱! 푸푸푹!
196|
197|목, 가슴, 복부……. 전신이 베이고 꿰뚫린 채 비명 한 번 못 지르고 죽는 무인들이 곳곳에서 속출했다.
198|
199|기세가 오른 적풍단의 마적들은 쉬지 않고 몰아쳤다. 어느새 성벽의 절반이 적들로 가득 찼다.
200|
201|“하아, 하아.”
202|
203|퉁, 퉁, 퉁!
204|
205|이소월은 젖 먹던 힘까지 끌어모아 활시위를 당겼다. 섬섬옥수 같던 손가락과 악문 잇새에서는 피가 흘렀고 바짝 말라붙은 입 안에서는 단내가 풀풀 풍겼다.
206|
207|“저기다!”
208|
209|쉴 새 없이 화살을 쏘아 댄 탓에 결국 얼마 지나지 않아 위치가 발각됐다. 이십여 명의 마적들이 방패를 세우고 망루로 돌격해 오자 다급한 외침이 터져 나왔다.
210|
211|“문주!”
212|
213|“피하셔야 합니다! 놈들이 오고 있습니다!”
214|
215|공성전이 시작되고 이제 세 시진. 취미 삼아 활을 수련했을 뿐, 무인이 아닌 이소월의 체력은 한계에 다다른 지 오래였다.
216|
217|그러나 그녀는 멈추지 않았다. 덜덜 떨리는 가느다란 팔뚝에 억지로 힘을 주고 다음 표적을 찾았다.
218|
219|‘피해? 어디로?’
220|
221|평생을 이곳에서 살았다. 항산검문은 이소월에게 있어 고향이자 생애 마지막 순간까지 지켜야 할 무언가였다.
222|
223|그것은 지금까지도 최후의 항전을 이어 가는 무인들에게도 마찬가지였다.
224|
225|“놈들을 막아라!”
226|
227|“결코 문주께 보내서는 안 된다!”
228|
229|필사적인 외침이 무색하게도 이미 성벽은 점령당한 뒤였다.
230|
231|살아남은 항산검문의 무인들은 망루로 퇴각했다. 그러나 일백은 족히 넘어 보이는 마적들이 사방에서 조여 오고 있었다.
232|
233|적들이 들고 있는 횃불 사이로 살기와 욕망으로 번들거리는 눈동자들이 비친다.
234|
235|“이 망할 년놈들이 감히…….”
236|
237|“한 놈도 빠짐없이 갈기갈기 찢어 개밥으로 던져 주마.”
238|
239|둥글게 망루를 포위한 마적들의 살기가 피부를 찔렀다.
240|
241|모두 절망에 빠진 그때, 이소월이 돌연 하늘을 향해 활시위를 당겼다.
242|
243|후우웅.
244|
245|불의 꼬리를 늘어트리며 떨어지는 한 발의 화시(火矢)의 목적지는 어둠에 잠긴 성문.
246|
247|그것은 한 사람을 찾기 위한 불빛이었다.
248|
249|‘철 숙부.’
250|
251|항산호 철무백. 그가 항산검문의 마지막 희망이다.
252|
253|불화살이 밝힌 불빛 아래로 한 사람이 걸어 나온 것은 그때였다.
254|
255|저벅. 저벅.
256|
257|“이제 와서 말하긴 뭣하지만…….”
258|
259|단 한 번 들었을 뿐이지만 꿈에서도 잊지 못하는 목소리.
260|
261|차마 쳐다보지 못하고 눈을 감는 이소월에게, 풍양이 활짝 웃어 보였다.
262|
263|“나와 혼인해 줘야겠소.”
264|
265|
266|
267|* * *
268|
269|
270|
271|사냥꾼 철무백이 항산의 호랑이가 될 수 있었던 이유는 기연(奇緣)을 만났기 때문이다.
272|
273|광활한 항산 산맥의 어느 산자락에서 늑대를 추적하던 그는 절벽 사이 숨겨져 있던 비동(秘洞)으로 추락했고, 그곳에서 은거 고수가 남긴 비급과 영약을 발견했다.
274|
275|
276|
277|‘나는 돌아간다. 반드시 살아 돌아간다!’
278|
279|
280|
281|철무백은 살기 위해 무공을 익혔다. 비동에 있던 벽곡단이 떨어지자 절벽 사이에 난 풀을 뜯어 먹거나 박쥐를 잡아먹으며 수련했다.
282|
283|자그마치 삼 년 만에 맨손으로 절벽을 기어올라 마을로 돌아간 그를 기다리고 있던 것은 폐허가 된 집, 그리고 아내와 자식의 죽음이었다.
284|
285|
286|
287|‘소식이 끊긴 지 두어 달쯤 됐나? 평소 자네 내자를 눈독 들이고 있었던 황가 놈이…….’
288|
289|
290|
291|정신을 차렸을 때는 이미 마을의 대지주와 그의 하인들을 모두 때려죽인 후였다.
292|
293|원수를 갚은 철무백은 다시 비동으로 돌아가 무공을 수련했다. 그건 스스로에 대한 채찍질이었고 가족에 대한 속죄였다.
294|
295|그렇게 시간이 얼마나 흘렀을까, 어느새 철무백은 항산의 호랑이라 불리고 있었다.
296|
297|하지만…….
298|
299|“후욱, 호랑이가, 울겠군.”
300|
301|철무백은 거칠게 숨을 몰아쉬었다. 형형하던 눈빛은 먹구름이 낀 것처럼 흐렸고 수염은 피로 흠뻑 젖었다.
302|
303|‘어서 가야 하는데, 놈을 막아야 하는데…….’
304|
305|그러나 그에게 남아 있는 것은 의지뿐, 사지가 부러진 몸은 이미 통제를 벗어났다. 항산호(恒山虎)라는 별호가 아깝지 않은 무공을 펼쳤건만 풍양을 꺾을 수는 없었다.
306|
307|‘그놈이 도대체 어떻게.’
308|
309|결과는 분명해 보였다. 풍양은 이제 간신히 도기(刀氣)를 만들어 내는 절정 초입의 경지였고 철무백은 완숙한 경지에 오른 절정 고수였다.
310|
311|바람 앞의 촛불처럼 위태롭던 풍양이 돌변한 것은 품에서 정체불명의 목곽을 꺼낸 후였다.
312|
313|‘붉은 단환. 맞아, 분명히 그거였어.’
314|
315|암기인가 싶어 물러난 것이 실수였다. 단환을 꿀꺽 삼킨 풍양은 더 이상 철무백이 알던 일개 마적단의 우두머리가 아니었다.
316|
317|‘어찌 인간이 그토록 강해질 수 있단 말인가.’
318|
319|풍양의 움직임을 떠올린 철무백의 눈가가 파르르 떨렸다.
320|
321|열 번, 백 번을 다시 겨룬다 해도 이길 수 없을 것 같은 아득한 격차. 한순간에 전세를 역전시킨 풍양은 그의 사지를 부러뜨리고 막대한 내상을 입힌 다음 떠났다.
322|
323|
324|
325|‘당장은 살려 주지. 이번 혼인의 예물로 당신의 무공 구결을 받고 싶어졌거든.’
326|
327|
328|
329|떠나기 전, 풍양이 남긴 말을 떠올린 철무백의 눈가가 붉게 물들었다. 수라멸권은 일인전승, 비인부전의 무공이다.
330|
331|풍양에게 넘기느니 자결을 택하겠지만 딸처럼, 손녀처럼 아끼는 이소월이 마음에 걸렸다.
332|
333|‘도대체 이를 어찌해야 한단 말인가.’
334|
335|철무백이 먹먹한 심정으로 하늘을 바라보던 그 순간이었다.
336|
337|두두두!
338|
339|멀리서 들려오던 말발굽 소리가 점점 가까워지더니, 철무백의 발치에서 우뚝 멈췄다. 휘영청 밝은 달 아래, 그를 내려다보는 네 쌍의 시선이 있었다.
340|
341|“적풍단 애들은 정년도 없나. 웬 노인네까지 마적질을.”
342|
343|“진 공자, 항산호 철무백 대협이에요.”
344|
345|“헉, 죄송합니다. 야, 무진아. 얼른 사과드리지 않고 뭐 해.”
346|
347|“실수는 조장이 했는데 왜 제가…….”
348|
349|빡!
350|
351|“할아버지, 아니 대협. 괜찮으세요?”
352|
353|철무백은 대답 대신 청년의 가슴팍을 뚫어져라 바라봤다.
354|
355|남색 무복에 새겨진 한 글자.
356|
357|진(進).
358|
359|“태원……진가?”
360|
361|“어, 알아보시네?”
362|
363|청년, 진태경이 씩 웃었다.
```

## Assembled English

```markdown
[P1]
# Chapter 114

[P2]
The Tiger of Mount Heng, Cheol Mubaek, stood like an iron tower.

[P3]
The entrance gaped wide enough for two carriages to pass through side by side, yet not one of the fifty-odd mounted bandits of the Red Wind Band dared set foot inside.

[P4]
They had seen clearly how the men who went ahead of them had died.

[P5]
Some had died with their heads blown apart. Others had been pierced through the abdomen or killed when their limbs were broken. No one had properly seen when or how Cheol Mubaek’s fist moved.

[P6]
More than twenty had died that way.

[P7]
“Monster…”

[P8]
A deep voice from behind rescued the mounted bandits, who were paralyzed with fear.

[P9]
“You may leave now. I’ll handle this place.”

[P10]
At the appearance of the voice’s owner, Pung Yang, the Red Wind Band Leader, the mounted bandits retreated like the tide going out. Only then did the two Peak masters face each other.

[P11]
“Good to see you again, Senior Cheol.”

[P12]
“I don’t recall ever taking a bandit as my junior.”

[P13]
“You’re still as prickly as ever. They say even brushing sleeves creates a bond, and you and I have traded blows, haven’t we?”

[P14]
“We did. Then you ran away without even looking back.”

[P15]
“Let’s call it a strategic retreat. I didn’t expect you to show up there either, Senior Cheol.”

[P16]
“Have your internal injuries healed?”

[P17]
“My insides were burning, so I had a rough few days. But it wasn’t enough to kill me, which is why I’ve shamelessly come back.”

[P18]
“Today, it won’t end with mere heat.”

[P19]
“Oh, dear. How about we settle this through conversation? For a man of your age to have such a fiery temper…”

[P20]
At Pung Yang’s shameless remark, Cheol Mubaek ground his teeth.

[P21]
“Conversation? If you hadn’t betrayed us, Lee Cheonbaek, my friend, might have lived.”

[P22]
“I’m not stupid enough to join a fight with no chance of winning.”

[P23]
“As if that weren’t enough, you killed Lee Seogwang too?”

[P24]
“I’m not softhearted enough to spare a brat who came at me without knowing his place.”

[P25]
Pung Yang smiled gently and continued.

[P26]
“If I’d known that brat would become my brother-in-law, I might have spared him.”

[P27]
“You bastard!”

[P28]
A lava-like aura boiled up from every inch of Cheol Mubaek’s body. Under the formidable Scorching Yang Qi of a Peak master, the snow blanketing the ground melted away, and the vegetation turned yellow.

[P29]
Pung Yang exclaimed in admiration at the sight.

[P30]
“Your internal energy is remarkable, as expected. If Senior Cheol had only set his mind to it, I’d be facing the Mount Heng Fist Sect today.”

[P31]
“I’ll rip off your limbs.”

[P32]
“Still, you shouldn’t be too confident.”

[P33]
“Don’t count on the same stroke of luck as last time. You have no one to use as a shield today.”

[P34]
Pung Yang smiled faintly.

[P35]
“Why do you think I sent my men away?”

[P36]
“That…”

[P37]
Cheol Mubaek hesitated. Pung Yang’s relaxed attitude had been bothering him for some time.

[P38]
*What is he plotting?*

[P39]
Last time, Pung Yang had withdrawn after suffering internal injuries in barely a hundred exchanges. The fact that the man who had used his subordinates as shields to escape had sent everyone away and come here of his own accord meant that he was confident enough to do so…

[P40]
“What dirty trick are you planning?”

[P41]
“A dirty trick? I simply couldn’t use a chicken-killing knife on a tiger, so I stepped in myself.”

[P42]
“You? Alone?”

[P43]
“Why not?”

[P44]
“There’s no way. I’m grateful, if anything.”

[P45]
Cheol Mubaek glared at Pung Yang suspiciously and clenched his fists.

[P46]
“Thanks to you, this will be over easily.”

[P47]
Whoooosh!

[P48]
The instant he finished speaking, a scorching gale rushed straight toward Pung Yang. Pung Yang swallowed a breath and swung his curved saber at the red fist energy flying toward his chest.

[P49]
Boom! Boom-boom!

[P50]
The two Peak masters collided. Roaring explosions rang out one after another, and the resulting wind swept across the snow-covered ground.

[P51]
Beneath a mound of snow that had leaped high into the air, one man staggered backward.

[P52]
“Ugh.”

[P53]
Pung Yang swallowed a groan and looked at his torn palm. He had avoided the disgrace of dropping his weapon, but the difference in strength was undeniable.

[P54]
“You’re still as strong as ever.”

[P55]
Cheol Mubaek stepped toward him and answered.

[P56]
“It’s too late for regrets.”

[P57]
“My thoughts exactly.”

[P58]
“I’ll start by tearing that mouth apart.”

[P59]
Fwoooooosh!

[P60]
Cheol Mubaek lunged forward with the movements of a tiger.

[P61]
The ferocious forms of the Shura Annihilating Fist, a martial art thought to have been lost long ago, poured down upon Pung Yang.

[P62]
Kwa-gwa-gwang!

[P63]
* * *

[P64]
A fierce bloody battle was raging along the fortress walls. Despite facing a four-to-one disadvantage in numbers, the martial artists of the Mount Heng Sword Sect refused to retreat.

[P65]
“Retreat, and all that awaits us is death!”

[P66]
“Are you going to let those mounted-bandit bastards steal our home?”

[P67]
“Let’s avenge the martial brothers they killed!”

[P68]
Slash! Thrust!

[P69]
“Aaargh!”

[P70]
“D-don’t push!”

[P71]
The mounted bandits of the Red Wind Band had fallen into confusion. The effects of the earlier fire attack and the fear that another trap might be waiting held them back.

[P72]
In stark contrast, the martial artists of the Mount Heng Sword Sect charged at them wild-eyed. The mounted bandits were helpless against their unstoppable momentum and were cut down one after another.

[P73]
“Don’t run away!”

[P74]
“Any bastard who retreats dies by my hand!”

[P75]
The mounted-bandit captains shouted at the top of their lungs, but they were unable to restore order. Instead, they too had to surrender their lives to arrows that seemed to fly out of nowhere.

[P76]
Thwack!

[P77]
“Ghk. Gaaah…”

[P78]
“C-Captain!”

[P79]
Lee Seowol stood atop the highest watchtower, drawing her bowstring without pause.

[P80]
Beside her were the five finest archers among the Mount Heng Sword Sect’s martial artists.

[P81]
Twung! Thud!

[P82]
Every time a bowstring was drawn, a mounted bandit fell. Captains, or those who appeared to rank even higher, were their highest-priority targets.

[P83]
*One more. One more.*

[P84]
But the battle was going worse than expected.

[P85]
The martial artists of the Mount Heng Sword Sect had entered the battle with fewer troops from the very beginning. They grew exhausted at an alarming rate, and before long, one or two at a time began losing their lives to stray blades.

[P86]
The mounted bandits, meanwhile, were gradually recovering from their confusion.

[P87]
“Get a grip! There aren’t many of these Mount Heng Sword Sect bastards!”

[P88]
“If we kill these men, victory is ours!”

[P89]
The martial artists of the Mount Heng Sword Sect had nothing left to lose. They fought desperately, heedless of the odds against them.

[P90]
“Kill them!”

[P91]
Slash! Slash! Slash!

[P92]
But every time one mounted bandit was cut down, two more appeared to fill the gap. When two were cut down, three took their place.

[P93]
“Gasp, gasp!”

[P94]
A martial artist of the Mount Heng Sword Sect swung his sword frantically, only to be hacked apart by five or six weapons that sprang at him from every direction.

[P95]
Slash! Thud-thud-thud!

[P96]
Neck, chest, abdomen… Martial artists were cut and pierced all over, dying without even having time to scream. Their bodies fell in growing numbers.

[P97]
The mounted bandits of the Red Wind Band, their momentum rising, continued pressing the attack without pause. Before anyone realized it, half the fortress wall was packed with enemies.

[P98]
“Haa, haa.”

[P99]
Twung! Twung! Twung!

[P100]
Lee Seowol summoned every last bit of strength she had and drew her bowstring. Blood ran from her once-delicate fingers and between her clenched teeth, while her parched mouth reeked of a sickly sweetness.

[P101]
“There!”

[P102]
After firing arrows without rest, her position was discovered before long. When about twenty mounted bandits raised their shields and charged toward the watchtower, desperate shouts rang out.

[P103]
“Sect Leader!”

[P104]
“You must get away! They’re coming!”

[P105]
Three shichen had passed since the siege began. Lee Seowol had only practiced archery as a hobby. She was no martial artist, and her Stamina had reached its limit long ago.

[P106]
But she did not stop. She forced strength into her thin, trembling arms and searched for her next target.

[P107]
*Get away? Where would I go?*

[P108]
She had lived here her entire life. To Lee Seowol, the Mount Heng Sword Sect was both her hometown and something she had to protect until the final moment of her life.

[P109]
The same was true of the martial artists still making their last stand.

[P110]
“Stop them!”

[P111]
“Never let them reach the Sect Leader!”

[P112]
Their desperate cries were in vain. The fortress walls had already been overrun.

[P113]
The surviving martial artists of the Mount Heng Sword Sect retreated to the watchtower. But well over a hundred mounted bandits were closing in from every direction.

[P114]
Eyes gleaming with killing intent and desire shone between the torches held by the advancing enemies.

[P115]
“You damned bastards dare…”

[P116]
“I’ll tear every last one of you apart and throw the pieces to the dogs.”

[P117]
The killing intent of the mounted bandits surrounding the watchtower in a circle stabbed at their skin.

[P118]
Just as everyone was falling into despair, Lee Seowol suddenly drew her bowstring toward the sky.

[P119]
Whoooosh.

[P120]
Trailing a tail of flame, a single fire arrow descended toward the gate shrouded in darkness.

[P121]
It was a light meant to find one person.

[P122]
*Uncle Cheol.*

[P123]
The Tiger of Mount Heng, Cheol Mubaek.

[P124]
He was the Mount Heng Sword Sect’s final hope.

[P125]
That was when a man walked out beneath the light revealed by the fire arrow.

[P126]
Clomp. Clomp.

[P127]
“I suppose it’s a little late to say this now…”

[P128]
Lee Seowol had heard that voice only once, but she could never forget it, not even in her dreams.

[P129]
Unable to bring herself to look at him, she closed her eyes.

[P130]
Pung Yang beamed at her.

[P131]
“You’ll have to marry me.”

[P132]
* * *

[P133]
The hunter Cheol Mubaek had become the Tiger of Mount Heng because of a fortuitous encounter.

[P134]
While tracking a wolf on a mountainside in the vast Mount Heng range, he fell into a hidden cave between the cliffs. There, he discovered a martial arts manual and an elixir left behind by a reclusive master.

[P135]
*I’m going back. I’m going back alive, no matter what!*

[P136]
Cheol Mubaek learned martial arts to survive. When the fasting pills in the hidden cave ran out, he tore up grass growing between the cliffs or caught bats to eat as he trained.

[P137]
After no less than three years, he climbed the cliff with his bare hands and returned to the village.

[P138]
What awaited him was his home in ruins—and the deaths of his wife and child.

[P139]
*Had it been two months or so since we last heard from you? That bastard Hwang, who’d always had his eye on your wife…*

[P140]
By the time Cheol Mubaek came to his senses, he had already beaten the village’s great landowner and all his servants to death.

[P141]
After avenging his family, Cheol Mubaek returned to the hidden cave and resumed his martial arts training. It was a whip he used against himself, and atonement for his family.

[P142]
How much time had passed like that?

[P143]
Before he knew it, Cheol Mubaek was being called the Tiger of Mount Heng.

[P144]
But…

[P145]
“Huff. Even a tiger would cry.”

[P146]
Cheol Mubaek panted harshly. His once-brilliant eyes were clouded as if by dark clouds, and his beard was drenched in blood.

[P147]
*I have to hurry. I have to stop that bastard…*

[P148]
But all he had left was his will. With all four limbs broken, his body had already slipped beyond his control. He had displayed martial arts worthy of the title Tiger of Mount Heng, yet he still could not defeat Pung Yang.

[P149]
*How in the world did that bastard…?*

[P150]
The result seemed obvious. Pung Yang had only just entered the Peak realm, barely capable of creating blade qi, while Cheol Mubaek was a Peak master who had reached a mature realm stage.

[P151]
Pung Yang had been as precarious as a candle in the wind. Then he had suddenly changed after pulling an unidentified wooden case from inside his robes.

[P152]
*The red pill. Yes, that was definitely it.*

[P153]
Cheol Mubaek had made a mistake by retreating because he thought it might be a hidden weapon. After Pung Yang gulped down the pill, he was no longer the mere leader of a mounted-bandit group Cheol Mubaek had known.

[P154]
*How can a human being become that strong?*

[P155]
Cheol Mubaek’s eyes trembled as he recalled Pung Yang’s movements.

[P156]
The gap between them was so vast that it seemed impossible to win, even if they fought ten or a hundred more times. Pung Yang had overturned the battle in an instant, broken all four of Cheol Mubaek’s limbs, inflicted massive internal injuries, and then left.

[P157]
*I’ll let you live for now. I’ve decided I want the formula for your martial art as a wedding gift.*

[P158]
Cheol Mubaek’s eyes reddened as he recalled Pung Yang’s parting words.

[P159]
The Shura Annihilating Fist was a martial art passed down to a single successor and never taught to outsiders.

[P160]
He would choose suicide rather than hand it over to Pung Yang, but Lee Seowol—whom he cherished like a daughter and a granddaughter—troubled him.

[P161]
*What on earth am I supposed to do?*

[P162]
Cheol Mubaek was staring at the sky with a heavy heart when it happened.

[P163]
Thud-thud-thud-thud!

[P164]
The sound of hooves in the distance drew closer and closer before stopping abruptly at his feet.

[P165]
Beneath the brilliantly shining moon, four pairs of eyes looked down at him.

[P166]
“Doesn’t the Red Wind Band have a retirement age? Why is an old geezer still out here playing bandit?”

[P167]
“Young Master Jin, that’s Great Hero Cheol Mubaek, the Tiger of Mount Heng.”

[P168]
“Gah! I’m sorry. Hey, Mujin. Hurry up and apologize. What are you waiting for?”

[P169]
“You’re the one who made the mistake, Captain. Why should I…?”

[P170]
Smack!

[P171]
“Grandpa—no, Sir. Are you all right?”

[P172]
Instead of answering, Cheol Mubaek stared intently at the young man’s chest.

[P173]
A single character was embroidered on his navy martial robe.

[P174]
進.

[P175]
“Taiyuan… the Jin Family?”

[P176]
“Oh, you recognize it?”

[P177]
The young man, Jin Taekyung, grinned.
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
# Chapter 114

[P2]
The Tiger of Mount Heng, Cheol Mubaek, stood like an iron tower.

[P3]
The entrance gaped wide enough for two carriages to pass through side by side, yet not one of the fifty-odd mounted bandits of the Red Wind Band dared set foot inside.

[P4]
They had seen clearly how the men who went ahead of them had died.

[P5]
Some had died with their heads blown apart. Others had been pierced through the abdomen or killed when their limbs were broken. No one had properly seen when or how Cheol Mubaek’s fist moved.

[P6]
More than twenty had died that way.

[P7]
“Monster…”

[P8]
A deep voice from behind rescued the mounted bandits, who were paralyzed with fear.

[P9]
“You’ve done enough. Go on now. I’ll handle this place.”

[P10]
At the appearance of the voice’s owner, Pung Yang, the Red Wind Band Leader, the mounted bandits retreated like the tide going out. Only then did the two Peak masters face each other.

[P11]
“Good to see you again, Senior Cheol.”

[P12]
“I don’t recall ever taking a bandit as a junior.”

[P13]
“You’re still as prickly as ever. They say even brushing sleeves with someone creates a connection, and you and I have crossed hands, haven’t we?”

[P14]
“We did. Then you ran away without even looking back.”

[P15]
“Let’s call it a strategic retreat. I didn’t expect Senior Cheol to show up there, either.”

[P16]
“Are your internal injuries healed?”

[P17]
“My insides were burning, so I had a rough few days. But it wasn’t enough to kill me, which is why I’ve come back despite my shame.”

[P18]
“Today, it won’t end with mere heat.”

[P19]
“Oh, dear. How about we settle this through conversation? For a man of your age to have such a fiery temper…”

[P20]
At Pung Yang’s shameless remark, Cheol Mubaek ground his teeth.

[P21]
“Conversation? If you hadn’t betrayed us, Lee Cheonbaek, my friend, might have lived.”

[P22]
“I’m not stupid enough to join a fight with no chance of winning.”

[P23]
“As if that weren’t enough, you killed Lee Seogwang too?”

[P24]
“I’m not softhearted enough to spare a brat who came at me without knowing his place.”

[P25]
Pung Yang smiled gently and continued.

[P26]
“If I’d known that brat would become my brother-in-law, I might have spared him.”

[P27]
“You bastard!”

[P28]
A lava-like aura boiled up from every inch of Cheol Mubaek’s body. Under the formidable Scorching Yang Qi of a Peak master, the snow blanketing the ground melted away, and the vegetation turned yellow.

[P29]
Pung Yang let out an exclamation at the sight.

[P30]
“Your internal energy really is remarkable. If Senior Cheol had only set his mind to it, the opponent I faced today would have been the Mount Heng Fist Sect.”

[P31]
“I’ll tear your limbs from your body.”

[P32]
“Still, you shouldn’t be too confident.”

[P33]
“Don’t expect the same stroke of luck as last time. Today, you won’t have anyone to use as a shield.”

[P34]
Pung Yang smiled faintly.

[P35]
“Why do you think I sent my men away?”

[P36]
“That…”

[P37]
Cheol Mubaek hesitated. Pung Yang’s relaxed attitude had been bothering him for some time.

[P38]
*What is he plotting?*

[P39]
Last time, Pung Yang had withdrawn after suffering internal injuries in barely a hundred exchanges. The fact that the man who had used his subordinates as shields to escape had sent everyone away and come here of his own accord meant that he was confident enough to do so…

[P40]
“What kind of dirty trick are you planning?”

[P41]
“A dirty trick? I simply couldn’t use a chicken-killing knife on a tiger, so I stepped in myself.”

[P42]
“You? Alone?”

[P43]
“Is there any reason I can’t?”

[P44]
“There’s no way. I’m grateful, if anything.”

[P45]
Cheol Mubaek glared at Pung Yang suspiciously and clenched his fists.

[P46]
“Thanks to you, this will be over easily.”

[P47]
Whoooosh!

[P48]
The instant he finished speaking, a scorching gale rushed straight toward Pung Yang. Pung Yang swallowed a breath and swung his curved saber at the red fist energy flying toward his chest.

[P49]
Boom! Boom-boom!

[P50]
The two Peak masters collided. Roaring explosions rang out one after another, and the resulting wind swept across the snow-covered ground.

[P51]
Beneath a mound of snow that had leaped high into the air, one man staggered backward.

[P52]
“Ugh.”

[P53]
Pung Yang swallowed a groan and looked at his torn palm. He had avoided the disgrace of dropping his weapon, but the difference in strength was undeniable.

[P54]
“You’re still as strong as ever.”

[P55]
Cheol Mubaek stepped toward him and answered.

[P56]
“You’ll regret this, but it’s already too late.”

[P57]
“I feel the same way.”

[P58]
“I’ll have to tear that mouth of yours apart first.”

[P59]
Fwoooooosh!

[P60]
Cheol Mubaek lunged forward with the movements of a tiger.

[P61]
The fierce forms of the long-lost Shura Annihilating Fist poured down upon Pung Yang.

[P62]
Kwa-gwa-gwang!

[P63]
* * *

[P64]
A fierce bloody battle was raging along the fortress walls. Despite facing a four-to-one disadvantage in numbers, the martial artists of the Mount Heng Sword Sect refused to retreat.

[P65]
“Retreat, and all that awaits us is death!”

[P66]
“Are you going to let those mounted-bandit bastards take our home from us?”

[P67]
“Let’s avenge the martial brothers they killed!”

[P68]
Slice! Thrust!

[P69]
“Aaargh!”

[P70]
“D-don’t push me!”

[P71]
The mounted bandits of the Red Wind Band had fallen into confusion. The effects of the earlier fire attack and the fear that another trap might be waiting held them back.

[P72]
In stark contrast, the martial artists of the Mount Heng Sword Sect charged at them wild-eyed. The mounted bandits were helpless against their unstoppable momentum and were cut down one after another.

[P73]
“Don’t run away!”

[P74]
“Any bastard who retreats dies by my hand!”

[P75]
The mounted bandits who served as squad leaders shouted at the top of their lungs, but they were unable to restore order. Instead, they too had to surrender their lives to arrows that seemed to fly out of nowhere.

[P76]
Thwack!

[P77]
“Ghk. Gaaah…”

[P78]
“Squad Leader!”

[P79]
Lee Seowol stood atop the highest watchtower, drawing her bowstring without pause.

[P80]
Beside her were the five best archers among the martial artists of the Mount Heng Sword Sect.

[P81]
Twung! Thud!

[P82]
Every time a bowstring was drawn, a mounted bandit fell. Squad leaders, or those who appeared to rank even higher, were their highest-priority targets.

[P83]
*One more. One more.*

[P84]
But the battle was unfolding more harshly than expected.

[P85]
The martial artists of the Mount Heng Sword Sect had entered the battle with fewer troops from the very beginning. They grew exhausted at an alarming rate, and before long, one or two at a time began losing their lives to stray blades.

[P86]
The mounted bandits, meanwhile, were gradually recovering from their confusion.

[P87]
“Get a grip! There aren’t many of these Mount Heng Sword Sect bastards!”

[P88]
“If we kill these men, victory is ours!”

[P89]
The martial artists of the Mount Heng Sword Sect had nothing left to lose. They fought desperately, disregarding their disadvantage.

[P90]
“Kill them!”

[P91]
Slice! Slice! Slice!

[P92]
But every time one mounted bandit was cut down, two more appeared to fill the gap. When two were cut down, three took their place.

[P93]
“Gasp, gasp!”

[P94]
A martial artist of the Mount Heng Sword Sect swung his sword frantically, only to be hacked apart by five or six weapons that sprang at him from every direction.

[P95]
Slice! Thud-thud-thud!

[P96]
His neck, chest, abdomen… Martial artists were cut and pierced all over, dying without even having time to scream. Their bodies fell in growing numbers.

[P97]
The mounted bandits of the Red Wind Band, their momentum rising, continued pressing the attack without pause. Before anyone realized it, half the fortress wall was packed with enemies.

[P98]
“Haa, haa.”

[P99]
Twung! Twung! Twung!

[P100]
Lee Seowol summoned every last bit of strength she had and drew her bowstring. Blood ran from her once-delicate fingers and between her clenched teeth, while the dry inside of her mouth reeked of a sickly sweetness.

[P101]
“There!”

[P102]
After firing arrows without rest, her position was discovered before long. When about twenty mounted bandits raised their shields and charged toward the watchtower, desperate shouts rang out.

[P103]
“Sect Leader!”

[P104]
“You have to get away! They’re coming!”

[P105]
Three shichen—six hours—had passed since the siege began. Lee Seowol had only practiced archery as a hobby. She was not a martial artist, and her Stamina had reached its limit long ago.

[P106]
But she did not stop. She forced strength into her thin, trembling arms and searched for her next target.

[P107]
*Escape? Where would I go?*

[P108]
She had lived here her entire life. To Lee Seowol, the Mount Heng Sword Sect was both her hometown and something she had to protect until the final moment of her life.

[P109]
The same was true for the martial artists who continued their last stand.

[P110]
“Stop them!”

[P111]
“Never let them reach the Sect Leader!”

[P112]
Their desperate cries were futile. The fortress walls had already been overrun.

[P113]
The surviving martial artists of the Mount Heng Sword Sect retreated to the watchtower. But more than a hundred mounted bandits were closing in from every direction.

[P114]
Eyes gleaming with killing intent and desire shone between the torches held by the advancing enemies.

[P115]
“You damned bastards dare…”

[P116]
“I’ll tear every last one of you limb from limb and throw you to the dogs!”

[P117]
The killing intent of the mounted bandits surrounding the watchtower in a circle stabbed at their skin.

[P118]
Just as everyone was falling into despair, Lee Seowol suddenly drew her bowstring toward the sky.

[P119]
Whoooosh.

[P120]
Trailing a tail of fire, a single fire arrow descended toward the gate, which was shrouded in darkness.

[P121]
It was a light meant to find one person.

[P122]
*Uncle Cheol.*

[P123]
The Tiger of Mount Heng, Cheol Mubaek. He was the Mount Heng Sword Sect’s final hope.

[P124]
That was when a man walked out beneath the light revealed by the fire arrow.

[P125]
Clomp. Clomp.

[P126]
“I suppose it’s a little late to say this now…”

[P127]
Lee Seowol had heard that voice only once, but she could never forget it, not even in her dreams.

[P128]
Unable to bring herself to look at him, she closed her eyes.

[P129]
Pung Yang smiled broadly at her.

[P130]
“You’ll have to marry me.”

[P131]
* * *

[P132]
The hunter Cheol Mubaek became the Tiger of Mount Heng because of a fortuitous encounter.

[P133]
While tracking wolves along a mountainside in the vast Mount Heng range, he fell between cliffs into a hidden cave. There, he discovered a martial arts manual and an elixir left behind by a reclusive master.

[P134]
*I’m going back. I’m going back alive, no matter what!*

[P135]
Cheol Mubaek learned martial arts to survive. When the fasting pills in the hidden cave ran out, he tore up grass growing between the cliffs or caught bats to eat as he trained.

[P136]
After no less than three years, he climbed the cliff with his bare hands and returned to the village.

[P137]
What awaited him was his home in ruins—and the deaths of his wife and child.

[P138]
*Had it been a couple of months since we lost contact? That bastard Hwang, who’d always had his eye on your wife…*

[P139]
By the time he came to his senses, he had already beaten the village’s leading landowner and all his servants to death.

[P140]
After avenging his family, Cheol Mubaek returned to the hidden cave and resumed his martial arts training. It was a whip he used against himself, and atonement for his family.

[P141]
How much time passed like that?

[P142]
Before he knew it, Cheol Mubaek was being called the Tiger of Mount Heng.

[P143]
But…

[P144]
“Hoo. Even a tiger would cry.”

[P145]
Cheol Mubaek panted harshly. His once-brilliant eyes were clouded like a sky covered in dark clouds, and his beard was drenched in blood.

[P146]
*I have to hurry. I have to stop that bastard…*

[P147]
But all he had left was his will. His body, with its limbs broken, had already slipped beyond his control. He had displayed martial arts worthy of the title Tiger of Mount Heng, yet he still could not defeat Pung Yang.

[P148]
*How in the world did he…?*

[P149]
The result seemed obvious. Pung Yang had only just entered the Peak realm, barely capable of creating blade qi, while Cheol Mubaek was a Peak master who had reached a mature realm stage.

[P150]
Pung Yang had been as precarious as a candle in the wind. Then he had suddenly changed after pulling an unidentified hard wooden case from inside his robes.

[P151]
*The red pill. Yes, that was definitely it.*

[P152]
Cheol Mubaek had made a mistake by retreating because he thought it might be a hidden weapon. After Pung Yang gulped down the pill, he was no longer the leader of the ordinary mounted-bandit group Cheol Mubaek had known.

[P153]
*How can a human being become that strong?*

[P154]
Cheol Mubaek’s eyes trembled as he recalled Pung Yang’s movements.

[P155]
The gap between them was so vast that it seemed impossible to win, even if they fought ten or a hundred more times. Pung Yang had overturned the battle in an instant, broken all four of Cheol Mubaek’s limbs, inflicted massive internal injuries, and then left.

[P156]
*I’ll let you live for now. I’ve decided I want your martial arts formula as a wedding gift.*

[P157]
Cheol Mubaek’s eyes reddened as he recalled Pung Yang’s parting words.

[P158]
The Shura Annihilating Fist was a martial art passed down to a single successor and never taught to outsiders.

[P159]
He would choose suicide rather than hand it over to Pung Yang, but Lee Seowol—whom he cherished like a daughter or granddaughter—troubled him.

[P160]
*What on earth am I supposed to do?*

[P161]
It was at that moment, as Cheol Mubaek stared at the sky with a heavy heart, that it happened.

[P162]
Thud-thud-thud-thud!

[P163]
The sound of approaching hooves grew louder and louder before coming to a sudden stop at his feet.

[P164]
Beneath the brilliantly shining moon, four pairs of eyes looked down at him.

[P165]
“Doesn’t the Red Wind Band have a retirement age? Why is an old geezer still out here playing bandit…?”

[P166]
“Young Master Jin, that’s Great Hero Cheol Mubaek, the Tiger of Mount Heng.”

[P167]
“Gah! I’m sorry. Hey, Mujin. Hurry up and apologize. What are you waiting for?”

[P168]
“The squad leader is the one who made the mistake, so why should I…?”

[P169]
Smack!

[P170]
“Grandpa—no, Sir. Are you all right?”

[P171]
Instead of answering, Cheol Mubaek stared intently at the young man’s chest.

[P172]
One character was embroidered on his navy martial robe.

[P173]
進.

[P174]
“Taiyuan… the Jin Family?”

[P175]
“Oh, you recognize it?”

[P176]
The young man, Jin Taekyung, grinned.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 영약     | **elixir**                                       |                                                       |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 사형     | **Senior Brother**                           |
| 선배     | **Senior**                                   |
| 체력               | **Stamina**                    |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 114,
  "passed": true,
  "metrics": {
    "source_characters": 5815,
    "translation_characters": 13648,
    "length_ratio": 2.347,
    "source_paragraphs": 171,
    "translation_paragraphs": 177
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "사형",
        "preferred": "Senior Brother"
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "전세",
        "preferred": "jeonse lease"
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
        "korean": "전하",
        "preferred": "His Highness"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "세가",
        "preferred": "great family"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "천백",
        "romanization": "cheonbaek"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "콰과광",
        "romanization": "kwagwagwang"
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
