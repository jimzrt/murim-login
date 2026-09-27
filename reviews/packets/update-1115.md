<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1115.txt",
      "sha256": "824b40451afe40b8fdf29cddc4c5ba7797dc7c5bcee8fdc639dca6af6299ee31",
      "bytes": 11564
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "15c75bec4b67204efd413e121891bce25468e92d84f104c1e172cf960a06dae1",
      "bytes": 1656
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "31812534175ab90a1ae43243464f560a3462689ef66803e5cfefef29a922b435",
      "bytes": 244625
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "7fa4722d25a62cae957c982874e4e29774da0293d28cac858bd16b9d922085ff",
      "bytes": 915
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "69b29608f0a5856dc2753a4fc67c254eeb528a595a3011081698e43ead32098e",
      "bytes": 760
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "8472a269c5a0c691b1f497fe0907465bbde5b205a6a4bd9fd7bd94b382f2e7c8",
      "bytes": 1001
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "eeb43652fd8965d72fb53fb2612255f017c6103bc0b2b62077e246c9758fbc51",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c146762021f297c40ce5a6529103e497d63fc13e26f4d349be555d68336e6115",
      "bytes": 623
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "36c209c13e37bc3b016fa4c5bc17b9f8d3eaa8ee13a174d9bfe810d813952f59",
      "bytes": 779
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "a595dd3c7c34ca1083b01740a408d4f1d05b9af1d7ef5949c359723bcf4318ed",
      "bytes": 926
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "078c6bfad0a7e7d39db946de4e851489f9d1f936c87c625ec731e60a68fb0f72",
      "bytes": 289028
    }
  ],
  "estimated_tokens": 10576
}
-->

# Durable State Update — Chapter 1115

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
1 and safe_through 1115. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1115. Profile updates may replace only one
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
  "chapter": 1115,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1115,
    "continuity_sources": [1115],
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
    "The West Gate has fallen; more than half its garrison are casualties, and some survivors retreated to the Inner City.",
    "Jin Taekyung and Cheongpung are badly injured in the Inner City; Taekyung is still alive and has forced himself to stand.",
    "Jeong Hogun died defending others; Taekyung remembers him as a steadfast officer.",
    "Taekyung has rallied those around him to keep fighting for the Inner City's people.",
    "The Slaughter Saint remains at the South Gate to support its defense; the Bow Saint’s motives are unclear.",
    "Jeok Cheongang left the North Gate and is heading toward the Inner City, severely exhausted and injured after fighting the Blood Lord.",
    "The Dalai Lama is dead; Perfected Being Hyeoncheon is alive but barely conscious.",
    "The Blood Lord killed a wounded follower and is advancing toward the Inner City.",
    "The Kunlun Five Immortals died after using Temporary Strength Pills to hold off the Blood Lord for fifteen minutes."
  ],
  "continuity_sources": [
    1113,
    1114
  ],
  "open_questions": [
    "Will Jin Taekyung survive his injuries, and can he receive treatment from the Divine Physician?",
    "What is the Bow Saint hiding, and why did she accept the possibility of Taekyung’s death?",
    "Can the South Gate hold against the Grand Mage and the four Black Ghosts?",
    "Can the Inner City’s defenders stop the Blood Lord?"
  ],
  "safe_through": 1114,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 굉도     | **Hong Dao**       |
