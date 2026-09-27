<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1097.txt",
      "sha256": "e8e54ccbeb36dbd1127dbdcd202a51a611ac0c30a33624357fe5448bfa3d31b7",
      "bytes": 12155
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2d685ab9e8d434c85b7fea44182db3e1af1e2dbe5d3fdd641f1c749eb159e538",
      "bytes": 1208
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e58ae46a1bac772cc7720c130c81de8fb5906bb3ba1496eb8e7943cb290731fa",
      "bytes": 244132
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "721e972fa852cfccd39165e146c8de79555b92a811e853c9e3a646e55d96f8ef",
      "bytes": 873
    },
    {
      "path": "characters/Dalai Lama.md",
      "sha256": "aec087c66a338d423d8c19ece213d01bc41d11e9956e71727a683aeb60d387f6",
      "bytes": 741
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "bcfee50f9e872cda8dbe75da693ada0f8bd2839aa3171977da61d430938dc549",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "32dfd48f7470275dbe788f7ffa471f3cb45daa5c9aaf8ca1b99ee0b08e6c1874",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e4d386a773c0afdfddbf8dc7a473665cdcbb2456c9a5631d8aa468ae1ae416b1",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9b6e0f5be15f906a9f97fa3d1c153cb4023203457946570ae19dbfa187999dc2",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "34333020496fb1076c32fa2b536366c4ae8a8a3a83548526b86c17e4abadb3e7",
      "bytes": 287451
    }
  ],
  "estimated_tokens": 10656
}
-->

# Durable State Update — Chapter 1097

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
1 and safe_through 1097. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1097. Profile updates may replace only one
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
  "chapter": 1097,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1097,
    "continuity_sources": [1097],
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
    "Dark Heaven’s army surrounds Xining under the Blood Lord; the Potala Palace has arrived with elephants and joined its forces.",
    "The Blood Lord expects thirty thousand reinforcements to reach Qinghai within one or two days.",
    "The Blood Lord wants Taekyung to resist so he can claim grounds to kill him, despite the Lord of Heaven’s apparent special interest in Taekyung.",
    "The Potala Palace and Dark Heaven are allies, but the Palace has a deep, longstanding hatred of the Fire Gate Clan.",
    "Namho fears Sichuan may be exposed to enemies from Tibet after the Nanman Beast Palace’s departure."
  ],
  "continuity_sources": [
    1095,
    1096
  ],
  "open_questions": [
    "Will the expected reinforcements reach Xining in time to decide the battle?",
    "Why does the Lord of Heaven appear to want Taekyung above all else?",
    "Will the Potala Palace continue cooperating with the Blood Lord after his threat to the Dalai Lama?"
  ],
  "safe_through": 1096,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 청해     | **Qinghai**            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 달뢰라마 | **Dalai Lama** | Traditional title of the Potala Palace’s leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 포달랍궁 | **Potala Palace** | Palace in Tibet. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 서녕 | **Xining** | Capital of Qinghai. |
| 십이밀승 | **Twelve Secret Monks** | The Potala Palace’s twelve top fighters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 혈주 | 달뢰라마 | allied leader to allied leader | Palace Lord | familiar, then threatening and insulting | Calls him 궁주, then warns him not to speak down to him. |
| 달뢰라마 | 혈주 | allied leader to allied leader | donor; you | formal, then angry and informal | Initially uses the Buddhist honorific 시주 before challenging the Blood Lord. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1096
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Cunning and controlling, he avoids costly risks while manipulating allies; beneath his devotion to the Lord of Heaven, he resents being treated as disposable and resents Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven with deep loyalty but resents the Lord’s apparent special interest in Jin Taekyung, whom he wants dead; he considers Taekyung and Cheongpung formidable adversaries.

### Dalai Lama.md

# Dalai Lama (달뢰라마)

