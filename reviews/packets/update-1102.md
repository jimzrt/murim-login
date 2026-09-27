<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1102.txt",
      "sha256": "b6bbf5d14606784c6af332e8490c68af4c28dad8a22d420c8d0df5fc591d3947",
      "bytes": 12358
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0cef6ee205335726887ffac79a36a60c2785f26ef0e9a81517b3f7b348092f7c",
      "bytes": 1471
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2195176fcecc1f2d4760ffbc4a2601370e7609089bc148ea8deda43236c266fc",
      "bytes": 244248
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "56351c602c33daf2392eb8ebdaec395dde374f039aabe4e4cb425f9f9c5aee75",
      "bytes": 907
    },
    {
      "path": "characters/Dalai Lama.md",
      "sha256": "9cf8fd104eac9c94b47654a17c160d09d8bfeb08b5f7990f559ffaa4f4140af4",
      "bytes": 779
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6e0fba6e700819c888abf96cddf40385f0fcb1bc71651ea24f5aba2bcb99d522",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "762ce639ec1cda23984bcab3ecbf41b31b0a3c3a538e47c23e8e0c6f506e8338",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "492e0ce41e170038c5a80e5a927761b30447cf5fde5e074c30ca1f1ba4fa510f",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "88b4a4d511f9eccbee1a28b5da42e001dfbbbf8f3a78ac3a9cd9e13c55aa228f",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f15b6bb616e0bd10e582c2c20db1381f3647dfe2374b0b254aed2c21ef827565",
      "bytes": 287948
    }
  ],
  "estimated_tokens": 10884
}
-->

# Durable State Update — Chapter 1102

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
1 and safe_through 1102. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1102. Profile updates may replace only one
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
  "chapter": 1102,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1102,
    "continuity_sources": [1102],
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
    "Dark Heaven and the Potala Palace are attacking Xining; the battle is underway.",
    "Jin Taekyung annihilated at least a thousand attackers beneath the western wall, including the monsters and pill-enhanced Dark Heaven followers.",
    "Giants’ corpses have piled up to the middle of Xining’s wall; Dark Heaven’s hundred-thousand-strong main force is advancing.",
    "Jin Taekyung’s System titles One Against a Hundred and One Against a Thousand activated; Intimidation rose, Fear lifted from some allies, and allied morale increased.",
    "The Blood Lord privately wants Jin Taekyung dead but conceals this from the Grand Mage and will not defy that person’s will."
  ],
  "continuity_sources": [
    1100,
    1101
  ],
  "open_questions": [
    "Can Xining’s walls withstand Dark Heaven’s advancing main force and the piled-up giants?",
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Whom do the Eldest Senior Brother and Elders serve, and what was Mu Song about to reveal?",
    "Who were the new allies gathering near the river?",
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?"
  ],
  "safe_through": 1101,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 문주     | **Sect Leader**                              |
| 정마대전   | **Great Faction War**         |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 달뢰라마 | **Dalai Lama** | Traditional title of the Potala Palace’s leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 포달랍궁 | **Potala Palace** | Palace in Tibet. |
| 황하 | **Yellow River** | River along which civilization began. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 서문 | **West Gate** | One of the Nanman Beast Palace's gates. |
| 북문 | **North Gate** | The gate where Jin Taekyung and Yohi arrive. |
| 남문 | **South Gate** | A gate that was never built because of the rear cliff. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |
| 서녕 | **Xining** | Capital of Qinghai. |
| 십이밀승 | **Twelve Secret Monks** | The Potala Palace’s twelve top fighters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 사령관 | captor to captive undead commander | you | casual, mocking, and dismissive | Taekyung addresses the Skeleton Warlord informally while rejecting its pleas to turn back. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 혈주 | 달뢰라마 | allied leader to allied leader | Palace Lord | familiar, then threatening and insulting | Calls him 궁주, then warns him not to speak down to him. |
| 달뢰라마 | 혈주 | allied leader to allied leader | donor; you | formal, then angry and informal | Initially uses the Buddhist honorific 시주 before challenging the Blood Lord. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1100
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Cunning and controlling, he avoids costly risks while manipulating allies; beneath his devotion to the Lord of Heaven, he resents being treated as disposable and resents Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven but resents the Lord’s apparent special interest in Jin Taekyung, whom he resolves to kill even if it means defying the Lord’s command; he considers Taekyung and Cheongpung formidable adversaries.

