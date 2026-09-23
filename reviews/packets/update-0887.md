<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0887.txt",
      "sha256": "b5d6f9ee58fa83d729612de1ba72f14eb48dd9b85aaeeb05b362b71e9d045b97",
      "bytes": 15121
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "385d2f1dd17587fb02bcce46858d68676919c22792aa0d8bcb1122d7517ddbed",
      "bytes": 3213
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "33739809db89fb2099bcfbfe9dc5318ac7da6508118aecd9d144910159017ec8",
      "bytes": 927
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "69cf6f5ad1211c1df126c0f05306e5bcfa3b536f5cacd76f924bbc81f0355aa4",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0a22d62e943dfd5859260f1fb49a43e7b6ed82ce578773d7de59b2b3f1912b86",
      "bytes": 622
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "450b707622f336cab73033b3bb70ff197cdea1cca96482c5211d524ea72815a9",
      "bytes": 952
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "cf510b6552b4b32412ccb01b5197ff6171f24d002611a22a0d13a4944cb190b0",
      "bytes": 656
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "d65a74912aef5b8f427e41822c87c7848556fbe466cfb5fdcb3ad5338e8032d5",
      "bytes": 715
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "088e80331613c8f9b946718a6f0d73e29ab5de8abc94b1ab186b1b17ba57a5b8",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "261f33db68979f080468a08d9b7bc6a9dd935694e74740594050c09d22767904",
      "bytes": 259256
    }
  ],
  "estimated_tokens": 12823
}
-->

# Durable State Update — Chapter 887

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
1 and safe_through 887. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 887. Profile updates may replace only one
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
  "chapter": 887,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 887,
    "continuity_sources": [887],
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
    "The Emperor has confined Prince Shangshan in Qianqing Palace and plans a banquet attended by Shangshan and officials; Taekyung returned without Shangshan.",
    "Ma Sanbao leads a covert faction seeking to enthrone Shangshan; its members signed a pact and expect the banquet to become a confrontation.",
    "Ma Sanbao’s faction has assassins disguised as laborers inside the palace; their mission remains unclear, and Ma told Taekyung to return and wait.",
    "Ma Sanbao says the person his allies asked about is safe and expects a young martial artist to help; he believes that martial artist’s master could be decisive.",
    "Ma Sanbao spread rumors using Taekyung’s information; the Emperor ordered the arrested rumor-spreaders released.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "The late Emperor died after mental confusion while confined; Taekyung suspects Blood Soul Gu may have been involved. The City Lord of Sichuan Province showed strange symptoms before his death, and Blood Soul Gu was found in his corpse.",
    "Jeok Cheongang received and burned two letters, then said the group was formally invited to the imperial palace; their contents remain unknown.",
    "Taekyung’s group entered the Outer Palace disguised as the Blazing Flame Troupe for the imperial banquet; the Divine Physician gave them Energy-Dispersing Poison to conceal their martial skill during screening, while Jeok Cheongang can conceal his aura without it.",
    "A courtesan seeking revenge against the Emperor died by her own hand during Jeong Hogun’s screening; her companions were taken to prison.",
    "The abandoned forbidden ground in the Outer Palace is where the late Emperor and direct imperial relatives were confined after the rebellion; it is unguarded because no one approaches it.",
    "So Gyo is searching for someone, has continued receiving news from Murim, and displayed movement skill beyond First Rate; she recognized Taekyung’s claim of fifteen years’ martial training as false."
  ],
  "continuity_sources": [
    885,
    886
  ],
  "open_questions": [
    "Is Aehyang pregnant, and what does the Emperor intend for her and Shangshan?",
    "Will the banquet become a confrontation, and what does the Emperor intend?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "Who is the person Ma Sanbao’s allies asked about, and what preparations has the faction made?",
    "Who is So Gyo searching for?"
  ],
  "safe_through": 886,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake.",
    "Render 연판장 as “a pact bearing their signatures”; retain “Hongmen Banquet” for 홍문연.",
    "Treat 거산 as Taishan’s uncertain name variant, not a confirmed separate person; render 열화단 as “Blazing Flame Troupe” and 마희단 as “circus troupe.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 신법     | **movement technique**                           |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 형장      | **Brother** / **Brother [Name]**                                |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 반박귀진 | **Returning to Simplicity** | Supreme Peak technique or phenomenon used by Jeok Cheongang. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 수공 | **water arts** | Water-based martial arts; the Dongting Fisherman's specialty. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 제니 | **Jenny** | East Asian news anchor interviewing Jacob. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 844
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 886
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 886
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 884
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 886
- **Aliases:** None
- **Role:** A palace attendant loyal to the Emperor who leads the attendants assigned to Prince Shangshan; her movement skill is beyond First Rate, and she is searching for someone she must find.
- **Personality:** Loyal and vigilant, she remains controlled while firmly enforcing the Emperor’s orders.
- **Voice:** Measured and formal, using deferential official phrasing that can turn into pointed warnings.
- **Relationships:** She serves the Emperor and leads the palace attendants assigned to Prince Shangshan.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 850
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 844
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃887화



