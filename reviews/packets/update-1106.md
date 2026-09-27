<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1106.txt",
      "sha256": "0606b3933cd12152cf039cd1558f60efd8baf3ff8e9d549cdf2a4b5171aa14ab",
      "bytes": 13036
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "abdd32dd43a796c49d681fe6db3ca8470271a00884fda2c5ae1f2e06792342b0",
      "bytes": 1417
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2195176fcecc1f2d4760ffbc4a2601370e7609089bc148ea8deda43236c266fc",
      "bytes": 244248
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "4b1aa0e382af4da82ebf9712a511afb93b2c19b9173c769aae3a2ad94f70f235",
      "bytes": 848
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3639c6eb3bee3365c0350bfb6fd0f8c3fb9a9ad984554e620aa01d04f7eaeac9",
      "bytes": 760
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "948480af84682cb42e21ec39f611562eb0cff7e4438b7eb815cc57ddff99bcea",
      "bytes": 866
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "043e361d5ff58dba89c06343bee002cf06edccdc945997cb7b22df324e0d9575",
      "bytes": 1513
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "5601de6a0e5bf016eac8aa2488fe2a23c2524189d2a4a1306cb2fb2ca69224cc",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3587b35f9f46255635c2b9217320b6613dd49879b3cf950be82def2526ffc095",
      "bytes": 288328
    }
  ],
  "estimated_tokens": 9902
}
-->

# Durable State Update — Chapter 1106

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
1 and safe_through 1106. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1106. Profile updates may replace only one
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
  "chapter": 1106,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1106,
    "continuity_sources": [1106],
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
    "Dark Heaven and the Potala Palace are attacking Xining; fighting continues at the breached western wall.",
    "The Blood Lord’s blast at the West Gate sends a shock wave as far as the North Gate; Jeok Cheongang considers the Blood Lord stronger than during their Mount Song encounter.",
    "Taekyung chose to face the enemy at the West Gate, where the Blood Lord’s main force is positioned; Jeok remains at the North Gate to face the Potala Palace forces.",
    "The Dalai Lama and Potala Palace forces have joined the battle at the North Gate, where Jeok faces the Dalai Lama, the Twelve Secret Monks, two Black Ghosts, and the advancing army.",
    "Jeok fears for Taekyung but draws resolve from Taekyung’s refusal to turn away from fear."
  ],
  "continuity_sources": [
    1104,
    1105
  ],
  "open_questions": [
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Who are the allies approaching by river from the east?",
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?",
    "What happened to Cheongpung after he intercepted the attack?"
  ],
  "safe_through": 1105,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 암천     | **Dark Heaven**                  |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 귀가      | **your family**                                                 |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백주 | **baijiu** | Strong distilled liquor ordered at the inn. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 천산산맥 | **Tianshan Mountains** | Mountain range associated with the Demonic Cult. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 일기당천 | **One Against a Thousand** | Title that temporarily increases Taekyung’s attributes and Intimidation when facing many enemies. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 서문 | **West Gate** | One of the Nanman Beast Palace's gates. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 마조 | **Demon Bird** | Title given by the revealed impostor who wore Chinggen’s face. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1105
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality.
- **Personality:** Cunning and controlling, he avoids costly risks while manipulating allies; beneath his devotion to the Lord of Heaven, he resents being treated as disposable and resents Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven but suspects the Lord wants Jin Taekyung above all else; despite that, he attacks Taekyung, whom he considers a formidable adversary, as well as Cheongpung.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1105
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 994
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger was a Demon Realm being capable of regenerating in new bodies and was erased by Jin Taekyung.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1105
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1104
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1106화



꽈앙!

눈 앞을 가리는 섬광이 피처럼 붉다.

퍼어엉!

일격, 일격에 담긴 아득한 힘이 들끓는다.

콰드드득!

세상이 끊임없이 뒤집히며, 바로 서기를 반복한다.

아니, 세상이 아닌 내가.

쐐애애액, 쾅!

등줄기를 찌르르 울리며 전신으로 퍼져나가는 거대한 충격.