### Dalai Lama.md

# Dalai Lama (달뢰라마)

- **Safe through:** Chapter 1100
- **Aliases:** Palace Lord
- **Role:** The Dalai Lama is the Potala Palace’s leader and ruler of Xizang, commanding its Twelve Secret Monks.
- **Personality:** Fiercely hostile to the Fire Gate Clan and committed to the Potala Palace’s interests; he trusts the Lord of Heaven but distrusts the Blood Lord.
- **Voice:** Uses Buddhist self-reference and addresses others as “donor”; his Han speech is described as halting.
- **Relationships:** He leads the Potala Palace in an unequal alliance with Dark Heaven, accepting its terms to pursue their shared goal of destroying the Fire Gate Clan and avenge the Palace’s longstanding grievance.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1101
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1101
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1100
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1100
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1102화




인류의 모든 역사를 돌이켜 보아도, 공성전은 수비 측에게 압도적으로 유리한 싸움이다.

남의 것을 손에 넣기 위해서는 응당 그에 합당한 대가를 치러야 하는 법.

공격 측이 일반적인 형태의 성이나 요새를 함락시키기 위해서는 최소 세 배 이상의 병력이 필요하며, 설령 그 이상이라 할지라도 공성전에서 패배할 가능성은 차고 넘쳤다.

물론, 누군가에게 있어 그것은 낡고 녹슬어 버린 옛 역사에 지나지 않았지만.

“난공불락(難攻不落)이란, 결국 나약한 패배자들이 남긴 헛소리에 불과하지.”

드드드득.

낮게 깔린 혈주의 목소리 위로 덧씌워지는 거대한 울림.

지금 이 순간, 푸르고 광활했던 대지를 칠흑으로 물들인 암천의 대군세는 하나의 파도처럼 성벽을 향해 나아가고 있었다.

인간과 괴물의 시체를 발판삼아, 저 높은 성벽을 넘기 위해.

그들만의 새로운 역사를 쓰기 위해.

‘생각했던 것 이상으로 빠르게 선봉대가 궤멸하긴 했지만…… 상관없다. 서녕을 함락시키고 놈의 숨통을 끊을 수만 있다면.’

선봉대를 막아 낸 것은 서문을 지키고 있던 진태경뿐만이 아니었다.

궁성과 살성이 각각 남문과 동문을, 그리고 화왕 적천강이 북문 일대를 방어했고 또 다른 네 명의 초절정 고수들이 그들의 뒤를 보좌하고 있었으니.

하지만 그렇게 네 방면의 성벽을 향해 무모한 돌격을 감행한 수천의 선봉대가 증발했음에도, 혈주는 조금도 동요하지 않았다.

‘목적을 이루기 위해서라면, 이 정도 피해는 아무것도 아니다.’

어차피 이런 순간을 위해 준비해 두었던 괴물들이었다.

만약 공성전이 아니라 평지에서 벌어지는 전투였다면 강력한 전력이었겠지만, 모든 소모품은 상황에 따라 쓰임새가 달라지는 법.

비록 그 대가로 절반에 달하는 괴물들을 잃었으나, 혈주는 스스로의 선택이 옳다고 확신했다.

한낱 인간에 지나지 않는 교도들을 앞세웠다면, 수천이 아니라 수만을 잃은 후에야 지금처럼 제대로 된 공성을 시작할 수 있었을 테니까.

“술사들은? 모두 정해진 위치에 배치했나?”

혈주가 불쑥 던진 물음에 대술사가 고개를 끄덕였다.

그녀의 휘하에 배속된 일백여 명의 술사는, 현대의 마법병단(魔法兵端)이나 다름없는 핵심 전력인 동시에 이번 전투에서 매우 중요한 역할을 맡고 있었다.

철벽과도 같은 아군의 보호 아래, 초절정 고수들의 손발을 어지럽히는 것이 바로 그 임무였다.

