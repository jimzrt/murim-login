<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0913.txt",
      "sha256": "9c0c779eae7fdfe1e9600ebb1cc894824ee91290eb556001ea041b12d6ac4232",
      "bytes": 13307
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b5216012b1a558e4fa7545037b7dfc0f91b8cd10e3bdd25005dd1366857d8ad3",
      "bytes": 1250
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "66855c040f4342a0b241cbbead8026d866de6b64af95427c21f76fe8c96ddd55",
      "bytes": 231435
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "2338ef23164b503bcae9e02cd40e43ef3c087bccb705ad852dfd96596a623867",
      "bytes": 759
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a63e0f7afe9ebe95c478943febc3b5100cda97ce2974c2bb6a453282291892d5",
      "bytes": 1270
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "baa831784bcdc3d11b7693d06ecb27cae9ec772ae785377f612b8723d2f25097",
      "bytes": 628
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "05220aed61e0fd60230272505ce7ef6df3ef9716ba9b3459efd95d37ce5cd5b2",
      "bytes": 1390
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d868c22b7500d4c0c3cf619f54ad5342134343c73f2c03204688604faefccacd",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "a4b78d9d77d7bba2509cf010fb91fd69e47e2e460902b01c894ed94e0216e6f2",
      "bytes": 699
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "adee20bfa817416ef772cb2c4a5cec6004ee70b1248d4e82534af2140015de70",
      "bytes": 850
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "5461e5aed5a856f37e8a089d06824c091637558a479a8b65c4f840ec4b9d89b8",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3a94cb321253dba01ba17df72780ce292559aa12d2e1c6a31ae7a47a31bc09bc",
      "bytes": 263566
    }
  ],
  "estimated_tokens": 11509
}
-->

# Durable State Update — Chapter 913

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
1 and safe_through 913. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 913. Profile updates may replace only one
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
  "chapter": 913,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 913,
    "continuity_sources": [913],
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
    "Jeok Cheongang vowed to kill every member of Dark Heaven after Hong Dao was killed by the Blood Lord.",
    "Jeok Cheongang suffers unexplained cold pain immediately after the duel.",
    "The Eastern Heaven Demon Lord survived a seemingly fatal death and can no longer be described as human.",
    "The Eastern Heaven Demon Lord was once part of the Maoshan Sect; its members died resisting the forced relocation of the capital.",
    "Ma Sanbao is alive and is the Eastern Heaven Demon Lord’s disciple.",
    "Jeok Cheongang is gravely injured after the Demon Lord’s surprise attack but continues fighting.",
    "Jeok Cheongang and Jin Taekyung each shielded the Fire Dragon Pavilion members from danger.",
    "The undead army breached the stone wall and entered the grand banquet hall."
  ],
  "continuity_sources": [
    912
  ],
  "open_questions": [
    "What caused Jeok Cheongang’s unexplained cold pain?",
    "How did the Eastern Heaven Demon Lord survive what appeared to be his death?",
    "Can Jeok Cheongang defeat the Demon Lord despite his injuries?",
    "What will happen as the undead army enters the banquet hall?"
  ],
  "safe_through": 912,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 열화문    | **Fire Gate Clan**               |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 민첩               | **Agility**                    |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 시산혈해 | **sea of corpses and blood** | Description of the preceding months of bloodshed. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 선계 | **realm of immortals** | The other world that Jin travels to and from. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 태조 | **Taizu** | The Great Nation’s founding emperor. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 정호군 | 태산 | guard officer questioning a performer | you | blunt and direct | He calls Taishan forward and asks whether he belongs to the circus troupe. |
| 마삼보 | 정호군 | East Depot de facto leader to Embroidered Uniform Guard Thousand Captain | Commander Jeong | courteous and controlled | Ma Sanbao addresses him as 정 천호 while asserting procedural limits and drawing him into a conversation. |
| 정호군 | 마삼보 | Embroidered Uniform Guard Thousand Captain to East Depot official | Eunuch Ma | formal and guarded | Jeong Hogun addresses him as 마 태감 and shows wariness despite his restrained replies. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 마삼보 | 동천마군 | disciple_to_master | Master | deferential | Ma Sanbao addresses the Eastern Heaven Demon Lord as 스승님 when rejoining him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 912
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 912
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 912
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 907
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Taekyung killed Ma Sanbao during the banquet-hall battle, while Jeong Hogun and the Embroidered Uniform Guard have declared themselves allies of the Emperor, and So Gyo’s allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 907
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 912
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 912
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan as a disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 912
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃913화



