<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0898.txt",
      "sha256": "f29e1952520ad5844b06263ab9473c621d6cfae9ccfbcdc4bd0b9a80733aca44",
      "bytes": 13557
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f283bdac05ab503c9cf24d4a05ea7029cc1001b0a2214ec80798b457ef89b1ff",
      "bytes": 1523
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b095c036feda74e09729daf1aa6d95a5b05b56fa871d442cbb7c8b98f5da42ef",
      "bytes": 230750
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "00dc10677e56ea1ffeefb4e3dc27b73962947bcde0f639244aee240b81682891",
      "bytes": 837
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "7c58295ec846f4bf58bcc878f2d0e8393a890c1eee14d61f361fb8f892b180fb",
      "bytes": 1432
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8ead4207b37bea0c8bdc317b844fae2124946506bd434491dd7489b0ce8d1c7b",
      "bytes": 261385
    }
  ],
  "estimated_tokens": 9725
}
-->

# Durable State Update — Chapter 898

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
1 and safe_through 898. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 898. Profile updates may replace only one
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
  "chapter": 898,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 898,
    "continuity_sources": [898],
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
    "The Emperor has announced a three-day birthday banquet for the imperial prince, starting the day after the announcement, while flood-stricken residents suffer losses.",
    "Public anger over the Emperor’s response to the flood is growing.",
    "A mysterious bamboo-hat man’s speech led a crowd to associate Shangshan with Prince Shangshan and imagine the prince ascending the throne; the man vanished.",
    "Ma suspects the Emperor has allied with Dark Heaven and that Baek Yeon and So Gyo are connected to it; these remain unconfirmed allegations.",
    "Jin gave Ma a cipher and a messenger’s location; he expects Murim Alliance reinforcements for the grand banquet, possibly including the Slaughter Saint or a Ten King."
  ],
  "continuity_sources": [
    896,
    897
  ],
  "open_questions": [
    "Who is the cipher’s intended recipient, and what information does it contain?",
    "Will the expected Murim Alliance reinforcements arrive for the banquet, and who will be among them?",
    "Are Ma’s suspicions about the Emperor, Baek Yeon, and So Gyo’s ties to Dark Heaven correct?",
    "Who was the bamboo-hat man, and what were his intentions?"
  ],
  "safe_through": 897,
  "temporary_decisions": [
    "Use “Twelve Palaces of the Zodiac” for 黃道十二宮.",
    "Use “Seal-Holding Eunuch of the East Depot” for 東廠掌印太監.",
    "Keep “Shangshan” in the crowd’s mountain imagery where it alludes to Prince Shangshan."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 주화입마   | **qi deviation**                                 |                                                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태               | **Status**                     |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 십상남자 | **Tenfold Man** | A joking title Zhu Bao grants Hyuk Mujin, who inscribes it on a bronze token. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 혁무진 | 홍진 | martial artist addressing a senior official and political ally | Comrade Hong | casual and coaxing | Hyuk Mujin addresses Hong Jin as 홍 동지님 while trying to calm him and de-escalate the confrontation. |

## Listed compact profiles

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 895
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 891
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

## Korean source

```text
＃898화



누군가 그랬다. 인간은 적응의 동물이라고.

그러나 이 세상 누구에게나 수없이 많은 경험을 통해서도 익숙해지지 않는 것이 한 가지쯤은 있기 마련이다.

나 같은 경우에는 다른 사람의 목숨을 책임져야 한다는 것이 그랬고, 눈을 뜨자마자 보이는 누군가의 못생긴 얼굴도 마찬가지였다.

“뭐 하냐.”

혁무진이 대답했다.

“조장님을 살펴보고 있었는데요.”

“왜?”

“출입도 금하시고 이틀 내내 방에 틀어박혀 운기조식만 하셨잖아요. 주화입마라도 온 거 아닌가 싶어서 슬쩍 들어와 봤죠.”

“이틀?”

“예. 설마 모르셨어요?”

“아니, 알았지.”

거짓말이다. 기껏해야 한나절쯤 지난 줄 알았는데 무려 이틀이라니.

어느새 햇빛이 비치는 창가를 바라본 나는 내심 한숨을 내쉬며 말했다.

“걱정해 주는 건 고마운데, 다음부터는 그냥 놔둬라.”

“왜요?”

“눈 뜨자마자 네 얼굴 보고 주화입마 걸릴 뻔했으니까.”

“말씀이 너무 심하신 거 아닙니까?”

“심한 건 네 얼굴이야.”

“그럼 옆에만 있겠습니다. 호법은 필요하잖아요.”

“호법도 서지 마.”

“아니, 그건 또 왜요.”

“네 코골이 들으면 주화입마 오니까.”

“……이쯤 되면 그냥 제가 없는 게 낫겠네요. 계속 이러시면 저도 수틀려서 혼자 본가로 복귀하는 수가 있습니다.”

막 가부좌를 풀고 자리에서 일어나려던 나는, 짐짓 으름장을 놓는 혁무진을 물끄러미 바라보았다.

“왜, 왜요. 제가 뭐 조장님만 따라다니라는 법이라도 있습니까?”

말과는 달리 살살 눈치를 보는 그 모습에 피식 웃음이 새어 나온다.

언제 날아올지 모르는 내 주먹을 피하기 위해, 혹은 가장 덜 아프게 맞기 위해 몸을 한껏 움츠리고 있던 혁무진이 당황한 표정을 지었다.

“뭐지? 내가 헛것을 보나? 조장님 갑자기 왜 이러세요?”

“뭐가?”

“아니, 이미 열두 대는 때렸을 사람이 성인군자처럼 웃고만 있으니까 그러죠.”

나는 터져 나오려는 웃음을 가까스로 참았다.

그리고 다음 순간, 섬광과도 같은 속도로 자리를 박차며 솟구쳤다.

쉭!

혁무진은 본능적으로 방어하려 했고, 찰나의 순간 보여 준 움직임은 아직 일류 고수라는 게 믿기지 않을 만큼 빠르고 침착했다.

물론, 그 상대가 나라는 점에서 이미 실패한 대처였지만.

“흡.”

모든 것이 수포로 돌아갔음을 깨달은 혁무진이 헛숨과 함께 질끈 눈을 감는다. 아마도 여느 때처럼 곧 들이닥칠 강렬한 충격을 대비하고 있었겠지.

하지만 그런 마음의 준비가 무색하게도, 녀석이 예상했던 일은 벌어지지 않았다.

툭.

평소처럼 후려갈기는 대신, 가볍게 뒤통수를 건드린 나는 짐짓 혀를 찼다.

“이 새끼 이거 지금까지 무공 헛배웠네. 누가 눈감으래?”

“……어?”

“처맞더라도 두 눈 부릅뜨고 있어라. 눈깔만 제대로 굴려도 절반은 먹고 들어가니까.”

얼떨떨한 얼굴로 뒤통수를 문지르던 혁무진이 불쑥 입을 열었다.

“갑자기 왜 이러세요?”

“뭐가?”

“아니, 이상하잖아요. 평소라면…….”

“그래서, 평소대로 때려 줘?”

혁무진이 냉큼 대답했다.

“아뇨. 그건 좀.”

“그럼 입 다물고 있어. 전력 보존해 주는 거니까.”

“전력 보존이요?”

“그래. 안 그래도 곧 피 터지게 싸울 텐데 네 뒤통수 때려서 뭐 하냐. 그러다가 네가 눈먼 칼이라도 한 방 맞으면 괜히 꿈자리 뒤숭숭해져.”

혁무진이 히죽거리며 웃었다.

“아아. 그러셨구나. 그래도 조금 더 솔직해지셔도 되는데.”

“뭐?”

“다 압니다. 제가 갑자기 떠난다고 하니까 조장님께서도 괜히 신경 쓰이신 거 아닙니까. 맞죠?”

뭐라 대답하려던 나는 그냥 실소를 흘렸다.

“그래, 인마. 눈치 빨라서 좋겠다.”

“역시. 그럴 줄 알았습니다. 아무리 조장님이라고 해도 저 같은 오른팔이 옆에 딱 붙어 있어야 힘을 쓰죠.”

“오른팔은 무슨. 새끼발가락이라니까.”

“어허, 왜 이러실까. 오른팔도 저 나름대로 많이 양보한 겁니다.”

“양보?”

“예. 저만큼 충성하는 부하를 또 어디서 구해요. 이 정도면 사실상 오른팔이 아니라 심장이지. 심장.”

“심장은 어림도 없지. 불알 달린 놈 주제에 어딜 감히.”

“그럼 불알만 떼면 가능합니까?”

딱!

이번에는 어느 정도 힘을 실어 때렸는데, 어째서인지 억 소리와 함께 뒤통수를 감싸 쥔 혁무진의 얼굴은 되려 밝아졌다.

“크으. 이거지.”

“……어?”

“그래도 아직은 좀 부족한데. 더 세게 때려봐요.”

뭐지, 이 소름 끼치는 반응은?

내가 혁무진의 취향을 의심하고 있던 그때, 녀석이 씩 웃으며 말을 이었다.

“그냥, 별건 아니고요. 평소와는 너무 달라서 좀 신경 쓰이지 뭡니까.”

“……!”

“어느 순간부터 고민이 많아지신 건 알겠는데, 다 잘될 겁니다. 그러니까 하던 대로 하세요. 늘 하던 대로.”

나도 모르게 순간 말문이 막혔다.

동시에 숨겨 두었던 마음속 진심이 끓어올라 목구멍을 간지럽혔다.

하지만…….

‘안 돼.’

일시적인 감정에 휩쓸려 말할 수는 없었다. 괴물들이 즐비한 이 거대한 도박판에서 살아남아 승리하기 위해서는 말을 아껴야 했으니까.

결국 내가 고민 끝에 끄집어낸 말은 하나뿐이었다.

“안 무섭냐?”

“네? 뭐가요?”

“지금 우리가 처해 있는 이 상황. 그리고 곧 맞닥트려야 하는 그 알 수 없는 상황이.”

그리고 내 말을 들은 혁무진은 한참이나 눈을 끔뻑거리더니, 이렇게 대답했다.

“그걸 말이라고 하세요? 당연히 무섭죠.”

“그런 것치고는 언행일치가 전혀 안 되는데?”

“무서운 거야 이미 익숙하거든요.”

“익숙하다고?”

“예. 그러니까 이게 뭐랄까. 전 항상 좀 겁이 많았어요.”

혁무진이 머쓱한 얼굴로 뒤통수를 벅벅 긁었다.

“어릴 때는 부모님의 사랑을 동생한테 빼앗기는 게 무서워서 매일같이 울었고, 어느 정도 크고 나서 무인이 되기로 마음먹었을 때는 검을 잡는 것만으로도 덜덜 떨리더라고요. 태원진가에 들어오면서 좀 나아졌다 싶었는데 조장님과 함께하고 난 뒤부터는…… 진짜 매일 오줌 지릴 것 같았고.”

처음 듣는 이야기다.

돌이켜 생각해 보면 나는 혁무진에 대해 이렇게 자세한 과거를 물어본 적이 딱히 없었다.

녀석이 삼대째 이어져 내려오는 대형 포목점의 장남이라는 것도 우연한 기회에 알게 되었던 거지, 굳이 알려고 하진 않았다.

아마도 그래서였을 것이다.

평소였다면 진작 딱밤 한 대와 함께 끊어 냈을 이 장황한 이야기가, 오늘따라 묘하게 더 듣고 싶어진 것은.

“……그랬는데, 뭐 어쩌다 보니 조장님 옆에 철썩 달라붙어 있게 됐네요.”

어깨를 으쓱하며 말을 끝맺은 혁무진이 문득 나를 바라봤다.

“이게 다 조장님 때문이에요.”

“나?”

“예. 이건 뭐 귀신도 아니고, 매번 사지(死地)만 찾아가시잖아요. 그 과정에서 하도 단련되다 보니까 이젠 무서운데도 무섭지가 않더라고요. 무슨 뜻인지 아시죠?”

“그래서, 많이 힘들었냐?”

“힘든 게 아니라 죽을 것 같았죠. 그런데 막상 죽진 않더라고요. 아니, 정확히는 죽을 것 같을 때마다 조장님께서 저를 구해 주셨어요.”

이번에는 아닐지도 몰라.

입 안에 맴도는 그 한마디를, 나는 꿀꺽 삼켰다.

그런 내 마음을 모르는 혁무진은 아무렇지 않게 말을 이어 가고 있었다.

“그래서 그런지 이번에도 딱히 크게 무섭지 않아요. 얼마 전에 저와 홍 동지한테 해 주신 이야기들을 들으면서도 마음이 담담하더라고요.”

“왜, 이번에도 당연히 내가 구해 줄 테니까?”

“아뇨.”

“아니라고?”

“네. 그냥 문득 어떤 생각이 들더라고요.”

순간. 혁무진이 나를 똑바로 바라보며 입을 열었다.

“아, 이번만큼은 내가 조장님을 구해 줄 수도 있겠구나, 하는 생각이요.”

“……!”

“위험하다면서요. 조장님이나 적 대협도 목숨을 걸어야 할 만큼. 사실상의 도박이나 다름없다고 그러셨잖아요. 그럼 이번만큼은 저 같은 하수도 도움이 되지 않겠어요?”

혁무진이 환하게 웃으며 덧붙였다.

“비록 한참 부족한 일류 나부랭이지만, 어려운 상황에서는 고양이 손이라도 빌린다는데. 안 그래요?”

나는 대답하지 않았다.

아니, 못 했다.

보이지 않는 손이 목줄기를 움켜쥔 것처럼 숨이 턱 막혀서.

지금 입을 열면 나도 모르게 진심을 내뱉는 실수를 할 것 같아서 그 어떤 대답도 할 수 없었다.

그래서 환하게 웃고 있는 녀석의 얼굴을 말없이 바라보다가, 그저 따라 웃었다.

“그래, 이제야 좀 도움이 되겠네.”

“엣헴. 이번에는 저만 믿으십쇼. 이 혁무진이야말로 조장님의 오른팔이자 심장. 태원진가의 십상남자 아닙니까.”

과장된 움직임으로 제 가슴을 퍽퍽 두드리는 혁무진을 보며, 나는 마음속에 남아 있던 모든 고민을 털어냈다.

그리고 확신했다.

지금부터 내릴 선택은, 모두 옳은 것이라고.

“이틀 전에 내가 했던 말. 기억해?”

입가에 감돌던 웃음을 지워 낸 혁무진이 고개를 끄덕했다.

“그중에 어떤 걸 말씀하시는지…….”

“무림맹의 원군.”

“아, 당연히 기억하죠. 그런데 조장님께서는 도대체 어느 틈에 무림맹과 연락을 주고받으신 겁니까?”

“그거야 중요한 게 아니니까 넘어가고. 임무 하나만 하자.”

“저 혼자서요?”

“아니, 화룡각 전원.”

“전원이라면…… 조장님도 함께 가십니까?”

“나는 제외야. 물론 스승님도. 넌 남은 인원들을 이끌고 내가 알려 주는 장소로 가서 대기하면 돼.”

“그곳에서 무림맹의 원군들과 접선하는 겁니까?”

“그래, 짧으면 한나절. 길면 내일 안에 도착할 거야.”

감 잡았다는 얼굴로 고개를 끄덕이던 혁무진이 문득 미간을 좁혔다.

“하지만 생각보다 오래 걸리는데요. 지금 같은 상황에서 자리를 비우는 건 좀…… 조장님 몸 상태도 평소 같지 않으시잖아요.”

“물론 평소 같진 않지. 그래서, 평소 같지 않은 초절정 고수가 당장 피거품 물고 쓰러질까 봐 무섭냐?”

혁무진이 씩 웃었다.

“하긴, 뱁새가 천응(天鷹)을 걱정했네요.”

“보통은 천응이 아니라 황새일 텐데.”

“열화신룡이면 천응도 부족합니다. 어쨌건 제게 맡기실 임무는 그것뿐입니까?”

“그래, 지금 당장.”

나는 대답과 함께 품에서 잘 접은 쪽지를 꺼내어 건넸다.

이미 이틀 전 준비해 두었던, 마지막까지 꺼낼까 말까 망설였던 물건이었다.

“나나 스승님이라면 모를까. 다른 사람들은 별다른 제약 없이 황궁을 빠져나갈 수 있을 거야. 미행이 따라붙지 않았다는 확신이 들면 그때 거기 적혀 있는 목적지를 확인해.”

“이러니까 꼭 화룡각이 아니라 은영각이 된 기분이네요.”

조심스럽게 종이를 받아 품에 잘 간직한 혁무진이 포권을 취했다.

“그럼 이만 가 보겠습니다.”

“마지막으로 하나만 더.”

“예?”

“몸조심해라. 너나, 다른 사람들 모두.”

어리둥절한 표정을 짓고 있던 혁무진이 장난스럽게 웃었다. 그리고 등을 돌려 사라졌다.

그리고 녀석의 기척이 완전히 멀어졌을 때, 천천히 방을 나선 나는 아직 남아 있던 한 사람과 마주했다.

후욱.

느릿하게 흘러나오는 숨결. 곰방대의 뿌연 연기 너머로 나를 바라보던 홍진이 문득 혼잣말처럼 중얼거렸다.

“혁 무인이 꽤 바빠 보이던데.”

“그럴 겁니다. 한 가지 임무를 맡겼거든요.”

“중요한 임무였나 보네요. 지금 같은 상황에서 보낼 정도라면.”

“네. 그렇죠.”

“그 마음, 충분히 이해해요.”

끼익.

낡은 나무 의자가 비명을 내지른다. 우아한 자세로 자리에서 일어난 홍진이 희끄무레한 연기와 함께 입을 열었다.

“어떻게 될지 모르는 이 위험한 도박판에서, 한 명이라도 더 살리고 싶을 테니까.”

“……!”

“그래서 진 공자, 준비는 됐나요?”

나는 쓴웃음과 함께 고개를 끄덕였다.

“언제나 준비는 되어 있었습니다.”

잠시 후, 우리를 대연회장으로 데려가기 위한 황금빛 갑옷들이 전각 앞에 도열했다.
```

## Final English reading copy

```markdown
# Chapter 898

Someone once said humans are creatures of adaptation.

But there’s always at least one thing in the world that no one can get used to, no matter how many times they experience it.

For me, one such thing was being responsible for other people’s lives. Another was waking up to someone’s ugly face.

“What are you doing?”

Hyuk Mujin answered, “I was checking on you, Captain.”

“Why?”

“You barred everyone from coming in and spent two whole days shut up in your room circulating your qi. I thought you might’ve suffered qi deviation, so I slipped in to check.”

“Two days?”

“Yes. You didn’t know?”

“No, I knew.”

That was a lie. I’d thought half a day had passed at most. I couldn’t believe it had been two whole days.

I looked toward the window, where sunlight streamed in, then sighed inwardly.

“I appreciate you worrying about me, but next time, just leave me alone.”

“Why?”

“Because seeing your face first thing when I woke up nearly gave me qi deviation.”

“Isn’t that a bit harsh?”

“Your face is harsh.”

“Then I’ll just stay nearby. You need someone to stand guard, don’t you?”

“Don’t stand guard, either.”

“Why not?”

“Your snoring will give me qi deviation.”

“……At this point, it’d be better if I just disappeared. Keep this up and I might get fed up and head back to the Jin Family on my own.”

I had just uncrossed my legs and was about to get up when I stared at Hyuk Mujin, who was putting on a show of threatening me.

“W-Why are you looking at me like that? Is there some rule that says I have to follow you around, Captain?”

He was talking tough, but his eyes kept darting nervously. A laugh escaped me.

Hyuk Mujin had been shrinking into himself, either to dodge the punch he never knew when I might throw, or to make sure it hurt as little as possible. Now he looked confused.

“What’s going on? Am I seeing things? Why are you acting like this all of a sudden, Captain?”

“Like what?”

“I mean, you’d normally have hit me at least twelve times by now, but you’re just smiling like some virtuous gentleman.”

I barely held back the laugh bubbling up inside me.

Then, in the next instant, I kicked off the floor and shot forward at lightning speed.

Whoosh!

Hyuk Mujin instinctively tried to defend himself. The movement he showed in that split second was so quick and composed, it was hard to believe he was still only a First Rate martial artist.

Of course, the fact that he was facing me meant his response had already failed.

“Hup.”

Realizing everything had gone wrong, Hyuk Mujin let out a strangled breath and squeezed his eyes shut. He was probably bracing for the usual bone-rattling blow.

But despite all that mental preparation, what he expected never happened.

Tap.

Instead of smacking him like I usually did, I lightly tapped the back of his head and clicked my tongue.

“You’ve been learning martial arts wrong all this time. Who told you to close your eyes?”

“……Huh?”

“Even if you’re getting hit, keep your eyes wide open. Even just keeping your eyes on your opponent puts you halfway there.”

Hyuk Mujin rubbed the back of his head, looking dazed, then blurted out, “Why are you acting like this all of a sudden?”

“Like what?”

“Isn’t it strange? Normally…”

“So, you want me to hit you like I usually do?”

Hyuk Mujin answered at once. “No. Not really.”

“Then shut up. I’m saving your strength.”

“Saving my strength?”

“Yeah. We’re going to be fighting like hell soon. Why would I hit you on the back of the head? If you get hit by some stray blade after that, I’ll have nightmares for nothing.”

Hyuk Mujin grinned.

“Ohhh. So that’s what it is. You could be a little more honest, you know.”

“What?”

“I know all about it. When I said I might leave, it bothered you, didn’t it, Captain? Right?”

I was about to say something, but all that came out was a quiet laugh.

“Yeah, you little shit. Must be nice to be so perceptive.”

“I knew it. I thought so. Even you need someone like me, your right-hand man, stuck to your side if you want to get anything done.”

“Right-hand man, my ass. You’re a little toe.”

“Now, why would you say that? Calling me your right-hand man is already a pretty big concession on my part.”

“A concession?”

“Yes. Where else are you going to find a subordinate as loyal as me? At this point, I’m not your right hand—I’m your heart. Your heart.”

“Not a chance. You’ve got balls, for crying out loud. How dare you?”

“Then if I get them removed, do I qualify?”

Whack!

This time I put a bit of force into it, but for some reason, Hyuk Mujin clutched the back of his head with a groan, looking happier than ever.

“Now that’s more like it.”

“……Huh?”

“It’s still a little weak, though. Hit me harder.”

What was with that creepy reaction?

As I began to question Hyuk Mujin’s tastes, he grinned and went on.

“It’s just… nothing special. You’ve been acting so different from usual that it was bothering me.”

“……!”

“I know you’ve had a lot on your mind lately, but it’ll all work out. So just keep doing what you’ve always done. Same as always.”

For a moment, I couldn’t speak.

At the same time, the truth I’d kept buried in my heart welled up and tickled the back of my throat.

But…

*I can’t.*

I couldn’t let myself speak while swept up in a passing emotion. To survive and win in this enormous gamble, crawling with monsters, I had to keep my words to myself.

In the end, after thinking it over, I managed to say only one thing.

“Aren’t you scared?”

“Hm? Scared of what?”

“This situation we’re in. And the unknown situation we’re about to face.”

Hyuk Mujin blinked for a long while after hearing me, then answered, “What kind of question is that? Of course I’m scared.”

“Your words and actions don’t seem to match.”

“I’m used to being scared.”

“You’re used to it?”

“Yes. How do I put it? I’ve always been kind of a coward.”

Hyuk Mujin scratched the back of his head, looking embarrassed.

“When I was little, I was afraid my parents’ love would go to my younger sibling, so I cried every day. Then, when I got a bit older and decided to become a martial artist, I’d tremble just from holding a sword. I thought I’d gotten better after joining the Jin Family of Taiyuan, but after I started going around with you, Captain… I really thought I’d piss myself every single day.”

That was the first I’d heard of it.

Thinking back, I’d never really asked Hyuk Mujin much about his past.

I’d only found out by chance that he was the eldest son of a huge textile shop that had been in his family for three generations. It wasn’t as if I’d gone out of my way to learn about him.

Maybe that was why.

Normally, I would’ve cut off this long-winded story with a flick to his forehead. But today, for some reason, I wanted to hear more.

“……Anyway, I wound up stuck to your side somehow.”

Hyuk Mujin finished with a shrug, then suddenly looked at me.

“This is all your fault, Captain.”

“Mine?”

“Yes. You’re like a ghost, always heading straight for places where people die. I got so much practice along the way that now, even when I’m scared, I don’t feel scared anymore. You know what I mean?”

“Then, was it hard for you?”

“It wasn’t hard. I thought I was going to die. But I never actually did. Or, to be more precise, whenever I thought I was going to die, you saved me.”

*Maybe not this time.*

I swallowed the words that had been circling in my mouth.

Unaware of what I was thinking, Hyuk Mujin continued speaking as if nothing were wrong.

“Maybe that’s why I’m not all that scared this time, either. Even when I heard what you told Comrade Hong and me recently, I felt pretty calm.”

“Because you figure I’ll save you again this time?”

“No.”

“No?”

“No. I just had a thought.”

For a moment, Hyuk Mujin looked straight at me and spoke.

“Oh, I thought, maybe this time I can be the one to save you, Captain.”

“……!”

“You said it was dangerous. That you and Great Hero Jeok might have to risk your lives. That it was basically a gamble. Then this time, couldn’t even a low-level fighter like me be useful?”

Hyuk Mujin added with a bright smile, “I may be a First Rate nobody, still a long way from good, but they say in a tough spot, even a cat’s paw will do. Right?”

I didn’t answer.

No, I couldn’t.

It felt as if an invisible hand had closed around my throat, cutting off my breath.

I was afraid that if I opened my mouth, I might accidentally let the truth slip out. I couldn’t manage any answer at all.

So I silently looked at his bright smile, then simply smiled back.

“Yeah. Now you’re finally going to be useful.”

“Ahem. This time, just trust me. I, Hyuk Mujin, am your right hand and your heart. I’m the Tenfold Man of the Jin Family of Taiyuan, aren’t I?”

Watching Hyuk Mujin thump his chest with exaggerated force, I let go of every worry still weighing on my mind.

And I was certain.

Every choice I made from here on out would be the right one.

“Do you remember what I told you two days ago?”

Hyuk Mujin’s smile faded as he nodded.

“Which part do you mean…?”

“The Murim Alliance reinforcements.”

“Oh, of course I remember. But when did you manage to get in touch with the Murim Alliance, Captain?”

“That’s not important, so forget it. I have a mission for you.”

“Just me?”

“No, the entire Fire Dragon Pavilion.”

“The entire pavilion means… you’re coming with us, Captain?”

“I’m not going. And neither is my Master. You’ll lead the rest of the group to the place I tell you and wait there.”

“Are we meeting the Murim Alliance reinforcements there?”

“Yeah. They’ll arrive within half a day at the earliest, and by tomorrow at the latest.”

Hyuk Mujin nodded as if he understood, then suddenly furrowed his brow.

“But that’s longer than I expected. Being away at a time like this is a bit… And you’re not in your usual condition, either.”

“I’m not. So, are you worried that a Supreme Peak master who isn’t in his usual condition might keel over, coughing blood, at any moment?”

Hyuk Mujin grinned.

“Right, I was a crow-tit worrying about a Heavenly Eagle.”

“Usually, it’d be a stork you were worried about, not a Heavenly Eagle.”

“With the Blazing Flame Divine Dragon, even a Heavenly Eagle isn’t good enough. Anyway, is that the only mission you’re giving me?”

“Yeah. Right now.”

I answered and took a neatly folded note from inside my robe, then handed it to him.

I’d prepared it two days ago, but until the last moment, I’d wavered over whether to take it out at all.

“People other than me and my Master should be able to leave the imperial palace without any particular restrictions. Once you’re sure no one’s following you, check the destination written there.”

“This is starting to feel less like the Fire Dragon Pavilion and more like the Hidden Shadow Pavilion.”

Hyuk Mujin carefully took the paper and tucked it away. Then he clasped his hands in a salute.

“I’ll get going, then.”

“One last thing.”

“Yes?”

“Be careful. You and everyone else.”

Hyuk Mujin, who’d been looking at me in confusion, gave a playful grin. Then he turned and disappeared.

When his presence had faded completely, I slowly left the room and came face to face with the one person still there.

Whoosh.

A slow exhalation. Hong Jin looked at me through the cloudy smoke of his long-stemmed tobacco pipe, then murmured as if to himself,

“Martial artist Hyuk seemed pretty busy.”

“He is. I gave him a mission.”

“It must be an important one, if you sent him off at a time like this.”

“Yes. It is.”

“I understand how you feel.”

Creak.

The old wooden chair let out a groan. Hong Jin rose with elegant poise and spoke through the faint haze of smoke.

“In a dangerous gamble where no one knows what will happen, you must want to save even one more person.”

“……!”

“So, Young Master Jin, are you ready?”

I nodded with a bitter smile.

“I’ve always been ready.”

A little while later, golden-armored guards lined up in front of the pavilion to escort us to the Grand Banquet Hall.
```
