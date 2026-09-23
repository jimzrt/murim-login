<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0896.txt",
      "sha256": "661136ba600c05334d3f20c059f0085248bd6550af2e12a11ded776899360e7c",
      "bytes": 12804
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bc5f961e6ae2a299e12337b698ebed47c296ab984d9926f2230167c7c7603f42",
      "bytes": 901
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e97b0d558b9273a9257e26e760fa1192201c3613127339daa699815904154f1b",
      "bytes": 230652
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "cd4584e82213c9c3e1eec24a60ff869539ae187f92e39c730dbce5d0146581da",
      "bytes": 983
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f4da4733288019eadead86f47184b6a24e76642100a93446b3d16d24054e663d",
      "bytes": 759
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c0df92778bf1a150720fdc30175286b423aab3b520b51706ebe5df7788853163",
      "bytes": 1958
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "94492124055911f2fecfa079be847dbf67c7868e98a241588f4a8b63199011ed",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "07655934a7cbb3b97878cccfd9f5912b8eab6966dc7d7c58ff0baeaccd846cfa",
      "bytes": 936
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "df749591daed38f8a657edf4c82529975baa39d13fd4cfe20c3082712f54df76",
      "bytes": 952
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "b4ba33803d79470cefad4df5c0ec8f5b04ee197cabbfd621720172b387fdb32d",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8ead4207b37bea0c8bdc317b844fae2124946506bd434491dd7489b0ce8d1c7b",
      "bytes": 261385
    }
  ],
  "estimated_tokens": 10993
}
-->

# Durable State Update — Chapter 896

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
1 and safe_through 896. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 896. Profile updates may replace only one
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
  "chapter": 896,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 896,
    "continuity_sources": [896],
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
    "So Gyo first appeared during the coup more than ten years ago and, alongside Baek Yeon, defeated Cang Gong, leaving him gravely injured; Ma Sanbao says her intervention made the coup succeed.",
    "Ma Sanbao chose Jin Taekyung and Jeok Cheongang as discreet allies for the restoration army because they would help Prince Shangshan and could face So Gyo; he avoided formal Murim Alliance involvement to preserve secrecy.",
    "Jin responds to Ma Sanbao’s invitation to join the restoration army by asking about the joint pledge, signaling willingness to join."
  ],
  "continuity_sources": [
    895
  ],
  "open_questions": [
    "Who is So Gyo, and what are her true aims and allegiance?",
    "How much of her strength did So Gyo use during the coup and in her later encounters with Jin?"
  ],
  "safe_through": 895,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 살성     | **Slaughter Saint**           | —              |
| 십왕     | **Ten Kings**       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 칭호               | **Title**                      |
| 사천     | **Sichuan**            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 시산혈해 | **sea of corpses and blood** | Description of the preceding months of bloodshed. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 소교 | 백연 | political ally addressing a senior military commander | you | informal and direct | So Gyo uses 당신 and speaks without formality; no personal name or title is established. |
| 백연 | 소교 | military commander addressing a powerful political ally | you | formal and deferential | Baek Yeon uses 그대 while questioning So Gyo; she speaks without formality, which he accepts as her due. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 895
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 895
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 895
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Ma Sanbao recruited Jin and Jeok as discreet allies for the restoration effort supporting Prince Shangshan, and Jin signals willingness to join by asking for the joint pledge. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 895
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 895
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and Supreme Peak martial artist, leading it in place of the bedridden Cang Gong and organizing a secret restoration effort for Prince Shangshan.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin, leads the restoration effort for Prince Shangshan, and recruited Jin Taekyung and Jeok Cheongang as discreet allies; he hired assassins for their loyalty when fairly paid.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 895
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 895
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃896화



마삼보가 품에서 꺼내 든 연판장은 지난 세월을 알려 주듯, 이미 상당히 낡아 있었다.

노르스름하게 변색 된 종이와 군데군데 번진 얼룩.