시산혈해(屍山血海).

말 그대로였다.

시선이 닿는 곳마다 시체가 가득하고 핏물이 흘러넘쳤다.

황실의 경사를 치르기 위해 만들어진 이 광활한 공간은 오늘날에 이르러 수많은 이들이 죽고 죽이는 전장이 되었고, 정호군이 이끄는 금의위는 마침내 대부분의 배신자들을 처단했음에도 승리의 기쁨을 마음껏 누리지 못했다.

아니, 되려 두려움을 느끼며 서로를 향해 등을 맞대어야 했다.

그들의 전투는 아직 끝나지 않았으니까.

그리고 이제 그들이 맞서야 하는 상대는, 상리(常理)를 아득히 벗어난 괴물들이었으니까.

그륵. 그어어어.

짙은 피비린내마저 지워 버리는 끔찍한 악취.

진태경과 등을 맞댄 채, 의미를 알아들을 수 없는 괴성을 내뱉으며 포위망을 형성하는 놈들을 바라보던 적천강이 문득 입을 열었다.

“하나만 묻자.”

“숫자 제한 없이, 사흘 내내 물어보셔도 됩니다.”

입에 고인 피를 탁 뱉어 낸 진태경이 바닥에 널브러져 있던 창칼을 주워들며 덧붙였다.

“그때까지 저 새끼들이 기다려 준다면요.”

물론 진태경 역시 알고 있었다.

애초에 그런 일은 벌어지지 않을 거라는 것쯤은.

‘다들 똑같은 생각이겠지.’

어느덧 서로를 향해 등을 맞대고 원진(圓陣)을 형성한 화룡각 대원들과 금의위들의 얼굴에서, 그리고 뒤이어 들려온 적천강의 가라앉은 목소리에서 숨길 수 없는 긴장감이 느껴졌다.

“선계(仙界)…… 그러니까, 네 녀석의 고향에도 저런 것들이 존재하느냐?”

진태경이 망설임 없이 대답했다.

“당연히 있죠. 심지어 많아요.”

“많다니, 도대체 몇이나 있는 게냐.”

“그, 노야께서는 태산이가 지금까지 살면서 처먹은 끼니 수가 얼마나 될 거라고 생각하십니까?”

“그야 엄청나게 많겠지. 헤아릴 수도 없을 만큼.”

“저도 그렇게 생각합니다. 그런데 거기에서 최소 수십, 아니 수백 배라고 생각해 보세요.”

깨달음을 얻은 적천강이 탄식했다.

“존나 많군.”

“예. 진짜 존나 많습니다. 어느 정신 나간 새끼가 취향 차이까지 고려했는지 종류도 다양해요.”

“빌어먹을. 선계가 아니라 마계였구먼.”

“아, 마계는 따로 있습니다. 제가 지난번에 말씀드렸던 것 같은데.”

“……염병할. 거긴 도대체 어떻게 되먹은 세상이냐.”

“어떻게 되먹긴요. 개 같은 세상이죠. 그런데 혹시 그거 아세요?”

“뭘?”

“여기도 제 고향 못지않게 개 같아지고 있는 것 같아요.”

진태경의 대답에 잠시 침묵하던 적천강이 이내 입을 열었다.

“그래, 노부가 생각하기에도 그런 것 같군. 아무래도 노부가 너무 오래 살았던 모양이야. 이런 거지 같은 꼴을 보다니.”

“오래 살았다니, 그런 말씀은 왜 하십니까. 재수 옴 붙게.”

“쓸데없는 걱정일랑 집어치워라. 앞으로 오십 년은 더 살아 볼 작정이니까.”

“훨씬 낫네. 예. 당연히 그러셔야죠.”

애써 밝게 대답했지만, 이미 진태경의 마음 한구석에는 커다란 바윗덩어리가 얹혀 있었다.

‘젠장.’

말없이 주위를 훑자 익숙한 동시에 낯선, 수많은 얼굴들이 시야에 들어온다.

현재 느끼고 있는 복잡한 감정의 소용돌이가 고스란히 드러나 있는 얼굴들이.

긴장. 경악. 두려움.

