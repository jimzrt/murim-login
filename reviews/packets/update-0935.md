<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0935.txt",
      "sha256": "5a9057f4ee1e9d682e384a93dfac493becd478679ee4d7ea550f552208df74b9",
      "bytes": 14101
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6f949e4f3cab3c644adea1a48531368f68a73310ecbe8b6ffcaf4585c4ce661f",
      "bytes": 1906
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b51f7a56cfa82ca1164fe5c2453945cbf42f0adc0ae050d159295fd4e544b433",
      "bytes": 232009
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "e18c29e3328cc4a8fb846985b6e99ef0dcf7d00316a1c7b13a93d53bbbcb011b",
      "bytes": 837
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b87645beafb8f84fd6cf6443afcfd57787588a3e51bde72613d4564d77ada975",
      "bytes": 759
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "77e7e59d93e5d9b562b960084c4abb81e478f86610544696ae1208e60d2fe423",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "72fe6ecd84baa9a54023540281a3f8f65a538fe89a5275c87db8d6483fedf4b2",
      "bytes": 1343
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2ec07365ac28f3e84224e1feac40641d8fc00927960592c2ade3c7070e8919cd",
      "bytes": 622
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "8e1a1417e84cd81652bc8e65b83ec523f0147dd9a1a7d1039e72c8ee888df2df",
      "bytes": 767
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 11829
}
-->