그리고 벼락처럼 펼쳐진 수십 합의 공방이 낳은 결과는, 층층이 쌓인 성벽의 잔해 깊숙이 처박힌 나 자신의 모습이었다.

쿨럭.

내 의지와는 달리 울컥 솟구친 핏물이 입술을 비집고 흘러나온다.

귓가에는 이명(耳鳴)과 함께 찾아온 시스템 경고음이 맴돌고, 몸뚱어리 구석구석에서 전해지는 통증은 그것이 결코 거짓이 아님을 증명하고 있었다.

‘분명히, 무슨 소리를 들었던 것 같은데.’

나는 마음속으로 힘없이 뇌까렸다.

맹공에 의해 튕겨 나가기 직전, 찰나의 순간 저 멀리서 울려 퍼졌던 누군가의 익숙한 목소리를 떠올리며.

하지만 아무래도 환청이었던 모양이다.

지치고 힘들 때마다 한 번씩 찾아오고는 하는, 그런 환청.

“……빌어먹을.”

계속해서 핏물이 차오른다. 찢겨나간 손아귀가 저릿하다.

그럼에도 불구하고, 나는 나직한 욕설과 함께 욱신거리는 몸을 일으켜 세웠다.

아니, 그래야만 했다.

내가 아니라면, 지금 이 순간에도 목숨을 걸고 서문을 지키고 있는 수천 명의 아군 중 그 누구도 저 괴물 같은 놈을 막을 수 없을 테니까.

철벅, 철벅.

빠르지도, 느리지도 않은 무거운 발걸음이 이곳을 향해 다가온다.

더불어 그렇게 나아가는 걸음마다, 쏟아지는 빗줄기에 뒤섞여 발목까지 출렁이던 핏물이 살아 있는 생물처럼 부르르 몸을 떨었다.

촤아아악.

그건 보는 이로 하여금 등골을 얼어붙게 만드는 광경이었다.

머리부터 꼬리까지, 온통 붉게 물든 수백 마리의 뱀이 수면 위를 미끄러지는 듯했으니까.

그리고 그 섬뜩한 움직임의 끝에는, 이미 새로운 힘을 받아들일 준비를 끝낸 어느 괴물이 있었다.

스아아아.

마치 처음부터 존재하지 않았다는 듯 피부 위로 스며드는 핏물.

뒤이어 더욱 강렬해진 괴물의 핏빛 안광(眼光)이, 거센 빗줄기 너머에서 번뜩였다.

석상처럼 굳어버린 수많은 아군 속 오직 단 한 사람, 바로 나를 향해.

“분명 말하지 않았더냐.”

낮게 깔린 음성이 또렷하게 귓가를 파고든다.

반경 십여 장에 존재하는 모든 핏물을 흡수하고, 그 안에 담겨 있던 생명력과 힘을 집어삼킨 피의 괴물이 희열 어린 눈빛으로 나를 응시했다.

“네놈은 결코 내 상대가 될 수 없어. 아니, 이 전장의 그 누구라도.”

무림이라는 험난한 도산검림 속에서 긴 세월을 살아남은 노강호들은 말한다.

자신감이 과하면 자만과 오만이, 그마저도 넘어선다면 광오함이 되니 이와 같은 감정을 가장 경계하라고.

만약 눈앞의 적이 그러한 감정들에 휩싸여 있다면, 그것을 약점으로 삼아 생로(生路)를 열라고.

이는 무림인들 사이에서는 일종의 격언(格言)처럼 전해져 내려오는 말이었고, 적천강 역시 내게 종종 비슷한 조언을 건네기도 했다.

하지만.

‘결코, 자만 따위가 아니다.’

나는 본능적으로 알 수 있었다.

아니, 저 괴물과 직접 맞서고 있는 나였기에 그 누구보다 잘 알 수밖에 없었다.

저건 오만도, 광오함도 아닌 확신이었다.

천하의 그 누구보다 무수한 가능성과 변수를 만들어 온 나조차도 감히 부정할 수 없는.

