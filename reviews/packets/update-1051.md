<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1051.txt",
      "sha256": "891e88343456796277f7a29b6ee61206e5e2c6418345bda13861c9ab2bed2c32",
      "bytes": 12880
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fa2c4bedb9dd8a7607cacab193622df14b2866768349a2f7c885d6ddc595c48f",
      "bytes": 1265
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "868b4198ccb7fd80afe930ae78b2952791045491214eca3a3f4a712023e3d1f7",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "d1e10237498f66f27e47d656fb914a7680692090aef48e8c2dd32f926f27b070",
      "bytes": 643
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c1b1dbfb3fc067db3738126cdb57e29b4d1e358a9f9fea77be02b86a120a48b9",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "eb606703b2a08409d465791f2fee2d532c8abb78410d772830e62e67b0b6ff4d",
      "bytes": 1827
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "dc2d74a0341273b41e2edd249e3f7b2f41dafeb7798662bf227901d7fc1725b6",
      "bytes": 623
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "516139a6ad9f448dac132db950dc3b7f1e41a8fc4bdcb6f7d999fe6a70be60e2",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e476e49cdcddf6de4980fb9437ae78bed54ffc02a595fe7c61e28608999f8e34",
      "bytes": 281989
    }
  ],
  "estimated_tokens": 10713
}
-->