# Durable State Update — Chapter 935

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
1 and safe_through 935. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 935. Profile updates may replace only one
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
  "chapter": 935,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 935,
    "continuity_sources": [935],
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
    "The System update reward is a very durable pocket watch that appears broken and bears the faint inscription, “A broken clock is right twice a day”; its significance is unknown.",
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin.",
    "Hong Jin is Eunuch Hong, responsible for the East Depot; the Cang Gong post remains vacant.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Eastern Heaven Demon Lord’s final instruction was to find an unspecified object at a particular place.",
    "The Emperor was poisoned with the Blood Soul Gu after the coup; it has reached his marrow, and he has endured its effects for more than ten years.",
    "The Divine Physician examined the Emperor three days before chapter 934 and said the condition was too advanced for him to treat at present.",
    "The Emperor wants to live, chiefly to protect Zhu Bao and serve the country and its people.",
    "The Emperor expects a devastating war and fears Zhu Bao is too young to bear the burden of ruling through it.",
    "Taekyung promises to save the Emperor."
  ],
  "continuity_sources": [
    934
  ],
  "open_questions": [
    "What is the Martial God’s identity, and how did he know a chosen one would appear?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "What object and place did the Eastern Heaven Demon Lord refer to, and what significance does the object have?",
    "What is the significance, if any, of the broken pocket watch given as the System update reward?"
  ],
  "safe_through": 934,
  "temporary_decisions": [
    "Taekyung will keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 상태               | **Status**                     |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 황하 | **Yellow River** | River along which civilization began. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 혈혼고 | **Blood Soul Gu** | Rare gu poison found deep in Nanman. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |
| 무영 | **No Shadow** | The concealed Supreme Peak assassin serving the Emperor. |
| 앵속 | **poppy** | The dried poppy sap Hong Jin describes; Taekyung identifies it as opium. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 무영 | employer addressing a hidden assassin in his service | No Shadow | authoritative | The Emperor calls him by name and tells him to withdraw. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 소교 | 백연 | political ally addressing a senior military commander | you | informal and direct | So Gyo uses 당신 and speaks without formality; no personal name or title is established. |
| 백연 | 소교 | military commander addressing a powerful political ally | you | formal and deferential | Baek Yeon uses 그대 while questioning So Gyo; she speaks without formality, which he accepts as her due. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 소교 | Emperor questioning a political ally | you | quiet and direct | The Emperor questions So Gyo through Sound Transmission about why she is only watching. |
| 소교 | 황제 | political ally answering the Emperor | Your Majesty | calm and direct | So Gyo answers the Emperor through Sound Transmission without wavering. |
| 황제 | 백연 | Emperor to the imperial court’s foremost military commander and trusted comrade | Baek Yeon | Direct and familiar; framed as a request rather than an order | The Emperor asks Baek Yeon to sound the war drum. |
| 황제 | 주표 | older brother addressing his younger brother and newly appointed Crown Prince | Bao’er | intimate and authoritative | The Emperor uses a warm childhood-style name before commanding Zhu Bao to accept the succession. |
| 주표 | 황제 | younger brother and Crown Prince addressing the Emperor | Your Majesty | formal and deferential | Zhu Bao formally accepts the Emperor’s command. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 934
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor, carrying out the late Emperor’s final command to plan for the future alongside the fourth prince; he treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 934
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 930
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 934
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 934
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 933
- **Aliases:** None
- **Role:** So Gyo is the Bow Saint, a Supreme Peak master and palace attendant assigned to Prince Shangshan, whose two curved swords can join into their original bow form.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** So Gyo recognizes Jin Taekyung as the chosen one spoken of by the Martial God; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃935화



“진태경이 다녀갔다 들었습니다.”

드넓은 침소에 홀로 남아 생각에 잠겨 있던 황제는, 불현듯 들려온 사내의 목소리에도 당황하지 않았다.

그는 어떠한 허락 없이도 건청궁의 안팎을 자유롭게 드나들 수 있는 극소수, 아니 어쩌면 유일한 사람이었으니까.

“한발 늦었네, 백연. 그는 이미 반 시진 전에 떠났어.”

“상관없습니다. 소장은 폐하를 뵈러 온 것뿐이니까요.”

금의위 지휘사 백연의 담담한 대답에, 황제가 짐짓 눈살을 찌푸렸다.

“그건 짐이 사양하고 싶군. 자네 얼굴이라면 이미 질리도록 보지 않았나.”

“해서, 지난 사흘 동안은 평안하셨습니까?”

“말이라고 하나? 잔소리꾼이 없어지니 속이 다 시원하더군.”

“섭섭하군요.”

“너무 토라지진 말게. 시도 때도 없이 날 감시하던 누군가도 자네와 비슷한 처지니까.”

“무영(無影), 그 친구가 들으면 저보다도 섭섭해할 겁니다.”

“그래서 없을 때 말하는 것 아닌가. 이제 더 이상 짐의 호위가 아니니, 이렇게 가끔 뒷담화도 할 수 있겠지.”

“이런. 폐하는 못 당하겠습니다.”

졌다는 듯 고개를 내젓는 백연의 모습에, 황제가 피식 실소를 흘렸다.

“그래, 표아는 잘 지내고 있나?”

“물론입니다. 더할 나위 없으시지요.”

그러나 백연의 대답에도 황제의 낯빛에 깃든 근심은 사라지지 않았다.

“그 어린 나이에 이와 같은 일을 겪었으니 아직 심신이 불안정할걸세. 자네들이 곁을 지켜 주어야 해.”

우려가 담긴 음성.

백연 역시 그런 황제의 마음을 모르지 않았다.

십수 년 만에 돌아온 친혈육이다.

안전을 위해서였다고는 하나, 사실상 방치된 것이나 다름없었던 막냇동생을 향한 애정과 걱정은 아무리 해도 모자랐다.

오죽했으면 암중 호위인 무영과 최측근인 백연을 황태제의 직속으로 붙였을까.



‘그 아이를 보살펴 주게. 자네들이라면 믿고 맡길 수 있어.’



사흘 전, 황제의 명령 아닌 부탁을 받았던 기억을 떠올리며 백연이 입을 열었다.

“비록 지학(志學, 열다섯)도 되지 않으셨으나, 제가 본 이들 중 두 번째로 단단하고 올곧은 심지를 지니신 분입니다. 나이가 믿기지 않을 정도지요.”

“두 번째?”

“첫 번째는 폐하십니다.”

백연의 망설임 없는 대답에, 잠시 할 말을 찾지 못하던 황제는 두 손을 들어 올렸다.

“이번에는 짐이 졌군. 안 하던 아부를 하다니. 백연 자네도 많이 변했어.”

“맞습니다. 폐하께서 안 하시던 농담을 하시는 것처럼 말이지요.”

“이런. 졌다고 하지 않았나. 흰소리는 그만하게.”

“지금 소장이 드린 말씀이, 그저 듣기 좋은 아부나 흰소리로 들리십니까?”

백연이 희미하게 웃으며 말을 이었다.

“진심입니다. 언제나 폐하를 경애하고 존경했습니다. 다른 이라면 몇 번이나 포기했을 험난한 가시밭길을, 폐하께서는 피투성이가 된 두 발로 나아가지 않으셨습니까.”

오롯이 느껴지는 그 진심에, 황제는 입을 다물었다.

갑작스럽게 북받친 무언가가 목을 꽉 막아 버려서 당장은 아무 말도 할 수 없을 것 같았다.

단지 차오르는 감정을 애써 억누르며 목소리를 쥐어짜 낼 뿐이었다.

“그 가시밭길을 홀로 걸어야 했다면, 짐은 도중에 포기했을걸세. 자네들이 없었다면 불가능했어.”

“소장은 그렇게 생각하지 않습니다.”

고개를 가로저은 백연이 천천히 말을 이었다.

“다른 누구도 아닌 폐하셨기에 저희가 믿고 따를 수 있었습니다. 오직 폐하께서 가장 큰 책임감과 고통을 감내하셨기에, 오늘 같은 날이 있을 수 있는 겁니다.”

“……!”

“칼날을 감춘 역적들을 경계하면서도 정무(政務)를 소홀히 하신 적이 있습니까? 소장이 본 폐하께서는 언제나 잠을 줄이며 무공을 연마하시고, 상소(上疏)를 처리하셨으며 동시에 병마와 싸우셨습니다.”

황제의 얼굴 위로 만감이 스쳐 지나갔다.

그래, 그랬다.

그런 시절이, 그럴 수밖에 없었던 시절이 있었다.

“당연한 일이었네. 잠은 사치였으니.”

지난 십여 년간, 하루 한 시진 이상 자본 적이 없었다.

아니, 그조차도 편안히 잠들지 못했다.

서서히 죽어 가는 육신을 느끼면서도 정신을 늘 깨어 있어야 했으니까.

천자(天子)란 그런 존재였다.

천하에서 가장 높은 위치였기에 누구보다 먼저 거센 비바람을 맞아야 하며, 동시에 발밑에 펼쳐진 모든 것을 굽어보고 보살펴야 하는.

그것이 황제가 생각하는 자신의 위치였고, 바로 그랬기에 백연은 그를 마음 깊이 존경할 수밖에 없었다.

“결심하는 것은 손바닥 뒤집듯이 쉽지만, 그 결심을 행동으로 보이는 것은 산을 옮기는 것만큼이나 어렵습니다.”

처음에는 백연도 확신할 수 없었다.

마지막 선택지였던 대국의 네 번째 황자가 과연 함께 대업을 도모할 수 있는 인물인지.

천자라는 무소불위의 지위에 오를 만한 사람인지.

그러나 그는 해냈다.

누구보다 훌륭하게.

황실의 비고에 산더미 같은 금은보화를 쌓아 두었음에도 늘 검소했고, 천하절색의 미인들을 앞에 두고도 여색을 탐하지 않았으며, 심지어는 자신의 막냇동생이 위태로워질 것을 우려해 후사(後嗣)조차 보지 않았다.

그래야만 암천이 주표에게 어떤 위해도 끼치지 않을 테니까.

황제를 대체할 명분과 정통성을 갖춘 그 어린아이를 섣불리 죽이거나, 빠르게 숙주의 숨통을 끊는 혈혼고를 주입할 수 없을 테니까.

“폐하께서 당연하게 여기셨던 그 모든 것들은, 하나같이 당연할 수 없었던 것들뿐이었습니다.”

“……!”

나직하게 울려 퍼지는 백연의 음성에, 황제의 눈꺼풀이 파르르 떨렸다.

몰랐다.

백연이 자신을 이렇게 생각하고 있었는지.

지나온 길을 문득 되돌아보니, 지금껏 진심을 드러내지 못했던 건 황제 자신뿐만이 아니었다.

“짐이…… 도대체 무슨 말을 해야 할지 모르겠군.”

황제의 입술 사이로 흘러나오는 억눌린 목소리에 백연이 너털웃음을 터트렸다.

“아무 말씀 안 하셔도 됩니다.”

“그래도 무슨 말이라도 하는 것이 좋지 않을까.”

“글쎄요. 괜히 분위기만 더 어색해지지 않을까 싶습니다만.”

절레절레 고개를 내저은 황제가 문득 혀를 찼다.

“백연 자네, 지금껏 짐이 알던 그 사람이 맞긴 한가?”

“그것이 대관절 무슨 말씀이십니까.”

“몰라서 묻나? 언제나 인정사정없이 굴었으면서.”

“설마 무공을 익히셨을 때를 말씀하시는 겁니까?”

“맞네. 감히 옥체(玉體)에 손을 대는 것을 용서해 주시기 바랍니다, 하더니 오만 곳을 두들겨 패던 그때 말일세.”

“아니, 갑자기 그 이야기가 왜 나오는 겁니까.”

불쑥 튀어나온 옛 과거에 백연이 눈살을 찌푸렸다.

“그리고 그때도 말씀드렸지만, 무공은 원래 맞아야 느는 겁니다. 소교…… 아니, 궁성도 소장의 의견에 동의하지 않았습니까.”

“그래, 그랬지. 심지어 나중에는 둘이 같이 두들겨 패더군. 너무 아파서 지금이라도 때려치울까 한참을 고민했네.”

“소장이 칼 들고 협박이라도 했습니까? 먼저 가르침을 청하신 것은 폐하십니다.”

“지금 같은 말투도 마찬가지일세. 짐이 힘들어할 때마다 어김없이 찾아와서 온갖 쓴소리에, 천자를 대하는 예법 따위는 어디에 버리고 왔는지 하오체까지 써 가며 몰아세우지 않았나.”

“그건…….”

말꼬리를 흐린 백연이 슬쩍 고개를 돌려 허공을 바라봤다.

무공 수련 과정에서 옥체에 손을 댄 것은 지도 차원이라고 넘어갈 수 있지만, 지금 나오는 이야기는 다르다.

비록 황제를 북돋기 위해서라고는 하나, 백연이 생각하기에도 자신이 간혹 보였던 언행은 군신 간의 예의라고는 찾아볼 수 없는 불충한 것이었으니까.

“그, 폐하.”

“불과 얼마 전까지도 그랬으니 모르는 척하지 말게. 표아가 입궁한 뒤 며칠 지나지 않아서 짐을 찾아와 한바탕 퍼부었었지.”

“그것은 대업을 코앞에 두고 앵속(罌粟)을 하고 계시니, 심신이 무너질까 염려되어 그런 것뿐입니다.”

“그거랑 하오체가 무슨 상관인가? 심지어 짐은 며칠 내내 앓아누워 있다가 막 기운을 차린 상태였네. 조금이라도 고통을 잠재우기 위해 앵속을 할 수밖에 없었단 말일세.”

“압니다. 소장도 알긴 했는데, 그래도 폐하를 걱정하는 마음에.”

괜히 허공을 향해 눈동자를 이리저리 굴리며 말을 잇던 백연이 문득 입을 다물었다.

그의 시야 끝에 아슬아슬하게 들어온, 황제의 웃고 있는 얼굴 때문이었다.

“……이런.”

“패배를 인정하나?”

모든 것이 황제의 장난이었음을 안 백연이 한숨을 내쉬었다.

“그리하지요.”

“이것으로 자네가 한 번, 짐이 두 번 이겼군.”

“전적까지 따질 셈이십니까?”

“짐도 한때는 자네와 같은 무장(武將)이었네. 장수에게 승패보다 중요한 것이 있나?”

재미있다는 듯이 웃고 있는 황제의 모습에, 이제는 백연도 덩달아 너털웃음을 터트릴 수밖에 없었다.

무엇이 중요하랴.

황제가 즐겁다면 그것으로 되었다.

그에게는 사흘 전만 하더라도 서서히 드리워지는 죽음의 그림자에 그늘져 있던 황제의 얼굴이, 보름달처럼 환하게 빛나고 있다는 것만이 중요했다.

그리고…… 한편으로는 씁쓸했다.

지금 이 순간, 이미 예정된 죽음을 마음 깊이 인정하고 받아들인 것 같은 황제의 모습이.

그런 황제를 바라보며 따라 웃어 주는 것밖에 할 수 없는 자신의 처지가.

‘압니다. 왜 소장과 무영을 황태제 전하께 보내셨는지.’

단지 혹시 모를 사태를 우려해서, 하나뿐인 아우이자 후계자를 지키기 위해서가 아니다.

황제는 스스로 죽음 그 이후를 대비하고 있었다.

더 늦기 전에 그를 따르는 충복들과 세력을 황태제 주표에게 넘기고 있었다.

정작 그토록 아끼고 사랑하는 아우에게는 지난 사흘간 얼굴 한 번 보여 주지 않은 채.

‘보여 주기 싫으신 거겠지요. 당신의 이런 모습을.’

십수 년 만에 만난 두 형제에게 있어, 곧 다가올 죽음은 비단 황제 한 사람만의 이별이 아니다.

주표.

대국의 새로운 후계자 역시 이별을 겪어야 한다.

이제야 가족의 정과 진심을 알게 된 일점혈육(一點血肉)을 떠나보내야 한다.

황제 역시 그 사실을 알고 있을 것이다.

하지만 이별을 준비해야 한다는 사실을 알려야 함에도, 슬퍼할 아우를 마주하기 두려워 만남을 거부하고 있으리라.

‘……이런.’

백연은 어느새인가 내려간 입꼬리를 억지로 끌어올렸다.

그리고 이 순간 황제가 느끼고 있을 찰나의 즐거움을 깨트리지 않기 위해, 애써 밝은 목소리로 입을 열었다.

“그나저나 오늘은 기분 좋은 일이 있으신 모양입니다. 진태경 그자가 무슨 재미있는 소식이라도 가져왔습니까?”

“재미있는 소식이라, 있었지.”

“소장도 듣고 싶군요.”

“별거 아닐세.”

그리고 다음 순간 황제가 웃으며 덧붙인 말에, 백연의 입가에 맺혀 있던 미소가 씻은 듯이 사라졌다.

“짐을 살려 주겠다더군. 어떻게 해서든.”

“……!”

“재미있더군. 의술에 관해서는 아무것도 모르면서 그토록 호언장담하는 모습이. 그런데 백연, 더 재미있는 사실이 무엇인지 아나?”

황제가 대답을 기다리지 않고 말을 이었다.

“그 허무맹랑한 말 몇 마디가, 짐을 기대하게 만든다는 거야.”

희한한 일이었다.

어찌 그리 확신에 찬 얼굴로, 반짝이는 눈으로 그토록 호언장담할 수 있는 것인지.

그리고 황제는 그런 진태경의 모습이 썩 즐거웠다. 고마웠다.

자신도 포기한 목숨을, 저 무엄한 무림인은 어떻게든 되살리겠다 하고 있었으니.

그러나 그와는 별개로, 황제가 인지하고 있는 현실은 냉정했다.

‘불가능하겠지. 아마도.’

예정된 죽음 앞에 놓인 이에게 희망은 얼마나 잔인한가.

잠깐의 기대감은 이미 고이 접어 마음 깊숙한 곳에 보관해 두었다. 지금은 그저 훨씬 홀가분해진 마음으로 눈앞의 충신을 대하고 싶었다.

“표정이 좋지 않군. 짐은 괜찮으니 백연 자네는 신경 쓰지 말게.”

“허나 이 사실이 밖으로 새어 나가기라도 한다면…….”

근심 어린 백연의 모습에, 황제는 웃으며 손을 내저었다.

“이미 다른 누구에게도 발설하지 않겠다고 짐과 약조했네. 진태경은 충분히 믿을 만한 사내야.”



* * *



“그러니까.”

내 이야기를 끝까지 들은 적천강이 무거운 목소리로 말을 이었다.

“황제가 혈혼고에 중독되었다?”

나는 망설임 없이 고개를 끄덕였다.

“예.”

약속은, 어기라고 있는 거다.
```

## Final English reading copy

```markdown
# Chapter 935

“I heard Jin Taekyung came by.”

The Emperor, alone in his vast bedchamber and lost in thought, wasn’t startled by the man’s sudden voice.

He was one of the very few—perhaps the only one—who could come and go freely in Qianqing Palace, inside or out, without asking permission.

“You’re a step too late, Baek Yeon. He left half a shichen ago.”

“That doesn’t matter. I came only to see Your Majesty.”

At Commander Baek Yeon’s calm reply, the Emperor affected a frown.

“I’d rather decline. I’ve already seen your face more than enough.”

“Then have you been at peace these past three days?”

“What kind of question is that? It’s been a relief not having a nag around.”

“I’m hurt.”

“Don’t sulk too much. Someone who used to keep an eye on me around the clock is in much the same position as you.”

“If No Shadow heard that, he’d be even more hurt than I am.”

“That’s why I’m saying it while he’s not here. He’s no longer my bodyguard, so I can indulge in the occasional bit of gossip behind his back.”

“Well. I can’t win against Your Majesty.”

Baek Yeon shook his head as if conceding, and the Emperor let out a quiet laugh.

“So, is Bao’er doing well?”

“Of course. He couldn’t be doing better.”

Yet even Baek Yeon’s answer couldn’t banish the worry from the Emperor’s face.

“He’s still young, and he’s been through something like this. He must be unsettled, body and mind alike. You all need to stay by his side.”

There was concern in his voice.

Baek Yeon understood how the Emperor felt.

His own flesh and blood had returned after more than a decade.

Though it had been for his safety, the youngest brother he’d all but abandoned deserved all the love and worry he could give him.

That was why he had assigned No Shadow, his hidden bodyguard, and Baek Yeon, his closest confidant, directly to the Crown Prince.



*“Look after him. I can trust him to you.”*



Remembering the Emperor’s request—not an order—from three days ago, Baek Yeon spoke.

“Though His Highness hasn’t even turned fifteen, he has the second strongest and most upright spirit of anyone I’ve ever met. It’s hard to believe he’s so young.”

“Second?”

“First is Your Majesty.”

At Baek Yeon’s immediate answer, the Emperor couldn’t find a response for a moment. Then he raised both hands.

“I’ll concede this one. You’re flattering me when you never used to. You’ve changed a lot, Baek Yeon.”

“That’s true. Much like how Your Majesty has started making jokes.”

“Come now. I already said I conceded. Enough with the nonsense.”

“Do the words I just spoke sound like empty flattery or nonsense to you?”

Baek Yeon continued with a faint smile.

“I meant every word. I’ve always admired and respected Your Majesty. You kept walking down a brutal, thorn-covered road that others would have given up on time and time again, your feet covered in blood.”

Faced with the sincerity in his words, the Emperor fell silent.

Something surged up inside him and caught in his throat. He didn’t think he could say anything just then.

All he could do was fight down the rising emotion and force his voice out.

“If I’d had to walk that road alone, I would have given up along the way. I couldn’t have done it without you all.”

“I don’t believe that.”

Baek Yeon shook his head and continued slowly.

“It was because it was Your Majesty, and no one else, that we were able to trust and follow you. It’s because you alone bore the greatest responsibility and pain that a day like this is even possible.”

“……!”

“Even while watching out for rebels with blades hidden up their sleeves, did you ever neglect the affairs of state? The Your Majesty I saw always cut back on sleep to practice martial arts, handle memorials, and fight your illness all at once.”

A jumble of emotions crossed the Emperor’s face.

Yes. That was how it had been.

There had been such days—days when it could be no other way.

“It was only natural. Sleep was a luxury.”

For more than ten years, he had never slept for more than one shichen in a day.

No—even then, he had never slept peacefully.

He had to keep his mind alert, even as he felt his body slowly dying.

That was what it meant to be the Son of Heaven.

The highest person under heaven had to face the fiercest storms before anyone else, while looking down on and caring for everything spread out beneath him.

That was where the Emperor believed he stood. And that was why Baek Yeon could do nothing but respect him from the bottom of his heart.

“Making a decision is as easy as turning your hand over, but showing that decision through your actions is as hard as moving a mountain.”

At first, Baek Yeon hadn’t been certain, either.

Whether the Great Nation’s fourth prince, their last remaining choice, was someone with whom they could pursue their great undertaking.

Whether he was fit to ascend to the Son of Heaven’s all-powerful position.

But he had done it.

Better than anyone.

Though the Imperial treasury was piled high with mountains of gold and silver, he had always lived frugally. Though peerlessly beautiful women had been presented before him, he had never indulged in women. He had even chosen not to produce an heir, for fear of putting his youngest brother in danger.

That way, Dark Heaven wouldn’t be able to harm Zhu Bao.

They couldn’t recklessly kill a child with the legitimacy and right to replace the Emperor, or inject him with Blood Soul Gu, which would quickly kill its host.

“Everything Your Majesty took for granted was something that could never have been taken for granted.”

“……!”

At the quiet ring of Baek Yeon’s voice, the Emperor’s eyelids trembled.

He hadn’t known.

He hadn’t known Baek Yeon thought of him that way.

Looking back over the road he’d traveled, the Emperor realized he wasn’t the only one who had kept his true feelings hidden. Baek Yeon had, too.

“I…… don’t know what I should say.”

At the Emperor’s choked voice, Baek Yeon burst into hearty laughter.

“You don’t have to say anything.”

“Wouldn’t it be better to say something, though?”

“I’m not sure. I think it would only make things more awkward.”

The Emperor shook his head and clicked his tongue.

“Baek Yeon, are you really the same person I’ve always known?”

“What on earth do you mean?”

“Do you really have to ask? You’ve always been merciless.”

“Are you talking about when you were learning martial arts?”

“I am. You said, ‘Please forgive me for laying hands on Your Majesty’s precious body,’ then proceeded to beat me all over.”

“Why are you bringing that up all of a sudden?”

Baek Yeon frowned at the unexpected reminder of the past.

“And as I told you back then, the way to improve at martial arts is to get hit. So Gyo…… I mean, the Bow Saint agreed with me, didn’t she?”

“Yes, she did. The two of you even teamed up to beat me later. It hurt so much I spent ages wondering if I should quit right then and there.”

“Did I threaten you with a sword? You were the one who asked me to teach you.”

“Your manner of speaking now is just the same. Whenever I struggled, you’d come by without fail and lay into me, and you’d push me around using the familiar *hao* form of address, as if you’d forgotten every bit of etiquette due to the Son of Heaven.”

“That was……”

Baek Yeon trailed off and glanced away at the empty air.

During martial arts training, he could excuse laying hands on the Emperor’s person as instruction. But this was different.

Even if it had been to encourage the Emperor, Baek Yeon himself had to admit that some of his words and actions had been entirely unbecoming of a loyal subject.

“Your Majesty……”

“Don’t pretend you don’t remember. You were like that until just recently. It wasn’t even a few days after Bao’er entered the palace that you came to see me and gave me a thorough tongue-lashing.”

“You were taking poppy with the great undertaking right in front of us. I was worried it would destroy you, body and mind.”

“What does that have to do with using the familiar form of address? I’d been bedridden and suffering for days, and had only just recovered some strength. I had to take poppy to ease the pain, even a little.”

“I know. I did know, but I was worried about you, Your Majesty.”

Baek Yeon’s eyes darted around as he kept talking to the empty air. Then he suddenly fell silent.

At the edge of his vision, he caught sight of the Emperor’s smiling face.

“……I see.”

“Do you concede defeat?”

Realizing that the Emperor had been teasing him the whole time, Baek Yeon sighed.

“I do.”

“Then you’ve won once, and I’ve won twice.”

“Are you keeping score now?”

“I used to be a general, just like you. What matters more to a general than victory or defeat?”

At the sight of the Emperor laughing with evident delight, Baek Yeon couldn’t help joining in with a hearty laugh.

What else mattered?

If the Emperor was happy, that was enough.

What mattered was that the Emperor’s face, still shadowed by the approaching specter of death just three days earlier, now shone as brightly as a full moon.

And yet…… a part of him felt bitter.

The Emperor looked as though he had already accepted, deep in his heart, the death that was waiting for him.

All Baek Yeon could do was look at him and laugh along.

*I know why you sent No Shadow and me to serve His Highness.*

It wasn’t only because the Emperor feared something might happen and wanted to protect his one and only younger brother and heir.

The Emperor was preparing for what would come after his death.

Before it was too late, he was handing over his loyal retainers and his power base to Crown Prince Zhu Bao.

All while not showing his face even once to the younger brother he cherished and loved so dearly these past three days.

*You don’t want him to see you like this.*

For the two brothers who had reunited after more than a decade, the death drawing near wouldn’t be a parting that only the Emperor had to face.

Zhu Bao.

The Great Nation’s new heir would have to endure a parting, too.

He would have to say goodbye to the only blood relative he had, now that he had finally come to know the affection and sincerity of family.

The Emperor must have known that, too.

Even though he had to tell his younger brother to prepare for their parting, he was afraid to face him in his grief and so refused to meet.

*……I see.*

Baek Yeon forced the corners of his mouth back up.

Then, to keep from spoiling the brief joy the Emperor was feeling at that moment, he opened his mouth in as bright a voice as he could manage.

“By the way, something good must have happened today. Did Jin Taekyung bring you some amusing news?”

“Amusing news? There was some.”

“I’d like to hear it, too.”

“It was nothing special.”

And the next words the Emperor added with a smile caused the smile on Baek Yeon’s lips to vanish completely.

“He said he’d save me. No matter what it took.”

“……!”

“It was amusing. He doesn’t know the first thing about medicine, yet he made such a bold promise. But Baek Yeon, do you know what’s even more amusing?”

Without waiting for an answer, the Emperor continued.

“Those few absurd words made me feel hopeful.”

It was strange.

How could Taekyung make such a bold claim, with such certainty on his face and such a gleam in his eyes?

And the Emperor had found the sight of Jin Taekyung like that rather delightful. He was grateful to him, too.

His own life was something he had already given up on, yet that irreverent martial artist was determined to bring him back to life somehow.

But separate from that, the Emperor was fully aware of reality.

*It’s probably impossible.*

How cruel was hope to someone standing before a death that had already been foretold?

He had folded away that brief surge of hope and put it somewhere deep in his heart. For now, he simply wanted to speak to the loyal subject before him with a much lighter heart.

“You look troubled. I’m fine, so don’t worry about me.”

“But if this were to get out……”

The Emperor smiled and waved a hand at Baek Yeon’s worried expression.

“I’ve already made a promise with him that he won’t tell anyone else. Jin Taekyung is a man I can trust.”

* * *

“So……”

Jeok Cheongang spoke in a heavy voice after hearing me out.

“The Emperor’s been poisoned with the Blood Soul Gu?”

I nodded without hesitation.

“Yes.”

A promise is there to be broken.
```