스아아아.

용암과도 같은 열기가 수많은 혈도를 뜨겁게 달구며 휘몰아친다.

나는 타오르는 눈동자로 소교를 노려보았다. 숨결과 함께 흘러나오는 목소리는 잿가루처럼 퍼석했다.

“당신…… 도대체 뭐야?”

“반응이 격하네. 적당히 하고 공력을 가라앉히는 게 좋을 거야.”

소교가, 아니…… 이제는 누구인지 모를 그녀가 대답했다.

언제나 그렇듯 담담하고 차분하게.

하지만 지금껏 스스로를 포장하던 존댓말과 예의 바른 태도를 벗어던진 채.

그리고 다음 순간 그녀의 입술 사이로 흘러나온 한마디가, 마치 격랑처럼 일어나 나를 덮쳤다.

“지금 몸 상태를 생각한다면 더더욱. 안 그래?”

“……!”

벼락에 정수리를 관통당한다면 아마 이런 기분일까.

나도 모르게 파르르 떨리는 목소리가 흘러나왔다.

“어……떻게?”

“공력의 흐름이 불안정하니까.”

소교의 대답은 짧고 간단했으며, 무엇보다 반박할 여지가 없는 정론(正論)이었다.

그러나 내가 순간 할 말을 잃어버린 이유는 따로 있었다.

저 당연한 대답을 위해서는 한 가지의 전제 조건이 필요하니까.

‘기감(氣感).’

그것도 극도로 뛰어난, 칼날처럼 예리한 감각.

모든 전투는 상대를 가늠하는 것으로 시작된다.

고수는 하수가 지닌 공력의 크기와 그 상태를 꿰뚫어 보지만, 하수는 고수의 정확한 수준을 제대로 가늠하지 못한다.

그리고 지금의 나는…… 명백한 후자(後者)다.

‘고수!’

틀림없다.

눈앞의 저 여인, 소교는 실로 엄청난 고수였다.

심지어 내 눈을 속일 정도로 완벽하게 스스로를 숨길 수 있는, 반박귀진(返璞歸眞)의 경지에 도달한 초절정 고수.

‘앞서 보였던 그 움직임이, 우연이 아니었어.’

터져 나오려는 탄식을 애써 억누른 나는 조용히 주먹을 말아 쥐었다.

그럴듯한 무기 하나 없는 적수공권(赤手空拳)에 불안정한 몸 상태까지.

제아무리 긍정적으로 생각해 보아도 한 수 위의 고수를 상대하기에는 좋지 않은 상황이었지만, 나는 자세를 비스듬히 낮춘 채 재차 공력을 끌어 올렸다.

“누구냐, 너.”

소교가 담담한 목소리로 대답했다.

“그 물음에 답해 줄 의무는 없지. 먼저 약속을 어기고 거짓말한 건 너였으니까, 열화신룡 진태경.”

“아가리 닥치고 대답이나 해. 정확히 누구의 명령을 따르고 있지? 황제? 아니면…….”

나는 소교를 노려보며 두 글자를 씹어뱉었다.

“천주(天主)?”

“글쎄.”

잠깐의 침묵.

도무지 그 의중을 짐작할 수 없는, 모호한 표정으로 나를 물끄러미 바라보던 소교가 불쑥 입을 열었다.

“내가 누구인지 알면, 그런다고 해서 뭐가 달라질까?”

“달라지겠지. 생사(生死)가 걸린 문제니까.”

“생사라…….”