| 법왕     | **Dharma King**               | Hong Dao       |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마교     | **Demonic Cult**                                 |                                                       |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 우모침 | **ox-hair needle** | Extremely fine Tang Clan hidden weapon. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 시산혈해 | **sea of corpses and blood** | Description of the preceding months of bloodshed. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 철옹성 | **impregnable fortress** | Metaphor for Ares Guild's entrenched defenses. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 북문 | **North Gate** | The gate where Jin Taekyung and Yohi arrive. |
| 남문 | **South Gate** | A gate that was never built because of the rear cliff. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 성우 | **Sacred Rain** | Name later given to the rain released as the Earth Mother Goddess's blessing. |
| 마조 | **Demon Bird** | Title given by the revealed impostor who wore Chinggen’s face. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 천주 | 대술사 | master to servant | you | commanding and authoritative | Addresses her through mind-voice, ordering her to report, raise her head, and depart. |
| 대술사 | 천주 | servant to master | Lord of Heaven | extremely deferential | Uses reverent titles and self-abasing language while reporting and pleading. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1114
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and learns from past mistakes; his confidence in his overwhelming power is genuine rather than bluster, and he remains devoted to the Lord of Heaven despite resenting being treated as disposable and Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and suspects the Lord wants Jin Taekyung above all else; he recognizes Cheongpung and remembers a debt to Sword Saint Mae Jonghak.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1114
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 1105
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1114
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1114
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1111
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 919
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom he helped free from his Heart Demon, he once trained Jin Taekyung, and the Salcheonmun he destroyed now vows to pursue him.

## Korean source