# Durable State Update — Chapter 1051

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
1 and safe_through 1051. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1051. Profile updates may replace only one
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
  "chapter": 1051,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1051,
    "continuity_sources": [1051],
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
    "The Grand Mage says the Lord of Heaven ordered her faction to watch Jin Taekyung and wants him to survive and grow stronger; the reason is unknown.",
    "The Grand Mage identifies Jin as the Chosen One, matching the title the Bow Saint used based on the Martial God’s letter.",
    "Jin severs his heart meridians while bound by the Grand Mage’s plant magic, using the faint healing power she gave him; his condition is unresolved."
  ],
  "continuity_sources": [
    1049,
    1050
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Why does the Lord of Heaven want Jin to survive and grow stronger?",
    "How did the Martial God foresee the Chosen One, and what connects his letter to the Lord of Heaven’s plans?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?"
  ],
  "safe_through": 1050,
  "temporary_decisions": [
    "Render 대마도사 and 대술사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation."
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
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 상태               | **Status**                     |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 이형환위 | **Shifting Form and Position** | Supreme Peak movement or evasion technique used by Jeok Cheongang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 심맥 | **heart meridian** | Meridian severed by an infiltrator to commit suicide. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 블링크 | **Blink** | Arch Lich movement spell |
| 탈진 | **Exhaustion** | System status effect caused by exhausting all internal energy while severely injured. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 진취 | **Jin Chui** | Ming dynasty general identified as Taekyung's ancestor. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 대라신선 | **Great Firmament Immortal** | Legendary immortal invoked by Mungyeong as unable to stop the dragon's death. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 대마도사 | 궁성 | Adversaries | Bow Saint | Not established | She identifies him by title when recognizing the archer who struck the Hell Fire sphere. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1050
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1050
- **Aliases:** None
- **Role:** The Grand Mage leads the white-robed mages and is a formidable mage who has reached the edge of truth.
- **Personality:** Fanatically devoted to the Lord of Heaven, she stays composed while coercing her enemies and treats their resistance with contempt.
- **Voice:** Calm and formally polite while taunting, but drops the courtesy for blunt, scornful challenges when addressing an enemy.
- **Relationships:** She commands the white-robed mages and is an adversary of Jin Taekyung.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1050
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1050
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1050
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1048
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1051화



“너…….”

새파랗게 질려 가던 진태경의 얼굴에 떠오른 미소를 발견한 순간, 대술사는 본능적으로 직감할 수 있었다.

조금 전의 자신이 얼마나 멍청한 실수를 저질렀는지.

‘이런.’

돌이킬 수 없는 패착이었다.

죽일 테면 죽여 보라는, 너무나도 선명하게 전해지는 그 진심에 무의식적으로 속박 마법을 느슨하게 푼 것은.

그리고 바로 그 찰나의 실수를 통해 드러난 대술사의 진짜 속내를, 진태경은 즉각 알아차렸다.

“왜, 못하겠냐? 이 미친년아.”

“……!”

정곡을 찔린 대술사는 입술을 깨물었다.

진태경의 말은 사실이었다.

사냥개가 목표의 숨통을 끊을 수 있는 것은 오직 주인의 허락이 떨어졌을 때뿐.

하지만 그녀에게는 아직 그만한 권한이 없었고, 앞서 섭리를 운운한 허장성세(虛張聲勢)는 이미 들통나버린 후였다.

물론 그렇다 할지라도.

‘변하는 건 없어. 아무것도.’

내심 중얼거린 대술사는 잠시 흐트러졌던 마법에 다시금 힘을 불어넣었다.

콰득!

언제 그랬냐는 듯, 더욱 강하게 진태경의 목을 조여드는 굵고 단단한 줄기들.

지금 이 순간 명백하게 드러난 힘의 격차는 그 무엇으로도 메울 수 없었다.

한 줌밖에 되지 않은 기력을 지닌 그와 달리, 대술사의 몸속 깊은 곳에는 아직도 엄청난 기운이 웅크리고 있었으니.

그뿐만이 아니다.

진태경을 포로로 잡은 이상, 화왕과 궁성이라는 두 거인 역시 감히 경거망동하지 못하는 상황.

이제 자신에게 남은 것은 눈앞의 핏덩이를 굴복시키는 것뿐이라고.

대술사는 분명 그렇게 생각했다.

진태경의 만면에 깃든, 그 어느 때보다 환하게 빛나고 있는 미소를 보기 전까지는.

‘……웃어?’

도저히 이해할 수 없었다. 저 웃음에 담긴 의미를.

아니, 정확히는 그 의미를 본능적으로 짐작했음에도 이성적으로 받아들이지 못했다.

이토록 완벽하게 제압당한 상황 속에서, 진태경이 만들어 낼 수 있는 변수는 단 한 가지뿐이었으니까.

그리고 자결(自決)이라는 정신 나간 변수를 택할 미친놈은 세상 그 어디에도 없을 테니까.

하지만.

으득!

있었다. 바로 그 미친놈이.

바로 이곳에.

다름 아닌 그녀의 눈앞에.

푸확, 촤아악!

그 순간, 대술사는 자신도 모르게 눈을 부릅떴다.

붉었다. 온 세상이.

동시에 보였다.

그녀의 백색 면사를 뒤덮으며 끈적하게 흘러내리는 핏물 사이로, 전신을 잘게 떨며 토혈(吐血)하고 있는 진태경의 모습이.

“이, 이건.”

붉은 입술 사이를 비집고 흘러나온 넋 나간 탄식.

틀림없다. 스스로 심맥(心脈)을 끊은 것이다.

제아무리 벌목꾼의 도끼질에도 쉽사리 쓰러지지 않는 거대한 고목이라 할지라도, 껍질을 뚫고 안을 파고든 개미 군락에는 견딜 재간이 없는 법.

그렇기에 무림인에게 있어, 심맥을 끊는다는 것은 곧 죽음을 의미했다.

매우 고통스러우면서도, 신속한 죽음을.

‘도대체 왜, 이렇게까지?’

순간 얼어붙은 대술사는 경악에 물든 눈빛으로 진태경을 바라보았다.

그녀가 알려 준 것은 고작 반쪽짜리 진실이었을 뿐이다.

확신을 심어 주기에는 턱없이 부족한, 그저 무언가를 어렴풋이 짐작할 수 있을 정도의 자그마한 진실.

한데 자신이 살아 숨 쉬는 것만으로도 누군가에게 위협이 된다는 짐작을 떠올렸을 때, 주저 없이 목숨을 내버릴 이가 하늘 아래 몇이나 되겠나.

없을 것이다. 단연코.

인간에게 주어진 가장 큰 욕망은 살고자 하는 것이고, 설령 이와 같은 선택을 내린다 할지라도 실행에 옮기기까지는 수많은 망설임과 각오가 필요하다.

하지만 진태경은 해냈다.

일말의 망설임도, 두려움도 없이.

심지어 환하게 웃기까지 하며.

지금 이 순간에도 빠르게 빛이 꺼져 가는 그의 눈동자에는, 한 치의 흔들림도 없는 확신이 담겨 있었다.

스스로가 옳은 길을 택했다는 확신이.

그리고 그런 진태경의 모습에, 대술사는 불현듯 자신이 저지른 가장 치명적인 실수가 무엇이었는지 비로소 깨달았다.

‘선택받은 자.’

앞서 마음을 읽힌 것 따위는 아무것도 아니었다.

저 다섯 글자에 담긴 뜻을 알았어야 했다. 짐작했어야 했다.

그녀의 위대한 주인이 어째서 눈앞의 청년을 그토록 찾고자 했었는지.

당신의 충복들로 하여금 일거수일투족을 주시해 왔는지.

진태경은 그런 인간이었다.

욕설을 쏟아내면서도 인의(人義)를 알고, 침을 뱉으면서도 협의(愜意)을 좇으며, 길가의 가장자리를 걸을지언정 끝끝내 정도(正道)를 벗어나지 않는.

모두의 앞에서 나아가는 협객인 동시에, 모두의 상상을 초월한 미친놈.

그렇기에, 선택받은 자.

까득!

대술사는 이를 악물었다.

더 이상 머뭇거릴 시간도, 선택의 여지도 없었다.

그녀의 주인은 이미 너무나도 오랜 시간을 기다려 왔고, 오늘 이 자리에서 진태경이 죽음을 맞이한다면 또다시 기약 없는 기다림을 이어 가야 할 테니까.

‘살려야 한다. 무슨 수를 써서라도!’

느릿하게 흘러가는 시간 속, 대술사는 그 어느 때보다 간절하고 다급하게 손을 뻗었다.

스아아아아!

가냘픈 체구를 중심으로 솟아오르는 거대한 기운.

필살(必殺)이 아닌, 필활(必活)의 의지에 따라 심장에 둘러싼 기운이 거세게 맥동한다.

대기에 잠재된 기운이 그에 맞춰 교감하고, 이내 빛으로 터져 나와 온 사방을 집어삼켰다.

파앗, 화아아악!

크게 부풀어 오른 섬광이 언덕을 휘감았다.

아니, 이내 언덕 전체를 뒤덮으며 뻗어 나갔다.

그 눈부신 광휘는 인질로 잡혀 있던 진태경의 신변에 문제가 생겼음을 깨닫고 쏘아지던 궁성과 적천강의 동공을 새하얗게 물들이고, 아직까지도 생을 포기하지 않은 채 벌레처럼 꿈틀거리던 대마두의 눈을 감기게 했다.

심지어는, 광휘를 불러일으킨 대술사 자신조차도.

‘어떻게 된 거지?’

대술사는 순간 아득해진 시야 속에서 입술을 깨물었다.

돌무더기가 쓰러지면 흙먼지가 일어나지만, 태산이 허물어지면 지진이 일어나는 법.

드높은 경지에 오른 초절정 고수가 스스로 심맥을 끊었다는 것은, 설령 대라신선이라 해도 회생시킬 수 없는 부상이라는 뜻이다.

그녀가 할 수 있는 최대한의 치유를 발휘했지만 장담할 수 있는 것은 아무것도 없었고, 그 어느 때보다 강렬하게 터져나온 광휘는 쉽게 사그라들 기미가 보이지 않았다.

아니, 지금 이 순간 오히려 강하게 번뜩이는 듯했다.

마치.

햇빛 아래에서 더욱 빛을 발하는 날붙이처럼.

“……!”

무언가를 알아차린 대술사의 두 눈이 크게 뜨인 순간.

슈확!

소름 끼치도록 낮고 예리한 파공성이, 백염(白炎)이라 불리기에 조금의 손색이 없는 은백색의 창날이 공간을 찢었다.

여전히 아득한 광휘 너머에서 들려오는, 누군가의 나직한 목소리와 함께.

“잡았다.”

퍼걱!



* * *



속이 울렁거린다.

머리는 어지럽고 시야는 흐릿하다.

그래서일까.

사실, 아직도 잘 모르겠다.

지금 이 순간이, 꿈인지 현실인지.

만약 둘 다 아니라면…….

‘지옥, 아니 천국인가?’

그렇게 생각할 수밖에 없었다.

온 사방이 눈을 제대로 뜰 수 없을 정도로 새하얗게 물들어 있었으니까.

만약 어느 진취적인 염라대왕이 지옥에 떨어진 죄수들의 옥중복지를 위해 미친 성능의 LED 전구를 전면 도입하지 않았다면, 이곳은 분명 천국이겠지.

하지만.

띠링. 띠링. 띠리링!

저 멀리에서 되돌아온 메아리처럼 귓가에 울려 퍼지는 맑은 종소리로 충분히 짐작할 수 있었다.

이곳이 현실이고, 내가 살아 있다는 것을.

목숨을 판 돈으로 걸었던 이 미친 도박판에서, 또 한 번 승리했다는 것을.



- 상태 이상, [끔찍한 내상]이 해제되었습니다!

- 상태 이상, [극심한 출혈]이 해제되었습니다!

- 상태 이상, [탈진]이 해제되었습니다!

- 상태 이상, [내장 파열]이 해제되었습니다!

- 상태 이상, [골절]이 해제되었…….

.

.

.

- 강력한 치유의 힘이 당신의 신체에 깃듭니다!

- 어떻게 했나 싶은 업적, [배 째]를 달성하셨습니다!



허공에 줄줄이 떠오르는 반투명한 홀로그램 창.

그와 함께 흐려졌던 시야가 언제 그랬냐는 듯이 또렷해진다. 어느덧 호흡은 안정되고 선명해진 오감(五感)은 반경 십여 장의 모든 것을 느끼고 받아들였다.

빛. 공기. 바람. 짙은 피비린내처럼 형체가 없는 것들도.

또한 지금 이 순간에도 그 모든 것들 속에서 호흡하고 있는, 나와 같은 생기(生氣)를 띤 것들도.

그리고 이제는, 내가 걸었던 판돈의 대가를 상대에게서 받아야 할 때였다.

‘와라.’

마음속으로 속삭이고, 의지를 실어 명령했다.

한 줌의 생기도 없으나, 수많은 생기를 꺼트려 왔던 차가운 날붙이를 향해.

내 손아귀를 떠나 저 멀리 홀로 외롭게 지면을 뒹굴고 있던 애병을 향해.

슈확!

그 모든 것은 거의 동시에 이루어졌고, 나는 낮게 읊조렸다.

“잡았다.”

그 순간.

퍼걱!

뼈와 살이 터져 나가는 소리와 함께, 빈틈없이 내 전신을 옥죄고 있던 굵은 초목의 줄기들이 느슨해졌다.

‘지금.’

공력을 불어넣을 필요도 없었다.

그저 초인적이라는 표현으로도 다 담을 수 없는 엄청난 거력(巨力)을, 사지에 실어 펼쳐낼 뿐이었다.

콰드드드득!

갈라지고, 이내 터져 나간다.

끔찍하리만치 거대한 힘을 이기지 못한 줄기들이 조각조각 끊어짐과 동시에 자유를 되찾은 나는, 한 줄기의 섬광이 되어 이쪽으로 쏘아지던 백염을 향해 손을 뻗었다.

탁.

더없이 익숙한, 서늘한 그 감촉.

그러나 은백색 창날에 점점이 흩뿌려져 있는 누군가의 핏물은 여전히 뜨거웠고, 그리 멀지 않은 곳에서 터져 나온 비명은 처절했다.

“아아아악!”

지금처럼 시야가 가려진 전장에서 소리만큼 완벽한 좌표가 있을까.

사라리지 않은 광휘 너머에서 울려 퍼지는 날카로운 비명을 따라, 나는 크게 한 걸음을 내디뎠다.

파앙!

쏘아지는 발끝을 따라 압축된 공기가 폭발한다.

눈앞을 겹겹이 가로막고 있던 광휘가 부서지고, 삼 장에 달하던 거리가 단숨에 지워졌다.

그리고…….

쏴아아악!

비스듬히 내리긋는 창날의 궤적 끝에, 내게 판돈을 돌려줘야 할 누군가가 있었다.

보이지 않아도 선명하게 느껴지는 그곳. 그 순간에.

팟, 서걱!

서늘한 절삭음과 함께 검붉은 핏물이 튀었다.

하지만 조금 전까지만 하더라도 한 사람이 고통에 찬 비명을 내지르던 그 자리에는 이미 아무것도 존재하지 않았다.

‘빠르다.’

아니, 단순히 빠르다는 말로는 이 움직임을 완전히 표현할 수 없다.

만약 무림인 중 누군가 이 보았다면, 초절정 고수나 되어야 펼칠 수 있는 이형환위(移形換位)를 입에 담았을 광경.

그러나 이 세상의 모든 사람이 그렇게 생각할지라도, 오직 나만큼은 예외였다.

‘블링크(Blink)……!’

말 그대로 찰나의 깜빡임과 같이 사라지는, 순간 이동 마법.

대마도사가 펼친다면 이형환위보다도 쾌속하게 발현되는 엄청난 회피 능력이지만, 그것이 전부였다.

‘좌측으로부터 세 걸음. 다섯 장.’

나는 블링크 마법의 한계를 천하의 누구보다 잘 알고 있는 사람인 동시에.

콰드득.

단거리라는 한계를 지닌 블링크를 따라잡을 수 있는, 한계 이상의 신체 능력과 감각을 지닌 초인이었으니까.

쾅!

단 한 걸음.

순식간에 지워진 그 공간 속, 나는 눈을 부릅뜬 채 굳어 버린 대마도사를 향해 활짝 웃어 보였다.

“또 보네?”

쐐애액!
```

## Final English reading copy

```markdown
# Chapter 1051

“You…”

The moment the Grand Mage saw a smile spread across Jin Taekyung’s face, which had been turning deathly pale, she instinctively realized how foolish a mistake she’d made.

*Shit.*

It was an irreparable blunder.

She’d loosened the binding spell without thinking, in response to the unmistakable sincerity of his *Go ahead and kill me if you can.*

And through that split-second mistake, Jin Taekyung had immediately seen the Grand Mage’s true intentions.

“What? Can’t do it, you crazy bitch?”

“……!”

The Grand Mage bit her lip. He’d hit the mark.

What he said was true.

A hunting dog could only cut its target’s throat when its master gave permission.

But she didn’t yet have that authority, and her earlier bluster about the laws of nature had already been exposed.

Of course, even so—

*Nothing changes. Nothing at all.*

The Grand Mage thought to herself, then poured her strength back into the Magic that had briefly faltered.

Crack!

As if nothing had happened, the thick, sturdy vines squeezed Jin Taekyung’s neck even tighter.

The overwhelming difference in power, now laid bare, was impossible to bridge.

Unlike him, with barely a trace of internal energy left, a tremendous force still lay coiled deep within the Grand Mage’s body.

And that wasn’t all.

Now that Jin Taekyung was her hostage, even the two giants—the Fire King and the Bow Saint—couldn’t dare act recklessly.

All she had left to do was make the young brat before her submit.

That was what the Grand Mage had been certain of.

Until she saw the smile on Jin Taekyung’s face, brighter than ever.

*…He’s smiling?*

She couldn’t understand what that smile meant.

No—more precisely, she instinctively guessed its meaning, but couldn’t accept it rationally.

There was only one variable Jin Taekyung could create in a situation where he’d been so completely subdued.

And there wasn’t a single lunatic in the world who’d choose a variable as insane as suicide.

But—

Crack!

There was one.

That lunatic.

Right here.

Before her very eyes.

*Splatter!*

In that instant, the Grand Mage’s eyes opened wide without her meaning to.

Everything was red.

And at the same time, she saw him.

Through the blood sliding stickily over her white veil, Jin Taekyung trembled all over and spat up blood.

“Th-This…”

The stunned gasp slipped between her red lips.

There was no doubt. He’d severed his own heart meridians.

Even a massive old tree, one that wouldn’t easily fall to a lumberjack’s axe, couldn’t withstand a colony of ants boring through its bark and into its core.

That was why, for a Murim martial artist, severing the heart meridians meant death.

A swift death, and an agonizing one.

*Why would he go this far?*

Frozen for an instant, the Grand Mage stared at Jin Taekyung in utter shock.

The truth she’d told him had been only half the truth.

A tiny truth, nowhere near enough to give him certainty—just enough to make him vaguely suspect something.

And yet, when he’d realized that his mere existence might threaten someone, how many people under heaven would give up their lives without hesitation?

None. Without question.

The strongest desire granted to a human being was the desire to live. Even if someone made this choice, it would take countless doubts and resolve to carry it out.

But Jin Taekyung had done it.

Without the slightest hesitation or fear.

Even smiling brightly as he did.

In his eyes, already dimming rapidly, lay absolute certainty. Not the slightest wavering.

The certainty that he’d chosen the right path.

And seeing Jin Taekyung like that, the Grand Mage finally realized what her most fatal mistake had been.

*The Chosen One.*

Having had her thoughts read earlier was nothing.

She should have understood what those five syllables meant. She should have guessed.

Why her great master had searched so desperately for the young man before her.

Why he’d ordered his loyal servants to watch his every move.

Jin Taekyung was that kind of person.

He could curse up a storm and still understand human decency. He could spit in someone’s face and still pursue the chivalrous path. He might walk along the edge of the road, but he’d never stray from the right one.

A chivalrous hero who led the way before everyone—and a lunatic beyond anyone’s imagination.

That was why he was the Chosen One.

Crack!

The Grand Mage clenched her teeth.

There was no more time to hesitate, no choice left to make.

Her master had already waited far too long. If Jin Taekyung died here today, he would have to wait once more, with no end in sight.

*I have to save him. Whatever it takes!*

As time seemed to slow, the Grand Mage reached out, more desperate and frantic than ever.

Swoooooosh!

An immense force surged up around her slender frame.

Not with the will to kill, but the will to save. The force surrounding her heart pulsed fiercely.

The power lying dormant in the air resonated with it, then burst into light, devouring everything around them.

*Fwoom!*

The swelling radiance swept over the hill.

No—it spread until it covered the entire hill.

Its dazzling brilliance bleached the eyes of the Bow Saint and Jeok Cheongang as they raced toward them, having realized something had happened to Jin Taekyung, who was being held hostage. It forced the eyes shut of the fiend, still writhing like an insect as he clung to life.

Even the Grand Mage herself, who had summoned that radiance.

*What happened?*

With her vision suddenly fading, the Grand Mage bit her lip.

When a pile of rocks collapses, it kicks up dust. But when Taishan crumbles, it causes an earthquake.

A Supreme Peak master who had severed his own heart meridians had suffered an injury that not even a Great Firmament Immortal could heal.

She’d unleashed the greatest healing power she could, but there was nothing she could guarantee. And the radiance that had erupted more fiercely than ever showed no sign of fading.

No—at that very moment, it seemed to flash even brighter.

Like a blade shining all the more beneath the sun.

“……!”

Just as the Grand Mage’s eyes widened when she realized something—

*Shwaaak!*

A chillingly low, razor-sharp whistle tore through the air. A silver-white spearhead, worthy of being called the White Flame, ripped through space.

And beyond the still-dazzling radiance came someone’s quiet voice.

“Got you.”

*Thud!*

* * *

My stomach’s churning.

My head’s spinning, and my vision is blurry.

Maybe that’s why.

Honestly, I still don’t know.

Is this moment a dream or reality?

If it’s neither…

*Hell? Or heaven?*

I couldn’t think of anything else.

Everything around me was so white I couldn’t even open my eyes properly.

Unless some enterprising Yama had gone and installed ridiculously powerful LED bulbs throughout hell to improve conditions for its prisoners, this had to be heaven.

But—

Ding. Ding. Diiiing!

The clear chimes ringing in my ears, like an echo returning from far away, were enough to tell me.

This was reality. I was alive.

And I’d won again in this insane gamble, where I’d staked my life.

> **System**
>
> Status Effect: Terrible Internal Injury has been removed!
>
> Status Effect: Severe Bleeding has been removed!
>
> Status Effect: Exhaustion has been removed!
>
> Status Effect: Ruptured Organs has been removed!
>
> Status Effect: Fracture has been removed…
>
> .
>
> .
>
> .
>
> A powerful healing force takes root in your body!
>
> You’ve earned the somehow-you-managed-it achievement: Go Ahead, Gut Me!

Translucent holographic windows floated one after another in midair.

Along with them, my blurry vision cleared as if it had never been blurred. My breathing steadied, and my senses sharpened, letting me feel and take in everything within a dozen or so *jang*.

Light. Air. Wind. Even things without physical form, like the thick stench of blood.

And the beings breathing among all of it, with the same vitality as me.

Now it was time to collect my winnings from the other side of the bet.

*Come.*

I whispered inwardly and sent out my will.

Toward the cold blade that held not a trace of life, yet had extinguished countless lives.

Toward my beloved weapon, which had left my grasp and lay alone on the ground, far away.

*Shwaaak!*

It all happened almost at once, and I murmured,

“Got you.”

At that moment—

*Thud!*

With the sound of bone and flesh bursting, the thick vines that had bound my entire body loosened.

*Now.*

I didn’t even need to pour in internal energy.

I simply put an immense force—one that the word *superhuman* couldn’t begin to describe—into my limbs and let it loose.

*Crack!*

The vines split, then burst apart.

Unable to withstand that hideous force, they snapped into pieces. At the same time, I broke free and reached out toward the White Flame, which was shooting my way like a streak of light.

Tap.

That cool sensation was more familiar than anything.

But the blood scattered across the silver-white spearhead was still warm, and the scream that burst out not far away was desperate.

“Aaaah!”

Could anything make a more perfect landmark than a sound on a battlefield where your vision was blocked like this?

Following the sharp scream ringing beyond the still-unfaded radiance, I took a long step forward.

*Bang!*

Compressed air exploded beneath my thrusting foot.

The radiance layered across my vision shattered, and the distance of three *jang* vanished in an instant.

And then…

*Shaaak!*

At the end of the spear’s slashing arc, there was someone who owed me my stake.

I couldn’t see her, but I could feel her clearly. In that instant—

*Fwoom!*

Dark red blood sprayed with a cold slicing sound.

But the person who’d screamed in pain only moments ago was no longer there.

*Fast.*

No—*fast* didn’t begin to describe the movement.

If any Murim martial artist had seen it, they’d have called it Shifting Form and Position, a technique only a Supreme Peak master could use.

But no matter what anyone else in this world thought, I was the one exception.

*Blink…!*

A Magic spell that made you disappear in an instant, like the literal blink of an eye—a short-range teleport.

In the hands of a Grand Mage, it was an incredible evasion ability, faster than Shifting Form and Position. But that was all.

*Three steps from my left. Five *jang*.*

I was the person who knew the limits of Blink better than anyone in the world.

*Crack.*

And I was a superhuman whose extraordinary strength and senses could catch up with Blink despite its limited range.

*Boom!*

One step.

In the space that vanished in an instant, I smiled brightly at the Grand Mage, frozen with her eyes wide open.

“See you again?”

*Shing!*
```
