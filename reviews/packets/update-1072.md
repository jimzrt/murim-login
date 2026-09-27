<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1072.txt",
      "sha256": "b67a265437a8ce9781c7617fb9481432d6ab6c7a2749b2dd50c3a5debca94ad6",
      "bytes": 11729
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "412a9163c882f2624a236fb89eb1d1b52a214b0122ebd8fe0401fca3126c29db",
      "bytes": 1594
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5be93eb6bd068e9f3140c82d613f582e8e72d687cb3b90fa54d2c393096f3e5c",
      "bytes": 242356
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "dc115cb9d9d13ee92f22288372dd2c1fff694af9e272fac3db336e91df10fe4b",
      "bytes": 760
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7df8b2357d0faa08e63a571debd66c331206f8c9af0b11d116826f4c7dad2ad4",
      "bytes": 284375
    }
  ],
  "estimated_tokens": 7605
}
-->

# Durable State Update — Chapter 1072

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1072. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1072. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 1072,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1072,
    "continuity_sources": [1072],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Jin’s roughly three thousand allies are now fighting at least ten thousand surrounding monsters, including mutants.",
    "Jin’s circular formation has Sama Pyo and Jeong Hogun on the wings, Hyeoncheon and the Kongtong Disciples plus Hyuk Sopyung and the Zhongnan Disciples at the rear, and Jeok Cheongang, Bow Saint, and the Fire Dragon Pavilion at the vanguard.",
    "Thirty sorcerers use bells to coordinate monsters; the Blood Lord ordered them to reduce the allied force and capture Jin alive.",
    "A person disguised as or transformed into a monster is among the guards and has spoken despite a bell command.",
    "Ma Sanbao serves the Blood Lord and covertly watched Jin’s force; Great Sir first detected the surveillance in Ningxia.",
    "The East Depot’s network shared its view with Dark Heaven through the Eastern Heaven Demon Lord.",
    "The Grand Mage suspects Hyeoncheon and the Kongtong survivors went to Great Sir."
  ],
  "continuity_sources": [
    1070,
    1071
  ],
  "open_questions": [
    "Who is Great Sir, and what is his connection to Hyeoncheon and the surviving Kongtong Disciples?",
    "Did Jin’s sword strike kill or otherwise affect the watching crow?",
    "Are Dark Heaven’s forces broadly composed of reanimated corpses, and has Ma Sanbao spread the Corpse Art to others?",
    "What is the Lord of Heaven seeking through Jin, and when will he appear?",
    "Who is the person among the monsters, and how did they come to be there?"
  ],
  "safe_through": 1071,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 정파     | **orthodox faction**                             |                                                       |
| 지능               | **Intelligence**               |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 수혈 | **Sleep Acupoint** | Acupoint whose successful strike prevents the target from resisting sleep. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 답보 | **stagnation** | Taekyung's current lack of progress in martial arts. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 초일류 | **Supreme First Rate** | Realm attained by each Baekcheon Unit member. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1071
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

## Korean source