진정한 의미로의 혈주(血主)로 거듭난 괴물이, 오늘 이 전장의 그 누구보다도 거대한 힘과 존재감으로 사방을 짓누르며 다가오고 있었다.

드드드득.

주위의 공기가, 지면이 뒤흔들렸다.

미친 듯이 쏟아지던 폭우도, 아직 완전히 무너지지 않은 성벽 위의 궁수들이 용기를 쥐어짜 내어 쏘아 보낸 화살들도 놈의 털끝 하나 건드리지 못했다.

그저, 괴물의 심기를 건드렸을 뿐이었다.

우우웅.

마치 보이지 않는 손에 의해 붙잡히기라도 한 듯, 혈주의 머리 위 허공에 멈춰 몸을 부르르 떨던 일백여 개의 화살촉이 돌연 고개를 돌렸다.

절대자를 향해 가까워진 괴물의 앞길을 감히 막아선, 죽어 마땅한 벌레들을 향해서.

“피해!”

본능에 가까운 외침이 입술 사이로 터져 나온 그 순간.

슈확! 푸푸푸푹!

한 줄기로 합쳐진 맹렬한 파공성과 함께, 섬광처럼 번뜩인 화살들이 공간을 관통했다.

철을 덧씌운 방패로 궁수들을 보호하던 방패병들도, 그 뒤에 엄폐하고 있던 궁수들도.

나아가는 경로에 놓인 그 모든 것을.

쿵.

가장 선두에서 지휘하던 부대장이 무릎을 꿇은 것이 시작이었다.

그들 모두는 멍한 눈빛으로 서로를 바라보았다.

믿을 수 없다는 듯이 부릅뜬 채, 각자의 몸뚱어리에 새겨진 커다란 구멍과 수십여 장 밖에 우뚝 서 있는 괴물을 번갈아 바라보다가 이승에서의 마지막 숨결을 내뱉었다.

“이, 이건 말도 안…….”

털썩, 투두둑.

피와 빗물 위로 하나둘씩 쓰러지는 시신들.

누군가는 공포에 휩싸여 뒷걸음질 쳤고, 누군가는 죽음을 부정하며 나아가고자 했으며, 누군가는 단말마조차 남기지 못하고 선 채로 허물어졌다.

그들이 죽음을 맞이하는 방식은 제각각이었으나, 그 누구도 죽음이라는 운명을 피할 수는 없었다.

그렇게 모두가 죽었다.

궁수와 방패병. 무림인들까지 포함되어 있던 이백여 명의 아군이.

그것도 단 한 순간에.

스르륵, 철퍽!

성벽 아래로 굴러떨어진 이름 모를 누군가의 몸뚱어리가 피 웅덩이 위로 처박힌 그 순간.

“천상천하.”

사방에 내려앉은 숨 막히는 정적 속.

어느덧 혈주의 등장과 함께 무너져 버린 전열과 성벽의 잔해를 넘어 진입한 암천의 교도들이, 홀린 듯한 목소리로 그들만의 교언을 읊기 시작했다.

“만마앙복.”

이제 더 이상, 놈들은 고함을 내지르지 않았다.

성벽을 넘기 위해 발악하며 내뿜던 살기(殺氣) 또한, 더는 찾아볼 수 없었다.

서걱!

그들은 그저 묵묵히 각자의 손에 쥔 날붙이를 휘둘렀고.

“천상천하……!”

하나 같이 황홀함에 물든 얼굴로 자신들의 눈앞에서 벌어진 이 놀라운 이적(異蹟)에 감격했으며.

“만마앙복……!”

지금 이 전장에 없는, 그럼에도 저 짙은 어둠 속에서 천하의 모든 것을 무릎 꿇릴 수 있는 유일무이한 지배자를 찬미했다.

설령 그 끝에 죽음이 기다리고 있을지라도.

퍼걱!

“천, 크륵. 천주시여.”

눈먼 칼에 맞아 목울대가 베어져도, 팔과 다리가 날아가도, 가슴이 관통되어도 놈들은 결코 입가에 새긴 웃음을 잃지 않았다.