“계속해서 압박해. 놈들이 쉴 새 없이 힘을 소모할 수밖에 없도록.”

명백한 우세를 점하고 있음에도, 혈주는 조금도 방심하지 않았다.

이미 불귀의 객이 되어 버린 네 명의 마군과 마후는 그에게 훌륭한 교훈이 되어 주었고, 설령 그뿐만이 아니더라도 수성 측의 면면은 실로 화려했다.

초절정 고수만 무려 여덟.

물론 그중에서도 대인이라 불리는 얼간이는 사람 구실이나 제대로 할까 싶을 정도로 맛이 가 있는 듯했지만, 저 정도의 전력이 한자리에 모인 것은 정마대전(正魔大戰) 중 벌어진 수많은 전투 중에서도 손에 꼽힐 정도다.

아니, 오늘 이 전장에 집결해 있는 총병력만 따지자면 무림 역사상 최초라 해도 과언이 아닌 상황.

그렇기에 혈주는 일말의 변수조차 용납할 수 없었다.

매번 그 누구보다 가장 큰 변수를 만들어 낸 한 사람의 존재는 더욱더.

‘진태경.’

어느덧 심유하게 가라앉은 눈빛.

저 멀리, 천지를 떨어 울리는 함성과 함께 돌격하는 교도들의 앞을 막아선 청년의 모습이 혈주의 눈동자에 비쳤다.

그를 중심으로 쉼 없이 솟구치는 피 분수도 함께.

푸화아악!

섬광이 번뜩일 때마다 하나둘씩 꺼져 가는 생명들.

이미 드높은 경지에 오른 그 움직임은 실로 간결하고, 빠르며, 압도적이기까지 하다.

그러나.

‘영원한 것은 없지.’

진태경은 분명 강하다.

심지어 지금 이 순간에도 조금씩 강해지고 있을지도 모른다.

하지만 모든 것에는 한계란 것이 존재하는 법이다.

‘결국은 지치게 되어 있다. 진태경도, 화왕을 비롯한 다른 늙은이들도.’

혈주의 명령이 떨어지지 않는 한, 압도적인 전력과 머릿수를 바탕으로 펼치는 이 거대한 차륜전(車輪戰)의 수레바퀴는 멈추지 않을 것이다.

저들의 머리이자 심장인, 여덟 명의 초절정 고수가 지치기 전까지는.

그리고 그 기회의 순간이 머지않았음을, 혈주는 직감적으로 느끼고 있었다.

진태경의 숨통을 끊기 위해 자신이 무엇을 준비해야 하는지도.

“지금부터 서문은 온전히 내가 맡는다.”

불현듯 흘러나온 혈주의 목소리에, 그 안에 담긴 뜻을 알아차린 대술사가 입을 열었다.

“어째서인지 축객령처럼 들리는데. 괜한 착각일까?”

“그 말 그대로, 착각이다.”

“그렇다면 내가 굳이 서문을 떠나야 할 이유는?”

“이유가 필요한가? 총사령관은 나다.”

“그건 인정해. 다만 혹시나 하는 의구심이 들어서.”

“의구심이라, 도대체 무슨 말을 하고 싶은 거지?”

“글쎄. 이를테면…….”

문득 말꼬리를 흐린 대술사가, 고군분투하며 서쪽 성벽을 지키고 있는 진태경과 혈주를 번갈아 보며 덧붙였다.

“그분의 가장 충실한 종복을 자처해 왔던 누군가가, 주인의 뜻을 거스르면서까지 과잉 충성을 하진 않을까 싶은 걱정이겠지.”

마치 속내를 꿰뚫어 보는 듯한 한 마디.

그러나 혈주는 손톱만큼의 동요조차도 내비치지 않았다.

대술사가 자신의 의도를 의심할지도 모른다는 것은, 이미 진태경을 죽이겠다는 결심을 한 순간부터 염두에 두었으니까.

“그 정도면 착각 수준이 아니라, 노망에 가깝군. 내가 그런 불충을 저지를 얼간이로 보이나?”

조금의 망설임이나 흐트러짐도 없는 담담한 대꾸에, 혈주를 물끄러미 응시하던 대술사가 어깨를 으쓱했다.