그리고 그 무겁고 어두운 감정들 속에서 힘겹게 쥐어 짜낸 한 줌의 용기까지.

‘과연…… 이 중에 몇 명이나 살아남을 수 있을까.’

진태경은 문득 머릿속에 떠오른 불길한 의문을 애써 지워 냈다.

적어도 지금 이 순간만큼은, 눈앞의 적을 향해 촉각을 곤두세우는 것만으로도 벅찼으니까.

“이날이 오기를, 실로 오랫동안 기다려왔다.”

전장을 포위한 망자들의 군대. 그 선두이자 중심에 우뚝 선 동천마군이 천천히 말을 이었다.

이 자리의 모두를 향해.

아니, 황제를 향해.

“오늘 이 자리에서, 대국(大國)은 사라진다.”

그 순간.

스아아아악.

알 수 없는 한기(寒氣)가 뻗어 나왔다.

동천마군의 전신에서 흘러나온 희끄무레한 기운은 마치 연기처럼 전장 곳곳으로 스며들었다.

아니, 잠식했다.

어느새 동천마군의 손에 들린, 한 자루의 요령(瑤領)으로부터 흘러나온 방울 소리에 맞춰서.

딸랑.

선명하게 울려 퍼지는 그 스산한 방울 소리는 귓가가 아닌 뇌리로 전해졌고, 소리보다는 음파(音波)에 가까운 것이었다.

무공의 경지가 부족한 대부분의 사람들은 알아들을 수 없는.

동시에 더는 살아 있지 않는 이들을 죽음으로부터 일으켜 세우는 음파.

그리고 진태경이 그 사실을 깨달았을 때는, 이미 한발 늦은 후였다.

턱.

“노야!”

“그만두어라.”

동천마군을 향해 쏘아지려던 진태경의 어깨를 붙잡은 적천강이 침잠한 목소리로 말을 이었다.

“이미 늦었으니.”

“……!”

다음 순간. 진태경의 눈이 크게 뜨였다.

이미 늦었다는 적천강의 한 마디가 무엇을 뜻하는지, 곧이어 시작된 변화를 통해 느꼈기 때문이었다.

드득. 드드득.

지면이 흔들린다. 점점 커지는 진동에 맞춰 핏물이 출렁이고 공기가 차갑게 가라앉았다.

‘아니, 그게 아니야.’

진태경은 터져 나오려는 탄식을 삼켰다. 파르르 떨리는 그의 눈동자는, 자신의 발아래에서 조금씩 들썩이는 이름 모를 누군가의 시신에 못 박혀 있었다.

‘지금 흔들리고 있는 건…… 지면이 아니라 시체들이다.’

전장을 가득 메운 무수한 시체들. 수천에 달하는 그것들이 깨어나고 있었다.

돌아와서는 안 될 이승으로. 인간이 아닌 다른 무언가로.

“흐읍……!”

“이, 이게 무슨.”

“놈들이, 저 괴물들이 일어나기 전에 쳐라! 어서!”

퍽! 서걱!

차가워지는 공기와 함께 점점 더 농도를 더해 가는 공포.

그리고 미친 듯이 내리찍는 창칼에도 쉽게 쓰러지지 않는 시체들.

그 어지러운 혼돈 속에서 적천강은, 이미 아득한 과거에 무림에서 지워진 모산파의 전설들을 떠올리며 자신의 제자를 바라보았다.

“이런 것들을, 네가 사는 그곳에서는 무엇이라 부르느냐.”

콰직!

발아래의 시체를 짓밟은 진태경이 이를 악물며 대답했다.

“언데드(Undead).”

그. 아. 아.

목젖이 쩍 갈라진 시체가 피 웅덩이 속에서 고개를 든다. 이미 진태경에게 짓밟혀 척추뼈가 으스러졌음에도, 그것은 여전히 일어나려 애쓰고 있었다.

“죽지 않은, 그러나 살아 있는 것도 아닌 괴물들을 뜻하는 말입니다.”

적천강은 고개를 끄덕였다.

비록 발음은 생소하나, 의미하는 바는 비슷하다.

천하에 산재한 수많은 문파와 무가(武家)들 중, 유일하게 모산파만이 간직한 전설과도 같은 이야기 속에서 등장하는 괴물들을 표현하는 말로는 더할 나위 없을 만큼.

‘죽지 않은, 그러나 살아있지도 않은 괴물들이라.’