“그래. 대답 여하에 따라 이 자리의 누군가는 반드시 죽는다.”

“만약 그렇게 된다면 죽을 사람은 이미 정해져 있네. 안 그래?”

그 순간.

스아아아.

공기가 파르르 떨렸다.

바람이 되어 풀과 꽃을 뒤흔드는 그 기세는 북풍(北風)과도 같았고, 서늘한 눈빛과 목소리는 설한(雪寒)이 되어 나를 휘감는다.

하지만 나는 동요하지 않았다.

단지 상대가 강적이라는 이유 하나만으로 두려움을 느끼기에는 이미 내가 헤쳐 온 수라장이 너무 많았다.

헌터로서도, 무림인으로서도.

“그래, 어느 정도는 정해져 있을지도 모르지. 하지만 꼭 둘 중 하나만 죽어야 한다는 법이라도 있나.”

“뭐?”

“넌 내가 죽인다. 반드시.”

“……!”

“내 모든 걸 걸고 약속. 아니, 장담하지.”

나 스스로도 내심 놀랄 만큼 무덤덤한 목소리.

그러나 이건 결코 위기에 몰린 약자가 보이는 허장성세(虛張聲勢) 따위가 아니었고, 내 확신은 고스란히 소교에게 전해졌다.

“너…… 진심이구나?”

“당연히.”

“동귀어진(同歸於盡)이라. 하.”

작게 헛웃음을 흘린 소교가 신기한 동물 보듯이 나를 위아래로 훑었다.

“역시 그 정보들이 사실이었네. 하긴, 뭔가 숨겨 둔 한 수라도 있으니 지금까지 살아남을 수 있었겠지.”

“혈주와 서천마군, 가장 최근에는 남천마후까지. 물론 위기마다 검성(劍星)이나 화왕(火王)의 도움이 있었다고는 해도, 그들을 상대하고도 무사하다는 건 불가능에 가까운 일이니까.”

“……!”

나는 깊게 가라앉은 눈으로 소교를 응시했다.

조금 전 물음의 대답은 굳이 듣지 않아도 될 것 같다는 생각과 함께.

‘이 여자, 서천마군과 남천마후에 대해 알고 있다.’

그것도 단지 정보로만 접한 것이 아니라 그들이 어떤 인물이었는지, 어느 수준의 강자였는지 알고 있다는 투다.

마치 예전부터 일면식이 있던 것처럼.

비로소 소교라는 이름과 신분으로 정체를 감춘 저 여자의 배후가 선명하게 그려졌다.

‘……암천(暗天).’

그래, 그것밖에는 없다.

심지어 저 입으로 직접 밝히기까지 하지 않았나.

자신이 황궁에 머무르는 가장 큰 이유 중 하나는, 그 방대한 정보력 때문이라고.

이는 소교가 황제의 충복이 아니라는 뜻인 동시에 또 다른 목적을 갖고 있음을 의미했다.

‘황궁을, 아니…… 황제를 손아귀에 쥐고 흔들 셈이었겠지.’

조각조각 흩어져 있던 퍼즐이 맞아떨어진다.

사 황자의 갑작스러운 반란. 선황을 비롯한 직계 황족들의 죽음과 지금에 이르기까지.

그러나 결과적으로는 절반의 성공에 지나지 않았다.

하루아침에 황제가 뒤바뀌고, 수많은 사람이 형장의 이슬로 사라졌어도 반대파를 완전히 뿌리 뽑아 대국 전체를 손에 넣는 것에는 실패했으니.

‘그렇다면 혹시.’

머릿속의 퍼즐이 거의 완성되려던 그때, 말없이 나를 바라보던 소교가 불쑥 입을 열었다.

“하나만 묻자. 도대체 이렇게까지 하는 이유가 뭐야?”

“이유?”

“그래. 동귀어진마저 각오하는, 그 성치 않은 몸으로 굳이 내게 맞서려는 이유.”

나는 잠시 침묵했다.

그 이유에 대해 고민할 시간이 필요해서가 아니라, 나로서는 너무나도 당연한 일이었기 때문에.

“그렇게라도 해야, 내 사람들이 덜 죽으니까.”

“뭐?”

“설령 이 자리에서 둘 다 죽는다고 해도, 너 같은 년을 살려 두는 것보다는 훨씬 나을 테니까.”