“확실히 지금껏 봐 온 당신은 불충과는 거리가 멀지. 가끔 충성심이 과한 탓에 얼간이처럼 보이긴 했지만.”

예전이었다면 곧장 이빨을 드러내고 으르렁댔을 혈주였지만, 그의 머릿속은 어느 때보다도 차갑게 식어 있었다.

“그래서, 대답은?”

“좋아. 어디로 가면 되지?”

“남문을 맡아라.”

“남문이라면, 궁성?”

“흑귀 셋. 아니, 넷을 붙여 주지. 그 정도 전력이라면 제아무리 궁성이라 해도 별다른 수를 쓰지 못할 거다.”

혈주의 그 말은 명백한 사실이었지만, 대술사는 미간을 찌푸렸다.

“흑귀를, 그것도 넷이나?”

현재까지도 전장에 투입되지 않은 흑귀의 숫자는 총 아홉.

비록 적천강과 살성의 급습으로 인하여 허망하게 한 기를 잃었다 해도, 생전의 무위를 고스란히 간직한 데다가 불사에 가까운 회복력을 지닌 흑귀를 넷이나 붙여 준다는 것은 언뜻 이해가 되지 않았다.

그건 대술사 자신의 안위를 떠나, 필요한 순간에 사방의 성벽을 돌파할 전력에 공백이 생긴다는 뜻이었으니까.

그러나 찰나에 떠오른 그 의문은, 다음 순간 들려온 혈주의 목소리에 곧장 사그라졌다.

“힘을 아끼지 말고 몰아붙여라. 너와 술사들. 거기에 더해 흑귀들이 나타난다면 놈들 역시 남문에 더욱 강한 전력을 배치할 테니.”

그제야 혈주의 의도를 알아차린 대술사가 실소를 흘렸다.

“그러니까 결국, 화왕이나 살성을 끌어들이는 미끼가 되어라?”

“반은 맞고, 반은 틀렸군.”

“뭐?”

“화왕은 남문으로 가지 못할 거다. 생각지도 못한 손님을 맞이하느라 바쁠 테니.”

망설임 없이 대답한 혈주가, 차갑게 가라앉은 시선으로 줄곧 북쪽 성벽을 응시하고 있던 달뢰라마를 향해 덧붙였다.

“그렇지 않습니까, 궁주.”

“……!”

일순간 격동으로 파르르 떨리는 눈동자.

마침내 그토록 기다려왔던 복수의 시간이 찾아왔음을 깨달은 달뢰라마가, 천천히 입술을 뗐다.

“빈승이 어찌하면 되겠소?”

“화왕, 그 늙은이에게 똑똑히 보여 주십시오. 기나긴 인고의 세월 속에서 쌓아 올린 포달랍궁의 원한과 저력을.”

“지난 일평생을, 오직 이 순간만을 기다려 왔소.”

진심을 담은 합장(合掌)과 함께, 달뢰라마의 신형이 거대한 코끼리 위로 솟구쳤다.

“가자. 선조들의 원한을 갚을 때가 왔다.”

나직하지만 공력이 담긴 음성이 끝없이 뻗어 나간다.

두 명의 초절정 고수가 포함된 십이밀승(十二密僧)이, 그리고 물경 일만에 달하는 포달랍궁의 승려들이 귓가가 먹먹해질 만큼의 함성을 내질렀다.

부우우우!

전장을 떨어 울리는 뿔피리 소리.

그렇게 하나의 교국으로 거듭난 서장 무림의 대군(大軍)은 거센 빗줄기를 뚫고 북문을 향해 질주했다.

같은 하늘을 지고는 살 수 없는 불구대천의 원수, 열화문의 후예를 짓밟기 위해서.

그 저주받은 명맥을 이은 당대의 열화문주, 화왕 적천강의 목을 선조들의 영전에 바치기 위해서.

그리고 삽시간에 멀어지는 그들의 뒷모습을 바라보던 혈주의 귓가로, 대술사의 목소리가 파고들었다.

“이렇게 되면, 결국 남은 건 동문뿐인가?”