처음 그에 관한 이야기를 들었을 때, 적천강 역시 호사가들이 지어낸 허무맹랑한 헛소리라고 생각했다.

도무지 있을 수 없는 일이니까.

하늘이 정한 순리를 정면으로 거스르는, 그야말로 기괴하기 짝이 없는 전설이었으니까.

그러나 이제는 아니었다.

그 믿을 수 없던 전설이, 이제는 눈앞에 있다.

“……강시(僵尸).”

신음하듯 뇌까린 적천강은 꿈틀거리며 일어나는 시체를 향해 손을 뻗었다.

화륵. 퍼어엉!

결코 가볍지 않은 내상을 입었음에도 조금도 사그라지지 않은 광염이 터져 나온다. 돌아와서는 안 될 강을 건넌 그것의 살갗을 파고들어 뼈와 내장을 불태웠다.

푸스슥. 철벅.

잿더미가 되어 피 웅덩이에 녹아드는 시체를 짓밟은 적천강이, 자신의 제자를 향해 고개를 돌렸다.

“천하의 그 무엇이, 열화문의 화염 앞에서도 성할 수 있단 말이냐.”

“……!”

“끝없이 불태워라. 죽지 않는다면 죽을 때까지 잿더미로 만들어 쓰러트려라. 본문의 선조들이 그리했던 것처럼.”

동그랗게 뜬 눈으로 적천강을 바라보던 진태경이, 짐짓 진중한 얼굴로 대답했다.

“어떻게 아셨습니까. 그거야말로 제가 가장 자신 있는 건데.”

스승과 제자는 누가 먼저랄 것도 없이 서로를 따라 웃었다.

그리고 사방에서 밀려드는 시체들을 향해 쏘아졌다.

한 줄기의 불꽃. 아니, 두 줄기의 불꽃이 되어.

딸랑. 딸랑.

끝없이 울려 퍼지는 음산한 방울 소리를 들으며.

콰아아아!



* * *



그것은 죽은 이와 산 자들 간의 격돌이었고, 계란을 향해 떨어져 내리는 바위를 보는듯한 광경이었다.

그아아아!

언데드. 강시.

혹은 또 다른 무언가일지도 모르는 시체들은 살아남은 인간들을 향해 사방에서 송곳처럼 쏘아졌다.

그들은 강시처럼 뻣뻣하거나 느리지 않았고, 언데드처럼 나약하지도 않았다.

바로 그렇기에, 강했다.

콰드드득!

“막아라!”

“황제 폐하를 위하……!”

카카캉! 서걱!

충성스러운 외침이 흔적도 없이 파묻힌다.

마치 방패처럼 원진을 그린 사람들을 덮친 수천의 시체들은 생전의 모습처럼 민첩하게 움직였고, 방울 소리에 사로잡힌 그들의 영혼은 더는 부상이나 죽음을 두려워하지 않았다.

콰직!

“끄아아악!”

선홍빛 핏물이 분수처럼 솟구친다. 폐부를 쥐어 짜낸 듯한 비명은 오로지 산 자들의 것이었다.

검기에 의해 팔이 잘리고, 다리가 베이고, 가슴이 관통당해도 끝없이 일어서서 나아가는 망자들은 조금씩 인간들의 진영을 허물어트리고 있었다.

점점 더 빠르고 가파르게 울려 퍼지는 방울 소리를 따라. 그것의 주인이 명하는 바를 위해서.

딸랑, 딸랑.

동천마군은 천천히 걸음을 옮겼다. 마삼보를 비롯한 수백의 망자들이 그를 따라 움직였고, 그들이 향하는 방향 끝에는 높게 솟은 연단이 있었다.

아니, 황제가 있었다.

“길고 치열했던 군웅할거(群雄割據)의 시대가 저물어 갈 때, 내 나이는 고작 열셋이었지.”

노래하듯 흥얼거리는 목소리로, 동천마군은 뇌까렸다.

느슨하게 움직인 회색빛 눈동자에, 황제의 곁에서 몸을 떨고 있는 어린 왕의 모습이 비쳤다.

고작 십 대 초반.

한 사람의 노인이자 인간을 벗어난 괴물이 되어 버린 그에게도, 한때 소년이라 불리던 시절이 있었다.