그러나 저마다의 필체로 직접 빼곡하게 적어 넣은 이름과 직위는 여전히 선명하게 남아 있었고, 그 중심에는 가장 크고 힘 있는 필체로 적힌 한 사람의 이름이 있었다.

동창장인태감(東廠掌印太監) 위충(魏忠).

“창공(廠公)이시네.”

내 시선이 향하는 곳을 알아차린 마삼보가 불쑥 입을 열었다.

“가장 처음으로 연판장을 만들고 서명하셨지. 설령 당신께서 귀천(歸天)하신다 해도 반드시 반정을 성공시켜야 한다며 신신당부하셨어.”

“죽음을 염두에 둘 만큼 심각했던 모양이군요.”

“당장 돌아가셔도 이상하지 않을 정도의 내상이었지. 천만다행으로 목숨을 건지시긴 했지만…….”

마삼보가 안타까운 얼굴로 한숨을 내쉬었다.

“좋지 않아. 지금까지도 완전히 회복하지 못하셨을 정도니. 물론 그만한 부상을 입지 않았다면 지금까지 살아 계시지도 못했겠지만 말일세.”

“그 말씀은?”

“황제가 무슨 이유로 창공 어른을 살려 두었겠나. 그분은 선황을 모셨던 노신(老臣) 중에서도 가장 으뜸이셨어. 직접 목을 치기에는 그 후폭풍을 감당하기 어려웠지.”

그렇지 않아도 나 역시 의문이 들었던 부분이다.

그 철두철미한 황제가 자신의 앞길을 가로막은 창공을, 그것도 가장 위협적인 동창의 수장을 살려두다니.

“아직 제가 모르는 뭔가가 또 있습니까?”

내 물음에 마삼보가 조용히 고개를 끄덕였다.

“있었지, 대국의 명운을 건 거래가.”

“이를테면?”

“아직 걸음마도 떼지 못했던 한 아이의 목숨. 그리고 그와 맞바꿀 수많은 충신들의 목숨.”

“……!”

“그래, 지금 자네가 생각하는 그대로일세. 상산왕 전하를 살리기 위해 일백에 달하는 중신(重臣)들이 희생되었지. 그들 자신은 물론 가문 전체가.”

주위의 공기가 가라앉는다. 마삼보의 눈동자에 깃든 불꽃이 일렁이고 있었다.

“선황은 물론 황태자 전하와 다른 황자들까지 중병에 걸린 이상, 그렇게라도 우리의 마지막 희망인 상산왕 전하를 지켜야 했네. 그것만이 유일한 방법이었어.”

“그럼 그 거래의 대가로 황제가 얻었던 건 뭡니까?”

“명분과 시간. 상산왕 전하의 처우를 약속받은 선황께서는 정식으로 황위를 선양(禪讓)하셨고, 창공 어른은 새로운 황제에 맞서 싸우려 했던 반발 세력을 진정시켰지.”

천하의 중심은 황도지만, 황도가 곧 천하는 아니다.

대국의 광활한 국토는 수많은 신하와 군대가 있었기에 존재하는 것.

비록 선황으로부터 정식으로 황위를 선양 받으며 최소한의 명분은 얻었지만, 천하 각지에서 들끓는 반란의 기운을 가라앉힐 최소한의 시간이 필요했을 것이다.

선황을 따르던 중신 중에서도 가장 명망과 권위 높은 노신이었던 창공과 상산왕의 안위가 바로 그 억제기였을 테고.

“우리로서는 극심한 타격을 입었지만, 그래도 그 거래를 통해 최소한의 목적은 달성할 수 있었네. 몸을 추스를 시간이 필요했던 건 비단 황제뿐만이 아니었으니까.”

아마도 황제는 머지않아 창공이 죽음을 맞이하리라 예상했을 것이다.

그러나 창공은 극심한 내상을 입고도 기적처럼 살아남았고, 그가 이끌던 동창도 지금껏 유지될 수 있었다.

창공을 중심으로 반란을 꿈꾸는 반정군(反正軍) 역시도.

“두 개의 파로 갈라져 대치 중이었던 거군요. 이미 십여 년 전부터.”