```text
＃1115화



격전(激戰)이었다.

머나먼 땅에서 온 어느 승려가 갈댓잎 하나에 몸을 실어 장강을 건넌 그날로부터, 자그마치 천 년에 달하는 세월 동안 이어졌던 무림의 역사를 통틀어도 유례가 없는.

동시에, 혈전(血戰)이었다.

비단 무림뿐만이 아닌, 대륙의 지난 역사를 되짚어도 찾아볼 수 없을.

퍼걱!

정수리가 갈라지고 뇌수가 튄다.

단말마조차 남기지 못한 죽음.

그러나 이제 그 누구도 약관도 채 되지 않은 소년병의 최후에 가슴 아파하지 않는다.

아니, 할 수조차 없었다.

멈추지 않는 이 잔혹한 지옥도(地獄道)의 수레바퀴 속에서 죽음이라는 단어는 헐값이 되어 버린 지 오래였으니까.

다만 그들이 해 줄 수 있는 유일한 것이 있다면, 오직 복수뿐이었다.

“천주께서 우리와 함께 하신……!”

눈이 붉게 충혈된 광신도가 소년병의 시체를 밟으며 성벽 위에 발을 디딘 그 순간.

푹.

그의 미간 사이로, 번뜩이는 날붙이가 불쑥 튀어나왔다.

“누가 함께한다고?”

당연하게도, 이미 절명한 광신도는 대답하지 못했다.

그리고 썩은 통나무처럼 허물어지는 시체의 뒤통수에 박힌 단도(短刀)를 뽑아낸 자그마한 그림자는, 마침내 성벽 위를 점령했다는 기쁨에 휩싸여 있던 또 다른 적들을 향해 발걸음을 내디뎠다.

팟.

마치 유령처럼 사라지는 신형.

뒤늦게 발출한 검기가 그림자가 서 있던 공간을 향해 쏘아졌지만, 어디선가 불어온 한 줄기의 서늘한 바람은 이미 그들을 스쳐 지나간 후였다.

서걱, 푸화악!

칠흑 같은 밤하늘 위로 피 분수가 솟구친다.

섬광 같은 속도에 더하여 조금의 낭비도 없는 효율적인 움직임.

하지만 고작 눈 깜짝할 사이에 수십여 명의 적들을 쓰러트린 그림자, 아니 살성의 눈빛은 더없이 깊게 가라앉아 있었다.

‘한계다. 더 이상은 버티지 못해.’

비단 그 자신만을 두고 한 말이 아니다.

살성과 궁성.

두 거인의 존재감으로 철옹성이나 다름없던 남문(南門)이, 그곳을 지키는 수비군 전원이 흔들리고 있었다.

‘사실 지금까지 버틴 것만으로도 기적이나 다름없었지.’

어쩌면 처음부터 불가능한 싸움이었을지도 몰랐다.

양민들까지 동원해야 했던 아군과는 달리, 적들은 하나 같이 일정 이상의 무공에 잠력단이라는 수단까지 동원했으니.

머릿수로도, 질적으로도 턱없이 부족한 상황을 조금이나마 유지할 수 있었던 것은 그저 어디까지나 수성(守城)의 이점을 극대화하고 소수의 정예 병력을 적재적소에 운용했기 때문이었다.

그러나.

‘결국, 여기까지인가.’

살성은 혀끝에 맴도는 침음성을 삼키며 주위를 둘러보았다.

그치지 않는 장대비 너머, 말 그대로 시산혈해(屍山血海)나 다름없는 광경이 그의 시야에 가득 담겼다.

이미 의지의 한계를 아득히 넘어선, 극심한 피로에 사로잡혀 무너져 가는 아군들의 모습도 함께.

지쳤다. 모두가.

육체는 물먹은 솜처럼 무겁고, 정신은 가까스로 유지하는 것만이 고작이다.

심지어는 살성 그 자신조차도, 적지 않은 피로와 텅 비어 가는 단전을 느끼고 있었다.

‘……대술사(大術士)만 처치했더라면. 그럴 수만 있었다면 반격의 기회를 잡을 수도 있었을 텐데.’

하지만 살성이 들었던 것만큼이나. 아니, 그 이상으로 대술사는 결코 쉬운 상대가 아니었다.

그녀를 비롯한 일백여 명의 술사들을 지키는 적들의 방어진은 철벽처럼 두터웠고, 전력을 다해 그 중심부를 파고든 살성을 기다리고 있던 것은 무려 네 기나 되는 흑귀(黑鬼)였다.

그것도 온갖 강화 마법의 힘을 받아 한층 강해진.

만약 수백여 장 밖에서도 표적을 찢어발길 수 있는 천하제일의 궁사(弓師)가 그를 돕지 않았다면, 제아무리 살성이라 할지라도 지금과 같이 사지 멀쩡히 되돌아올 수 없었을 터였다.

물론, 그 와중에도 두 기의 흑귀를 쓰러트린 건 살성의 자존심과 집념이 만들어 낸 성과였다.

쉬이이잉!

불현듯 터져 나온 휘황한 섬광과 함께 찰나의 상념이 깨져 나간 그 순간.

퍼엉!

커다란 빛줄기가 살성의 뒤를 노리고 달려들던 이십여 명의 광신도들을 집어삼키며 폭발했다.

“여유롭군요. 한눈팔 시간도 있고.”

궁성의 뼈 있는 한 마디에, 살성은 대답 대신 소매를 떨쳤다.

푸푸푹!

보이지 않는 사각에서 활을 겨누고 있던 적들이 동시다발적으로 허물어졌다.

하나같이 길고 얇은 우모침(牛毛針)을 미간에 박아넣은 채.

“차라리 당신 말대로 여유로워 보였으면 좋겠소. 그래야 저놈들이 조금이라도 겁을 먹을 테니.”

“아직도 저들에게 두려움이라는 감정이 남아 있다고 생각하나요?”

“……제기랄.”

씁쓸한 욕설과 함께, 살성은 재차 신형을 내쏘았다.

광신(狂信)이라는 두 글자에 영혼까지 저당 잡힌 악귀들로부터, 한 사람이라도 더 많은 아군을 지키기 위해서.

서걱! 콰드득!

닥치는 대로 베고, 찌르고, 부러트리는 동시에 꺾었다.

그러나 그뿐이다.

한 시대를 화려하게 장식한 두 거인이 아무리 쉼 없이 적들을 쓰러트려도, 이미 지칠 대로 지친 수비군의 저항은 빠르게 수그러들었고 광신도들의 열기 띤 목소리가 성벽을 뒤덮었다.

“위대한 천주시여!” 

“당신의 위엄과 권능을 이 땅에 내리소서!”

으득.

마치 거대한 파도와 마주한 듯한 기분에, 살성은 자신도 모르게 이를 악물었다.

수백을 죽이면 수천이, 수천을 쓰러트리면 수만이 그 뒤에 있다.

과연 이 전투에 진정 끝이라는 존재하기는 할까 하는 의문이 들 정도로.

‘도대체 어떻게 해야…….’

머릿속에 떠오른 생각조차 쉽사리 이어지지 못했다.

그 또한 결국 피륙으로 이루어진 인간이지, 전지전능한 신이 아니었으니까.

‘……처음이군. 누군가가 이토록 보고 싶어지는 건.’

어느새 전신 곳곳에 아로새겨진 크고 작은 상처 때문일까.

혹은 지금 이 순간에도 빠르게 바닥을 드러내고 있는 공력 때문일까.

잊고 있던 피로와 공허함에 사로잡힌 살성은 문득 생각했다.

오래전 그날, 열 배가 넘는 마교의 대군 앞에서도 언제나 그렇듯 변함없는 승리와 확신을 가져다 주었던 한 사람을.

‘무신(武神), 당신이었다면 어떻게 했겠소?’

멍청한 질문이었다.

그였다면 애초에 이런 의문 따위는 품지 않았을 테니까.

그는 그런 사람이었다.

천하 무림에서 가장 강인하게 빛나는 세 개의 별조차 감히 범접할 수 없는, 진정한 하늘.

하지만 어째서일까.

지금 이 순간, 살성은 불현듯 또 다른 누군가의 이름을 떠올리고 있었다.

‘진태경.’

일찍이 법왕 굉도가 말한 바 있다는 신성(新星)의 주인이자, 이제는 천주의 알 수 없는 집착마저 한 몸에 받고 있는 새파란 청년.

그리고.

‘선택받은 자.’

살성은 아무것도 확신할 수 없었다.

과연 이 모든 것이 단순한 우연인지, 혹은 아주 오래전부터 저 아득한 하늘 위의 누군가에 의해 결정된 운명인지.

다만, 유일한 희망을 있는 힘껏 움켜쥘 뿐이었다.

비록 그것이 한 줌밖에 되지 않는다 하여도.

서걱!

허공을 가로지르는 단도를 따라 흘러나온 강기가 마치 채찍처럼 휘어져 성벽을 휩쓴다.

조각난 사지와 흘러넘치는 핏물 속, 얼마 남지 않은 공력을 끌어모아 일거에 적들을 도륙 낸 살성이 굳게 닫혀 있던 입술을 열었다.

“전원, 퇴각한다.”

“……!”

“……!”

가까스로 저항을 이어가고 있던 수비군들이 눈을 부릅떴지만, 이미 결심을 내린 살성의 음성에는 추호의 흔들림도 없었다.

“전령은 지금 즉시 남문과 북문에도 소식을 전하라. 각 문에 배치된 정예가 후미를 맡아 잠시 시간을 버는 동안, 남은 병력은 최대한 신속하고 질서정연하게 퇴각하도록.”

찰나지만, 한편으로는 영원과도 같은 침묵이 공간을 짓눌렀다.

그들에게 있어 성벽을 포기한다는 것은, 애써 외면해 왔던 패배라는 단어가 현실로 다가왔다는 뜻이나 진배없었으니까.

하지만 지금 이 자리에서 살성의 의견에 반대할 수 있는 유일한 사람은, 아직 침착함을 잃지 않은 눈빛으로 그를 응시하고 있었다.

― 결국, 그게 최선인가요?

문득 귓가에 내려앉는 한 줄기의 전음.

살성은 궁성의 시선을 피하지 않은 채, 담담하게 대답했다.

― 모르겠소. 다만……. 믿고 싶을 뿐이오.

그래, 그뿐이다.

천기를 읽었던 법왕 굉도가.

그 천기마저 어그러트린 혈주가.

이제는 죽었는지 살았는지조차 알 수 없는 무신이 선택한 유일한 사람을.

― 이 두 눈으로 똑똑히 보아야겠소. 어디까지가 우연이고, 운명인지.

설령 그 끝에 비참한 최후가 기다리고 있을지라도, 살성은 결코 후회하지 않을 터였다.

그가 살성이 아닌 문경으로서 지켜본 어느 애송이의 모습은, 연배와 무위를 떠나 목숨을 걸 수 있을 만한 대종사(大宗師)의 그릇을 지니고 있었으니까.

그 마음만은 모두가 같을 테니까.

― 궁성.

나직한 부름과 함께, 살성은 깊게 가라앉은 눈빛으로 궁성을 바라보았다.

― 당신이 정확히 무슨 의중을 품고 있는지는 모르나 한 가지만큼은 알고 있소. 아니, 진태경을 조금이라도 가까이했던 이들이라면 모두가 알 거요.

― …….

― 제아무리 거리를 두고 애써 입을 닫아도, 그 녀석만큼은 도무지 미워할 수 없다는 걸.

― ……!

― 나는 믿고 싶소. 그 녀석뿐만 아니라, 당신 역시도.

찰나 지간 흔들리는 동공.

하지만 그런 궁성의 동요도, 침묵도 길게 이어지지 못했다.

화아아악!

아득한 허공 위, 거센 빗줄기마저 증발시키는 거대한 불덩어리들이 유성우처럼 쏟아져 내리던 그 순간.

쉬이이잉!

벼락과도 같은 속도로 움직인 궁성의 손을 따라, 눈부신 섬광의 화살이 쏘아졌다.

꽈아아앙!

천지가 쪼개지는 듯한 굉음과 함께 붉게 물드는 하늘.

수백, 수천 개의 조각으로 나뉘어 떨어져 내리는 크고 작은 불덩어리들 아래, 굳은 얼굴로 그 광경을 바라보던 궁성이 문득 입을 열었다.

“사실 모르겠어요. 어떤 선택을 해야 하는지.”

살성이 침음성을 흘리려던 그때, 그녀가 나직이 덧붙였다.

“그래도, 나 역시 믿고 싶네요.”

“……!”

“함께 가요. 내성(內城)으로. 그 아이에게로.”

그제야 비로소, 살성의 지친 입가에 흐릿한 미소가 걸렸다.
```

