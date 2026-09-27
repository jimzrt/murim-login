<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1035.txt",
      "sha256": "df9247376c4764149aba2b94705b47d78aa1c619ac2304c6093bb6f9d32be766",
      "bytes": 12360
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "57bc5561c392491dd8d203720562dc44e0a1de25b16499fe4373ed1ffecb24d4",
      "bytes": 1137
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2067dd2b7fa33b1fa5ed0aadd49d6f2d144d2878b5e0ef369f14bcd34c117262",
      "bytes": 240195
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "fdd1832f1b1cf1c1c7c4aecc0a76bd522f4205d2e47c1f17ca17a028939c6dcf",
      "bytes": 843
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "81ff12da01c2d564312105986281966dfcb35cdf48132e7de99efb326c61cd6e",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "5e652347af9debc5f02dd71243afc798a08847424f644b0f7224fa527967cc71",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "494cde9b0705d28e7c700f8264354273b8212e3ef003a37ee527233880bb1141",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1607c11b6bb49b7e582a07657aae4eb9754b20209f4f3becf90f220369580a8c",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9fcdc873075b9cb2d4039976a1b6c6915530d22e136ba779219b7eb6f324ba96",
      "bytes": 279401
    }
  ],
  "estimated_tokens": 10094
}
-->

# Durable State Update — Chapter 1035

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
1 and safe_through 1035. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1035. Profile updates may replace only one
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
  "chapter": 1035,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1035,
    "continuity_sources": [1035],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "The Blood-Sword Demon Lord commands more than thirty thousand soldiers and seven Black Ghosts.",
    "Four Black Ghosts and the followers attacking Jeok Cheongang and his disciple were destroyed by Heavenly Strike.",
    "Jeok Cheongang and his disciple are fighting on the battlefield.",
    "Roughly twenty white-robed followers take orders from the Lord of Heaven through an unnamed woman who served him more closely than the Blood-Sword Demon Lord.",
    "The Blood-Sword Demon Lord believes the Lord of Heaven distrusts him and is resolved to prove himself."
  ],
  "continuity_sources": [
    1034
  ],
  "open_questions": [
    "Who are the seven Black Ghosts, and what were their identities before becoming Black Ghosts?",
    "What is the Lord of Heaven’s identity and purpose?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who is the unnamed white-robed woman, and what are the white-robed followers’ purpose?"
  ],
  "safe_through": 1034,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 살기     | **killing intent**                               |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 반박귀진 | **Returning to Simplicity** | Supreme Peak technique or phenomenon used by Jeok Cheongang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 멸지 | **Land of Ruin** | Name used for the desert region beyond which Dark Heaven’s forces are approaching. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1034
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion but believes his master does not fully trust him; he has been ordered not to kill Jin Taekyung and admires Jeok Cheongang.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1034
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1034
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1033
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1033
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1035화



띠링. 띠링. 띠링.

맑은 종소리가 귓가를 울린 그 순간이었다.

행동에 따른 결과를 증명하는 시스템 알림과 함께, 몸속 깊은 곳에서 새로운 활력이 샘솟은 것은.



- [Lv.152 고광륭]을 처치하셨습니다!

- [Lv.150 적환양]을 처치하셨습니다!

- [Lv.155 풍소귀]를 처치하셨습니다!

- [Lv.160 황독소]를 처치하셨습니다!

- 막대한 경험치와 명성을 획득하셨습니다!

- 레벨 업!

- 레벨 업의 효과로 모든 기력과 상태 이상, 그리고 일부 부상이 치유됩니다!



스아아아.

무더운 여름날, 시원한 계곡물로 전신을 씻어 내린다면 이런 기분일까.

나는 짧지만 치열했던 격전 끝에 쌓인 피로가 일거에 녹아내리는 것을 느끼며 심호흡했다.

후우.

그러나 이것은 네 마리나 되는 흑귀를 쓰러트린 것에 대한 안도의 한숨이 아니다.

아직 쓰러지지 않은, 이 전장에서 승리하기 위해서는 반드시 쓰러트려야 하는 누군가를 기다리며 심신을 안정시키는 호흡일 뿐이다.

“노야.”

“그래.”

내 짧은 부름에 고개를 끄덕인 적천강이 말을 이었다.

“놈이 온다.”

그 순간.

처처처척.

죽여도 죽여도 도무지 줄어들지 않던 암천의 교도들이, 흑귀들의 최후에도 아랑곳하지 않고 포위를 좁혀 오던 그 광신도들이 동시에 발걸음을 멈췄다.