“맞네. 오래전부터 이 격돌은 기정사실이었어. 서로를 향해 칼날을 겨누고 있으면서도 누구 하나 쉽게 나서지 못했지. 적어도 표면적으로는 말일세.”

나는 마삼보가 덧붙인 뒷말에 미간을 좁혔다.

“표면적, 이라고 하셨습니까?”

“지금껏 암살 시도가 수 차례 있었네. 황제는 창공 어른을, 우리는 황제를 노렸지.”

결과는 안 물어봐도 뻔하다.

황제와 창공. 둘 다 멀쩡히 살아 있으니까.

하지만 삼엄한 경계가 유지되는 건청궁에 머무르는 황제와 달리, 창공이 암살 시도를 버텨 냈다는 것은 상당히 의외였다.

“건청궁에 가서 직접 확인한 바로는, 황제 측에 엄청난 살수가 하나 있던데요. 어떻게 막았습니까?”

“물론 황제의 휘하에는 여러 초절정 고수들이 있지. 하지만 아군의 전력 역시 그에 비해 떨어지지 않아. 혹시 황도십이궁(黃道十二宮)이라고 들어봤나?”

“몇 번 들어 보긴 했는데, 그건 별자리 명칭 아닙니까?”

“일반적으로는 그렇지. 하지만 황도를 수호하는 초절정 고수 열두 명을 뜻하는 칭호이기도 하네.”

뭐?

나는 놀라움을 감추지 못하고 눈을 크게 떴다.

무림에서도 보기 힘든 초절정 고수가, 그것도 무려 열두 명이나 이곳 황도에 있다니.

대국의 전력 중 상당 부분이 집약된 황도라고는 해도 충분히 놀라운 일이었고, 뒤이어 들려온 마삼보의 한 마디는 더욱 뜻밖이었다.

“그리고 바로 그 황도십이궁에 속한 열두 명의 초절정 고수 중 절반이 아군이지. 그중 일부가 창공 어른 곁에 머무르고 있네.”

“……!”

“그뿐만이 아닐세.”

마삼보는 연판장에 적힌 직위와 이름을 하나씩 짚으며 말을 이어갔다.

그중에는 천하 유생들의 압도적인 지지를 받는 노학자도 있었고, 가장 높은 관직 중 하나인 삼공(三公)과 같은 조정의 거두도 있었으나 정작 중요한 인물들은 따로 있었다.

바로 군부(軍部)에 속한 무장들이 바로 그 주인공이었다.

황도, 혹은 황도 밖의 경계선을 지키는 지휘관들.

심지어 그중에는 수만에 달하는 병력을 거느린 도독(都督)도 포함되어 있었다.

“이제 알겠나, 이 대치가 그토록 오랫동안 유지되었던 이유를?”

나는 무겁게 고개를 끄덕였다.

이 연판장에 적힌 이름들은 대국의 반쪽이라 칭해도 부족함이 없다. 이런 형국에서 어느 한쪽이 먼저 칼을 휘두른다면, 그야말로 시산혈해가 펼쳐질 것이다.

“먼저 칼을 빼든 것은 황제일세. 우리는 이 균형을 깨트릴 생각이 없었어. 적어도 상산왕 전하께서 더 장성하시길 기다리고 싶었지.”

현대와 비교했을 때, 이 시대의 어린아이들은 통상적으로 훨씬 조숙한 편이다.

그러나 이 거대한 제국을 감당하기에는, 상산왕의 연치(年齒)가 부족하다는 것이 냉정한 현실이었다.

“그토록 영민하시던 황태자 전하께서도, 황실의 일원으로서 부족함이 없던 두 황자님과 다른 황족들도 모두 시름시름 앓다 세상을 떴네. 자네가 알고 있는 누군가처럼.”

“……사천성주.”

“그래. 그 또한 황제를 알현한 직후 그렇게 되었다고 했지. 과연 이것이 우연이겠나?”

마삼보가 무겁게, 동시에 확신에 찬 목소리로 말을 이었다.