“동문으로는 흑귀 둘을 보낼 거다.”

“둘이라, 애매한 숫자네. 되려 살성에게 당할 수도 있을 만큼.”

“하지만 그런 일은 벌어지지 않겠지. 최대한 살성과의 정면 승부를 피하고, 소극적인 공세로 일관하라는 명령을 내릴 테니까.”

“조금 전에 애매하다고 했던 말, 취소할게.”

면사 아래로 드러난 대술사의 입가가 부드럽게 호선을 그렸다.

“적절한 숫자인 것 같네. 위기에 처한 남문을 구원하기 위해 살성이 자리를 비우기에는.”

그런 그녀를 따라, 혈주도 흐릿하게 웃었다.

“거기에 더해, 놈들의 의심도 피할 수 있을 테지.”

만약 암천이 동문에만 별다른 전력을 배치하지 않는다면 되려 의심을 살 것이다.

하지만 충분한 전력을 갖춘 채로 조금 느슨하게만 조여 온다면, 살성을 비롯한 동문의 병력들은 조금이나마 트인 숨통과 함께 주위를 살펴볼 여유를 갖게 된다.

자신들과는 달리 무너지기 일보 직전인, 또 다른 아군들을 지원할 여유를.

그리고 바로 그 순간 생기는 공백이야말로, 저 단단하고도 거대한 둑을 단숨에 무너트릴 균열이었다.

화아아악!

거친 비바람에 의해 나부끼는 옷자락.

평범한 이라면 전신을 흠뻑 적시는 것으로도 모자라 뼛속 깊이 파고드는 한기(寒氣)에 몸을 떨었겠지만, 혈주는 웃으며 손을 뻗었다.

동풍(東風)이었다.

황하의 지류를 따라 동쪽에서 불어오는, 어느 때보다 거센 동풍이 불어오고 있었다.

포달랍궁에 이어 이 전장의 대미를 장식할, 출렁이는 강물을 타고 달려오는 또 다른 손님들과 함께.

- 삐이잇!

빗줄기가 쏟아지는 어두운 하늘 속, 동쪽으로부터 날아든 독수리 한 마리가 힘찬 울음을 토해 내며 혈주의 어깨에 내려앉았다.

군데군데 새하얗게 드러난 뼈마디와, 핏빛 눈동자를 번들거리며.

그리고 독수리의 등장이 의미하는 낭보(朗報)를 알아차린 혈주가, 허리춤에 꽂힌 칼자루를 어루만지며 뇌까렸다.

“때가 왔군.”
```

## Final English reading copy

```markdown
# Chapter 1102

Looking back over the whole of human history, sieges had always been overwhelmingly favorable to the defending side.

If you wanted to take something that belonged to someone else, you had to pay a price worthy of it.

An attacking force needed at least three times as many soldiers to capture an ordinary castle or fortress. And even with more than that, the chances of losing a siege were still considerable.

Of course, to some people, that was nothing but old history, worn out and rusted.

“‘Impregnable’ is nothing but nonsense left behind by weak losers.”

*Rumble.*

A vast rumble rolled over the Blood Lord’s low voice.

At that very moment, Dark Heaven’s enormous army, turning the once-green, vast expanse of land pitch-black, advanced toward the city wall like a single wave.

They would climb that towering wall using the corpses of humans and monsters as footholds.

They would write a new history of their own.

*The vanguard was annihilated faster than I expected…but it doesn’t matter. As long as we take Xining and cut that bastard’s throat.*

Jin Taekyung, defending the West Gate, hadn’t been the only one to stop the vanguard.

The Bow Saint and Slaughter Saint had defended the South Gate and East Gate, respectively, while the Fire King, Jeok Cheongang, held the area around the North Gate. Four other Supreme Peak masters supported them from behind.

Yet even after thousands in the vanguard had vanished in reckless charges against the walls on all four sides, the Blood Lord remained utterly unmoved.

*This much damage is nothing if it means achieving my goal.*

The monsters had been prepared for a moment just like this.

They would have been powerful forces in a battle on open ground, but every expendable asset had its use, depending on the situation.

Though he had lost nearly half the monsters as a result, the Blood Lord was certain he’d made the right choice.