```text
1072화




그 순간, 흑의인의 머릿속에 떠오른 생각은 하나뿐이었다.

‘혹시 지금 내가 헛것을 보고 있는 건가?’

흑의인으로서는 당연한 의문이었다.

그는 술사(術士)다.

그것도 아주 숙련되고, 상당한 실력을 지닌 술사.

갑자 단위의 공력도, 신공(神功)이라 불릴 정도로 뛰어난 무공도 없지만 흑의인에게는 수백 마리의 괴물을 완벽하게 통제할 수 있는 능력이 있었다.

그런데…….

‘도대체 이놈은 뭐지?’

흑의인은 멍한 눈빛으로 눈앞의 괴물, 아니 정확히는 괴물의 거죽을 뒤집어쓴 것이 분명한 불청객을 바라보았다.

그리고 자신의 팔을 세게 꼬집어 이것이 꿈이 아니라는 사실을 확인한 후에야, 줄곧 참고 있던 한마디를 간신히 쥐어 짜낼 수 있었다.

“네놈은 누구냐?”

움찔, 하고 몸을 떤 정체 모를 불청객이 더듬거리는 목소리로 대답했다.

“괴, 괴물인데요.”

“……사람 말을 하는데?”

“그, 사람 말을 하는 괴물도 있지 않나요?”

“……있을 수가 없는데?”

전문가답게 매우 논리정연한 흑의인의 반박에, 잠시 침묵하던 불청객이 입을 열었다.

“그워어어어.”

“…….”

“크흠. 크워어어어.”

“…….”

“그, 그아아아아.”

이제는 숫제 강시처럼 두 팔까지 쳐든 채로 자신 없는 괴성을 이어 가는 불청객의 모습에, 일순간 더욱 큰 혼란에 빠진 흑의인이 버럭 외쳤다.

“그만!”

“헉. 왜요?”

“이게, 이게 도대체 무슨 개 같은 짓거리냐?”

“최대한 따라 해 본 건데…… 마지막 건 비슷하지 않나요?”

“아니, 그나마 조금 비슷하긴 했는데.”

“와아, 역시! 감사합니다!”

상식을 아득히 벗어난 대화는 사고를 마비시키는 법.

흑의인이 할 말을 잃어버린 그때, 숨길 수 없는 기쁨을 내비친 불청객이 의기양양한 어조로 덧붙였다.

“이틀 내내 연습한 보람이 있네요. 노력은 배신하지 않는다는 말이 맞았어요.”

생각지도 못한 불청객의 대답에, 혼란 속에서 허우적거리던 흑의인이 눈을 깜빡였다.

“지, 지금 뭐라고?”

“네?”

불청객이 고개를 갸웃거렸다. 썩은 거죽 너머로 드러난 그의 눈동자는 맑고 깨끗했다.

“아, 노력을 배신하지 않는다는 말이요? 그건 할아버지께서 제가 아주 어릴 때부터 해 주셨던 말씀인데…….”

“그거 말고!”

“아, 뭘 말씀하시는지 알겠어요. 덩치 큰 사람들. 음, 사람이라고 하긴 뭣 하지만 아무튼 저 안에 숨어서 열심히 따라 했거든요.”

“그, 그러니까 그 말은.”

“맞아요. 앞서 말씀드렸다시피 이틀 전부터 쭉 그랬어요.”

“……!”

천진난만한 대답과는 달리, 이를 듣고 있던 흑의인은 순간 등골이 얼어붙는 듯한 충격에 휩싸였다.

‘이틀 전부터? 그런데도 내가 몰랐다고?’

말도 안 되는 일이었다.

그는 혹독한 수련 끝에 오백여 마리의 괴물을 완벽히 통제할 수 있는 능력을 얻었고, 그렇기에 살아 있는 인간이 품고 있는 생기(生氣)쯤은 눈을 감고도 간파해 낼 수 있었으니까.

하지만…….

‘거짓말이 아니다.’

흑의인은 본능적으로 느낄 수 있었다.

지금 자신의 눈앞에 서 있는 저 정체 모를 불청객이 했던 모든 말들이, 조금의 거짓도 담겨 있지 않은 진실이라는 것을.

그가 생각하기에 저놈에게는 능숙하게 거짓말을 할 정도의 지능도, 이렇게 시원하게 들통난 이상 감출 이유도 없었다.

그리고 이러한 일련의 생각과 상황들은, 귀신에 홀린 것처럼 극심한 혼란에 빠져 있던 흑의인으로 하여금 마침내 제정신을 차릴 수 있게 도와주었다.

“네놈…… 정파의 끄나풀이로군.”

헉, 하고 헛숨을 삼킨 불청객이 황급히 손을 내저었다.

“아, 아닌데요?”

“입 닥쳐라. 이 미친놈 같으니.”

“미친놈이라니, 그건 아주 상스럽고 나쁜 말이에요. 할아버지가 절대 쓰지 말랬어요.”

“이런 개 같은……!”

흑의인은 피가 거꾸로 솟는 것 같았다.

제아무리 예상치 못한 상황이었다고는 해도 잠시나마 이런 정신 나간 놈에게 놀아났다니.

그는 분노를 실어 손에 쥔 요령(妖鈴)을 흔들었다.

딸랑!

방울 소리에 유독 힘이 실렸다고 느낀 것은 결코 착각이 아니었다.

술사, 그중에서도 괴물들을 부리는 이들만이 지닌 특유의 사기(死氣)는 소리를 더욱 음산하고, 또렷하게 만들었고 그 소름 끼치는 음율 안에는 두 가지의 의미가 담겨 있었다.

첫째. 일대에 포진해 있는 또 다른 술사들에게 현재의 상황을 알리는 것.

그리고 둘째.

쉬쉭! 쿠웅!

호위를 위해 데려온 일백여 마리의 괴물들에게, 저 미친놈의 처리를 맡기는 것.

“이제 네놈에게 베풀 수 있는 자비는 하나뿐이다.”

그 거대한 체격과는 어울리지 않는 속도로 삽시간에 주위를 에워싸는 한편, 철벽처럼 앞을 가로막은 괴물들 너머로 흑의인은 씹어뱉듯 말을 이었다.

“지금이라도 얌전히 투항하여 알고 있는 모든 정보를 털어놓는다면, 비교적 빠르고 편안한 죽음을 약속하마.”

흑의인으로서는 결코 머릿수만 믿고 하는 말이 아니었다.

그를 호위하는 괴물들은 저마다 최소 초일류에서 절정의 고수들과 비견될 정도의 실력을 지녔다.

인간의 한계를 훌쩍 뛰어넘은 힘과 속도, 또한 무엇보다 끈질긴 생명력은 악몽이나 다름없다.

그런 괴물들이 무려 일백여 마리.

설령 눈앞의 불청객이 미친놈인 것과는 별개로 엄청난 실력을 지니고 있다고 해도, 결과는 조금도 달라지지 않을 것이라고 흑의인은 생각했다.

불청객이 상대해야 하는 것은, 단지 이곳에 있는 괴물들뿐만이 아니었으니까.

“어디 한번 마음껏 발악해 보거라. 촌각 후에는 그마저도 불가능할 테니.”

지금쯤 신호를 전달받고 즉각 이곳으로 오고 있을 동료 술사들을 생각하며, 흑의인이 비스듬히 입꼬리를 말아 올린 그때였다.

“그런데 왜 답장이 안 와요?”

불청객이 불쑥 던진 물음에, 흑의인이 반사적으로 되물었다.

“뭐?”

“답장이요. 어, 이 경우에는 답음(答音)이라고 해야 하나? 여하튼 제가 이틀 동안 지켜본 바로는 사소한 것 하나도 항상 방울 소리로 주고받던데.”

“……어?”

그 순간, 불현듯 무언가를 깨달은 흑의인은 황급히 고개를 들어 사방을 둘러보았다.

아니, 정확히는 온 신경을 집중하여 귀를 기울였다.

이곳으로 오고 있다는 동료 술사의 답을, 자신의 것과 닮아있는 그 음산한 방울 소리를 듣기 위해서.

그러나 귓가에 닿는 소리라고는 저 멀리서 불어오는 바람과 주위를 에워싼 괴물들의 숨결뿐. 되돌아오는 것은 아무것도 없었다.

아무것도.

“……!”

일순간, 흑의인의 가슴이 덜컥 내려앉았다.

무언가 잘못됐다.

그것도 아주 단단히.

그리고 머릿속을 스치는 불길한 예감과 함께, 혼란에 휩싸인 그의 눈동자가 한 존재를 향해 움직였다.

끔찍한 괴물들에게 포위된 상황에서도 귀를 쫑긋 세운 채, 두 손으로 나팔 모양까지 만들어 주위의 소리를 듣고 있던 불청객을 향해.

“오. 확실히 안 들려요. 아무것도.”

“너, 너…….”

도대체 무어라 말해야 할까.

어떻게 지금 이 상황을 이해해야 할까.

제대로 된 말조차 하지 못하고 목소리를 흐리는 흑의인의 시야에, 변색 된 괴물의 거죽 너머로 반달처럼 휘어지는 눈매가 선명히 틀어박혔다.

“다행이에요. 역시 작은할아버지라니까.”

“작은……할아버지?”

“네, 저한테 이것저것 많이 가르쳐 주시는 분이세요. 작은할아버지라고 부를 때마다 엄청 화를 내시긴 하는데…… 가끔 보면 한편으로는 은근히 좋아하시는 것 같기도 해요.”

주절주절 떠들던 불청객이 헙, 하고 입을 다물었다.

“아, 제가 했던 말은 작은할아버지한테는 말하지 마세요. 들으시면 또 화낼 거예요.”

흑의인은 대답하지 않았다.

보다 정확히는, 대답할 정신조차 남아 있지 않았다.

다만 이제야 겨우 입을 닥친 불청객을 멍하니 바라보다, 이제야 떠오른 의문을 간신히 쥐어 짜낼 뿐이었다.

“넌…… 아니 너희는 도대체 누구지?”

어느샌가 시야가 어지러웠다. 조금 전 들었던 말을 통해 도저히 믿고 싶지 않은 진실을 깨달았기 때문이었다.

자신과 함께 이곳에 온 다른 삼십여 명의 술사들은, 이미 모두 죽었다.

불청객이 자신의 곁에 스며든 방식으로. 혹은 그보다 더 은밀하고, 치명적인 방법으로.

설령 아직 살아 있는 이가 있다 할지라도, 그리 오래 지나지 않아 불귀의 객이 될 것이다.

지금 이 순간, 불청객의 대답보다 먼저 흑의인의 뇌리를 스쳐 지나간 별호의 주인이 이곳에 있다면.

“그, 그 작은할아버지라는 자가 설마…….”

흑의인이 차마 말을 잇지 못하고 말꼬리를 흐린 그 순간이었다.

“지금, 뭐라고 했느냐?”

“……!”

불현듯 귓가를 파고드는 그 무감정한 음성에, 흑의인은 마치 번개가 정수리를 관통하는 듯한 충격에 휩싸였다.

왔다.

작은할아버지, 아니 ‘그’가.

그것도 바로 자신의 등 뒤까지.

그럼에도 호흡을 느끼지 못했다. 

목소리와 함께 응당 뒷덜미에 닿아야 할 숨결을, 조금의 인기척과 생기(生氣)조차 감지해 내지 못했다.

그리고 석상처럼 굳어 버린 흑의인의 귓가로, 숨결 없는 목소리가 재차 흘러들었다.

“물었다. 뭐라 지껄였느냐고.”

흑의인은 소리 내어 말하는 법도, 숨을 쉬는 것조차 잊었다.

다만 그저 자신이 할 수 있는 마지막 발악을, 생존을 위한 본능적인 최후의 몸부림을 펼칠 뿐이었다.

그가 가진 모든 것이나 다름없는, 낡고 피에 물든 요령을 움직이기도 전에 한 줄기의 선이 손목을 가로질렀음을 인지하지도 못한 채.

서걱. 툭.

모든 것이 한발 늦었다.

주인을 잃은 손목이 땅에 떨어진 것도, 자신의 것을 잃어버린 주인이 그것을 발견하는 것도.

마지막으로 뒤늦게 찾아온 고통을 인지한 흑의인이, 공포가 담긴 비명을 토해 내는 것도.

“끄……!”

툭, 털썩.

수혈(睡血)이 눌림과 동시에 힘없이 허물어지는 몸뚱어리.

그렇게 흑의인은 비명조차 제대로 지르지 못한 채, 도무지 끝이 보이지 않은 캄캄한 암흑 속으로 곤두박질쳤다.

어느덧 꿈결처럼 흐릿하게 들려오는, 두 사람의 목소리를 뒤로한 채.

“또 한 번만 그렇게 부르면 죽여 버린댔지.”

“죄송해요. 작은할아버지.”

“……돌아 버리겠군. 그 녀석이나 만나러 가자.”

“네! 작은할아버지!”

정말로, 그건 마지막까지 악몽 같았다.
```