“나는 태어날 때부터 죄인이었다. 난세에 태어났다는, 씻을 수 없는 죄를 지은 죄인.”

평범한 농부였던 아버지와 고작 십대였던 두 형님이 함께 전장에 끌려나갔던 날. 동천마군은 처음으로 깨달았다.

불행은 죄를 지은 이들에게만 찾아오는 것이 아니라는 것을.

재물이 없고, 힘이 없고, 맞서 싸울 창칼이 없다면 그것이 죄라는 것을.

“그러나 정작, 무고한 백성들을 창칼 앞에 세운 위정자(爲政者)들은 죄인이 아니었다. 그들은 곧 하늘이었다. 자신들이 만들어 낸 전장에서 수천, 수만의 목숨이 사라져도 쌀과 고기로 배를 불리는 이들이었지.”

난세의 마지막 불꽃은 화려했다. 스스로를 일국의 왕이요, 천자로 자처하는 이들은 낭떠러지 끝에서 가장 치열하게 싸웠다.

그리고 그 불꽃 속에서 잿더미로 화한 무수한 생명 중에는, 어린 동천마군의 아버지와 두 형의 것도 포함되어 있었다.

열세 살에 불과한 동천마군을 징집하기 위해 찾아온 병사들에게 맞섰다가, 겁간당하고 죽음을 맞이한 그의 어머니도.

바로 그날부터, 소년은 울지 않았다.

그로부터 일 년 후, 가장 날카롭고 강한 창칼로 난세를 종결지은 최후의 승자가 황위에 오른 뒤에도.

떠돌이 생활을 하던 동천마군의 자질을 알아본 어느 도사가 자신의 제자로 삼아 문파에 데려갔을 때도.

그렇게 스승을 만났다. 사형제들을 알았다.

모산파에서 찾은 것은 눈물이 아닌 웃음이었다. 행복이었다.

그리고 그 행복은, 불과 몇 년 만에 끝났다.

“알고 있었느냐?”

동천마군은 걸음을 멈췄다. 그리고 수백 개의 계단 위에서 자신을 굽어보는, 원수의 핏줄을 향해 물었다.

“네 조부가, 태조(太祖)가 우리에게 무슨 짓을 했는지.”

딸랑.
```

## Final English reading copy

```markdown
# Chapter 913

A sea of corpses and blood.

That was exactly what it was.

Everywhere the eye could reach, corpses piled up and blood pooled in overflowing streams.

This vast space had been built to celebrate the imperial family’s good fortune. Now it had become a battlefield where countless people killed and died. Even though the Embroidered Uniform Guard led by Jeong Hogun had finally put down most of the traitors, they couldn’t fully enjoy the taste of victory.

No—instead, fear gripped them, and they had to stand back-to-back.

Their battle wasn’t over yet.

And now, the enemies they had to face were monsters far beyond the bounds of common sense.

*Grrk. Grrrr.*

A foul stench so vile it drowned out even the thick smell of blood.

Jeok Cheongang stood back-to-back with Jin Taekyung, watching the creatures circle them and shriek in a language no one could understand. Then he suddenly spoke.

“Let me ask you one thing.”

“You can ask me all day and night for three days straight. No limit.”

Jin Taekyung spat out the blood pooling in his mouth, picked up a spear and sword lying on the ground, and added:

“If those bastards are willing to wait that long, of course.”

Naturally, Jin Taekyung knew it, too.

There was no chance of that happening.

*They’re all thinking the same thing.*

The faces of the Fire Dragon Pavilion members and the Embroidered Uniform Guards, now standing back-to-back in a circle, showed the same feelings swirling inside him. And then Jeok Cheongang’s subdued voice came from behind him, tense in a way he couldn’t hide.

“The realm of immortals… In other words, your homeland. Does it have things like those?”

Jin Taekyung answered without hesitation.

“Of course. There are tons of them.”

“Tons? Just how many?”

“Uh, Old Master, how many meals do you think Taishan’s eaten in his whole life?”

“An awful lot, I’d imagine. Too many to count.”

“I think so, too. Now imagine at least dozens—no, hundreds of times that many.”

Jeok Cheongang let out a sigh as understanding dawned.

“Fuck, that’s a lot.”

“Yeah. A fucking lot. Some lunatic must’ve even taken different tastes into account, because there are all kinds.”

“Damn it. So it wasn’t the realm of immortals. It was the Demon Realm.”