“황제는 암천(暗天)이라 불리는 그 불온한 무리와 손을 잡은 것이 틀림없네. 갑작스럽게 선황을 배반한 백연, 그리고 소교라는 그 여인 또한 암천과 밀접한 연관이 있겠지.”

“……!”

“자네나, 나나. 여기까지 온 이상 돌이킬 수 없어. 이제 이 길고도 끔찍한 혼란을 끝내야 할 때가 온 거야. 곧 열리는 대연회는…….”

마삼보의 눈동자가 형형하게 빛났다.

“비로소 옳게 된, 새로운 천자의 성대한 즉위식이 될 걸세.”

나도 모르게 지그시 눈을 감았다.

어둡다.

이미 한바탕 쏟아붓고 잦아든 빗소리는 더 이상 들리지 않는다.

숨 막히는 고요함.

그 침묵 속에서 스스로를 관조했다. 내면의 생각과 의문을 다시 한번 깊게 들여다보았다.

무엇이 옳은가. 무엇이 그른가.

이 선택의 끝에는 무엇이 기다리고 있을까.

이미 주사위는 던져졌다.

마삼보에게 연판장을 요청한 순간부터 나는 이미 결정을 내렸고, 지금의 이 선택은 목적지로 향하기 위한 마지막 갈림길일 뿐이다.

스륵.

감고 있던 눈을 뜨자, 굳어있는 마삼보의 얼굴이 보인다.

한동안 말없이 그를 응시하던 나는 손을 입으로 가져갔다.

으득. 툭.

아릿한 통증과 함께 점점이 떨어지는 핏방울. 나는 옅은 핏물에 젖은 새끼손가락으로 연판장의 빈자리를 채워 넣었다.

진태경.

이름 석 자.

오직 그것만이 전부였다.

연판장을 빼곡하게 메운 다른 이들과는 달리 그 어떤 별호도, 가문도, 소속도 적어 넣지 않았다.

그리고 마삼보는 그런 내 행동이 의미하는 바를 즉각 깨달았다.

“오롯이 혼자 짊어지겠다는 뜻이로군. 반정이 실패했을 때를 대비해서.”

“제가 비겁한 겁니까?”

“아니, 나로서는 비난할 수 없지. 과거 대국에 맞선 죄로 멸문(滅門)당한 모산파와 같은 전철을 밟기는 싫을 테니까. 더군다나…….”

새롭게 내 이름이 적힌 연판장을 품에 넣은 마삼보가 말을 이었다.

“자네와 자네 스승이 아군에 합류한다면, 반정은 결코 실패하지 않을 걸세.”

확신에 찬 표정과 말투.

그런 마삼보를 물끄러미 바라보던 나는 불쑥 입을 열었다.

“그 정도로는 부족합니다.”

“뭐?”

“실패하지 않는다, 가 아니라 반드시 성공해야 한다, 가 맞지 않겠습니까?”

“그게 무슨.”

마삼보가 뭐라 말을 잇기도 전에, 나는 전각 내부의 구석에 세워진 책장으로 다가가 서책 한 권을 뽑아 들었다.

그리고 망설임 없이 한쪽 면을 찢어낸 다음, 아직 피가 마르지 않은 손가락으로 짧은 글귀를 휘갈겨 쓴 뒤 마삼보에게 건넸다.

“이건…….”

적혀 있는 내용을 확인한 마삼보가 미간을 좁혔다.

“대관절 무슨 말인지 모르겠군. 아니, 제대로 읽을 수조차 없어.”

“그럴 겁니다. 밀마(密嗎)니까요.”

“밀마?”

“네. 극소수만 알아볼 수 있는 암호문입니다.”

“그럼 이걸 왜…… 잠깐, 자네 설마?”

“맞습니다.”

눈을 크게 뜬 마삼보를 향해 고개를 끄덕여 준 나는, 천천히 말을 이었다.