그리고 엄중하면서도 일사불란한 움직임으로 길을 텄다.

오직 단 한 사람만을 위한 길을.

저벅, 저벅.

“미안하군. 뜻하게 않게 늦어 버려서.”

멀리서도 선명하게 들려오는 걸음 소리와 담담한 목소리.

나는 그런 혈검마군을 향해 어깨를 으쓱해 보였다.

툭.

이제는 크고 작은 수십여 개의 파편이 되어 버린, 흑귀(黑鬼)라 불렸던 그것들을 걷어차면서.

“미안하면 자결하든지.”

“그건 곤란하겠군.”

“그럴 것 같더라. 여하튼 괜찮아. 당신 친구들이랑 놀고 있었거든.”

“친구라, 거기 널브러져 있는 쓰레기들을 말하는 거라면 상당한 착오가 있는 듯싶은데.”

“쓰레기?”

“모두 한심하기 짝이 없는 놈들이었지. 정마대전에서 제 분수도 모른 채 천둥벌거숭이처럼 날뛰다가 죽거나, 진정한 하늘을 제대로 알아보지 못하고 되레 칼을 들이댔으니.”

그 말을 듣자 문득 짚이는 것이 있었다.

오늘 이 자리에 나타난 흑귀, 즉 데스 나이트들이 생전에 어떤 존재들이었는지.

“마교(魔敎)의 거마들이었군. 당신과 한솥밥을 먹던.”

혈검마군이 순순히 고개를 끄덕였다.

“한때는 그랬었지. 아주 오래전의 일이지만.”

혹시나 했는데, 역시다.

세상에 탄생하게 된 모든 것에는 그에 맞는 원인이 있는 법.

이 정도 수준의 데스 나이트를 만들기 위해서는, 그만한 격을 지닌 ‘재료’가 필요했음은 자명한 사실이었다.

“어쩐지, 이름만 봐도 영 상놈 새끼들 같더라.”

“이름?”

“고광륭, 적환양, 풍소귀, 황독소…… 이게 정상적인 대가리로 나올 수 있는 이름은 아니지. 안 그래?”

한 치의 망설임도 없이 흘러나온 이름들에, 혈검마군이 의외라는 눈빛으로 나를 바라보았다.

“희한한 일이군. 그 이름들을 자네가 어떻게 알고 있는 거지?”

“왜, 얘네 다 유명한 놈들 아니야? 이름만 들어도 기분이 괜히 개 같아지는 게, 어떤 인생들을 살아왔는지 빤히 보이는 것 같은데.”

“물론 한때는 중원에도 모르는 이가 없었네. 어디까지나 별호로는. 하지만…….”

나와 적천강을 번갈아 바라보던 혈검마군이 덧붙였다.

“무림인은 이름이 아닌 무공과 별호로 증명되는 법이니, 저들의 이름은 과거에도 아는 이가 극히 드물었지. 이건 설령 오랜 세월 동안 경륜을 쌓은 누군가가 곁에 있다 해도 알 수 없는 부분이야.”

혈검마군의 목소리에는 확신에 차 있었다.

그도 그럴 것이, 마교의 총본산이자 이제는 암천의 본거지로 자리매김한 신강은 아득한 과거부터 그래 왔던 곳이었으니까.

그 누구도 허락 없이는 발을 디딜 수 없는 멸지(滅地).

바로 그 은영각조차 길고 치밀한 준비 끝에 조금이나마 장막을 들춰 볼 수 있었던 사막 너머의 교국(敎國).

하지만 나는 다르다.

비록 극히 단편적이라고는 해도, 내게는 알려지지 않는 정보를 읽어낼 수 있는 능력이 있었다.

그 대상이 내 눈앞에 존재하기만 한다면.

그리고 거기에 더하여, 내가 지닌 힘과 능력이 상대방과 그리 큰 격차가 없다면.

솨아아아악.

그 순간, 내 의지와 함께 보이지 않는 푸른 원이 빛살처럼 공간을 집어삼켰다.

어느덧 구성에 다다른 [기감]이 나를 중심으로 뻗어 나가, 무려 반경 오십여 장에 달하는 공간을 푸르게 물들였다.

띠링. 띠리리링.

기감의 범위 안에 존재하는 수백, 아니 수천이 넘는 적들의 정수리 위로 떠오르는 무수한 시스템 창.

그러나 내 시선은 오직 한 사람에게 고정되어 있었다.