## Final English reading copy

```markdown
# Chapter 1115

It was a fierce battle.

Unprecedented in all the history of Murim—a history stretching back a full thousand years, to the day a monk from a distant land crossed the Yangtze on a single reed leaf.

And at the same time, it was a bloodbath.

One the entire continent’s history had never seen, not just Murim’s.

CRUNCH!

A skull split open. Brain matter sprayed.

A death without even a final cry.

But no one grieved anymore for the end of a boy soldier who hadn’t even reached twenty.

No—they couldn’t.

In the relentless turning of this brutal hellscape, the word “death” had long since become cheap.

If there was one thing they could do for the dead, it was take revenge.

“The Lord of Heaven is with us……!”

The fanatic’s eyes were bloodshot as he stepped onto the wall, trampling the boy soldier’s corpse.

Thud.

A gleaming blade suddenly burst out between his brows.

“Who’s with you?”

Of course, the fanatic—already dead—couldn’t answer.

The small shadow pulled a dagger from the back of the corpse’s head as it crumpled like a rotten log, then strode toward the other enemies, still caught up in the joy of having seized the wall.

Whoosh.

The figure vanished like a ghost.

The Sword Energy that came flying a beat too late shot toward the space where the shadow had stood, but a cool breeze from somewhere had already swept past them.

Slice—SPLAT!

A fountain of blood arced into the pitch-black night sky.

Blinding speed, paired with efficient movement that wasted nothing.

But the shadow—no, the Slaughter Saint—had just cut down dozens of enemies in the blink of an eye, and his eyes were sunk deeper than ever.

*I’ve reached my limit. I can’t hold out any longer.*

He wasn’t talking about himself alone.

The South Gate, once an impregnable fortress thanks to the presence of two giants—the Slaughter Saint and the Bow Saint—was faltering. Every last defender stationed there was wavering.

*It was a miracle we held out this long.*

Perhaps this had been an impossible fight from the start.

Their side had even needed to call up commoners, while the enemy were all trained in a certain level of martial arts and had used Temporary Strength Pills as well.

They were hopelessly outmatched in both numbers and quality. The only reason they’d managed to hold on at all was that they’d made the most of the advantages of defending a fortress and deployed their small elite force wherever it was needed.

But—

*So this is as far as we go.*

The Slaughter Saint swallowed the groan at the tip of his tongue and looked around.

Beyond the unrelenting downpour, the scene before him was a sea of corpses and blood.

His own forces were collapsing, gripped by exhaustion that had carried them far beyond the limits of their will.

Everyone was tired.

Their bodies were heavy as waterlogged cotton, and all they could manage was to keep their minds from giving way.

Even the Slaughter Saint felt the weight of his exhaustion and his dantian running empty.

*If only we’d taken out the Grand Mage. If we’d managed that, we might have had a chance to counterattack……*

But the Grand Mage had been no easy opponent. If anything, she was more formidable than he’d heard.

The enemy’s defensive formation around the hundred or so mages, including her, had been as solid as an iron wall. When the Slaughter Saint threw everything he had into breaking through its center, he found no fewer than four Black Ghosts waiting for him.

And they had all been strengthened by every kind of enhancement spell.

If the greatest archer under Heaven hadn’t helped him—a man who could tear apart a target from hundreds of jang away—even the Slaughter Saint would never have made it back in one piece.

Still, he had managed to defeat two Black Ghosts. That was an achievement born of his pride and sheer determination.

Sssshing!

A brilliant flash suddenly erupted, shattering his brief reverie.

BOOM!

A massive beam of light swallowed and exploded among the twenty or so fanatics who had been charging at the Slaughter Saint from behind.

“You seem relaxed. Even enough to daydream.”

In response to the Bow Saint’s pointed remark, the Slaughter Saint flicked his sleeve.

Thud-thud-thud!

The enemies who had been aiming their bows from unseen blind spots crumpled all at once.

Every one of them had a long, slender ox-hair needle embedded between the brows.

“I wish I looked relaxed, like you said. Maybe then those bastards would be at least a little scared.”

“Do you think they still have any fear left in them?”

“……Damn it.”

With a bitter curse, the Slaughter Saint launched himself forward again.

To protect as many of his allies as he could from those fiends who had mortgaged their very souls to the two words “fanatical faith.”

Slice! CRACK!

He cut, stabbed, and broke whatever was in his way, striking down one foe after another.

But that was all.

No matter how tirelessly the two giants who had once adorned their age cut down their enemies, the resistance of their exhausted defenders quickly faded, and the fanatics’ fervent voices overwhelmed the wall.

“Great Lord of Heaven!”

“Let your majesty and power descend upon this land!”

Grit.

Feeling as if he were facing a massive wave, the Slaughter Saint clenched his teeth without realizing it.

For every hundred he killed, a thousand came. For every thousand he cut down, tens of thousands stood behind them.

He could hardly help wondering if this battle would ever truly end.

*What the hell are we supposed to do……?*

Even the thought that came to mind refused to take shape.

He was human, made of flesh and blood—not an all-knowing, all-powerful god.

*……This is the first time. The first time I’ve wanted to see someone this badly.*

Was it because of the large and small wounds etched across his body?

Or because his internal energy was rapidly running dry even now?

Caught in the exhaustion and emptiness he’d forgotten, the Slaughter Saint suddenly thought of someone who, long ago, had always brought him confidence and certain victory—even when facing a Demonic Cult army more than ten times their size.

*Martial God, what would you have done?*

It was a foolish question.

If he were here, he wouldn’t have entertained such doubts in the first place.

That was the kind of man he was.

A true heaven, beyond the reach even of the three brightest stars in all the Murim world.

And yet, for some reason, at that very moment, the Slaughter Saint found himself thinking of someone else.

*Jin Taekyung.*

The master of the Morning Star, the new star Dharma King Hong Dao had once spoken of—and now the young man who had drawn the Lord of Heaven’s inexplicable obsession.

And—

*The Chosen One.*

The Slaughter Saint couldn’t be sure of anything.

Was all this merely a coincidence, or was it a fate decided long ago by someone high above in the distant heavens?

All he could do was hold on to his one hope with all his might.

Even if it was no more than a handful.

Slice!

Force streamed from the dagger as it cut through the air, bending like a whip and sweeping across the wall.

Amid scattered limbs and overflowing blood, the Slaughter Saint gathered what little internal energy he had left and slaughtered his enemies in a single sweeping attack. Then he parted his tightly closed lips.

“Everyone, retreat.”

“……!”

“……!”

The defenders, who had barely been holding on, stared wide-eyed. But the Slaughter Saint had already made up his mind, and there wasn’t a hint of wavering in his voice.

“Messenger, take word to the South and North Gates immediately. The elites stationed at each gate will cover the rear and buy us some time. The rest of the troops are to retreat as quickly and orderly as possible.”

Silence pressed down on the space between them. It lasted only an instant, yet felt like eternity.

To them, abandoning the wall meant that the word they’d been trying so hard to ignore—defeat—was finally becoming real.

But there was only one person there who could oppose the Slaughter Saint’s decision, and she was watching him with an unshaken gaze.

*In the end, is that the best we can do?*

A line of Sound Transmission settled in his ear.

Without looking away from the Bow Saint, the Slaughter Saint answered calmly.

*I don’t know. But…… I want to believe.*

Yes. That was all.

The one person chosen by Dharma King Hong Dao, who had read the heavenly patterns.

By the Blood Lord, who had thrown those very patterns into disarray.

And by the Martial God, whose life or death was now unknown.

*I want to see it clearly with my own eyes. Where coincidence ends and fate begins.*

Even if a wretched end awaited him, the Slaughter Saint would never regret it.

The young brat he’d watched as Mungyeong—not as the Slaughter Saint—had the bearing of a Great Master worth risking one’s life for, regardless of age or martial prowess.

Everyone felt the same way.

*Bow Saint.*

At his quiet call, the Slaughter Saint looked at the Bow Saint, his gaze sunk deep.

*I don’t know exactly what you have in mind. But there’s one thing I do know. No—anyone who’s been even a little close to Jin Taekyung knows it.*

*……*

*No matter how much you distance yourself and try to keep your mouth shut, you just can’t bring yourself to hate that boy.*

*……!*

*I want to believe in him. And in you, too.*

Her pupils wavered for an instant.

But the Bow Saint’s agitation—and her silence—didn’t last long.

Fwoosh!

Far above them, enormous balls of fire that evaporated even the torrential rain came pouring down like a meteor shower.

Sssshing!

The Bow Saint’s hand moved with the speed of lightning, and a dazzling arrow of light shot forth.

KABOOM!

The sky turned red with a crash that seemed to split heaven and earth.

Beneath the massive and small fireballs that fell in hundreds, then thousands of pieces, the Bow Saint watched the scene with a grim expression before speaking.

“I honestly don’t know what choice I should make.”

Just as the Slaughter Saint was about to groan, she quietly added:

“Still, I want to believe, too.”

“……!”

“Come with me. To the Inner City. To that boy.”

At last, a faint smile touched the Slaughter Saint’s tired lips.
```
