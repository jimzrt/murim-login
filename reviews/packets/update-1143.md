<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1143.txt",
      "sha256": "4d26d59532a7480a5402fd233dac8d83437c7a1c97a541042e094fb6e42fa6d7",
      "bytes": 12862
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b93e59fd823f9900edeac3af24ec0cf378c2d90ad4a7481ecba21c98150f2910",
      "bytes": 1620
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b61b8a0a9dcce5092595d3312be12ffe6dc42f435a19d85546a1a78eb9063ca2",
      "bytes": 245855
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "e6853e4eca46ecfdf5de26559be236a8c5f317f776f67cf62cd8f90c5d56dd09",
      "bytes": 867
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b5f02a946c5a22cfb7dd0a0da6f604d100feba5bd4e9d14e6d9e51d887b193c3",
      "bytes": 1377
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "360557d698e9a3a03aeba7dae6eed37ee5a8f903c1a932ed43eda7e5fdd14961",
      "bytes": 509
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "6778d4a98f83d53e43f927c52cf3448c4af9dbd48b9d22bc864a35614cda5e3e",
      "bytes": 1583
    },
    {
      "path": "characters/The Helper.md",
      "sha256": "d0af447ee186c1502bffda3149eb8d094410da54ca851bf92a2881cd01290635",
      "bytes": 569
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "43439c3a04e26c1f05d2f90e119c4024c52f9919b19355186c9b78090a79fdc9",
      "bytes": 291243
    }
  ],
  "estimated_tokens": 9582
}
-->