지금 이 순간, 한 치의 두려움도 없이 내게 달려들었던 십여 명의 광신도들 역시 마찬가지였다.

“드, 드디어. 순교(殉敎)의 영광을…….”

푸푹! 콰드득!

결국 피륙으로 이루어진 인간인 이상, 머리가 사라진다면 더는 말을 할 수 없다.

이는 목숨을 담보로 한계 이상의 힘을 발휘하는 잠력단(潛力團)이 아니라, 그 무엇을 복용한다 해도 마찬가지다.

하지만 어째서일까.

수도(手刀)를 휘둘러 놈들의 목을 단숨에 날려 버렸음에도, 지금 내 귓가에는 미처 끝맺어지지 못한 조금 전의 음성이 이어지고 있는 듯했다.

계속해서. 단 한 시도 끊임없이.

“이런…… 미친 새끼들.”

어느새인가 가빠진 숨결 속, 나도 모르게 욕설이 터져 나왔다.

전신의 피가 차갑게 얼어붙는 듯한 기분이다.

정신 나간 놈들이라면 이미 이골이 날 정도로 보고 겪었다고 생각했다.

내가 나고 자란 21세기의 현대는 바로 이곳, 무림과는 또 다른 야만을 간직하고 있는 세상이니까.

구름 위에 솟은 마천루가 즐비하고, 인류가 우주를 향해 나아간 지 어언 반세기도 넘는 세월이 흘렀으며, 최첨단 과학과 마법이 결합 된 문명은 그 어느 때보다 눈부시고 강력하게 거듭났지만 달라지는 건 없다.

아직도 현대에는 미친놈이 즐비하다.

해가 중천에 뜬 백주대낮에 살인이 일어나고, 판사의 법봉과 기자의 카메라는 돈과 술의 무게에 흔들린다.

뿐인가.

구시대의 유산과도 같은 독재자들은 전쟁을 준비하고, 또한 일으킨다.

저마다의 종교와 종파 간의 거리를 용서와 화해대신, 미사일과 테러로 메우려는 놈들도 한 무더기다.

이렇듯 내가 지켜본 세상 속에서는, 그들 모두가 광신도였다.

저마다의 목적에 맹목적인 가치를 두느라 정신이 나가버린. 원하는 것만 보고 느끼며 그것에 한껏 취해 비틀거리는 미친놈들.

물론 그중에서도 가장 압권이었던 것은 도플갱어를 따르던 광신도들이었지만, 지금 나는 감히 단언할 수 있었다.

과거 그들에게서 보았던 광기의 크기와 순도는, 눈앞의 저 암천의 교도들에 비하면 새 발의 피나 다름없다고.

그리고 이 광기에 휩싸인 피바람의 중심에는, 태산(太山)과도 같은 기세로 쏘아지는 괴물이 있었다.

“부나방을 본 적이 있나?”

느껴졌다.

여유롭지만, 결코 방심하지 않는 혈주의 태도가.

사방 곳곳에서 벌어지는 난전(亂戰) 따위는 관심조차 없다는 듯, 오직 나만을 응시하는 붉은 눈동자는 확신과 살기로 가득 차 있었다.

“나는 보았다. 천산산맥(天山山脈)이 그분의 지배하에 놓이기 이전에 수도 없이 보았지. 횃불에 달려든 그 멍청한 놈들이 불타 죽는 꼬락서니를.”

나는 대답하지 않았다.

대신 손아귀에 쥐고 있던 백염의 창대를 발치에 깊숙이 박아 넣고, 그 즉시 주위에 널브러진 병장기들을 발로 차올려 놈을 향해 쏘아 보냈다.

쐐애애액, 콰앙!

콰드드득!

강기가 실린 날붙이들이 차례차례 공간을 가르고, 곧이어 굉음을 동반한 엄청난 충격파가 공간을 후려쳤다.

본래의 목표였던 혈주가 아닌, 허공과 지면 어딘가에서.

“한데, 어느 날에는 부나방들을 보던 중 문득 그런 의문이 들더군.” 