If he had sent ordinary followers—mere humans—out in front, they would have lost not thousands but tens of thousands before they could begin a proper siege like this.

“What about the mages? Are they all in their assigned positions?”

The Grand Mage nodded at the Blood Lord’s sudden question.

The hundred or so mages under her command were a core part of their forces, no different from a modern magic corps, and they had a vital role in this battle.

Under the ironclad protection of their allies, their task was to throw the Supreme Peak masters off balance.

“Keep up the pressure. Make sure they have no choice but to spend their strength without a moment’s rest.”

Even with an overwhelming advantage, the Blood Lord wasn’t letting his guard down.

The four Demon Lords and the Demon Empress who had already met their ends had taught him a valuable lesson. And even without them, the defenders were an impressive lot.

No fewer than eight Supreme Peak masters.

One of them, the fool they called Great Sir, seemed so far gone that it was hard to imagine he could function like a normal person. But it was rare for so many powerful fighters to gather in one place, even among the countless battles of the Great Faction War.

No—for that matter, the total number of troops assembled on this battlefield might be unprecedented in the history of Murim.

That was why the Blood Lord couldn’t allow even the slightest variable.

Especially not the one person who had created more variables than anyone else, time and again.

*Jin Taekyung.*

His gaze settled into a deep, still calm.

In the distance, a young man stood before the charging followers, whose cries shook heaven and earth. His figure appeared in the Blood Lord’s eyes.

So did the fountains of blood erupting ceaselessly around him.

*Fwoosh!*

With every flash of light, one life after another flickered out.

His movements had reached an astonishing realm: simple, swift, and utterly overwhelming.

And yet—

*Nothing lasts forever.*

Jin Taekyung was undoubtedly strong.

He might even be growing stronger, little by little, at this very moment.

But everything had its limits.

*In the end, he’ll grow tired. Jin Taekyung, the Fire King, and all the other old men.*

Unless the Blood Lord gave the order, the wheels of this enormous war of attrition, turning on the back of overwhelming numbers and strength, would never stop.

Not until those eight Supreme Peak masters—their heads and hearts—were exhausted.

And the Blood Lord had an instinctive feeling that the moment was drawing near.

He also knew what he needed to prepare in order to cut Jin Taekyung’s throat.

“From now on, I’ll take full responsibility for the West Gate.”

At the Blood Lord’s sudden announcement, the Grand Mage understood the meaning behind it and spoke.

“For some reason, that sounds like you’re ordering me to leave. Am I imagining things?”

“That’s exactly what it is: your imagination.”

“Then why should I leave the West Gate?”

“Do you need a reason? I’m the commander in chief.”

“I acknowledge that. I’m just a little suspicious, that’s all.”

“Suspicious? What exactly are you trying to say?”

“Who knows. For instance…”

The Grand Mage let her voice trail off. She glanced back and forth between the Blood Lord and Jin Taekyung, who was fighting desperately to defend the western wall, then added:

“I worry that someone who’s always claimed to be *that person’s* most devoted servant might go overboard with his loyalty—even to the point of defying his master’s wishes.”

The words sounded as if she’d seen straight through him.

But the Blood Lord showed not the slightest hint of agitation.

He had considered that the Grand Mage might suspect his intentions ever since deciding to kill Jin Taekyung.

“That’s not just a misunderstanding. It’s senility. Do I look like an idiot who’d commit such an act of disloyalty?”

At his calm reply, not a trace of hesitation or uncertainty in his voice, the Grand Mage stared at him for a moment, then shrugged.

“Certainly, the you I’ve known so far has been far from disloyal. Though sometimes your loyalty was so excessive that you looked like an idiot.”

In the past, the Blood Lord would have bared his teeth and snarled at that. But his mind was colder than ever.

“So, what’s your answer?”

“Fine. Where should I go?”

“Take the South Gate.”

“The South Gate? You mean the Bow Saint?”

“I’ll assign you three Black Ghosts. No, four. With that much force, even the Bow Saint won’t have many options.”

What the Blood Lord said was undoubtedly true, but the Grand Mage furrowed her brow.

“Four Black Ghosts?”