기감의 발현과 동시에 불현듯 걸음을 멈춘, 혈검마군에게.



[Lv.170 척방혈]



놈의 머리 위를 장식한 레벨 창은 이십여 장 밖에서도 또렷하게 알아볼 수 있었다.

미간을 좁힌 채 의문 어린 표정을 하고 있는 그 얼굴 역시도.

“지금 도대체…….”

기감(氣感)이라는 단어는 비단 나 혼자만의 전유물이 아니다. 경지에 오른 무림인들은 자신과 상대의 기운을 가늠하고 읽어 내는 것이 일상이니까.

그러나 시스템의 일부로서 존재하는 기감은, 무림인들의 그것과는 느낌부터가 달랐다.

“무슨 짓을 한 것이냐.”

조금 전과는 달리 착 가라앉은 목소리와 삭막해진 말투.

하지만 나는 그런 혈검마군을 향해 입꼬리를 말아 올렸다.

“우리 방혈이는 궁금한 게 참 많네. 아직 한창때라 그런가.”

“……!”

“아, 혹시 그 이름도 비밀이었나? 아니 마두라는 새끼들이 뭐 이렇게 감추는 게 많아?”

처음 산서성에서 만났을 당시, 내 기감을 경험해 본 적이 있던 적천강이 입맛을 다시며 말을 받았다.

“네놈은 모르겠지만, 저거 은근히 기분 더럽다. 노부도 처음에는 해괴한 사술에 당한 줄 알았지.”

“그런데 저 새끼는 마두잖아요. 사술이면 오히려 익숙해야 하는 거 아니에요?”

“그건…….”

내 합리적인 반박에, 굳은 얼굴을 한 혈검마군의 모습을 유심히 바라보던 적천강이 대답했다.

“부끄러운가 보지. 대충 들어봐도 그렇게 썩 괜찮은 이름은 아니지 않느냐. 명색이 사람 이름인데 방혈이가 뭐냐 방혈이. 방귀도 아니고.”

“에이, 아무리 나이를 똥구멍으로 처먹었어도 그렇지 무슨 그런 걸 가지고 그럽니까. 저 인간도 내일모레면 백 살쯤 될 텐데.”

“네놈도 나이 들어 봐라. 가끔 괜히 별 이유도 없이 기분이 묘해질 때가 있어. 혹시 아느냐? 저놈도 매일 밤 달빛 아래 앉아서 눈시울을 적실지.”

“오.”

엄청난 악명을 떨친 대마두가 늦게나마 갱년기에 접어들었다는 건 꽤나 흥미로운 가설이었지만, 다음 순간 혈검마군이 불쑥 내뱉은 한 마디는 내 얼굴을 굳게 만들기에 충분했다.

“네 말이 옳다. 열화신룡 진태경.”

“뭐?”

“조금 전 그 입으로 직접 말하지 않았느냐. 사술이면 오히려 익숙해야 하는 것 아니냐고.”

앞서 느꼈던 기감의 여운을 되새기려는 듯, 자신의 두 손을 물끄러미 내려다보던 혈검마군이 말을 이었다.

“그렇군. 내가 아는 것과는 조금 다르지만, 그래도 제법 익숙해.”

“……!”

그 순간, 나도 모르게 눈이 커졌다.

다르지만 익숙하다.

이 짧은 말에 담긴 의미가 무엇인지, 그리고 마음속 어디에선가 뭉클뭉클 솟아오르는 이 알 수 없는 불안감의 실체가 무엇인지 조금씩 선명해지고 있었다.

“처음에는 놀랐고, 이제야 비로소 납득 했다. 어찌하여 그분께서 너를 그토록 주시하셨는지.”

저벅. 저벅. 철벅.

메마르고 얼어붙은 땅을 지나, 혈검마군이 내뻗은 발걸음이 마침내 지면에 고여 있던 피 웅덩이를 밟았다.

투둑.

거칠어진 걸음을 따라 핏물이 튄다.

천천히 들어 올려지는 검신 위를 뒤덮는 거대한 기운은, 그보다 진하고 끈적거렸다.

“허나, 이번만큼은 그분의 판단이 틀렸다. 이 일은 처음부터 내가 직접 나섰어야 했어. 만류나 걱정 따위는 처음부터 필요 없었다.”

우우우웅.

그 순간, 나는 혈검마군을 중심으로 벌어지는 변화를 느꼈다.