섬광과도 같은 속도로 적도(赤刀)를 휘둘러, 날아드는 모든 것을 대수롭지 않게 쳐낸 놈이 또렷한 음성으로 말을 이었다.

“저놈들은 불에 타 죽을 것을 알면서도 횃불에 달려드는 것일까? 아니면 모르기에 달려들 수밖에 없는 것일까.”

퍼걱!

나는 곳곳에서 달려드는 적들을 베어 갈랐다. 무너진 성벽에 이어, 이제는 전열마저 빠르게 허물어지고 있었다.

순교를 부르짖으며 달려드는 광신도들의 모습이, 그로 인한 공포의 물결이 일기당천의 효과마저 짓누르고 있었다.

“그 의문에 대한 답은 아직도 찾지 못했다. 아니, 굳이 찾지 않았지. 나는 그리 오래되지 않아 그분을 만났고, 부나방의 심정 따위를 생각하지 않아도 될 만큼 강대한 힘을 얻었으니까.”

그 순간.

후우우우웅!

혈주의 손을 따라 높게 들어 올려진 적도의 시뻘건 도신 위로, 거대한 강기가 솟구쳤다.

지금껏 본 적 없는, 존재하리라고 생각해 본 적 없는 미증유의 기운이.

“하지만, 지금의 네놈이라면 그 답을 알 수 있을 것 같군.”

스스로에 대한 확신. 

칼날과도 같은 살기. 분노를 넘어선 증오. 마침내 목적을 이룰 수 있다는 희열.

그 모든 감정이, 기세와 힘이 오직 나를 향하고 있었다.

나도 모르게 숨이 막힌다. 손이 떨렸다.

하지만 준비했다.

내가 할 수 있는 최고의, 어쩌면 최후의 일격을.

그리고 크게 심호흡하며, 혀끝에서 맴돌던 한마디를 토해 냈다.

“난 그중에 없어.”

“뭐?”

“불길에 달려들어도 안 뒈지는 새끼. 모르건 알건 우선 달려들고 보는 새끼. 그게 나다.”

“……!”

영원과도 같았지만, 찰나였던 침묵. 

그 끝자락에서 혈주가 대답했다.

아니, 움직였다.

나 역시도.

팟.

단숨에 지워지는 십여 장의 공간 너머, 놈의 적도가 거대한 핏빛 선을 그렸다.
```

## Final English reading copy

```markdown
# Chapter 1106

*BOOM!*

The flash before my eyes was blood-red.

*Pwoom!*

Every strike carried an unfathomable force, churning through the air.

*Krrrunch!*

The world kept turning upside down, then righting itself.

No—not the world. Me.

*Fwoooooosh—BOOM!*

A tremendous shock ran up my spine, then spread through my entire body.

And the result of dozens of exchanges, unfolding like lightning, was me buried deep beneath layers of fallen stone from the wall.

*Cough.*

Blood surged up against my will and seeped past my lips.

A System warning chime rang in my ears along with the ringing in them, and pain radiating from every corner of my body proved it was no lie.

*I’m sure I heard something.*

I muttered weakly to myself.

Just before the assault sent me flying, I’d heard someone’s familiar voice ringing out in the distance for a brief instant.

But I must have imagined it.

One of those hallucinations that came to me every now and then when I was exhausted and hurting.

“……Damn it.”

Blood kept welling up. My torn-up hands tingled.

Even so, with a quiet curse, I forced my aching body upright.

No. I had to.

If I didn’t stop that monster, none of the thousands of allies risking their lives to defend the West Gate could.

*Splash. Splash.*

Heavy footsteps approached, neither fast nor slow.

With every step, the blood that swirled ankle-deep in the downpour trembled like a living thing.

*Shhhhhh.*

It was enough to make anyone who saw it feel a chill run down their spine.

Hundreds of snakes, red from head to tail, seemed to slide across the surface of the water.

And at the end of their eerie advance stood a monster, already prepared to take in new power.

*Hssss.*

The blood seeped into his skin as though it had never been anywhere else.