“지금부터 제가 알려 드리는 장소로 수하를 보내어 그 서신을 전해주시면 됩니다. 그럼 대연회가 열리는 날에 맞춰 무림맹의 지원군이 도착할 겁니다. 어쩌면 살성(殺星)이나 십왕(十王)이 포함된 강력한 지원군이.”

“……!”

“지난번에 그런 말씀을 하셨었죠. 성공하면 왕이요, 실패하면 역적이라.”

나는 충격과 놀라움으로 물든 마삼보의 얼굴을 똑바로 마주하며 뇌까렸다.

“그렇다면 이 반정을, 반드시 성공시켜야 하지 않겠습니까.”

그래.

이미 주사위는 던져졌다.



* * *



유례를 찾아보기 힘든 폭우였다.

간밤에 쏟아진 빗줄기로 황도의 일부가 수해(水害)을 입었고, 무려 수백여 채에 달하는 가옥이 물에 잠기며 적지 않은 사람들이 죽거나 다쳤다.

그리고 그 과정에서 흉흉한 소문이 퍼지기 시작했다.

황도 외곽의 우물에서 장정 여럿을 합친 것보다 커다란 독사가 발견되었다더라.

이는 천륜을 거스른 작금의 천자를 향한 하늘의 경고이자, 더 큰 재앙이 시작되리라는 예지라더라.

그나마 빗줄기가 일찍 그친 것은, 선황의 뜻을 이어받은 상산왕 전하의 덕이 있었기 때문이라더라.

미신을 곁들인 온갖 안 좋은 소문들은 들불처럼 번졌고, 불과 이틀이 지났을 무렵에는 드높은 성벽을 넘어 황실에까지 닿았다.

그중에서도 가장 깊고도 은밀한, 건청궁에까지.

그리고 그 소문을 들은 황제는 성마른 웃음을 지었다.

“아무래도 때가 된 모양이군.”

그것은 폭풍의 전조였다.

비바람과 시산혈해를 동반할, 대연회의 시작이기도 했다.
```

## Final English reading copy

```markdown
# Chapter 896

The pledge Ma Sanbao pulled from his robe was already quite worn, as if it had been keeping track of all the years that had passed.

The paper had yellowed, and stains had spread in places.

But the names and titles, written densely in each person’s own hand, remained clear. At the center was one person’s name, written in the largest, boldest script of all.

Wei Zhong, Seal-Holding Eunuch of the East Depot.

“Lord Cang Gong.”

Ma Sanbao noticed where I was looking and spoke without warning.

“He was the first to draw up and sign the pledge. He made me promise over and over that even if he passed away, we had to see the coup through.”

“His condition must have been serious enough for him to consider his own death.”

“His Internal Injury was bad enough that it wouldn’t have been surprising if he’d died right then and there. Thankfully, he survived…”

Ma Sanbao sighed, his face full of regret.

“But it’s not good. He still hasn’t recovered completely. Of course, if he hadn’t been injured that badly, he wouldn’t still be alive.”

“What do you mean?”

“Why do you think the Emperor let Lord Cang Gong live? He was the foremost among the late Emperor’s old retainers. The fallout from executing him outright would have been too much to bear.”

It was something I’d wondered about, too.

That meticulous Emperor had spared Lord Cang Gong, the man who stood in his way—and the head of the East Depot, the most threatening force of all.

“Is there something else I don’t know?”

At my question, Ma Sanbao quietly nodded.

“There was. A bargain that put the fate of the Great Nation on the line.”

“What kind of bargain?”

“The life of a child who hadn’t even learned to walk yet. And the lives of countless loyal officials in exchange.”

“……!”

“Yes. Just as you’re thinking. Nearly a hundred high-ranking officials were sacrificed to save His Highness Prince Shangshan. Not just them—their entire families.”

The air around us grew heavy. Flames flickered in Ma Sanbao’s eyes.

“With the late Emperor, His Highness the Crown Prince, and the other princes all seriously ill, we had to protect His Highness Prince Shangshan, our last hope, even at that cost. It was the only way.”

“Then what did the Emperor get in return?”