비단 바람이 멈추고, 공기가 몸을 떨었기 때문이 아니다.

그의 손아귀에서 거칠게 울어대는 검신이 막강한 강기를 토해 내고 있었기 때문도 아니었다.

삐빅.



[Lv.175 척방혈]



“……!”

바뀌었다.

놈이 발산하는 기운이, 레벨 창에 적힌 숫자가.

‘이건.’

본능적으로 알 수 있었다.

지금의 혈검마군은 단순히 반박귀진(返朴歸眞)의 경지로 본인의 힘을 숨겨 왔던 것이 아니라는 사실을.

‘분명, 분명히 이 정도가 아니었을 텐데.’

이미 전면전이 벌어지기 전에 한 차례 격돌해 본 적이 있다. 나도, 적천강도, 그리고 혈검마군도 전력으로 맞부딪혔고 그 결과는 틀림없이 놈의 열세였다.

그런데 어째서.

삐빅.



[Lv.178 척방혈]



도대체 어떻게.

삐빅.



[Lv.180 척방혈]



놈은, 혈검마군은 우리를 향해 서서히 가까워지는 지금 이 순간에도 강해질 수 있는 것일까.

“대관절…… 무슨 사술을 부리는 것이냐.”

제자가 느끼는 것을 스승이 느끼지 못할 리가 없다.

그리고 적천강의 입술 사이로 흘러나온 그 당연한 의문이, 어느덧 거대하게 부풀어 오른 내 마음속 불안감의 실체에 빛을 밝혔다.

‘사술(邪術).’

글자에 담긴 뜻 그대로 요사스럽고, 간사한 술법.

이와 같은 사술을 부리는 이는 옳고 곧은 길을 벗어난 자들, 즉 사마외도(邪魔外道)라 칭해지고, 그중에서도 가장 깊은 심연에 위치한 존재들을 사람들은 이렇게 부른다.

마도(魔道).

인간으로 살기를 거부하고, 마귀의 길을 택한 자들.

그렇다면, 이해할 수 없는 불가사의함으로 가득한 그들이 펼치는 사술은 무엇이라 불러야 하는가.

흑귀라 불리는 저 존재들은 어떻게 탄생하여 이 자리에 나타날 수 있었는가.

“……아닙니다.”

“뭐라?”

“사술이, 아닙니다.”

불현 듯 입술을 뗀 나는, 넋 나간 목소리로 중얼거렸다.

옆에서 계속해서 되묻는 적천강의 목소리는 어느덧 메아리처럼 멀게 들려왔고, 한 걸음 한 걸음을 내뻗을 때마다 더욱더 강해지는 혈검마군의 존재도 잠시나마 잊어버렸다.

나는 그저 무언가에 홀린 듯한 마음이 되어 바라보았다.

지금껏 혈검마군의 존재감으로 가려져 있었던, 지금 이 순간에도 치열한 전투가 계속되고 있는 이 광활한 전장의 극히 작은 일부로 존재했던 백의인들을.

아니, 흑귀들과 마찬가지로 이 세상에 존재할 수 없는 힘을 지닌 그들을.

“마법(魔法).”

그리고 더없이 익숙하면서도, 믿을 수 없는 그 두 글자가 입술 사이를 비집고 흘러나온 그 순간.

“풍귀(風鬼)의 힘이여.”

저 멀리, 또렷하게 울려 퍼지는 영창과 함께.

“그에게 깃들라.”

의지를 담은 주문이, 혈검마군의 몸으로 발현(發現)했다.
```

## Final English reading copy

```markdown
# Chapter 1035

Ding. Ding. Ding.

The clear chime rang in my ears, and at that very moment, new vitality welled up from deep within me, accompanied by System notifications proving the results of my actions.

> **System**
>
> Defeated Lv. 152 Go Gwangryung!
>
> Defeated Lv. 150 Jeok Hwanyang!
>
> Defeated Lv. 155 Pung Sogwi!
>
> Defeated Lv. 160 Hwang Dokso!
>
> Acquired a massive amount of EXP and Fame!
>
> Level Up!
>
> The effects of leveling up have restored all energy, cured all status conditions, and healed some injuries!

Shaaah.

Was this what it felt like to wash all the way down in a cool mountain stream on a sweltering summer day?

I took a deep breath, feeling the exhaustion built up over that brief but fierce clash melt away all at once.

Whew.

But this wasn’t a sigh of relief at having taken down four Black Ghosts.