“내가 지금 널 해할 생각이 없다고 해도?”

“당연히 헛소리겠지만, 물론.”

“어째서?”

“너처럼 독사 같은 년은 오래 살수록 해악이 되거든.”

그동안 얼마나 많은 이들이 죽었나.

암천이 한 번 움직일 때마다 수백이, 수천이, 끝내는 수만이나 되는 사람들이 고혼이 되어 사라졌다.

그러니 나 한 사람으로 퉁칠 수 있다면 오히려 다행이다.

물론 내가 살아남고 소교가 죽는다면 그것이야말로 최고의 결과겠지만…….

“아무래도 상관없어. 그 빌어먹을 독니 뽑고, 가죽까지 싹 벗겨 놔야 마음이 홀가분할 것 같으니까.”

이번에 침묵을 택한 것은 소교였다.

한참이나 입을 굳게 다물고 있던 그녀는 한마디를 툭, 내던졌다.

“이거, 생각했던 것보다 훨씬 미친놈이네?”

“뭐라는 거야, 미친년이.”

“그리고 상산왕, 그 어린아이가 왜 그리 널 따르는지 조금은 알 것 같네. 응, 확실히.”

“지금…… 어린애 하나 인질로 잡았다고 협박하는 거냐?”

“글쎄, 어떨까.”

“어떻긴, 씨발. 무슨 짓을 해서든 널 죽여야 하는 이유가 하나 더 생긴 거지.”

“의욕 넘치고 좋네. 하지만 모든 일이 마음먹은 대로 흘러가는 건 아니지.”

소교가 작게 고개를 내저었다.

“그 나이에 벌써 이 정도의 경지에 다다르다니, 하늘의 장난이라고 생각될 만큼 대단한 재능이고 성취야. 그것만큼은 누구도 부정할 수 없어. 하지만…….”

그녀가 천천히 말을 이었다.

“모든 것에는 때가 있는 법이란다. 천기(天氣)를 타고 났다고 해서 죽음마저 피할 수 있는 건 아니거든.”

스륵.

옷깃을 스치는 미세한 소음.

동시에 소교의 가느다란 허리춤을 감싸고 있던 요대. 아니, 한 자루의 연검(軟劍)이 막강한 공력을 머금은 채 나를 향해 겨누어졌다.

그 낭창한 검신 너머로 보이는 서늘한 눈동자와 함께.

“하늘이 널 구해 줄지, 아니면 이대로 죽게 내버려 둘지…… 이참에 한번 시험해 볼까?”

우우우웅.

그리고 낮지만 또렷한 검명(劍鳴)이 울려 퍼진 그 순간.

화아악.

나는 똑똑히 느낄 수 있었다.

지금껏 느끼지 못했던, 실로 끔찍하리만치 거대한 기운이 소교를 중심으로 퍼져 나가는 것을.

내 전신을 빈틈없이 옥죄고 짓누르는 것을.

흐읍.

나도 모르게 들이켠 호흡.

삽시간에 무거워진 공기가 숨통을 조인다.

피부로 느껴지는 그 막강한 기세에 온몸의 솜털이 곤두서고 식은땀이 맺혔다.

하지만.

“좆, 까.”

씹어뱉듯 토해 낸 한마디와 함께, 나는 보리지 않는 공력의 사슬을 밀어냈다.

내 팔과 다리를 꽁꽁 묶어 오는 그것을 버텨 내며 소교를 향해 나아갔다.

콰드득. 푹.

한 걸음.

고작 한 걸음일 뿐일진대, 발밑의 단단한 청석(靑石)이 단숨에 박살 나고 그 아래에 층층이 쌓여 있던 지면이 움푹 꺼진다.

단순히 내 몸무게가 그만큼 무거워서? 아니면 오랫동안 방치되었던 이 장소가 그만큼 낡아 있어서?

둘 다 틀렸다.

천 근, 만 근에 달하는 공력의 압력을 고스란히 받아 내며 내디딘 걸음이기 때문이다.

또한 공력으로 공력을 해소한 것이 아닌, 이미 인간의 한계를 아득히 벗어난 신체 능력만으로 이를 버텼기 때문이다.

우득. 콰드드득.