“Legitimacy and time. The late Emperor, after securing a promise about His Highness Prince Shangshan’s future, formally abdicated the throne. Lord Cang Gong calmed the opposition forces that had wanted to fight the new Emperor.”

The capital might be the heart of the realm, but the capital was not the realm itself.

The Great Nation’s vast territory depended on its many officials and armies.

The new Emperor had gained at least some legitimacy by receiving the throne through a formal abdication from the late Emperor. But he would have needed time to quell the rebellions simmering across the land.

Lord Cang Gong, the most respected and authoritative of the late Emperor’s old retainers, and Prince Shangshan’s safety must have been the restraints that kept them in check.

“We suffered a devastating blow, but the bargain still let us achieve at least our bare minimum. The Emperor wasn’t the only one who needed time to recover.”

The Emperor had probably expected Lord Cang Gong to die before long.

But despite his terrible Internal Injury, Lord Cang Gong had miraculously survived, and the East Depot he led had endured to this day.

So had the restoration army, which dreamed of rebellion under Lord Cang Gong’s leadership.

“So the two sides split apart and faced off against each other. And they’ve been doing that for more than a decade.”

“That’s right. This clash was inevitable from a long time ago. We kept our blades pointed at each other, but neither side could bring itself to act. At least, not openly.”

I frowned at the words Ma Sanbao added.

“Not openly?”

“There have been several assassination attempts. The Emperor went after Lord Cang Gong, and we went after the Emperor.”

The outcome was obvious without asking.

The Emperor and Lord Cang Gong were both still alive.

But unlike the Emperor, who lived in Qianqing Palace under strict guard, Lord Cang Gong had survived attempts on his life. That was quite a surprise.

“When I went to Qianqing Palace, I saw that the Emperor had one hell of an assassin working for him. How did you stop them?”

“Of course, the Emperor has several Supreme Peak masters under his command. But our side is no weaker. Have you ever heard of the Twelve Palaces of the Zodiac?”

“I’ve heard the name a few times, but aren’t those constellations?”

“Usually, yes. But it’s also the title given to the twelve Supreme Peak masters who protect the capital.”

What?

I couldn’t hide my surprise. My eyes widened.

There were twelve Supreme Peak masters in the capital—people rare even in Murim.

Even knowing that much of the Great Nation’s strength was concentrated in the capital, it was astonishing. And what Ma Sanbao said next was even more unexpected.

“Half of those twelve Supreme Peak masters belong to our side. Some of them are staying with Lord Cang Gong.”

“……!”

“And that’s not all.”

Ma Sanbao continued, pointing to the titles and names written on the pledge one by one.

Among them were old scholars who enjoyed the overwhelming support of the realm’s Confucian scholars, and senior court officials of the highest rank, such as the Three Dukes. But the most important figures were others.

The military officers—that was who mattered most.

Commanders guarding either the capital or the borders beyond it.

One of them was even a governor-general with tens of thousands of troops under his command.

“Do you understand now why this standoff has lasted so long?”

I nodded heavily.

The names on this pledge were enough to make up half the Great Nation. If either side struck first under these circumstances, the land would become a sea of corpses and blood.

“The Emperor was the one who drew his sword first. We had no intention of breaking this balance. At least, we wanted to wait until His Highness Prince Shangshan had grown older.”

Compared with children in the modern world, children of this era generally matured much faster.

But the cold reality was that Prince Shangshan was still too young to take on the burden of this vast empire.

“Even His Highness the Crown Prince, who was so intelligent, and the two princes, who were every bit as fit to be members of the imperial family, along with other members of the imperial family, all wasted away and died. Just like someone you know.”

“……The City Lord of Sichuan Province.”

“That’s right. He supposedly fell ill like that right after meeting the Emperor. Do you really think that was a coincidence?”

Ma Sanbao continued in a voice that was both grave and certain.

“The Emperor must have joined hands with that treacherous group called Dark Heaven. Baek Yeon, who suddenly betrayed the late Emperor, and that woman So Gyo must also be closely connected to Dark Heaven.”