Then the monster’s eyes glowed an even fiercer red, flashing through the pounding rain.

They were fixed on a single person among the countless allies frozen like statues.

Me.

“Didn’t I tell you?”

His low voice cut clearly through the rain.

The monster of blood had absorbed all the blood within a radius of more than a hundred feet, devouring the life and strength it contained. He fixed his gaze on me, eyes bright with delight.

“You can never be my equal. No one on this battlefield can.”

The veterans who’d survived for years in Murim, a mountain of sabers and a forest of swords, had a saying.

Confidence could turn into conceit and arrogance—and beyond those lay sheer hubris. Those were the feelings you had to watch out for most.

If an enemy was swept up in them, you were supposed to seize on that weakness and find a way to survive.

It had passed down among martial artists like a maxim, and Jeok Cheongang had often given me similar advice.

But—

*This isn’t conceit.*

I knew it instinctively.

No—I was the one facing that monster, so I couldn’t help but know better than anyone.

This wasn’t arrogance, or hubris. It was certainty.

A certainty even I, who had created more possibilities and variables than anyone under heaven, couldn’t deny.

The monster who had become the true Blood Lord was approaching, his power and presence crushing everything around him—greater than anyone else on this battlefield.

*Krrr.*

The air trembled. The ground shook.

Neither the torrential rain nor the arrows that the archers on the still-standing parts of the wall had summoned the courage to loose could touch a hair on his head.

They had only managed to provoke him.

*Vmmmm.*

As if caught by an invisible hand, the hundred or so arrows hovering above the Blood Lord’s head suddenly trembled and turned around.

Toward the insects who deserved to die for daring to bar the path of a monster who had drawn close to the absolute ruler.

“Get out of the way!”

The instinctive cry burst from my lips.

*Fwhoosh! Thud-thud-thud!*

With a single, ferocious roar, the arrows flashed through the air like streaks of light.

The shield-bearers protecting the archers with their iron-plated shields. The archers taking cover behind them.

Everything in the arrows’ path.

*Thud.*

It began with the unit commander at the front dropping to one knee.

They stared blankly at one another.

Eyes wide with disbelief, they looked back and forth between the huge holes torn through their bodies and the monster standing hundreds of feet away. Then they breathed their last.

“T-This can’t be……”

*Thump. Clatter.*

One by one, bodies fell onto the ground slick with blood and rain.

Some stumbled backward in terror. Some tried to advance, refusing to believe death was coming. Some crumpled where they stood without even a final cry.

Each met death in a different way, but not one of them could escape it.

They all died.

Two hundred of our allies—archers, shield-bearers, even martial artists.

In a single instant.

*Slide. Splash!*

At that moment, someone’s nameless body rolled over the wall and landed in a pool of blood.

“Heaven above and earth below.”

In the suffocating silence that settled over everything, Dark Heaven’s followers had entered past the broken ranks and wall ruins that had crumbled with the Blood Lord’s arrival. As if bewitched, they began reciting their creed.

“All demons bow!”

They no longer shouted.

The killing intent they’d unleashed in their desperate efforts to cross the wall was gone, too.

*Shhk!*

They simply swung the blades in their hands without a word.

“Heaven above and earth below……!”

Their faces glowed with rapture as they marveled at the miracle unfolding before their eyes.

“All demons bow……!”

They praised the one ruler who wasn’t on this battlefield, yet could bring all under heaven to their knees from within that deep darkness.

Even if death awaited them at the end.

*Crunch!*

“L-Lord of Heaven.”

Even when a stray blade cut their throats, when their arms and legs were severed, when their chests were pierced, they never lost the smiles etched across their lips.

The dozen fanatics charging at me without a hint of fear were no different.

“A-at last. The glory of martyrdom……”

*Stab! Krrrunch!*

In the end, humans were made of flesh. Once their heads were gone, they couldn’t speak.

That was true not only of the Temporary Strength Pill, which let a person draw on strength beyond their limits at the cost of their life, but of anything they could take.

But why?