# Durable State Update — Chapter 1143

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
1 and safe_through 1143. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1143. Profile updates may replace only one
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
  "chapter": 1143,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1143,
    "continuity_sources": [1143],
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
    "Murim forces from across the realm have gathered in Xining to fight the Lord of Heaven.",
    "The Son of Heaven survived by accepting the White Illusion Jiangshi Art and arrived in Xining with a hundred thousand Imperial Guards.",
    "The Son of Heaven enfeoffed Jin Taekyung as Prince Shangshan; Taekyung declined the offered title Prince of Ye.",
    "The Bow Saint says the Martial God’s final wish led her to search for the chosen one, whom she identified as Taekyung, the Player.",
    "Taekyung suspects Cheon Taemin and the Martial God are the same person; he theorizes the System may have treated Cheon’s unconscious state as death.",
    "The Helper saved Taekyung’s life and guided him to a higher level of enlightenment; Taekyung believes the Helper is more than part of the System.",
    "Jeok wears a pocket watch around his neck, which Taekyung notices."
  ],
  "continuity_sources": [
    1141,
    1142
  ],
  "open_questions": [
    "Are Cheon Taemin and the Martial God the same person, and how could Taekyung have acquired the capsule if so?",
    "What accounts for the time ratio between the modern world and Murim?",
    "Who is the Helper, and what is his relationship to the System?",
    "What is the significance of the pocket watch Jeok wears?",
    "What will happen in the campaign against the Lord of Heaven?"
  ],
  "safe_through": 1142,
  "temporary_decisions": [
    "Render 大明 as “Great Ming” and 親征 as “personal expedition.”",
    "Render 滅魔正天 as “Exterminate the Demons and Set Heaven Right.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 주화입마   | **qi deviation**                                 |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 제자     | **Disciple**                                 |
| 생도     | **cadet**                                    |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 로그인              | **Login**                      |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 도우미 | **The Helper** | Taekyung’s name for the mysterious being who first taught him to circulate qi. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 사자후 | **lion's roar** | Taekyung's term for Song Il's crowd-shattering roar. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 황하 | **Yellow River** | River along which civilization began. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |

## Listed compact profiles

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 1106
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger was a Demon Realm being capable of regenerating in new bodies and was erased by Jin Taekyung.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1138
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is deeply loyal to Taekyung, who trusts him as a close companion and values him as family, and has a warm friendship with fellow Fire Dragon Pavilion member Taishan; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung, and his parents own the Hyuk Family Textile Shop, which his younger sibling may inherit.

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 1135
- **Aliases:** Killing Ghost
- **Role:** Jang Sam is a bandit chief who abruptly rose from Level 40 to Level 60 and attacked Taekyung while apparently irrational; he is currently unconscious and being taken to the Nangong Family.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1142
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### The Helper.md

# The Helper (도우미)

- **Safe through:** Chapter 1142
- **Aliases:** None
- **Role:** A mysterious being who inhabits an enduring gray-white space and first taught Jin Taekyung to circulate qi.
- **Personality:** He chose to remain in his solitary prison and places his trust in Taekyung.
- **Voice:** Calm and instructive, he uses reflective questions and concise guidance.
- **Relationships:** He guided Taekyung from the beginning of his time in Murim and gave him an unidentified final gift.

## Korean source

```text
＃1143화



멈춰 있던 사고 회로가 정상 작동하기까지는, 총 세 단계에 걸친 준비 과정이 필요했다.

첫 번째는 대략 삼십 초 가량의 침묵.

두 번째는 물속 깊숙한 곳에서 울려 퍼지는 듯한 누군가의 먹먹한 외침.

그리고 마지막 대망의 세 번째.

후우웅!

성큼 가까워진 인영과 함께, 파공성을 일으키며 날아든 손바닥.

짝!

눈앞에 불빛이 번쩍인다.

흐려졌던 오감(五感)이 돌아오는 동시에 나도 모르게 참고 있던 숨이 헉, 하고 터져 나왔다.

“……신, 정신이 드느냐?”

나는 대답도 제대로 못 한 채 눈만 깜빡였다.

어느덧 코앞까지 다가온 적천강이 당황과 걱정이 뒤섞인 눈빛으로 나를 바라보고 있었다.

그의 장삼 사이로 슬쩍 모습을 드러낸 채, 마치 세 번째 눈동자라도 되는 것처럼 나를 노려보고 있는 어떤 물건도 함께.

“그, 그거. 저거.”

“뭐?”

“아니. 그, 어어…….”

사고 회로가 정상 작동하기는 개뿔이.

혀가 굳어 버린 나는 벙어리 삼룡이처럼 말을 잇지 못했고, 제자를 위해 다시금 손바닥을 들어 올리시는 스승님의 모습을 보고 나서야 가까스로 정신을 차릴 수 있었다.

“자, 잠깐!”

짜악!

아아, 드높기 그지없는 스승의 은혜에 고막이 울리는구나.

“……잠깐이라고 했잖아요.”

배신감에 물든 내 눈빛을 본 적천강이 움찔하며 대답했다.

“그게, 노부는 네가 주화입마(走火入魔) 직전인 줄 알고…….”

“아니, 진짜 주화입마였으면 더 조심히 다뤄야 하는 거 아닙니까?”

“직전이면 괜찮다. 이열치열 모르느냐?”

이 상황에 저게 맞는 표현인지는 모르겠지만, 여하튼 정작 중요한 건 따로 있다.

적천강으로 하여금 나를 주화입마 의심 단계까지 몰아가게 한 원흉이, 지금 이 순간에도 눈앞에서 천천히 흔들리고 있었으니까.

마치 최면이라도 거는 것처럼.

“그런데…… 그건 도대체 어디서 나신 겁니까?”

질문을 던지면서도 불안했다.

적천강의 목에 걸려 있는 저 생각지도 못한 물건이, 정말 내가 아는 그것이라면 도대체 이 사실을 어떻게 해석해야 하는지.

그리고 곧장 되돌아온 대답은, 내 가슴을 한층 무겁게 만들기에 충분했다.

“어디서 났냐니, 그걸 노부가 어찌 알겠느냐. 주인인 네놈이 가장 잘 알겠지.”

“……!”

“왜, 무슨 문제라도 있느냐?”

“아닙, 니다.”

가까스로 대답한 나는 즉시 마음속으로 뇌까렸다.

가장 확실한 방법이 있으니.

‘인벤토리 오픈. 소환.’

방법은 간단하다.

머릿속으로 이미지를 그리고, 어떤 방식이든 의지를 실어 명령을 하기만 된다.

그러나 수백, 수천 번도 넘게 반복하며 익숙해진 이 일련의 과정이 처음으로 낯설게 느껴졌다.

곧이어 허공에 떠오른 자그마한 시스템 창 역시도.

삐빅.



- [인벤토리]에 존재하지 않는 물품입니다.



염병.

작게 심호흡한 나는 애써 침착한 목소리로 입을 열었다.

“잠시 착각했습니다. 제가 갖고 있던 물건이 맞네요.”

“그럴 것 같았다. 노부도 일전에 몇 번인가 본적이 있으니. 한데 뭔가 사연이 있다거나, 중요한 물건인 모양이구나.”

“예?”

“열흘 전, 네 녀석이 의식을 잃고 쓰러진 바로 그 자리에서 발견한 것이다. 피 웅덩이에 잠겨 있던 걸 노부가 용케 알아봤지. 그토록 치열한 혈전을 치르는 와중에도 품고 있었던 걸 보니 챙겨야겠다 싶었던 거고.”

“……그렇습니까.”

“그나저나 이걸 뭐라고 부르는지 까먹었군. 회장? 화장 시계였나?”

나는 어느새 바싹 메말라 버린 입술을 핥았다.

“회중시계.”

“아, 그래. 저 멀리 바다 건너 양이(攘夷)들이 사용한다는 기물. 어쩐지 요상한 생김새라 그런지 제법 눈에 익더구나.”

사실 저 부분에 대해서는 그냥 주위에 듣는 귀가 많아서 대충 둘러댄 것뿐이다.

내가 파악한 바로는 애초에 이 세상부터가 오대양 육대주로 이루어진 것이 아닌데, 바다 건너에 사는 게 금발 태닝 양아치든 티라노사우루스든 어찌 알겠나.

그러나, 최소한 한 가지는 확실하게 알고 있다.

저 회중시계는, 이미 두 달이 넘도록 인벤토리 깊숙이 처박혀 있었다는 것.

‘내가 꺼낸 적이 있었나?’

단순한 기억의 오류?

절대 아니다.

애초에 저런 게 있었다는 것조차도 반쯤 잊고 있었는데 무슨.

‘말도 안 돼.’

그래, 이건 정말 말도 안 되는 일이다.

인벤토리는 오직 내 의지에 따라 열고 닫히는 무한의 창고.

하지만 저것, 정확한 명칭으로는 [누가 만들었는지 모를 회중시계]라 불리는 물건은 시스템이 정한 규칙을 벗어났다.

나조차도 인지 못 한 사이에.

“그렇지 않아도 요 며칠간 돌려준다는 걸 깜빡해서 아예 목에 걸고 다니던 참이었는데, 때마침 잘 됐구나.”

나는 무언가에 홀린 사람처럼, 적천강이 건넨 회중시계를 받았다.

그리고.

“……!”

불현듯 깨달았다.

아니, 기억해 냈다.



‘자, 이제 떠날 시간이다. 네가 머물러야 할 곳으로.’



마치 휘몰아치듯 어딘가로 빨려 들어가는 시야 속, 부드럽게 귓가에 닿았던 찰나의 음성을.



‘받아라. 이 늙은이가 줄 수 있는 마지막 선물이다.’



흐릿해지는 의식 너머, 본능적으로 움켜쥐었던 무언가의 단단한 촉감과 그것이 간직하고 있던 반짝임을.

‘도우미 노인.’

틀림없다. 이제야 비로소 선명히 기억났다.

끝없이 펼쳐져 있던 공허의 공간.

그곳에서의 마지막 순간, 그가 내게 준 것이 무엇이었는지.

꾸욱.

나도 모르게 힘주어 회중시계를 붙잡은 그 순간이었다.

띠링.



- 아이템 정보가 새롭게 갱신되었습니다!



[누가 만들었는지 모를 회중시계]의 새로운 정보를 확인하시겠습니까?

Y / N



* * *



시스템 창을 확인한 뒤, 나는 무거운 침묵에 짓눌렸다.

적천강과 함께 처소로 되돌아가는 길에도, 계단을 오르는 와중에도, 그리고 답답함을 이기지 못한 적천강의 채근에도 굳게 입을 다물었다.

아니, 미처 듣지 못했다.

이미 내 오감을 사로잡은 생각의 끈은, 그만큼 질기고 길었다.

‘뭘까.’

긴 시간이 흘러도 뇌리에 선명하게 남는 기억은, 크게 두 가지로 종류로 나뉜다.

끝내주게 좋은 기억이거나, 빌어먹게 나쁜 기억이거나.

그리고 그런 의미에서, 지금 내 손에 들린 이 회중시계는 명백히 후자에 해당했다.

이미 두 달이 넘는 시간이 흘렀음에도, 토씨 하나의 오차도 없이 똑똑히 기억할 만큼.



아이템창



[누가 만들었는지 모를 회중시계]

종류 : 일반 아이템

등급 : 無

제한 : 無

설명 : 알려지지 않은 누군가에 의해 제작된 회중시계. 매우 단단하다. 언뜻 보면 낡고 고장 난 시계 같지만, 자세히 보아도 고장 난 시계 같다.



마치 어제 일처럼 새록새록 떠오른다.

아이템 정보를 확인한 순간, 가슴 깊숙한 곳에서 용암처럼 솟구치던 그 날의 분노가.

‘잊을 수가 없지. 하도 개 같은 기억이라.’

그럴 수밖에 없는 게, 당시의 나는 잔뜩 기대에 부풀어 있었다.

일반 어중이떠중이 퀘스트도 아니고, 무려 [시스템 업데이트]의 보상으로 주어진 아이템이었으니까.

‘있는 줄도 몰랐던 그놈의 업데이트 때문에 개고생도 실컷 했고.’

현대에서 도플갱어를 쓰러트린 직후, 곧장 무림으로 향한 건 결코 내 의지가 아니었다.

갑작스럽게 시작된 시스템 업데이트는 나를 강제로 로그인 시켰고, 업데이트가 진행되는 동안 먹통이 된 시스템은 황궁에서의 사건을 마무리 지은 후에야 정상화되었다.

그런데, 그 수많은 억까를 겪고 나서 고작 이딴 폐기물을 보상으로 받은 내 마음이 어땠겠나.

‘그때 심정만 생각하면, 오히려 버리지 않은 게 이상할 정도지.’

보다 정확히는, 버리지 않은 게 아니라 버리지 못했다.

그래도 명색이 업데이트 보상인데, 숨겨진 뭔가가 있을 거라는 한 줌의 희망 때문에.

하지만 꺼져가는 불씨처럼 남아 있던 그 희망조차 완전히 전소(全燒)되기까지는, 그리 오랜 시간이 필요하지 않았다.

회중시계는…… 진짜 쓰레기였다.

자세히 봐도 더럽게 낡았고, 오래 보아도 고장이 난 게 분명한.

나는 국보급 유물을 대하는 진품명품 심사위원의 마음으로 끈질기게 관찰했지만, 추가로 발견한 특이점이라고는 뒷면에 적힌 희미한 문구 한 줄 뿐이었다.



고장 난 시계도 하루에 두 번은 맞는다.



하루에 두 번은 무슨.

일주일이 지나도록 제 자리에서 꿈쩍하지 않는 시계 초침을 확인한 나는, 이 단단하기만 한 쓰레기를 인벤토리 깊숙이 처박았다.

어떤 놈이 만든 물건인지는 몰라도, 내 눈에 띄면 뒤지게 쳐맞을 거라는 확신과 함께.

‘그런데…… 이게 여기서 다시 나온다고? 그것도 이런 식으로 불쑥?’

나는 가느다랗게 뜨인 눈으로 허공에 떠오른 홀로그램 창을 바라보았다.



아이템창



[누가 만들었는지 모를 회중시계]

종류 : 특수 아이템

등급 : 無

제한 : 無

설명 : 알려지지 않은 누군가에 의해 제작된 회중시계. 매우 단단하다. 언뜻 보면 낡고 고장 난 시계 같지만, 자세히 보면 알아내지 못한 비밀이 숨겨져 있다.



새롭게 갱신된 아이템 정보.

아니, 이 정도면 갱신이라는 표현이 민망할 정도다.

고작 활자 몇 개가 추가되거나 뒤바뀐 것뿐이니까.

‘아이템 종류, 거기에 더해 설명란의 마지막 한 줄.’

변화는 실로 미미했다.

일반 아이템이 특수 아이템으로, 그리고 ‘자세히 보아도 고장난 시계 같다.’라는 문구가 지워지고 새로운 정보가 추가된 게 전부다.

하지만 이 변화에 담긴 의미는, 결코 미미하게 느껴지지 않았다.

아무런 쓸모도 없던 이 폐품을 다시 손에 넣게 된 과정을 생각한다면 더더욱.

‘도우미 노인, 끝없는 무한의 공간, 마지막으로 회중시계.’

내가 머릿속을 가득 채운 이 세 가지 키워드를 끊임없이 되뇌이던 그때였다.

탁, 드득, 탁.

살짝 열린 문틈 새로 가까워지는 불규칙한 발걸음 소리와 함께, 초대받지 않은 손님이 도착한 것은.

“꺼으윽, 어후. 취한다.”

흡사 사자후와도 같은 용트림을 거하게 내뱉으며 등장한 유사 미이라, 아니 혁무진이 반쯤 풀린 눈으로 나와 적천강을 바라보았다.

“어이쿠, 여기 계셨슴미까. 헤헤.”

내가 뭐라 말하기도 전, 적천강이 점잖게 입을 열었다.

“취했으면 곱게 쳐 자거라. 뒤지게 맞기 싫으면.”

혁무진이 대답했다.

“시른데?”

“…….”

“…….”

말 한 마디로 나와 적천강을 이렇게 당황하게 만들 줄이야.

하지만 지금껏 그 어떤 대마두도 못한 위업을 달성한 혁무진은 거기에서 그치지 않았다.

“우웁.”

“어어, 하지마라…….”

“구에에에엑!”

“……하지 말라니까.”

이런 미친놈을 봤나.

나이아가라 폭포처럼 쏟아지는 토사물 앞에 적천강은 대경하며 물러섰고, 한숨을 푹 내쉰 나는 녀석의 등을 두드려 주었다.

그리고 한바탕 염병을 떤 혁무진이 고개를 들었을 때.

“어라, 이거 그 시계 아님니까. 드디어 저하테 주시는 검미까?”

내 목에 걸려있는 회중시계를 본 녀석이, 생각지도 못한 한 마디를 내뱉었다.

“긍데, 드디어 꼬치신 검미까?”

“미친놈이 갑자기 웬 고추 타령…… 잠깐, 뭐라고?”

“꼬치치신 거, 맞자나요.”

잔뜩 혀가 꼬인 발음으로 중얼거린 혁무진이, 눈앞에서 흔들리는 회중시계를 움켜잡으며 히죽 웃었다.

“맞능데. 마지막으로 봤을 때랑 시간이 다른데?”

“……!”

그러니까. 뭐라고?
```

## Final English reading copy

```markdown
# Chapter 1143

It took three steps to get my stalled brain back up and running.

First, roughly thirty seconds of silence.

Second, someone’s muffled shout, as if it were echoing from deep underwater.

And finally, the grand third step.

Whoosh!

A figure strode closer, and a palm came flying at me with a sharp whistle.

Smack!

Light flashed before my eyes.

As my dulled senses returned, the breath I’d unknowingly been holding burst out of me in a gasp.

“……A-are you back with us?”

I could barely answer. All I managed was a blink.

Jeok Cheongang had come right up to me, staring with a look that mingled confusion and concern.

And peeking out from the gap in his robe, as if it were a third eye, was an object glaring right back at me.

“T-that. That thing.”

“What?”

“No, I mean, uh……”

So much for my brain being back up and running.

My tongue had gone stiff. I couldn’t get the words out, like the mute Samryong. It wasn’t until I saw my Master raising his hand again—for his Disciple’s sake, naturally—that I finally came to my senses.

“W-wait!”

Smack!

Ah, the eardrum-rattling grace of a Master’s boundless kindness.

“……I said wait.”

Jeok Cheongang flinched at the betrayal in my eyes.

“I thought you were on the verge of qi deviation……”

“Wouldn’t you have to be more careful if I really were having qi deviation?”

“You’re fine if you’re only on the verge. Ever heard of fighting fire with fire?”

I wasn’t sure that was the right expression for this situation, but the real issue was something else.

The culprit who’d made Jeok Cheongang suspect I was on the verge of qi deviation was still swaying before my eyes.

As if trying to hypnotize me.

“By the way…… where did you get that?”

Even as I asked, I felt uneasy.

If that unexpected object hanging around Jeok Cheongang’s neck really was the one I knew, how was I supposed to make sense of it?

The answer came right back, and it was enough to make my heart feel even heavier.

“Where did I get it? How would this old man know? You’re the owner. You’d know best.”

“……!”

“What? Is something wrong?”

“N-no.”

I managed to answer, then immediately muttered to myself.

There was one surefire way to find out.

*Open Inventory. Summon.*

It was simple.

I just had to picture it in my mind and issue a command with enough intent behind it.

But this sequence of actions, one I’d repeated hundreds—no, thousands—of times, suddenly felt unfamiliar.

So did the small System window that appeared in the air.

*Beep.*

> **System**
>
> This item does not exist in your **Inventory**.

Shit.

I took a small breath and forced myself to speak calmly.

“I was mistaken. It is mine.”

“That’s what I thought. I’ve seen it a few times before, too. Still, it must have some story behind it. Or it’s important to you.”

“Excuse me?”

“I found it ten days ago, right where you’d collapsed unconscious. It was lying in a pool of blood, but luckily I recognized it. You’d carried it through such a fierce battle, so I figured I ought to keep it safe.”

“……I see.”

“Come to think of it, I’ve forgotten what it’s called. Chairman? Was it a makeup watch?”

I licked my lips, which had gone dry.

“A pocket watch.”

“Ah, right. One of those foreign devices used by the barbarians across the sea. It has such an odd shape that it stuck in my mind.”

The thing about barbarians across the sea was just an excuse. There were too many people around to tell him the truth.

As far as I could tell, this world wasn’t even made up of five oceans and six continents. How would I know if there were blond, tanned punks or tyrannosaurs living across the sea?

But there was at least one thing I knew for certain.

That pocket watch had been buried deep in my Inventory for more than two months.

*Had I taken it out?*

A simple mistake in my memory?

Absolutely not.

I’d half forgotten the thing even existed. How could I have taken it out?

*This makes no sense.*

Right. This really made no sense.

The Inventory was an infinite storehouse that opened and closed only at my will.

But that thing—more precisely, the item called **[Pocket Watch of Unknown Make]**—had somehow broken the System’s rules.

Without me even realizing it.

“I meant to give it back these past few days, but kept forgetting, so I started wearing it around my neck. Good timing, eh?”

I took the pocket watch Jeok Cheongang handed me as if I were under a spell.

And—

“……!”

It suddenly came back to me.

*“All right. It’s time to go. To the place where you belong.”*

That fleeting voice, gentle against my ear, as my vision was swept away and pulled toward somewhere unknown.

*“Take it. It’s the last gift this old man can give you.”*

The hard feel of something I’d instinctively clutched beyond the haze of my fading consciousness, and the glimmer it held inside.

*The Helper.*

There was no doubt. At last, I remembered clearly.

The endless, empty space.

What he’d given me in that place, in our final moments together.

Squeeze.

It happened as I gripped the pocket watch without thinking.

*Ding!*

> **System**
>
> Item information has been updated!
>
> Would you like to view the new information for **[Pocket Watch of Unknown Make]**?
>
> **Y / N**

* * *

After checking the System window, I was weighed down by a heavy silence.

I kept my mouth shut on the way back to our quarters with Jeok Cheongang, as we climbed the stairs, and even when he prodded me, unable to stand the silence.

No—I hadn’t heard him.

The thread of thought holding my senses captive was that long and that tough.

*What is it?*

Memories that remain vivid in the mind long after the years have passed fall into two broad categories.

The unbelievably good kind, or the goddamn awful kind.

And in that regard, the pocket watch in my hand clearly belonged in the latter.

Even after more than two months, I remembered it so clearly that I could recall every last word.

**Item Window**

**[Pocket Watch of Unknown Make]**

**Type:** Common Item  
**Grade:** None  
**Restrictions:** None  
**Description:** A pocket watch made by someone unknown. Extremely sturdy. At a glance, it looks like an old, broken watch. Even on closer inspection, it looks like a broken watch.

The memory came back as fresh as yesterday.

The moment I checked the item information, the anger that had surged from deep in my chest like lava.

*How could I forget? It was such a goddamn awful memory.*

Of course it was. Back then, I’d been bursting with anticipation.

This wasn’t some ordinary run-of-the-mill Quest. The item had been given to me as a Reward for a **[System Update]**.

*I’d gone through all that shit because of an update I didn’t even know existed.*

Right after defeating the Doppelganger in the modern world, I’d been sent straight to Murim. It hadn’t been my choice.

The System Update had started without warning and forced me to Log In. The System stayed dead throughout the update, only returning to normal after I’d wrapped up the events in the imperial palace.

And after going through all that bullshit, how do you think I felt when I got this piece of trash as my Reward?

*Considering how I felt back then, it’s a miracle I didn’t throw it away.*

More accurately, it wasn’t that I didn’t throw it away. I couldn’t.

It was an update reward, after all. I’d held onto a sliver of hope that it might have some hidden use.

But it didn’t take long for that last flicker of hope to burn out completely.

The pocket watch was…… actual garbage.

It was filthy and worn no matter how closely I looked, and clearly broken no matter how long I stared.

I examined it like a judge on an antiques appraisal show scrutinizing a national treasure, but the only unusual thing I found was one faint line inscribed on the back.

*A broken clock is right twice a day.*

Twice a day, my ass.

After a week of watching the second hand stay exactly where it was, I shoved this sturdy piece of trash deep into my Inventory.

I was sure that whoever made it would get the shit beaten out of him if he ever showed his face.

*But…… why is it showing up here again? And like this, out of nowhere?*

I narrowed my eyes at the holographic window floating in the air.

**Item Window**

**[Pocket Watch of Unknown Make]**

**Type:** Special Item  
**Grade:** None  
**Restrictions:** None  
**Description:** A pocket watch made by someone unknown. Extremely sturdy. At a glance, it looks like an old, broken watch. On closer inspection, it seems to hold a secret I have yet to uncover.

The newly updated item information.

Actually, calling this an update seemed a little generous.

Only a few characters had been added or changed.

*The item type, and the last line of the description.*

The change was tiny.

It had gone from a Common Item to a Special Item, and the sentence “Even on closer inspection, it looks like a broken watch” had been replaced with new information. That was all.

But the meaning behind that change didn’t feel small at all.

Especially when I thought about how I’d gotten this useless piece of junk back.

*The Helper. The endless, infinite space. And finally, the pocket watch.*

I kept repeating those three keywords in my head, which was already crowded with thoughts, when—

Tap, scuff, tap.

A set of irregular footsteps drew closer through the slightly open door, and an uninvited guest arrived.

“Buuuurp. Whew. I’m drunk.”

A near-mummy—no, Hyuk Mujin—appeared with a burp like a lion’s roar and looked at Jeok Cheongang and me through half-lidded eyes.

“Well, well, you’re here, are ya? Hehe.”

Before I could say anything, Jeok Cheongang spoke in a dignified tone.

“If you’re drunk, go sleep it off. Unless you want a sound beating.”

Hyuk Mujin answered.

“Nah.”

“……”

“……”

Who knew one word could leave both me and Jeok Cheongang so dumbfounded?

But Hyuk Mujin, who’d just accomplished what no great fiend had ever managed, didn’t stop there.

“Uuugh.”

“Hey, don’t you dare……”

“Bwaaaaargh!”

“……I said don’t.”

What the hell was wrong with this guy?

Jeok Cheongang recoiled in alarm before the torrent of vomit, pouring down like Niagara Falls. I sighed and patted Mujin on the back.

Then, after he’d finished making a whole scene, he lifted his head.

“Huh? Isn’t this that watch? Are ya finally givin’ it to me?”

He spotted the pocket watch around my neck and came out with something I never would’ve expected.

“But did ya finally get it up and running?”

“You crazy bastard, why are you talking about getting it up all of a sudden—wait, what did you say?”

“You fixed it, didn’t ya?”

With his tongue thoroughly twisted, Hyuk Mujin mumbled and grinned as he grabbed the pocket watch swaying before him.

“’Course ya did. It’s showing a different time than the last time I saw it.”

“……!”

What did he just say?
```