“……!”

“You and I have come too far to turn back now. It’s time to put an end to this long and terrible turmoil. The grand banquet that’s coming…”

Ma Sanbao’s eyes shone brightly.

“Will be the grand enthronement ceremony of a new Son of Heaven—the rightful one.”

Without realizing it, I closed my eyes.

Dark.

The rain that had poured down in a single furious burst had stopped. I could no longer hear it.

A suffocating silence.

In that quiet, I looked inward. I examined my thoughts and questions once more, searching them deeply.

What was right? What was wrong?

What waited at the end of this choice?

The die had already been cast.

From the moment I’d asked Ma Sanbao for the pledge, I’d already made my decision. This choice was only the last fork in the road before I reached my destination.

Rustle.

I opened my eyes. Ma Sanbao’s face was tense.

After staring at him in silence for a while, I brought my hand to my mouth.

Crack. Tap.

A dull pain, and drops of blood began to fall. With my pinky finger wet with blood, I filled in the pledge’s empty space.

Jin Taekyung.

Just those three syllables.

That was all.

Unlike everyone else whose names and details filled the pledge, I wrote no sobriquet, family, or affiliation.

Ma Sanbao immediately understood what my action meant.

“You intend to bear it all alone. In case the coup fails.”

“Does that make me a coward?”

“No. I can’t blame you. You don’t want to suffer the same fate as the Maoshan Sect, annihilated for opposing the Great Nation in the past. Besides…”

Ma Sanbao tucked the pledge, now bearing my name, into his robe and continued.

“If you and your Master join our side, the coup won’t fail.”

His expression and tone were full of conviction.

I looked at him for a moment, then spoke without warning.

“That’s not enough.”

“What?”

“It shouldn’t be ‘it won’t fail.’ It should be ‘it has to succeed,’ shouldn’t it?”

“What are you—”

Before Ma Sanbao could finish, I walked over to the bookcase in the corner of the pavilion and pulled out a book.

Without hesitating, I tore off one of its pages. Then, with a finger that was still bleeding, I scrawled a short message and handed it to Ma Sanbao.

“What is this…?”

Ma Sanbao frowned as he read what I’d written.

“I have no idea what this means. I can’t even read it properly.”

“That’s to be expected. It’s a secret code.”

“A secret code?”

“Yes. A cipher only a tiny handful of people can decipher.”

“Then why are you—wait. You can’t mean…”

“I do.”

I nodded at Ma Sanbao, whose eyes had widened, and continued slowly.

“Send one of your men to the place I’m about to give you, and have them deliver that message. Then, on the day of the grand banquet, reinforcements from the Murim Alliance will arrive. It may even be a powerful force that includes the Slaughter Saint or one of the Ten Kings.”

“……!”

“You said it yourself last time. If we succeed, we’re kings. If we fail, we’re traitors.”

I met Ma Sanbao’s face, colored with shock and amazement, and muttered,

“In that case, shouldn’t we make sure this coup succeeds?”

Right.

The die had already been cast.

* * *

It was a downpour the likes of which had rarely been seen.

The rain that fell overnight flooded parts of the capital. Hundreds of homes were submerged, and many people were killed or injured.

As it happened, ominous rumors began to spread.

They said they’d found a venomous serpent in a well on the outskirts of the capital—one bigger than several grown men put together.

They said it was Heaven’s warning to the current Son of Heaven, who had defied the natural order—and a prophecy that an even greater disaster was about to begin.

They said the rain had stopped so soon thanks to His Highness Prince Shangshan, who had inherited the late Emperor’s will.

All sorts of ill omens, mixed with superstition, spread like wildfire. By the time just two days had passed, they’d crossed the towering city walls and reached the imperial palace.

Even the deepest, most secret part of it: Qianqing Palace.

When the Emperor heard the rumors, he gave an impatient laugh.

“Looks like the time has come.”

It was the first sign of a storm.

And the beginning of the grand banquet—with its wind, rain, and sea of corpses and blood.
```