- **Safe through:** Chapter 1096
- **Aliases:** Palace Lord
- **Role:** The Dalai Lama is the Potala Palace’s leader and ruler of Xizang, commanding its Twelve Secret Monks.
- **Personality:** Fiercely hostile to the Fire Gate Clan and committed to the Potala Palace’s interests; he trusts the Lord of Heaven but distrusts the Blood Lord.
- **Voice:** Uses Buddhist self-reference and addresses others as “donor”; his Han speech is described as halting.
- **Relationships:** He leads the Potala Palace, whose alliance with Dark Heaven rests partly on aid from the Lord of Heaven and a longstanding grievance against the Fire Gate Clan.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1095
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1096
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1096
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1096
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1097화




혈주의 입가에 맺혀 있는 광포한 미소를 마주한 순간, 달뢰라마는 등골을 타고 솟구치는 한기를 느꼈다.

‘이 자는 도대체.’

다르다. 확연히 달랐다.

눈앞의 저 사내에게는 인간이라면 누구나 품고 있는 원초적인 공포를 자극하는 무언가가 있었다. 

광활한 서장의 지배자인 자신조차도 섬뜩함을 느낄 수밖에 없는, 심연과도 같은 깊은 어둠이.

포식자.

불현듯 뇌리를 스친 그 세 글자와 함께, 달뢰라마는 떨리는 입술을 열었다.

어느덧 그와 십이밀승(十二密僧)을 감싸듯 포위한 암천의 교도들을 바라보며.

“빈승이…… 무례를 범했구려.”

잠시 잊고 있었다.

혈주가 어떤 사람인지. 그의 뒤에 누가 있는지.

하지만 조금 전 그가 숨겨 두었던 이빨을 드러낸 순간, 달뢰라마는 비로소 잊고 있던 현실을 깨달았다.

누가 약자이고 누가 강자인지.

지금 이 시점에서 돌이킬 수 없는 분란이 일어난다면, 잡아먹히는 것은 어느 쪽이 될지.

그렇기에 서장의 지배하는 교국(敎國)의 왕은 천천히 고개를 숙일 수밖에 없었다.

“천주(天主)께서 총애하시는 이에게 모욕을 주려는 뜻은 맹세코 없었소. 다만 심경이 복잡해진 탓에 실수를…….”

“실수라.”

이어지려는 달뢰라마의 말을 끊어 낸 혈주가 붉은 혀로 입술을 핥았다.

마치 먹잇감을 바라보며 입맛을 다시는 맹수처럼.

그리고 이내 달뢰라마를 향해 빙긋 웃어 보였다.

“이해합니다. 살다 보면 누구나 실수를 하기 마련이지요. 한 번쯤은.”

혈주가 나직이 덧붙인 뒷말에 담긴 의미는 명백했다.

한 번. 단 한 번뿐이다.

두 번째의 실수는 용납하지 않겠다.

그러나 언제 그랬냐는 듯 평소처럼 되돌아온 공대(恭待)와 그와는 상반된 태도를, 달뢰라마는 이를 악물며 받아들일 수밖에 없었다.

“그리 말씀해 주시니 고맙소.”

“어허, 이렇게까지 예의를 갖추실 필요는 없습니다. 우리는 함께 대업을 도모할 동지 아닙니까.”

“……백번 옳은 말씀이오.”

물론 귓가에 닿은 말이 얼마나 헛된 것인지, 달뢰라마는 모르지 않았다.

지금으로부터 수십여 년 전, 천주가 내민 손을 잡았을 때부터 힘의 우위는 이미 결정되어 있었다.

지금의 저 태도는 강자만이 보일 수 있는 아량이고, 한 차례의 채찍질 이후 선심 쓰듯 던져주는 당근이다.

하지만 어느덧 달뢰라마와 포달랍궁의 앞에 놓인 선택지는 하나뿐이었다.

모든 것을 인정하고, 받아들여야 한다.

그래야만 선대의 묵은 원한을 갚고, 더 나아가 추후 암천이 지배할 새로운 천하에서 살아남을 수 있을 테니까.

“본 궁은 최선을 다할 것이오. 천주께서 하사하신 은혜를 조금이나마 갚을 수 있도록. 다만…….”