It was just a breath to steady my body and mind as I waited for the person who hadn’t fallen yet—the person I had to defeat if we were going to win this battle.

“Old Master.”

“Yeah.”

Jeok Cheongang nodded at my brief call, then continued.

“He’s coming.”

At that moment—

Clack, clack, clack.

The Dark Heaven followers, who never seemed to grow fewer no matter how many we killed, had been closing in around us without so much as a pause after the Black Ghosts’ end. Now, those fanatics stopped in unison.

Then, with grave, orderly movements, they opened a path.

A path for just one person.

Step. Step.

“My apologies. I’m later than I intended.”

His footsteps and calm voice carried clearly, even from a distance.

I shrugged at the Blood-Sword Demon Lord.

Thump.

I kicked the remains of what had been called Black Ghosts—now scattered into dozens of large and small fragments.

“If you’re sorry, go kill yourself.”

“That would be difficult.”

“Figured. Anyway, I’m fine. I was playing with your friends.”

“Friends? If you mean those piles of trash lying over there, then I think you’re mistaken.”

“Trash?”

“They were all hopeless. During the Great Faction War, they either ran wild like reckless fools who didn’t know their place and got themselves killed, or failed to recognize the true Heaven and raised their swords against it.”

His words brought something to mind.

The Black Ghosts who had appeared here today—the Death Knights—and what they had been in life.

“They were Demonic Cult fiends. You used to share a bowl with them.”

The Blood-Sword Demon Lord nodded readily.

“Once, yes. A very long time ago.”

I’d suspected as much.

Everything that came into being had a cause to match. It was obvious that making Death Knights of this caliber required materials of comparable stature.

“No wonder. Even just from their names, they sounded like a bunch of lowlifes.”

“Their names?”

“Go Gwangryung, Jeok Hwanyang, Pung Sogwi, Hwang Dokso… Those aren’t names that could come from a normal person’s head. Don’t you think?”

The names came tumbling out without a moment’s hesitation. The Blood-Sword Demon Lord looked at me with surprise.

“That’s strange. How do you know their names?”

“What, weren’t they famous? Just hearing those names puts me in a bad mood. Makes it pretty obvious what kind of lives they led.”

“Of course they were once known throughout the Central Plains. But only by their sobriquets. Still…”

The Blood-Sword Demon Lord looked between Jeok Cheongang and me before adding, “A martial artist is known by their martial arts and sobriquet, not their name. Even back then, very few knew those men’s real names. Even with someone who’s spent many years gaining experience at your side, you couldn’t have learned those names.”

There was certainty in his voice.

And for good reason. Xinjiang, the Demonic Cult’s stronghold—and now Dark Heaven’s home—had been that way since time immemorial.

A Land of Ruin no one could enter without permission.

A religious state beyond the desert, where even the Hidden Shadow Pavilion had managed to lift the veil only a little after long and meticulous preparations.

But I was different.

Even if it was only in fragments, I had the ability to read information that no one else knew.

As long as the target was right in front of me.

And if the gap between my own strength and abilities and my opponent’s wasn’t too great.

Shaaah!

At that moment, a blue circle I couldn’t see swallowed up the space around us in a flash of light, responding to my will.

Qi Sense, now nine-tenths mastered, spread out from me, washing an area with a radius of more than fifty *jang* in blue.

Ding. Ding-ding-ding.

Countless System windows appeared over the heads of the hundreds—no, thousands—of enemies within Qi Sense’s range.

But my gaze stayed fixed on one person alone.

The Blood-Sword Demon Lord, who had abruptly stopped walking the moment Qi Sense activated.

> **System**
>
> Lv. 170 Chuk Banghyeol

I could make out the Level window above his head clearly, even from more than twenty *jang* away.

I could also see his face, brow furrowed in confusion.

“What in the world did you just—”

The term Qi Sense didn’t belong to me alone. It was routine for martial artists who’d reached a certain realm to gauge and read their own and their opponents’ energy.

But Qi Sense, as part of the System, felt different from theirs.

“What did you do?”

His voice was lower than before, his tone suddenly cold and barren.

But I only curled the corner of my mouth at him.

“Our Banghyeol’s got a lot of questions. Is it because you’re still in your prime?”

“……!”

“Oh, was that name a secret, too? What do you fiends have to hide so much for?”

Jeok Cheongang, who’d experienced my Qi Sense back when we first met in Shanxi Province, clicked his tongue before chiming in.

“You may not know this, but that thing feels pretty damn unpleasant. Even I thought I’d been hit with some bizarre dark art the first time.”