“Oh, that’s a separate place. I think I told you about it before.”

“……For fuck’s sake. What kind of world is that?”

“What kind? A shitty one. But do you know what?”

“What?”

“This place seems to be getting just as shitty as my homeland.”

Jeok Cheongang was silent for a moment after Jin Taekyung answered. Then he spoke.

“Yes. I think so, too. I suppose I’ve lived too long. To see a miserable sight like this.”

“Why say you’ve lived too long? Don’t jinx it.”

“Enough with the pointless worrying. I plan to live another fifty years.”

“That’s much better. Yes. You’d better.”

He forced a bright reply, but a massive boulder was already weighing down one corner of Jin Taekyung’s heart.

*Damn it.*

He silently surveyed the area. Familiar and unfamiliar faces alike filled his vision.

On every face, the whirlpool of complicated emotions they were feeling showed plainly.

Tension. Shock. Fear.

And, squeezed out with difficulty from those heavy, dark feelings, a handful of courage.

*How many of them will make it out alive?*

Jin Taekyung forced himself to erase the ominous question that had suddenly crossed his mind.

At least for now, even keeping every nerve trained on the enemy before him was more than enough.

“I have truly waited a long time for this day.”

The Eastern Heaven Demon Lord stood tall at the head and center of the army of the dead encircling the battlefield. He spoke slowly.

To everyone gathered there.

No—to the Emperor.

“Today, in this very place, the Great Nation will disappear.”

At that moment—

*Shhhhh.*

An inexplicable chill spread out.

A pale aura flowing from the Eastern Heaven Demon Lord’s entire body seeped like smoke into every corner of the battlefield.

No—it swallowed it up.

All in time with the sound of a bell, held in the Eastern Heaven Demon Lord’s hand.

*Jingle.*

The eerie chime rang out clearly. It reached not the ears, but the mind, and it was closer to a sound wave than a sound.

Most people whose martial arts realm was insufficient couldn’t hear it.

At the same time, the sound wave raised those who were no longer alive from the dead.

And by the time Jin Taekyung realized what was happening, he was already a step too late.

*Thump.*

“Old Master!”

“Stop.”

Jeok Cheongang grabbed Jin Taekyung by the shoulder as he was about to shoot toward the Eastern Heaven Demon Lord, and continued in a sunken voice:

“It’s already too late.”

“……!”

The next moment, Jin Taekyung’s eyes widened.

He understood what Jeok Cheongang meant by “too late” when the change began.

*Crick. Crrick.*

The ground trembled. As the vibrations grew stronger, the pools of blood rippled and the air turned cold.

*No, that’s not it.*

Jin Taekyung swallowed the gasp trying to burst out of him. His trembling eyes were fixed on the unknown corpse at his feet, shifting little by little.

*It’s not the ground that’s trembling… It’s the corpses.*

The countless corpses filling the battlefield. Thousands of them were waking up.

Returning to the world of the living, where they did not belong. Becoming something other than human.

“Hh…”

“W-what is this?”

“Attack before they—before those monsters get up! Hurry!”

*Thwack! Slice!*

The air grew colder, and with it the terror grew denser.

Yet the corpses refused to go down easily, even under the madly falling spears and swords.

Amid that chaotic turmoil, Jeok Cheongang thought of the legends of the Maoshan Sect, erased from Murim long ago, and looked at his Disciple.

“What do you call things like this, where you live?”

*Crunch!*

Jin Taekyung stomped on the corpse beneath his feet and answered through gritted teeth:

“Undead.”

*Grrr…*

A corpse with a throat split open lifted its head from a pool of blood. Even with its spine crushed beneath Jin Taekyung’s foot, it was still trying to rise.

“They’re monsters that aren’t dead, but aren’t alive, either.”

Jeok Cheongang nodded.

The pronunciation was unfamiliar, but the meaning was similar.

It was the perfect word for the monsters from the almost legendary stories that only the Maoshan Sect, among the countless sects and martial families spread across the land, had preserved.

*Monsters that aren’t dead, but aren’t alive, either.*

When he first heard stories about them, Jeok Cheongang had also thought they were baseless nonsense invented by gossipmongers.

It was simply impossible.

A grotesque legend that went directly against the natural order set by Heaven.

But now, that was no longer the case.

The unbelievable legend was right before his eyes.

“……Jiangshi.”