“다만?”

혈주의 눈썹이 꿈틀거린 그때, 달뢰라마가 깊게 가라앉은 목소리로 덧붙였다.

“약속은 반드시 이행하리라 믿겠소.”

달뢰라마를 꿰뚫어 보듯 응시하던 혈주가 혀를 찼다.

“무슨 말씀을 하시나 했더니…… 걱정 마십시오. 열화문의 명맥(命脈)은 바로 이곳, 서녕에서 끊어질 겁니다.”

“시주를 의심하는 것은 아니지만, 녹림맹과 장강수로맹이 후방을 완전히 봉쇄하기 전에 놈들이 서녕을 빠져나가 중원으로 도주할 수도 있지 않겠소?”

“도주? 지금 도주라고 했습니까? 다른 누구도 아닌 화왕과 진태경이?”

달뢰라마가 대답하기도 전, 소리 내어 웃은 혈주가 말을 이었다.

“궁주께서는 누구보다 열화문을 증오하시면서도, 놈들에 대해서는 아무것도 모르시는군요.”

“얼마 안 되는 소수의 인원, 그것도 그 두 사람뿐이라면 가능성은 차고 넘친다고 생각되오만. 제아무리 천지 분간도 못 하는 열화문의 종자들이라 해도 지금 같은 열세에서는 후일을 도모할 수도 있지 않겠소?”

맞는 말이다.

서녕에 웅크리고 있는 수만의 병력도, 수십 만의 백성도 아닌 극소수의 인원이라면.

그리고 그것이 다름아닌 화왕 적천강과 열화신룡 진태경이라면 지금 당장 후방으로 빠져나가 포위망을 찢어 버릴 수도 있다.

하지만 그런 달뢰라마의 우려에도, 혈주는 더욱 크게 웃을 수밖에 없었다.

“불가능합니다. 절대로.”

“그리 생각하는 근거가 뭐요?”

“모르십니까? 조금 전 궁주께서 직접 말씀하셨는데도.”

“그게 무슨.”

달뢰라마가 의문을 표한 그때, 돌연 웃음을 뚝 그친 혈주가 갈라진 목소리로 입을 열었다.

“천지 분간도 못 하는 병신들. 그게 바로 열화문이니까.”

“……!”

“스승이나 제자나, 하나같이 제 목숨 아까운 줄 모르는 종자들입니다. 더군다나 수만의 아군, 수십만의 양민들이 남아 있다면…… 두말할 필요도 없고.”

만약 그 두 사람이 후일을 도모하고자 했다면, 지금쯤 서녕에 없었을 것이다.

아니, 그 전에 지금까지의 모든 행적조차 존재하지 않았다.

한번 열이 받으면 상대가 마교가 아니라 옥황상제라 해도 들이받고, 생사가 오가는 위기 앞에서도 지켜야 할 것이 있으면 반드시 지킨다.

비록 혈주와 같은 누군가에게는 협행(俠行)이 아니라 병신 같은 짓거리라고 조롱받을지라도, 그것이 바로 열화문이었다.

“마지막으로 말씀드리지만, 놈들은 절대 서녕을 벗어나지 못할 겁니다. 내 목을 걸고 장담하지요.”

그 어느 때보다 확신에 찬 대답과 함께, 혈주는 문득 떠올렸다.

일 년 전, 피로 뒤덮인 숭산(嵩山)의 골짜기에서 감히 자신과 맞섰던 하룻강아지의 그 처절하던 모습을.

그리고 오늘 이 자리에서 다시 마주한, 더는 하룻강아지라 부를 수 없는 어린 맹수의 눈동자에 담겨 있던 불꽃을.

그제야 확실히 알았다. 

놈이, 열화신룡 진태경이 어떤 부류인지.

동시에 결심했다.

천주의 명령을 거스르는 한이 있더라도, 놈을 죽여 후환을 없애기로.

‘만에 하나, 저 안의 다른 누군가가 놈을 뒤로 빼돌린다 해도 상관없다.’