다시 한번 힘을 실어 내디딘 발끝이 흙과 꽃을 지르밟는다. 이미 앞서 산산이 부서졌던 청석 조각들이 수십, 수백으로 으스러지는 것이 느껴졌다.

한 걸음, 한 걸음 가까워질수록 더욱더 강해지는 압력도 함께.

하지만…….

‘버틸 수 있다.’

잘 벼려 낸 날붙이는 그 자체로도 훌륭한 무기인 법. 지금껏 숱하게 사선(死線)을 넘나들며 성장해 온 신체 능력 역시 마찬가지였다.

근력. 체력. 민첩.

그 모든 면에서 나는 월등했다. 한계를 뛰어넘었다.

한 수 위, 혹은 두 수 위의 강적들을 상대로 살아남을 수 있었던 가장 큰 이유 중 하나는, 공력 없이도 능히 초인의 힘을 발휘하는 이 몸뚱어리가 있었기 때문이다.

맨손으로 강철을 찢고, 이틀 밤낮을 쉼 없이 달려도 쓰러지지 않으며, 땅을 박찬 것만으로도 바람처럼 나아갈 수 있는.

그렇기에 설령 수 갑자의 공력이 몸을 옥죄어 온다 해도, 나는 버텨 낼 수 있었다.

아니, 깨트릴 수 있었다.

“합!”

짧은 기합성과 함께, 나는 온 힘을 다해 두 팔을 떨쳤다.

퍼엉!

엄청난 힘과 속도가 실리자 압축된 공기가 터져 나간다. 허공을 빈틈없이 에워싸며 짓누르던 공력이 흩어지는 것이 느껴졌다.

‘지금!’

무거웠던 전신이 민들레 홀씨처럼 가벼워진 그 순간. 나는 찰나의 빈틈을 놓치지 않고 신형을 쏘았다.

어느덧 크게 뜬 두 눈으로 나를 바라보고 있는 한 사람.

소교를 향해.

화륵, 콰앙!

염화일로(炎火一路).

그 한 걸음이면 족했다.

단전 깊숙한 곳에서 끌어 올린 열양지기가 발끝에서 폭발했고, 타오르는 열기와 함께 다섯 장의 거리를 단숨에 지워 낸 나는 흡사 포탄을 발사하듯 주먹을 내질렀다.

꽈앙!

세상이 뒤흔들렸다.

그리고 넘실거리는 청백색의 화염 너머, 하늘이 쪼개지는 듯한 굉음과 함께 세찬 속도로 튕겨 나가던 가느다란 신형이 허공에서 부드럽게 회전했다.

톡.

일 년 중 가장 강렬한 햇빛을 받아 활짝 만개한, 어느 이름 모를 꽃의 봉오리에 발끝이 닿는다.

스쳐 지나가는 바람처럼 한 송이 꽃 위에 착지한 소교의 모습에, 나는 그만 본능적으로 탄성을 흘릴 뻔했다.

‘아.’

표횰하면서도 우아하다.

그것은 실로 대단한 신법(身法)이었다.

순간적으로 적이라는 사실도 잊을 만큼. 이 기세를 몰아 계속해서 몰아붙여야 한다는 판단조차 잠시 접어 둘 만큼.

그리고 그런 나를 응시하는 소교의 눈동자는, 알 수 없는 이채(異彩)로 번뜩이고 있었다.

“분명 공력이 전혀 느껴지지 않았는데…… 도대체 어떻게 한 거지?”

나야말로 묻고 싶다.

전력을 다한 멸염신권을 어떻게 그리 쉽게 막을 수 있었는지.

어째서 그 섬광 같은 속도와 파괴력에 정면으로 맞부딪치고도 힘겨운 기색 하나 없는지.

‘개 같은 년. 양심상 후달리는 척이라도 좀 하지.’

내심 볼멘소리를 중얼거리며 툴툴 웃었다.

이런 상황에서 웃는 이유?

나도 모른다.

정말 미친놈이 된 건가 싶기도 하고, 이 싸움에 앞서 죽음을 각오했기 때문인지도 모른다.

그래, 맞다.

난 각오했다.

이미 오래전부터.

“너 죽고, 나 살자.”

나는 반쯤 실성한 사람처럼 웃으며 발걸음을 뗐다.

몸 상태?

괜찮을 리가.