“But he’s a fiend, isn’t he? Wouldn’t dark arts be familiar to him?”

“Well…”

Jeok Cheongang studied the Blood-Sword Demon Lord’s rigid face, then answered.

“Maybe he’s embarrassed. Even without hearing the whole thing, it doesn’t sound like a very good name. It’s a person’s name, and yet it’s Banghyeol. Banghyeol? Sounds like a fart.”

“Come on. Even if you’re old enough to have shoved your years up your ass, you can’t make fun of him for that. That man’s probably almost a hundred himself.”

“You wait till you’re old. Sometimes you feel strange for no reason at all. Who knows? Maybe that man sits beneath the moon every night with tears in his eyes.”

“Oh.”

The idea that the infamous great fiend had belatedly entered menopause was pretty interesting. But the next words out of the Blood-Sword Demon Lord’s mouth were enough to make my face stiffen.

“You’re right, Blazing Flame Divine Dragon Jin Taekyung.”

“What?”

“Didn’t you just say it yourself? That dark arts ought to be familiar to him.”

As if trying to recall the lingering sensation from my Qi Sense, the Blood-Sword Demon Lord gazed down at his hands before speaking again.

“I see. It’s a little different from what I know, but still quite familiar.”

“……!”

My eyes widened before I could stop them.

Different, but familiar.

The meaning behind those few words—and the source of the vague anxiety welling up somewhere in my heart—was slowly becoming clearer.

“At first, I was surprised. Now I finally understand why that person watched you so closely.”

Step. Step. Splash.

Crossing the dry, frozen ground, the Blood-Sword Demon Lord finally stepped into a pool of blood on the ground.

Plip.

Blood splashed with his roughened stride.

A powerful energy covered the slowly rising blade, thicker and more viscous than the blood itself.

“But this time, that person’s judgment was wrong. I should have handled this myself from the start. There was never any need for anyone to dissuade me or worry.”

Wooooong.

At that moment, I sensed something changing around the Blood-Sword Demon Lord.

It wasn’t because the wind had stopped or the air was trembling.

It wasn’t even because the sword in his grip was roaring and spewing out an immense Force.

Beep.

> **System**
>
> Lv. 175 Chuk Banghyeol

“……!”

It had changed.

The energy he was giving off. The number in his Level window.

*This is…*

I knew instinctively.

The Blood-Sword Demon Lord hadn’t simply been hiding his power with Returning to Simplicity.

*He definitely, definitely wasn’t this strong before.*

We’d already clashed once before the full-scale battle began. I, Jeok Cheongang, and the Blood-Sword Demon Lord had all fought at full strength. There was no doubt about the result: he had been at a disadvantage.

So why?

Beep.

> **System**
>
> Lv. 178 Chuk Banghyeol

How?

Beep.

> **System**
>
> Lv. 180 Chuk Banghyeol

How could he, the Blood-Sword Demon Lord, keep growing stronger even as he slowly approached us?

“What in the world… what kind of dark arts are you using?”

There was no way a master wouldn’t feel what his Disciple felt.

And the obvious question that slipped between Jeok Cheongang’s lips shed light on the anxiety swelling within me.

*Dark arts.*

A dark, devious technique, just as the words themselves meant.

Those who practiced such arts strayed from the righteous path, and were called practitioners of demonic, heterodox arts. As for those who dwelled in the deepest abyss among them, people called them—

The Demonic Path.

People who rejected the human way of life and chose the path of demons.

Then what should we call the dark arts they wielded, filled with inexplicable and mysterious power?

How had those beings known as Black Ghosts come into existence, and appeared here?

“……No.”

“What?”

“It’s not dark arts.”

I suddenly parted my lips and murmured, my voice dazed.

Jeok Cheongang’s repeated questions grew distant, like echoes. For a moment, I even forgot the Blood-Sword Demon Lord’s presence, growing stronger with every step he took toward us.

As if entranced, I looked at the white-robed figures.

They’d been obscured by the Blood-Sword Demon Lord’s presence until now, a tiny part of this vast battlefield where the fight was still raging.

No—their power was just as impossible in this world as that of the Black Ghosts.

“Magic.”

And at the moment that one word, so familiar and yet so unbelievable, slipped from between my lips—

“Power of the Wind Ghost.”

Far away, a chant rang out clearly.

“Take root in him.”

A spell imbued with intent manifested in the Blood-Sword Demon Lord’s body.
```