There were still nine Black Ghosts who hadn’t been sent into battle.

Even after one had been lost in vain to the Fire King and Slaughter Saint’s surprise attack, they still retained their living martial prowess and had near-immortal recovery. It was hard to understand why the Blood Lord would assign four of them to her.

That wasn’t just a matter of her own safety. It meant leaving a gap in the forces that could break through the walls on all sides when the time came.

But the question that had crossed her mind disappeared the moment she heard the Blood Lord’s next words.

“Don’t hold back. You and the mages. And if the Black Ghosts appear as well, the enemy will put even greater forces at the South Gate.”

The Grand Mage finally understood the Blood Lord’s intention and let out a quiet laugh.

“So, in the end, I’m bait to draw in the Fire King or the Slaughter Saint?”

“Half right, half wrong.”

“What?”

“The Fire King won’t go to the South Gate. He’ll be busy greeting an unexpected guest.”

The Blood Lord answered without hesitation, then turned his cold gaze toward the Dalai Lama, who had been watching the northern wall all this time.

“Isn’t that right, Palace Lord?”

“……!”

His eyes trembled with emotion.

Realizing that the moment of revenge he had waited so long for had finally arrived, the Dalai Lama slowly parted his lips.

“What should this humble monk do?”

“Show that old man, the Fire King, the resentment and strength of the Potala Palace—built up over a long, long age of endurance.”

“I have waited my whole life for this moment alone.”

The Dalai Lama pressed his palms together with heartfelt sincerity, then leaped atop a massive elephant.

“Come. The time has come to avenge our ancestors.”

His quiet voice, infused with internal energy, carried on without end.

The Twelve Secret Monks, including two Supreme Peak masters, and the Potala Palace’s monks, numbering a full ten thousand, let out a roar so loud it made their ears ring.

*Bwooooo!*

A horn sounded, shaking the battlefield.

And so the great army of Xizang’s Murim, now a single religious state, charged through the torrential rain toward the North Gate.

To trample the descendants of the Fire Gate Clan, sworn enemies with whom they could never share the same sky.

To offer the head of the current Fire Gate Clan Sect Leader, the Fire King Jeok Cheongang, heir to that accursed lineage, before the spirits of their ancestors.

As the Dalai Lama’s forces quickly disappeared into the distance, the Grand Mage’s voice reached the Blood Lord’s ears.

“Does that mean the East Gate is all that’s left?”

“I’ll send two Black Ghosts to the East Gate.”

“Two? An awkward number. The Slaughter Saint could take them.”

“But that won’t happen. I’ll order them to avoid a direct fight with the Slaughter Saint as much as possible and stick to a cautious attack.”

“I take back what I said about the number being awkward.”

The Grand Mage’s lips curved softly beneath her veil.

“It seems like the right number. The Slaughter Saint won’t leave his post to help the South Gate, even if it’s in danger.”

The Blood Lord gave a faint smile to match hers.

“And that will keep them from suspecting us.”

If Dark Heaven didn’t assign any significant forces to the East Gate, that alone would arouse suspicion.

But if they had enough forces there and merely kept up a looser assault, the troops at the East Gate, including the Slaughter Saint, would have a little room to breathe—and time to look around.

Time to help their other allies, who were on the verge of collapse, unlike themselves.

And the gap that opened up at that very moment would be the crack that brought down that strong, massive dam in an instant.

*Whoosh.*

The wind and rain whipped at his clothes.

An ordinary person would have trembled in the biting cold that seeped into their bones, soaked through and through. But the Blood Lord smiled as he reached out.

An east wind.

A fierce wind blowing from the east along a tributary of the Yellow River—stronger than ever.

Along with more guests riding the surging river currents, who would bring this battle to its grand finale after the Potala Palace.

*Preee!*

Against the dark sky and driving rain, an eagle flew in from the east, cried out with a powerful call, and landed on the Blood Lord’s shoulder.

Its bones showed through in patches, and its blood-red eyes gleamed.

Recognizing the good news heralded by the eagle’s arrival, the Blood Lord stroked the hilt of the sword tucked at his waist and murmured:

“The time has come.”
```