빗물에 휩쓸려 갈 작물을 걱정하는 농민들은 하늘을 예의주시하지만, 다른 이들은 머리 위로 떨어지는 빗방울을 느낀 후에야 먹구름이 몰려왔음을 깨닫는 법.

장장 오십여 년간이나 이어졌던 평화는 길었고, 천천히 다가온 먹구름은 어느덧 그들 위에 있었다.

오래전, 저들의 내부 깊숙이 숨겨 둔 암천의 복검(覆劍)이 살을 파고드는 지금 이 순간까지도 눈치채지 못할 만큼.

‘내부에서 신호가 오는 순간, 단숨에 들이쳐 끝낸다.’

흐릿하게 미소 지은 혈주는 문득 고개를 들어 하늘을 바라보았다.

어두컴컴한 하늘 속, 유례없는 폭우(暴雨)를 예고하는 빗방울들이 하나둘씩 떨어지고 있었다.

청해성의 모든 것을 휩쓸어 갈 폭풍의 전조가.



* * *



툭. 투둑.

갑작스럽게 떨어져 내리기 시작한 빗방울이 정수리를 적시는 것을 느끼며, 나는 생각했다.

‘승전(勝戰)을 축하하는 것치고는, 더럽게 축축한데.’

비록 계획에도 없던 격전을 치렀지만, 그 짧았던 시간에 비해 아군이 거둔 성과는 상당했다.

어림잡아도 수백에 달하는 적들을 쓰러트렸고, 그중에는 전력을 다한 적천강의 일격에 휩쓸려 잿가루가 되어 버린 흑귀(黑鬼)도 포함되어 있었으니까.

‘물론, 그마저도 일부에 불과하지만.’

차마 소리 내어 뱉지 못한 마음속 생각과 함께, 나는 성벽 너머를 새카맣게 물들인 대군을 응시했다.

수백이 줄었으나, 수천이 늘었다.

손톱만큼이라도 수평에 가까워졌던 힘의 무게추가, 포달랍궁의 가세로 인하여 전보다도 더욱 기울어져 버린 것이다.

그리고 그 육중한 힘의 무게는 나를 비롯한 모두의 가슴 한 구석을 짓누르고 있었다.

“어쩌면…… 우리는 이미 적기(適期)를 놓쳤을지도 모르겠네요.”

더욱더 견고하고 빈틈없는 포위망을 구축해 가는 적들을 바라보며, 궁성이 무거운 목소리로 말을 이었다.

“기왕 내친걸음, 차라리 포달랍궁이 합류하기 전에 끝냈어야 했어요. 그랬다면 조금이라도 승산이 있었을 테니.”

모두가 피부로 느끼고 있는 현실을 짚은 그 한 마디에, 팔짱을 낀 채 침묵하고 있던 한 사람이 불쑥 입을 열었다.

“그렇다 해도, 야음을 틈타 수뇌부를 모조리 제거한다면 승산은 충분하지.”

만약 혁무진이 저런 말을 했다면 당장 거꾸로 매달아서 성벽 너머로 던져 버렸겠지만, 다행히도 그런 유감스러운 상황은 벌어지지 않았다.

다른 누구도 아닌, 고금제일이라 불리는 살수의 입에서 나온 말이었으니까.

하지만 기대에 찬 눈빛으로 그의 뒷말을 기다리는 다른 사람들과 달리, 나는 망설임 없이 고개를 가로저었다.

“절대 안 됩니다.”

살성이 반문했다.

“반대하는 이유는?”

“솔직하게 말씀드려도 됩니까?”

“언제는 아니었느냐? 말해 봐라.”

“간단합니다. 가 봤자 개죽음만 당할 테니까요.”

“……!”

삽시간에 착 가라앉은 분위기 속, 살성이 심유한 눈빛으로 나를 응시했다.

“솔직한 것을 넘어, 도발에 가깝군.”

“장난이 취미고 도발이 특기인 건 맞는데, 한 배를 탄 아군한테는 해당 안 됩니다. 이미 아시잖아요?”