거대한 힘을 일거에 쏟아 낸 단전은 벌써부터 과부하가 걸린 엔진처럼 울컥거리고, 손발처럼 움직이던 공력은 예전만 못하다.

하지만 이건 링 위의 스포츠가 아니다.

시합을 중지시킬 심판도, 위험에 처한 선수를 대신해서 수건을 던져 줄 세컨드도 없다.

생사결(生死決)이란 그런 것이다.

내가 익히 알고 있던 그대로.

‘이미 각오했어.’

몸과 달리 마음은 흔들리지 않는다.

나는 그 일념(一念) 그대로, 소교를 향해 재차 쇄도했다.

화악!

세상이 느려진다.

주위의 풍경이 뒤바뀐다.

그리고 뜨거운 열기와 바람, 용암처럼 부글거리는 투지(鬪志)에 전신을 맡긴 그 순간.

쐐애애액!

강렬한 파공성과 함께, 한 줄기의 섬광이 벼락처럼 들이닥쳤다.
```

## Final English reading copy

```markdown
# Chapter 887

Sssshhh.

Heat like molten lava coursed through me, scorching countless acupoints.

I glared at So Gyo with burning eyes. The voice that escaped with my breath was dry as ash.

“You… what the hell are you?”

“That’s quite a reaction. You should calm down and settle your internal energy before you overdo it.”

So Gyo—or rather… the woman whose identity I no longer knew—answered.

As always, she was calm and composed.

But she’d shed the polite speech and courteous manner she’d used to keep up appearances until now.

Then, the next moment, one sentence slipped from her lips and surged over me like a raging tide.

“Especially considering the state you’re in right now. Don’t you think?”

“……!”

Maybe this was what it felt like to be struck by lightning right through the crown of your head.

A trembling voice slipped out before I knew it.

“H-How?”

“Your internal energy is flowing unevenly.”

So Gyo’s answer was short and simple—and, above all, impossible to refute.

But that wasn’t why I’d momentarily lost my words.

For such an obvious answer, one thing had to be true.

*Qi Sense.*

And not just any Qi Sense. It had to be exceptionally keen, sharp as a blade.

Every fight began with gauging your opponent.

A master could see through the amount and condition of a lesser martial artist’s internal energy, but a lesser martial artist couldn’t accurately gauge a master’s level.

And right now, I was unmistakably the latter.

*A master!*

There was no doubt.

The woman in front of me, So Gyo, was an incredible master.

A Supreme Peak master who’d reached the realm of Returning to Simplicity—able to hide herself so perfectly that even I couldn’t see through her.

*So that movement I saw earlier wasn’t a fluke.*

I suppressed the sigh threatening to escape and quietly clenched my fists.

I was unarmed, without a single decent weapon, and my body was in rough shape.

No matter how optimistically I looked at it, this wasn’t a good situation for facing a master a level above me. Still, I lowered my stance at an angle and drew up my internal energy again.

“Who are you?”

So Gyo replied in a calm voice.

“I have no obligation to answer that. You were the one who broke your promise and lied first, Blazing Flame Divine Dragon Jin Taekyung.”

“Shut your mouth and answer me. Whose orders are you following, exactly? The Emperor’s? Or…”

I glared at So Gyo and spat out the two words.

“Lord of Heaven?”

“Who knows.”

A brief silence.

So Gyo gazed at me, her expression too vague to read her intentions. Then she suddenly spoke.

“If you knew who I was, what would that change?”

“It would change things. This is a matter of life and death.”

“Life and death…”

“Yeah. Depending on your answer, someone here is definitely going to die.”

“If that happens, the person who dies has already been decided. Don’t you think?”

At that moment—

Sssshhh.

The air trembled.

The force that became wind and shook the grass and flowers was like the north wind, and her cold gaze and voice wrapped around me like winter’s chill.

But I didn’t waver.

I’d already lived through too many bloodbaths to feel afraid just because my opponent was strong.

As a Hunter and as a martial artist of Murim.

“Yeah, maybe it has been decided to some extent. But is there a rule that only one of us can die?”

“What?”

“I’ll kill you. No matter what.”

“……!”

“I swear on everything I have. No—I guarantee it.”

Even I was surprised by how calm my voice sounded.

But this wasn’t some desperate bluff from a weaker fighter backed into a corner. My conviction reached So Gyo intact.