Jeok Cheongang murmured the word like a groan and reached toward the corpse twitching as it rose.

*Fwoosh. Boom!*

Despite the serious Internal Injury he had suffered, the blazing light-flames burst forth without dimming in the slightest. They dug into the skin of the thing that had crossed the river it should never have returned from, burning its bones and organs.

*Psssh. Splash.*

Jeok Cheongang stamped on the corpse as it crumbled to ash and melted into the pool of blood. Then he turned his head toward his Disciple.

“What in this world could remain unharmed by the Fire Gate Clan’s flames?”

“……!”

“Keep burning them. If they won’t die, burn them to ash until they do. Just as our sect’s ancestors did.”

Jin Taekyung stared at Jeok Cheongang with wide eyes, then replied with a deliberately serious expression:

“How did you know? That’s exactly what I’m best at.”

Master and Disciple smiled at each other, neither one waiting for the other.

Then they shot toward the corpses surging in from every direction.

One streak of flame. No—two streaks of flame.

As they listened to the eerie bell toll without end.

*Jingle. Jingle.*

*KWAaaaah!*

* * *

It was a clash between the dead and the living, a sight like a boulder falling toward an egg.

*GRAAAH!*

Undead. Jiangshi.

Or perhaps something else entirely. The corpses shot at the surviving humans from every direction, like spikes.

They weren’t stiff or slow like jiangshi, nor were they weak like undead.

That was precisely why they were strong.

*Crunch!*

“Hold the line!”

“For His Majesty the Emperor—!”

*Clang! Slice!*

Their loyal cries were swallowed without a trace.

The thousands of corpses that descended on the people forming a defensive circle like a shield moved as nimbly as they had in life. Their souls, captured by the sound of the bell, no longer feared injury or death.

*Crunch!*

“Aaagh!”

Crimson blood spurted like a fountain. The screams, as if wrenched from someone’s lungs, belonged only to the living.

Even when Sword Energy severed their arms, cut through their legs, or pierced their chests, the dead kept rising and advancing. Little by little, they were tearing down the humans’ formation.

Following the bell as it rang faster and more sharply. Carrying out the orders of its master.

*Jingle, jingle.*

The Eastern Heaven Demon Lord moved forward at a slow walk. Hundreds of dead, including Ma Sanbao, followed him. At the end of their path stood a high dais.

No—the Emperor.

“When the long and fierce age of warring heroes was drawing to a close, I was only thirteen.”

The Eastern Heaven Demon Lord muttered in a voice that hummed like a song.

His gray gaze drifted to the young king trembling beside the Emperor.

Barely in his early teens.

Even he, an old man and a monster who had ceased to be human, had once been called a boy.

“I was a sinner from the moment I was born. A sinner guilty of being born in an age of chaos—a sin that could never be washed away.”

The day his father, an ordinary farmer, and his two older brothers, both barely in their teens, were dragged onto the battlefield, the Eastern Heaven Demon Lord understood for the first time.

Misfortune didn’t come only to those who had sinned.

That having no wealth, no strength, and no spear or sword with which to fight back was itself a crime.

“And yet the rulers who put innocent commoners in front of spears and swords were not sinners. They were Heaven itself. Even as thousands and tens of thousands died on the battlefields they had created, they filled their bellies with rice and meat.”

The final blaze of that age of chaos had been magnificent. Those who proclaimed themselves kings of their own nations and Sons of Heaven fought most fiercely at the edge of the precipice.

And among the countless lives reduced to ash in that blaze were the father and two older brothers of the young Eastern Heaven Demon Lord.

His mother, too, who had been raped and killed after resisting the soldiers who came to conscript the boy, barely thirteen.

From that very day, the boy stopped crying.

Even a year later, after the final victor—who had ended the age of chaos with the sharpest and strongest spears and swords—ascended the throne.

Even when a Daoist recognized the wandering boy’s aptitude, took him as a Disciple, and brought him to the sect.

That was how he met his Master. He came to know his Senior and Junior Brothers.

What he found in the Maoshan Sect was not tears, but laughter. Happiness.

And that happiness ended in just a few years.

“Did you know?”

The Eastern Heaven Demon Lord stopped walking. Then he asked his enemy’s descendant, who was looking down at him from hundreds of steps above:

“What your grandfather, Taizu, did to us?”

*Jingle.*
```