“조금 전 놈들을 직접 상대하며 느낀 바가 있다. 내가 나선다면 가능성이 있어.”

“그 가능성, 어느 정도나 됩니까?”

“일 할.”

희박한 확률을 대수롭지 않게 대답한 살성이, 지금 이 순간에도 시시각각 굵어지는 빗줄기를 바라보며 덧붙였다.

“하늘이 힘써 준다면, 이 할.”

“그 정도밖에 안 됩니까?”

“그 정도씩이나 되는 거다. 성공 시에 얻게 될 것을 생각한다면, 이 목숨 하나로는 충분히 남는 장사지.”

맞는 말이다.

하지만 그럼에도 불구하고, 나는 쓴웃음을 지을 수밖에 없었다.

“뭔가를 얻기라도 할 수 있다면, 제가 굳이 개죽음이라는 표현을 쓰진 않았겠죠.”

“내 존재가 알려진 이상, 놈들이 대비하리라는 것 정도는 충분히 예상하고 있다. 어쩌면 남아 있는 흑귀 전부를 호위로 세워 둘 수도 있겠지.”

“압니다. 그 외의 여러 상황까지 염두에 두신 것도.”

“그렇다면, 어째서냐?”

“그야 간단하지.”

당연하게도, 이 대답은 내가 한 것이 아니다. 

줄곧 침묵하던 중, 불현듯 입을 연 적천강이 모두의 시선을 받으며 말을 이었다.

“사술, 아니 마법(魔法). 그 빌어먹을 것에 대해서는 고금제일의 살수도 귀머거리에 소경이나 다름없을 테니까. 내 말이 틀렸느냐?”

나는 고개를 끄덕였다.

아니, 정확히는 고개를 끄덕이기도 전에 내 어깨를 붙잡은 적천강의 손에 의해 발걸음을 옮겨야 했다.

그리고 그 행동에 대한 이유를 묻기도 전, 나직이 귓가를 파고든 전음(傳音)에 입을 다물 수밖에 없었다.

- 그래서, 네 녀석은 끝까지 말하지 않을 셈이냐?

깊게 가라앉은 눈빛으로, 적천강이 나를 응시했다.

- 마지막 순간, 혈주 그놈이 무슨 헛소리를 지껄였는지.
```

## Final English reading copy

```markdown
# Chapter 1097

The moment he met the Blood Lord’s wild smile, the Dalai Lama felt a chill run up his spine.

*What in the world is this man?*

He was different. In every way.

There was something about the man before him that stirred the primal fear every human being carried within them.

A darkness as deep as the abyss, enough to send a shiver through even the ruler of Xizang’s vast lands.

A predator.

The three words flashed through his mind. The Dalai Lama’s trembling lips parted.

He looked at the Dark Heaven followers who had surrounded him and the Twelve Secret Monks as if to enclose them.

“This humble monk… has been discourteous.”

For a moment, he’d forgotten.

What sort of man the Blood Lord was. Who stood behind him.

But the instant the Blood Lord bared the fangs he’d kept hidden, the Dalai Lama finally remembered the reality he’d let slip from his mind.

Who was weak, and who was strong.

If an irreparable conflict broke out at this moment, which side would be devoured?

That was why the king of the theocratic state that ruled Xizang had no choice but to bow his head slowly.

“I swear, I had no intention of insulting someone the Lord of Heaven favors. It’s only that I was troubled, and made a mistake…”

“A mistake.”

The Blood Lord cut off the Dalai Lama’s words and licked his lips with a red tongue.

Like a beast savoring the sight of its prey.

Then he smiled gently at the Dalai Lama.

“I understand. Anyone can make a mistake now and then. Once.”

The meaning in the Blood Lord’s quiet final words was unmistakable.

Once. Just once.

He wouldn’t tolerate a second mistake.

The Blood Lord’s respectful manner had returned as though nothing had happened, but his attitude was the exact opposite. The Dalai Lama had no choice but to grit his teeth and accept it.