“You… you’re serious?”

“Of course.”

“So you’re ready to take me down with you. Heh.”

So Gyo let out a faint laugh and looked me up and down like some strange animal.

“So the reports were true after all. I suppose you must have had some hidden trick up your sleeve to survive this long.”

“The Blood Lord, the Western Heaven Demon Lord, and most recently, even the Southern Heaven Demon Empress. Of course, the Sword Saint and the Fire King helped you through your crises, but surviving encounters with all of them is all but impossible.”

“……!”

I stared at So Gyo with a cold, steady gaze.

I had a feeling I didn’t need to hear the answer to my earlier question.

*This woman knows about the Western Heaven Demon Lord and the Southern Heaven Demon Empress.*

Not just their names. She spoke as if she knew what kind of people they’d been and how powerful they were.

As though she’d known them personally.

At last, the identity of the woman hiding behind the name and status of So Gyo came into focus.

*…Dark Heaven.*

Yeah. It could only be that.

Hadn’t she practically admitted it herself?

She’d said one of the main reasons she stayed in the imperial palace was its vast intelligence network.

That meant she wasn’t a loyal servant of the Emperor, and that she had another purpose of her own.

*She meant to seize the imperial palace—or rather, the Emperor—and pull the strings.*

The scattered pieces of the puzzle fell into place.

The Fourth Prince’s sudden rebellion. The deaths of the late Emperor and the direct imperial family, and everything that had happened since.

But in the end, it had only been a partial success.

Even though the Emperor had been replaced overnight and countless people had vanished like dew on the execution grounds, they’d failed to completely root out the opposition and take control of the entire Great Nation.

*Then could it be…*

Just as the puzzle in my head was almost complete, So Gyo, who’d been watching me silently, suddenly spoke.

“Let me ask you one thing. Why are you going this far?”

“Why?”

“Yeah. Why insist on fighting me with that body of yours in such poor shape, when you’re even prepared to die taking me down?”

I fell silent for a moment.

Not because I needed time to think about the reason, but because it was so obvious to me.

“Because if I do, fewer of my people will die.”

“What?”

“Even if we both die here, that’d still be a lot better than letting a bitch like you live.”

“What if I told you I had no intention of harming you?”

“Sure. That’d obviously be bullshit, but fine.”

“Why?”

“Because a viper like you only causes more harm the longer she lives.”

How many people had died by now?

Every time Dark Heaven made a move, hundreds died. Then thousands. In the end, tens of thousands vanished as lonely ghosts.

So if I could put an end to it with just my life, I’d count myself lucky.

Of course, the best possible outcome would be that I survived and So Gyo died…

“But it doesn’t matter. I don’t think I’ll feel at ease until I pull out those damn fangs and strip the skin right off you.”

This time, So Gyo chose silence.

She kept her lips tightly shut for a long while, then tossed out a single remark.

“You’re much crazier than I expected.”

“What the hell are you talking about, you crazy bitch?”

“And I think I understand a little why Prince Shangshan, that child, looks up to you so much. Yes. I really do.”

“Are you threatening me now because you’ve got a kid hostage?”

“Who knows?”

“What the hell do you think? Now I’ve got one more reason to kill you, no matter what it takes.”

“I like the enthusiasm. But things don’t always go the way you want.”

So Gyo gave a small shake of her head.

“To have reached this level at such a young age… Your talent and achievement are so extraordinary they seem like a trick of heaven. No one can deny that. But…”

She continued slowly.

“Everything has its time. Being born with heavenly patterns won’t let you escape death.”

Swish.

A faint sound brushed against her collar.

At the same moment, the belt wrapped around So Gyo’s slender waist—no, a flexible sword—filled with powerful internal energy and pointed at me.

Beyond its supple blade, her eyes were cold.

“Shall we put it to the test? See whether heaven saves you, or leaves you to die right here?”

Whoooom.

At that very moment, a low but clear sword hum rang out.

Fwoosh.

I felt it unmistakably.

A truly horrifying, enormous aura spread out from So Gyo—a power I’d never felt before.

It squeezed and pressed down on my whole body, leaving no opening.

Hah.

I drew in a breath without meaning to.

The air had grown heavy in an instant, constricting my throat.