I’d swung my hand like a blade and cut their heads off in one blow, yet it sounded as if their unfinished words were still carrying on in my ears.

Again and again. Without a single moment of silence.

“These…… crazy bastards.”

A curse slipped out of me, my breathing suddenly ragged.

It felt like the blood in my body had turned to ice.

I thought I’d seen and dealt with enough lunatics to last a lifetime.

The twenty-first-century world I’d been born and raised in was a place with its own kind of barbarity, different from Murim.

Skyscrapers soared above the clouds. More than half a century had passed since humanity first ventured into space. A civilization combining cutting-edge science and Magic had grown brighter and more powerful than ever.

But nothing changed.

The modern world was still full of Madmen.

People were murdered in broad daylight. Judges’ gavels and reporters’ cameras swayed under the weight of money and liquor.

And that wasn’t all.

Dictators, relics of a bygone age, prepared for wars—and started them.

There were plenty of people trying to bridge the distance between religions and sects with missiles and terror instead of forgiveness and reconciliation.

In the world I’d seen, they were all fanatics.

Madmen who’d lost their minds by attaching themselves blindly to their own goals. They saw and felt only what they wanted, swaying as they got drunk on it.

Of course, the most extreme of them had been the fanatics who followed the Doppelganger. But now I could say it without a doubt.

The size and purity of the madness I’d seen in them was nothing next to the Dark Heaven followers before me.

And at the center of this blood-soaked storm of madness, a monster came hurtling forward with the momentum of Mount Taishan.

“Have you ever seen moths?”

I could feel it.

The Blood Lord’s ease—and the fact that he never let his guard down.

His red eyes were fixed solely on me, as though he had no interest in the battles raging all around us. They brimmed with certainty and killing intent.

“I have. Countless times, before the Tianshan Mountains fell under that person’s control. I saw those foolish things fly toward torches and burn to death.”

I didn’t answer.

Instead, I drove the shaft of White Flame, still in my grip, deep into the ground at my feet. Then I kicked up the weapons strewn around me and sent them flying at him.

*Fwoooooosh—BOOM!*

*Krrrunch!*

The blades, wreathed in Force, cut through the air one after another. Then an immense shock wave slammed into the space around them with a deafening roar.

Not where I’d aimed—the Blood Lord—but somewhere in the air and ground.

“But one day, as I watched them, a question occurred to me.”

The Blood Lord swung his Red Blade at lightning speed, casually knocking aside everything flying toward him, and continued speaking in a clear voice.

“Did those things fly toward the torch knowing they’d burn to death? Or could they only fly toward it because they didn’t know?”

*Crunch!*

I cut down the enemies charging at me from every direction. After the wall, our ranks were now collapsing fast, too.

The sight of fanatics charging in, shouting about martyrdom, and the wave of fear they stirred up were even overpowering the effect of One Against a Thousand.

“I still haven’t found the answer. No—I never bothered looking. It wasn’t long before I met that person and gained such overwhelming power that I didn’t need to think about how moths felt.”

At that moment—

*Whoooooom!*

The Blood Lord lifted his Red Blade high. A massive, crimson Force surged along its scarlet edge.

A power beyond anything I’d ever seen—or even imagined could exist.

“But I think someone like you could know the answer.”

Certainty in himself.

Killing intent sharp as a blade. Hatred beyond anger. The elation of finally achieving his purpose.

Every one of those feelings—his aura and power—was directed solely at me.

I found it hard to breathe. My hand trembled.

But I was ready.

I’d prepared my greatest attack. Maybe my last.

I took a deep breath and let the words that had been circling on the tip of my tongue spill out.

“I’m not one of them.”

“What?”

“I’m the kind of bastard who doesn’t burn to death even if he flies into the flames. Who flies in first whether he knows what’ll happen or not. That’s me.”

“……!”

The silence felt like an eternity, though it lasted only an instant.

At its very end, the Blood Lord answered.

No—he moved.

So did I.

*Pop.*

Across more than a hundred feet of space that vanished in an instant, his Red Blade carved a massive line of blood-red light.
```