“Thank you for saying so.”

“Now, there’s no need to be so formal. We’re comrades working together toward a great cause, aren’t we?”

“…You’re absolutely right.”

Of course, the Dalai Lama knew how hollow those words were.

The balance of power had been decided decades ago, when he took the hand the Lord of Heaven had offered.

This was the magnanimity only the strong could show—a carrot tossed to him as a gesture of goodwill after a crack of the whip.

But by now, only one choice remained before the Dalai Lama and the Potala Palace.

They had to accept everything and acknowledge it.

Only then could they avenge the old grudge handed down from their predecessors—and survive in the new world Dark Heaven would one day rule.

“The Potala Palace will do everything it can to repay, in some small measure, the grace the Lord of Heaven has bestowed upon us. However…”

“However?”

As the Blood Lord’s eyebrow twitched, the Dalai Lama added in a deeply subdued voice:

“I trust you’ll honor your promise.”

The Blood Lord, who had been staring at him as if to see right through him, clicked his tongue.

“So that’s what you were going to say… Don’t worry. The Fire Gate Clan’s lineage will end right here, in Xining.”

“I don’t doubt you, donor, but couldn’t they escape Xining and flee to the Central Plains before the Green Forest Alliance and Yangtze River Channel League have completely sealed off the rear?”

“Escape? Did you just say escape? And you mean the Fire King and Jin Taekyung, of all people?”

Before the Dalai Lama could answer, the Blood Lord laughed aloud and continued.

“Palace Lord, you hate the Fire Gate Clan more than anyone, yet you know nothing about those people.”

“They’re a small handful of people. If it’s just those two, there are more than enough opportunities to get away. Even the Fire Gate Clan’s reckless fools might think about living to fight another day when they’re at such a disadvantage.”

He was right.

They weren’t talking about the tens of thousands of troops huddled in Xining, or its hundreds of thousands of people. They were talking about a tiny handful.

And if that handful consisted of none other than the Fire King Jeok Cheongang and the Blazing Flame Divine Dragon Jin Taekyung, they could slip through the rear right now and tear a hole in the encirclement.

But despite the Dalai Lama’s concerns, the Blood Lord could only laugh even harder.

“Impossible. Absolutely impossible.”

“What makes you so sure?”

“Don’t you know? You just said it yourself.”

“What do you mean—”

The Dalai Lama’s question was cut short. The Blood Lord suddenly stopped laughing and spoke in a hoarse voice.

“Idiots who don’t know up from down. That’s the Fire Gate Clan.”

“……!”

“Master and Disciple alike—they’re all the sort who don’t give a damn about their own lives. And if tens of thousands of allies and hundreds of thousands of civilians are still here… well, there’s nothing more to say.”

If those two had wanted to live to fight another day, they wouldn’t be in Xining right now.

No. Their entire history up to this point would never have happened.

Once they lost their temper, they’d charge even if their opponent were the Demonic Cult—or the Jade Emperor himself. And even when their lives were on the line, if there was something they had to protect, they protected it.

Some people, the Blood Lord among them, might mock it as a stupid stunt rather than a chivalrous act.

But that was the Fire Gate Clan.

“I’ll say it one last time: they will never leave Xining. I’ll stake my life on it.”

As he answered with more conviction than ever, the Blood Lord suddenly remembered.

A year ago, in a valley on Mount Song drenched in blood, how desperately that young pup had fought when he dared to face him.

And today, in the eyes of the young beast he’d faced once more—eyes that held a fire too fierce for him to call it a young pup anymore.

At last, he understood for certain.

What kind of person that boy—the Blazing Flame Divine Dragon Jin Taekyung—was.

And at the same time, he made up his mind.

Even if it meant defying the Lord of Heaven’s command, he would kill the boy and eliminate the threat he posed.

*Even if someone else in there smuggles him out the back, it won’t matter.*

Farmers worried about crops being swept away by the rain kept their eyes on the sky. Everyone else only realized storm clouds had gathered when raindrops fell on their heads.