Under the pressure of her overwhelming aura, every hair on my body stood on end, and cold sweat beaded on my skin.

But—

“Fuck. Off.”

With those words spat from between my teeth, I pushed back against the chains of internal energy I couldn’t see.

I endured as they bound my arms and legs tight and forced myself toward So Gyo.

Crack. Thud.

One step.

It was only one step, yet the solid bluestone beneath my foot shattered at once, and the layers of earth beneath it caved in.

Was it because my body was that heavy? Or because this place, abandoned for so long, had grown that decrepit?

Neither.

It was because I’d taken that step while bearing the full pressure of internal energy weighing thousands upon thousands of geun.

And because I’d endured it through physical ability that had long since surpassed human limits—not by neutralizing her internal energy with my own.

Crack. Craaack.

I put more strength into my next step. My foot crushed the soil and flowers beneath it. I could feel the bluestone fragments that had already shattered crumbling into dozens, then hundreds of pieces.

With every step I took closer, the pressure grew stronger.

But…

*I can take it.*

A well-honed blade was a fine weapon all on its own. The same was true of the physical abilities I’d built by crossing the line between life and death countless times.

Strength. Stamina. Agility.

I was superior in every way. I’d gone beyond my limits.

One of the main reasons I’d survived against enemies a level—or even two levels—above me was this body, which could wield superhuman strength without internal energy.

The body that could tear steel apart with bare hands, run for two days and nights without collapsing, and surge forward like the wind by pushing off the ground.

So even if internal energy equivalent to several jiazi pressed down on me, I could endure it.

No—I could break through.

“Hah!”

With a short shout, I threw both arms out with all my strength.

Boom!

With so much power and speed behind it, the compressed air burst apart. I felt the internal energy that had surrounded and pressed down on me from every direction scatter.

*Now!*

The moment my heavy body felt as light as a dandelion seed, I seized the instant opening and launched myself forward.

One person, staring at me with eyes now wide open.

Toward So Gyo.

Fwoosh—Boom!

Flamefire Path.

One step was all it took.

Scorching Yang Qi surged up from deep within my dantian and exploded from my foot. Along with the blazing heat, I crossed the distance of five jang in an instant and drove my fist forward like a cannonball.

*BANG!*

The world shook.

Beyond the surging blue-white flames, a thin figure shot backward at tremendous speed, accompanied by a roar that seemed to split the sky—then spun gracefully through the air.

Tap.

Her toes touched the blossom of a nameless flower, opened wide beneath the year’s strongest sunlight.

So Gyo landed on the flower as lightly as a passing breeze. I nearly let out an involuntary gasp.

*Ah.*

Ethereal, yet graceful.

It was an extraordinary movement technique.

So much so that I forgot for an instant she was my enemy. So much so that I briefly set aside the thought that I had to keep pressing my advantage.

So Gyo stared at me, her eyes flashing with an inexplicable light.

“I couldn’t feel any internal energy from you at all… How did you do that?”

I should be the one asking.

How had she blocked the Flame-Extinguishing Divine Fist I’d thrown with all my strength so easily?

How could she meet that flash of speed and destructive force head-on without even looking strained?

*You damn bitch. Have some conscience and at least pretend you’re struggling.*

I grumbled to myself and gave a wry smile.

Why was I smiling in a situation like this?

I didn’t know.

Maybe I really had gone crazy. Maybe it was because I’d already prepared myself to die before this fight.

Yeah. That was it.

I’d prepared myself.

A long time ago.

“You die, I live.”

I laughed like a man half out of his mind and took a step forward.

My condition?

Of course it wasn’t fine.

The dantian that had unleashed an enormous amount of power all at once was already lurching like an overworked engine, and my internal energy no longer moved as freely as my hands and feet.

But this wasn’t a sport in a ring.

There was no referee to stop the match, no second ready to throw in the towel on behalf of a fighter in danger.

That was what a life-and-death duel was.

Just as I’d always known.

*I’d already made my choice.*

Unlike my body, my resolve didn’t waver.

With that single-minded determination, I charged So Gyo once more.

Fwoosh!

The world slowed.

The scenery around me shifted.

And at the moment I surrendered my whole body to the heat, the wind, and the fighting spirit bubbling like lava—

Screeeech!

With a violent whistle, a streak of light hurtled toward me like lightning.
```