## Final English reading copy

```markdown
# Chapter 1072

At that moment, there was only one thought in the black-robed man’s mind.

*Am I seeing things?*

It was a perfectly reasonable question for him to ask himself.

He was a sorcerer.

A highly experienced one, with considerable skill.

He had neither internal energy measured in jiazi nor martial arts exceptional enough to be called divine. But he did have the ability to control hundreds of monsters perfectly.

And yet…

*What the hell is this guy?*

The black-robed man stared blankly at the monster before him—or, more precisely, at the uninvited guest who had obviously pulled a monster’s hide over himself.

Only after pinching his arm hard enough to confirm he wasn’t dreaming could he finally squeeze out the question he’d been holding back.

“Who are you?”

The mysterious intruder flinched and answered in a halting voice.

“I-I’m a monster.”

“……You’re talking like a person.”

“A-aren’t there monsters that talk like people?”

“……There can’t be.”

At the black-robed man’s thoroughly logical rebuttal, delivered with all the confidence of an expert, the intruder fell silent for a moment, then opened his mouth.

“Grrroooar.”

“……”

“Ahem. Grrroooar.”

“……”

“G-grraaaah.”

The intruder kept making uncertain monster noises, now raising both arms like a jiangshi. The black-robed man sank into even greater confusion and shouted.

“Stop!”

“Gasp. Why?”

“What the hell is this supposed to be?”

“I was doing my best to imitate them… Wasn’t that last one pretty close?”

“No, that one was a little close.”

“Wow! I knew it! Thank you!”

An exchange that strayed far enough from common sense could paralyze the mind.

Just as the black-robed man ran out of words, the intruder, unable to hide his delight, added proudly:

“All that practice for two days straight paid off. I guess it’s true what they say: hard work doesn’t betray you.”

The black-robed man, still floundering in confusion, blinked at the unexpected answer.

“W-what did you just say?”

“Hm?”

The intruder tilted his head. His eyes, visible beyond the rotten hide, were clear and bright.

“Oh, that hard work doesn’t betray you? My grandfather’s been telling me that since I was little…”

“Not that!”

“Oh, I know what you mean. The big people. Well, it’s not quite right to call them people, but anyway, I hid in there and kept trying to imitate them.”

“S-so you mean…”

“That’s right. Like I said before, I’ve been doing it for two days.”

“……!”

Despite the intruder’s innocent answer, the black-robed man was struck by a shock that seemed to freeze his spine.

*For two days? And I never noticed?*

It made no sense.

After grueling training, he’d gained the ability to perfectly control some five hundred monsters. That was why he could detect the life energy of living humans with his eyes closed.

But…

*He’s not lying.*

The black-robed man sensed it instinctively.

Every word the mysterious intruder before him had spoken was true—not a single one a lie.

As far as he could tell, the man didn’t have the Intelligence to lie convincingly. And now that he’d been caught so plainly, he had no reason to hide anything.

Those thoughts, and the situation unfolding around him, finally helped the black-robed man come to his senses, as if he’d been bewitched.

“You… You’re an orthodox faction lackey.”

The intruder gasped and hurriedly waved his hands.

“N-no, I’m not!”

“Shut up, you lunatic.”

“Lunatic? That’s a very vulgar and bad word. My grandfather told me never to say it.”

“You little piece of—!”

The black-robed man felt his blood rushing to his head.

Even if the situation had caught him completely off guard, he’d let himself be played by some lunatic, if only for a moment.

He shook the evil bell in his hand, his anger lending force to the motion.

*Jingle!*

It wasn’t his imagination. There was unusual force behind the bell’s sound.

The distinctive death energy possessed only by sorcerers who commanded monsters made the sound more ominous and clear. That chilling tone carried two meanings.

First: alert the other sorcerers stationed nearby to the situation.

And second—

*Whoosh! Thud!*

Leave the disposal of that lunatic to the hundred or so monsters he’d brought as guards.

“You have one chance left to receive my mercy.”

The monsters swept around them with speed that belied their enormous frames, forming an impenetrable wall in front of the black-robed man. From behind it, he spoke through clenched teeth.

“If you surrender quietly right now and tell me everything you know, I’ll promise you a relatively quick and painless death.”

The black-robed man wasn’t relying on numbers alone.

Each monster guarding him had skill comparable to a master ranging from at least Supreme First Rate up to Peak.

Their strength and speed surpassed human limits, and, more than anything, their tenacious vitality was a nightmare.

And there were a hundred of them.

Even if the intruder before him was a lunatic with tremendous skill, the outcome wouldn’t change in the slightest.

The monsters here weren’t the only ones he’d have to face.

“Go ahead and struggle all you want. You won’t even be able to do that a few moments from now.”

The black-robed man curled one corner of his mouth as he thought of his fellow sorcerers, who should have received the signal and be rushing here at once.

“But why haven’t I gotten a reply?”

The intruder’s sudden question made the black-robed man reflexively ask:

“What?”

“A reply. Uh, in this case, should I call it a reply-sound? Anyway, from what I’ve seen over the past two days, you always communicate with the bell, even over the smallest things.”

“……Huh?”

The black-robed man suddenly realized something. He hurriedly looked around.

No—he focused all his attention on listening.

He was waiting to hear his fellow sorcerers answer, their sinister bell sounds similar to his own.

But the only sounds reaching his ears were the wind blowing from far away and the breathing of the monsters surrounding them. Nothing answered.

Nothing at all.

“……!”

The black-robed man’s heart lurched.

Something had gone wrong.

Terribly wrong.

With a sense of foreboding sweeping through his mind, his confused eyes turned toward one figure.

The intruder, surrounded by horrible monsters, had perked up his ears and even cupped his hands around them like a trumpet to listen.

“Oh. You’re right. I can’t hear anything. Nothing at all.”

“You, you…”

What was he supposed to say?

How could he make sense of this situation?

The black-robed man could barely get the words out. Beyond the discolored monster hide, the intruder’s eyes curved clearly into crescents.

“What a relief. I knew I could count on Little Grandpa.”

“L-Little Grandpa?”

“Yes. He’s the one who teaches me all sorts of things. He gets really angry whenever I call him Little Grandpa, but sometimes it seems like he secretly likes it, too.”

The intruder stopped rambling and snapped his mouth shut with a little gasp.

“Oh, don’t tell Little Grandpa I said that. He’ll get angry again.”

The black-robed man didn’t answer.

More precisely, he no longer had the presence of mind to answer.

He could only stare blankly at the intruder, who had finally stopped talking, then squeeze out the question that had just come to mind.

“Who… No, who are you people?”

His vision was blurring. The words he’d just heard had made him realize a truth he desperately didn’t want to believe.

The other thirty or so sorcerers who’d come here with him were already dead.

They’d been killed the same way the intruder had slipped in beside him—or in a manner even more secretive and deadly.

Even if anyone was still alive, they wouldn’t be for long.

If the owner of the sobriquet that had just flashed through the black-robed man’s mind was here now…

“Th-that Little Grandpa of yours—could it be…?”

The black-robed man’s voice trailed off. Then—

“What did you just say?”

The flat voice suddenly pierced his ears, and a shock like lightning striking the crown of his head swept over him.

He was here.

Little Grandpa—no, *that man.*

Right behind him.

And yet he hadn’t sensed the man’s breathing. He hadn’t detected the breath that should have brushed the back of his neck along with the voice—not even the slightest trace of presence or life energy.

The breathless voice sounded again in the black-robed man’s ear, whose body had gone rigid as a statue.

“I asked you. What the hell did you say?”

The black-robed man forgot how to speak. He even forgot how to breathe.

He could only make one last desperate attempt—the instinctive final struggle to survive.

He didn’t even realize that a thin line had cut across his wrist before he could move the old, bloodstained evil bell, which was practically everything he had.

*Slice. Plop.*

Everything happened a moment too late.

The wrist, severed from its owner, hit the ground. Its owner noticed it only after it was gone.

And the black-robed man recognized the pain only when it arrived at last, then let out a scream filled with fear.

“Guh…!”

*Thump. Collapse.*

His body crumpled helplessly as the Sleep Acupoint was pressed.

And so the black-robed man plunged into a pitch-black abyss with no end in sight, unable even to scream properly.

Behind him, the voices of two people sounded distant and dreamlike.

“I told you I’d kill you if you called me that one more time.”

“I’m sorry, Little Grandpa.”

“……This is driving me crazy. Let’s go find that guy.”

“Yes! Little Grandpa!”

Truly, right to the very end, it was like a nightmare.
```