The peace that had lasted more than fifty years was long. And the storm clouds that had crept slowly toward them were now overhead.

They still hadn’t noticed—not even now, as Dark Heaven’s hidden sword, planted deep within their ranks long ago, pierced their flesh.

*The moment I get the signal from inside, I’ll strike and finish this in one go.*

The Blood Lord smiled faintly, then lifted his head and looked at the sky.

In the dark, murky heavens, raindrops began to fall one by one, promising an unprecedented downpour.

An omen of the storm that would sweep away everything in Qinghai.



* * *



Tap. Plip.

As I felt the sudden raindrops wet the top of my head, I thought:

*For a victory celebration, this is one hell of a damp affair.*

Though we’d ended up fighting an unexpected battle, our side had achieved a great deal in the short time it lasted.

We’d taken down hundreds of enemies, by my estimate—and among them was the Black Ghost who’d been reduced to ashes by Jeok Cheongang’s full-powered strike.

*Of course, that was only a fraction of them.*

I kept the thought to myself and stared beyond the wall at the massive army that had turned the land black.

Hundreds fewer, but thousands more.

For a moment, the balance of power had edged the tiniest bit closer to even. With the Potala Palace’s arrival, it had tipped further against us than before. The weight of it pressed down on one corner of everyone’s heart, mine included.

“Maybe… we’ve already missed our chance.”

Watching the enemy build an ever tighter, more impregnable encirclement, Bow Saint continued in a heavy voice:

“Since we were already committed, we should’ve finished things before the Potala Palace arrived. We might’ve had a chance then.”

At that one sentence, which put into words what everyone already felt, someone who’d been standing with his arms crossed in silence spoke up.

“Even so, we have a good chance if we take advantage of the darkness and eliminate their entire leadership.”

If Hyuk Mujin had said that, I’d have strung him up by his ankles and thrown him over the wall. Thankfully, we weren’t in that unfortunate situation.

Those words had come from none other than an assassin hailed as the greatest of all time.

But unlike the others, who waited for the rest of his plan with hopeful eyes, I shook my head without hesitation.

“Absolutely not.”

The Slaughter Saint asked:

“Why do you object?”

“Can I be honest?”

“When have you ever been anything else? Go on.”

“It’s simple. We’d go there just to die like dogs.”

“……!”

The mood sank in an instant. The Slaughter Saint looked at me with a deep, searching gaze.

“That’s beyond honesty. It’s almost a provocation.”

“I know I like joking around and I’m good at provoking people, but that doesn’t apply to allies on the same boat. You know that already, don’t you?”

“I learned something by facing them myself just now. If I went in, there’d be a chance.”

“How much of a chance?”

“One in ten.”

The Slaughter Saint answered as if the slim odds were no big deal, then looked at the rain, growing heavier by the moment.

“One in five, if the heavens lend a hand.”

“That’s all?”

“That’s as much as one in five. Considering what we’d gain if we succeeded, staking my one life would be a bargain.”

He was right.

Even so, I could only smile bitterly.

“If we stood to gain anything at all, I wouldn’t have called it dying like dogs.”

“Now that they know I’m here, I expect them to prepare. They might even set every Black Ghost they have left to guard their leaders.”

“I know. And I know you’ve considered all the other possibilities, too.”

“Then why?”

“Because it’s obvious.”

Naturally, I wasn’t the one who answered.

Jeok Cheongang had been silent all along. Now he spoke up and continued as everyone turned to look at him.

“Dark arts—no, magic. When it comes to that cursed stuff, even the greatest assassin of all time would be as good as deaf and blind. Am I wrong?”

I nodded.

No—more precisely, before I could even nod, Jeok Cheongang grabbed my shoulder and made me move.

And before I could ask why he’d done that, the low Sound Transmission that slipped into my ear left me with no choice but to fall silent.

—So, are you really not going to tell me until the very end?

Jeok Cheongang stared at me, his gaze sunk deep.

—What nonsense that bastard the Blood Lord was spouting at the last moment.
```
