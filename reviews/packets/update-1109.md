<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1109.txt",
      "sha256": "fa0bc2076f1df006085c856248dceca8c5d77c3da4733f6fee88be4549c9bdda",
      "bytes": 13394
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f1baf29e5b7317708a0be28563d326ae3505e4a3131cdad5180cceeafbb9d1a8",
      "bytes": 1399
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bf6c4f7b66402118726cc38b45f04e6573af5660df71d2d9f176747ba040720c",
      "bytes": 244327
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "3f236ffec991234d01484ccd4eb9d0ab44b32188b4ca5e018c609f6ea96d0b6a",
      "bytes": 941
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "63a0b7df8435a0231a9ea87052b92a8e2e85e2dbaf9d0201d92c8e18b1a07a74",
      "bytes": 1230
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f21726386d11e1eaf36781f76cd3ac9ebe057b28bd18c480a7ddcd60c73e8dd4",
      "bytes": 760
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "35bb669a6cdfb5880de1534f5f80411e45ad7a08879ea3fd130adf094bfb5c22",
      "bytes": 700
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c2ac98e48e5f68b006574f759ab9253d5e11835051f253bfdc3017c07160232e",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2c159721e5d9931d2f4080da1967bae50c7bc8bd39fbfe003a24d22f9cd60316",
      "bytes": 623
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "7c56af5d2038816391227ef68e6d31305e70c5bc470500ac1c44fc94d49b77f0",
      "bytes": 700
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "8a20c30b9c82e31cfe0b48bc08fb6b8ce6d893e92f2c1afe2b41d4da4499ba21",
      "bytes": 1084
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3587b35f9f46255635c2b9217320b6613dd49879b3cf950be82def2526ffc095",
      "bytes": 288328
    }
  ],
  "estimated_tokens": 11874
}
-->

# Durable State Update — Chapter 1109

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
1 and safe_through 1109. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1109. Profile updates may replace only one
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
  "chapter": 1109,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1109,
    "continuity_sources": [1109],
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
    "Jin Taekyung collapsed after unleashing One Annihilation; the System gave no confirmation that the enemy died.",
    "Cheongpung survived the blast and struck the Black Ghost during Taekyung’s attack.",
    "The Blood Lord survived the flames but awoke without his memories or senses and is driven to drink blood.",
    "The Blood Lord began feeding on one of his subordinates.",
    "Jeok Cheongang remained at the North Gate to face the Potala Palace forces as of chapter 1105."
  ],
  "continuity_sources": [
    1107,
    1108
  ],
  "open_questions": [
    "What condition is Jin Taekyung in after collapsing, and what happened to the Black Ghost?",
    "Will the Blood Lord regain his memories, and what will become of him and the subordinate he attacked?",
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Who are the allies approaching by river from the east?",
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?"
  ],
  "safe_through": 1108,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 곤륜파    | **Kunlun Sect**                  |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 검법     | **sword technique**                              |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 일격     | **One Strike**                         |
| 화산     | **Huashan**            |
| 곤륜     | **Kunlun**             |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 매화삼십육검 | **Thirty-Six Plum Blossom Swords** | Huashan sword technique used by Cheongpung. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 창룡후 | **azure dragon's roar** | Battle cry released by Tang Jinhu. |
| 창룡 | **Azure Dragon** | Divine dragon form invoked in Hyeongong's blessing. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 서문 | **West Gate** | One of the Nanman Beast Palace's gates. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 초일류 | **Supreme First Rate** | Realm attained by each Baekcheon Unit member. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 정호군 | 진태경 | imperial officer responding to the Marquis of Shangshan | Marquis of Shangshan | formal and deferential | Accepts the command with a formal acknowledgment of Taekyung’s title. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1108
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and learns from past mistakes; his confidence in his overwhelming power is genuine rather than bluster, and he remains devoted to the Lord of Heaven despite resenting being treated as disposable and Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven but suspects the Lord wants Jin Taekyung above all else; despite that, he attacks Taekyung, whom he considers a formidable adversary, as well as Cheongpung.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1108
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1108
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1081
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1108
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1108
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1081
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1096
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

## Korean source

```text
＃1109화



맹렬한 화염이 공간을 휩쓴 그 순간, 적아(敵我)를 떠나 혈주의 죽음을 떠올리지 않았던 이는 없었다.

그만큼 거대한 기운이 담긴 일격이었으니까.

제아무리 불사에 가까운 회복력을 지닌 혈주라 할지라도, 지옥 불과 같은 저 끔찍한 열기 속에서 살아남는다는 것은 불가능해 보였으니까.

하지만 단 한 사람.

자신의 생명마저 장작으로 삼아 화염을 불러일으킨 진태경 만큼은 예외였다.

철퍽.

힘없이 꿇려진 무릎이 피 웅덩이에 처박히고, 죽음의 문턱에서 가까스로 멈춰선 괴물의 그림자가 흩날리는 잿가루 너머에서 일어난 그때였다.

어느새 새하얗게 질린 진태경의 입술 사이로, 온 힘을 다해 쥐어 짜낸 외마디 고함이 터져 나온 것은.

“쳐라-!”

사방을 떨어 울리는 창룡후(蒼龍吼)가 찰나의 정적을, 멈춰있던 시간을 움직인다.

그리고 이에 가장 먼저 반응한 것은, 일섬의 여파에 휩쓸려 저 멀리 튕겨 나가고 있던 또 하나의 신룡(神龍)이었다.

“……!”

일순간 부릅떠진 두 눈동자.

요동치는 청풍의 동공에서, 흑귀의 목을 벤 직후 떠올랐던 전율과 희열은 이제 어디에서도 찾아볼 수 없었다.

다만 아득한 경악과 의문만이 몰려와 빈자리를 채우고 있을 뿐.

‘도대체 어떻게……!’

믿을 수 없는 현실.

그러나 동시에, 받아들일 수밖에 없는 현실을 마주한 청풍은 이를 악물며 신형을 뒤집었다.

쉬릭.

휘몰아치는 바람을 거스르며 회전하는 몸. 그와 함께 내뻗은 발끝이 텅 빈 허공을 밟았다.

아니, 터트렸다.

퍼엉!

압축된 공기가 폭발한다.

이십여 장에 달하던 거리가 순식간에 좁혀지고, 비틀거리는 괴물의 모습이 성큼 다가왔다.

‘죽인다. 반드시!’

머릿속이 얼음장처럼 차갑다.

청풍의 본능이 비명을 지르고 있었다.

지금이 아니면 저 끔찍한 괴물을 막을 수 없다고.

본래의 힘을 되찾기 전에, 무슨 수를 써서라도 놈을 쓰러트려야 한다고.

하지만 바람을 가르며 내리그어진 청풍의 검을 기다리고 있던 것은, 광신도(狂信徒)라 불리는 또 다른 이름의 괴물들이었다.

“막아라!”

“천상천하, 만마……!”

쉬쉬쉬쉭, 서걱!

검신을 타고 흘러나온 자줏빛 강기가 망설임 없이 적의 살과 뼈를 가른다.

매화삼십육검(梅花三十六劍).

화산파가 자랑하는 최고의 절기가 공간을 뒤덮고, 검신이 그리는 궤적을 따라 흐드러지게 피어난 자하신공의 강기는 꽃잎처럼 흩날렸다.

아름답고도, 처연하게.

더불어, 그 무엇보다 처절하게.

퍼걱, 푸화아악!

베고, 베고, 또 베었다.

쓰러지고, 쓰러지고, 또 쓰러진다.

그러나.

‘물러서지…… 않아.’

청풍의 안색이 창백하게 질렸다.

어느덧 온 사방이 붉게 물들었다.

쉴 새 없이 터져 나오는 핏물은 검법에 담긴 향을 지우고 자줏빛 강기를 가린지 오래다.

그뿐인가.

뒤이어 가세한 수비군이 필사의 각오로 병장기를 휘두르고 있었지만, 그럼에도 광신도들이 세운 인(人)의 장벽은 허물어지지 않았다.

살아 있는 인간이라면 모두가 두려워 마지않는 죽음이, 그들에게는 거룩한 순교(殉敎)였으므로.

“위대하신 천주의 권능이 이 땅에 임하셨으니, 목숨 바쳐 그분의 사도를 지키리라!”

“천주시여, 우리를 이끄소서!”

혈주의 생존을 목격한 광신도들의 사기는 그 어느 때보다 높았다.

아니, 이제는 광기를 넘어선 그 이상이었다.

누군가에게는 기이하고도 끔찍한 재앙이었으나, 광신도들에게는 자신들의 믿음이 옳았음을 증명하는 이적(異蹟)이나 다름없었으니까.

그리고 그 미친 광기와 죽음의 소용돌이 속에서, 청풍은 똑똑히 볼 수 있었다.

사방에서 쏟아지는 적과 아군의 핏물을 흡수해 가며, 코앞까지 닥쳤던 죽음에서 서서히 멀어져 가는 어느 괴물의 모습을.

스륵.

가장 먼저 새카맣게 타들어 간 몸뚱어리에서 새로운 살이 돋아나기 시작했고.

으드득.

녹아내린 뼈와 근육이 재생되었으며.

툭. 투둑.

위아래로 눌러 붙어 있던 입술이 떨어져 나가며 날카롭고도 새하얀 이빨이 드러났다.

피처럼 붉은색을 지닌, 터무니없는 갈증으로 인해 날름거리는 기다란 혀도 함께.

“……더. 더 줘.”

메마른 괴물의 입술 사이로 쇳소리 같은 목소리가 흘러나온 순간, 청풍은 전신의 피가 차갑게 식는 것을 느꼈다.

‘벌써?’

그것은 말로는 표현할 수 없을 만큼 기괴한 장면인 동시에, 너무나도 빠른 회복이었다.

그를 포함한 아군 모두가 예상했던 범주를 아득히 벗어날 정도로.

어쩌면 지금 당장이라도 뒤로 물러나, 놈의 회복을 잠시라도 늦추는 것이 낫지 않을까 싶을 정도로.

하지만 그 찰나의 순간에도, 이지를 상실한 괴물은 놀라운 속도로 본연의 힘을 되찾아가고 있었다.

“더-!”

다음 순간, 불현듯 터져 나온 혈주의 외침을 들은 청풍의 등골이 찌르르 울렸다.

훨씬 더 또렷하고 선명해진 음성 때문에?

틀렸다.

조금 전까지만 해도 느낄 수 없었던, 저 외침에 담긴 웅혼한 공력 때문이었다.

‘안 돼!’

마음속에서 울려 퍼지는 비명과 함께, 청풍은 온 힘을 다해 검을 뻗었다.

쉬쉬쉬쉭!

어느 때보다 강렬한 빛을 머금은 강기가 공간을 난도질한다.

여덟 글자의 교언을 쉴 새 없이 뇌까리며 앞을 가로막은 광신도들의 육신이 조각나며 흩어졌다.

오직 일점(一點)을 노린 돌파.

그런 청풍의 뒤를 따라, 어느새 합류한 정호군과 휘하의 금의위들이 들이닥쳤다.

“역도들을 쓸어 버려라!”

“황제 폐하 만세!”

최소 초일류에서 절정으로 이루어진, 명실상부한 대국 제일의 최정예.

비록 천자가 하사한 황금빛 갑옷도, 투구도 버렸으나 그 눈부신 긍지와 맹세는 빛났고 그들의 검 끝은 오직 한 방향을 향해 나아가고 있었다.

바로, 혈주를 향해.

쐐애애액, 쾅!

굉음과 함께 짙은 피 보라가 휘몰아쳤다.

그리고 넘을 수 없는 철벽처럼 느껴졌던, 수많은 광신도들의 틈새로 미세한 균열이 생기기 시작했다.

서걱, 푸푸푹!

제아무리 잠력단을 복용했다 한들, 무학에 대한 깨달음의 간극은 좁힐 수 없는 법.

청풍이 휘두르는 검신을 타고 화산파가 자랑하는 수십 개의 절기가 쏟아지고, 정호군을 필두로 한 금의위들이 송곳처럼 광신도들의 전열을 파고들었다.

또 다른 적이 그 빈틈을 메우기 전에.

한 걸음이라도 더, 한순간이라도 빨리 혈주에게 다가갈 수 있도록.

‘이대로라면, 할 수 있다.’

아니, 해내야 했다.

비단 청풍만의 생각이 아니었다.

모두가 그렇게 생각했고, 죽음을 각오했다.

가슴에 칼이 박히고도 마지막 힘을 다해 광신도를 끌어안은 곤륜파의 도사도.

그런 그의 뒤에서 눈을 질끈 감고 창을 찌르는 어느 이름 모를 어린 병사도.

갈라진 뱃가죽에서 쏟아지려는 내장을 억지로 틀어막으며, 갑옷보다 빛나는 긍지로 무장한 채 나아가는 중년의 금의위도.

그들 모두는 본능적으로 직감하고 있었다.

진태경이 만들어 준 지금의 기회를 놓친다면, 두 번 다시 저 괴물을 쓰러트릴 수 없을지도 모른다는 것을.

이대로 서문이 무너진다면, 자신들뿐만이 아니라 내성(內城)에 대피해 있는 수십 여만의 백성들 역시 몰살당하리라는 것을.

그리고 그 굳건하고도 처절한 결사(決死)의 각오가, 그들의 등 뒤에 무릎 꿇은 누군가의 창처럼 광신(狂信)의 벽을 향해 쏘아졌다.

“지금-!”

청풍의 외마디 고함과 함께, 적진 깊숙이 파고든 아군 모두가 온 힘을 쥐어 짜내어 신형을 내뻗었다.

어쩌면 마지막이 될지도 모르는, 하지만 누구도 후회하지 않을 목숨을 건 돌격을.

콰드드드득!

피 분수가 솟구쳤다.

곳곳에서 고통에 찬 비명이 흘러넘치고, 아군과 적의 시체가 뒤엉켜 허물어졌다.

그러나 그것으로 충분했다.

아직도 그들의 사방에는 수많은 광신도가 도사리고 있었으나, 지금 이 순간 청풍의 목적은 오직 한 존재뿐이었으니까.

까득. 까드득.

알 수 없는, 알고 싶지도 않은 무언가를 씹고 있던 괴물이 문득 고개를 돌려 청풍을 바라보았다.

인간처럼 두 팔과 두 다리를 가졌으되, 더는 인간이라 부를 수 없는 붉은 손에는 목이 사라진 시체 한 구가 들려 있었다.

아니, 괴물의 발치에는 이미 수십여 구의 시신이 널려 있었다.

마치 목내이(木乃伊)처럼 바짝 메마른, 광신도들의 시신이.

“넌, 누구지?”

진심으로 궁금하다는 듯한 표정과 말투.

기억하지 못하는 이유는 모르겠으나, 한 가지는 확실했다.

‘아직, 아직 완전히 회복하지 못했다.’

핏빛 동공에 비치는 자신의 모습을 응시하며, 청풍은 씹어뱉듯이 대답했다.

그 어느 때보다 적의 어린 목소리로.

“너 따위가 들을 수 있는 이름이 아니야.”

그리고 그 순간.

팟.

소리를 앞질러간 청풍의 손끝을 따라, 자줏빛 섬광이 터져 나왔다.

서걱!

살갗이 갈라지고, 피가 튀었다.

어리둥절한 표정으로 청풍을 바라보던 혈주가, 깊게 베인 가슴의 상흔을 발견하고 눈을 깜빡였다.

“아, 아아?”

고통과 함께 잊고 있던 기억이 서서히 수면 위로 떠오르기 시작한다.

분노라는 감정과 함께.

“너…….”

홀린 듯이 내뻗은 손.

하지만 그가 기억을 되찾기도 전에, 청풍의 신형은 거침없이 움직이고 있었다.

서걱, 서걱, 서걱!

실로 빛살과도 같은 속도. 그들의 신형이 뒤얽히고 교차할 때마다 핏물이 뿜어졌다.

정확히는, 혈주의 피가.

투두두둑.

지면에 흩뿌려지는 자신의 핏물을 바라본 혈주는 눈을 부릅 떴다.

“……안 돼.”

고통 때문이 아니다.

갈증.

피를 흘리면 흘릴수록, 잠시나마 해소되었던 지독한 갈증이 다시금 그를 옥죄고 있었다.

쉬쉬쉬쉭!

폭풍과도 같은 검격이 쏟아지는 와중에도, 혈주는 점점 더 강해지는 갈증을 느끼며 주위를 둘러보았다.

‘필요해. 피가. 더 필요해.’

하지만 그런 간절한 마음과 달리, 마지막 힘까지 쥐어 짜내고 있는 청풍의 공격은 이 갈증을 채울 시간을 주지 않았다.

퍼걱! 콰드득!

계속되는 전투에 사방에 피가 흘러넘치고 있었지만, 그 정도로는 턱없이 부족했다.

전신에 하나둘씩 아로새겨지는 크고 작은 상처를 메우는 것이 고작이었으니까.

다만, 잠시 잊고 있던 또 다른 사실을 깨달았을 뿐이었다.

지금의 그에게는 아주 중요한, 이 갈증을 채워 줄 또 다른 존재들을.

‘그래, 그랬었지.’

혈주는 기쁨을 참지 못하고 히죽 웃었다.

그리고 기대에 찬 목소리로, 하늘을 향해 부르짖으며 두 손을 뻗었다.

“오너라, 어서!”

그 순간.

쉭!

청풍이 쏘아 보낸 자줏빛 강기가, 찰나에 멈춰선 그의 팔을 스쳤다.

아니, 베었다.

서걱!

높이 솟구치는 양팔. 동시에 치밀어오르는 격통과 갈증.

하지만 간신히 회복한 두 팔을 잃었음에도, 혈주의 입가에 맺힌 웃음은 사라지지 않았다.

그는 알고 있었다.

지금 이 순간 머리 위로 세차게 쏟아지던 빗줄기마저 가로막은, 이미 어두웠던 하늘을 완전한 칠흑색으로 물들이며 내리꽂히는 저 무수한 그림자들이 자신의 갈증을 채워 주리라는 것을.

- 키이이잇!

불현듯 허공에서 울려 퍼진 소름 끼치는 소리를 따라, 본능적으로 고개를 든 청풍은 볼 수 있었다.

아니. 모두가 똑똑히 보았다.

헤아릴 수조차 없을 만큼 수많은 날짐승들이, 핏빛 눈동자를 번뜩이며 전장을 향해 내리꽂히는 그 믿을 수 없는 광경을.

그리고 그 모든 것의 중심이자 끝에, 한 존재가 있음을.

파드드드득!

막을 수도, 피할 수도 없는 마물(魔物)의 파도.

공간을 뒤덮으며 쏟아져 내린 그 거대한 날갯짓 소리 너머로, 마침내 모든 힘과 기억을 되찾은 괴물의 목소리가 청풍의 귓가를 파고들었다.

“기억났다. 네 이름.”

“……!”

“검성 매종학, 그놈에게 진 빚도.”

그 순간.

콰드드득!

살과 뼈를 찢는 끔찍한 파열음과 함께, 끈적한 핏물이 청풍의 시야를 붉게 물들였다.
```

## Final English reading copy

```markdown
# Chapter 1109

The moment fierce flames swept through the area, there wasn’t a single person—ally or enemy—who hadn’t thought the Blood Lord was dead.

That was how much power the strike had contained.

Even with the Blood Lord’s near-immortal regenerative ability, surviving that dreadful, hellish heat had seemed impossible.

But there was one exception.

Jin Taekyung, who had summoned those flames by using even his own life as kindling.

*Splash.*

His knees crumpled into a pool of blood. Beyond the drifting ashes, the monster who had stopped just short of death began to rise.

And then, between Jin Taekyung’s lips, now pale as snow, burst a single shout, squeezed out with every ounce of strength he had left.

“Attack!”

The Azure Dragon’s Roar shook the world around them, breaking the momentary silence and setting time in motion again.

The first to respond was another Divine Dragon, still hurtling far away, swept up in the aftermath of One Annihilation.

“……!”

Cheongpung’s eyes flew open.

The thrill and elation that had filled his pupils just after he cut off the Black Ghost’s head were nowhere to be found.

Only overwhelming shock and confusion rushed in to fill their place.

*How is this even possible……!*

It was a reality he couldn’t believe.

But it was also one he had no choice but to accept. Gritting his teeth, Cheongpung twisted around.

*Whoosh.*

His body spun against the howling wind. As he did, the tip of his foot struck the empty air.

No—it burst through it.

*Boom!*

Compressed air exploded.

The distance of more than twenty jang closed in an instant, and the staggering monster loomed suddenly closer.

*I’ll kill him. No matter what!*

Cheongpung’s mind was cold as ice.

His instincts were screaming.

If he didn’t stop that terrible monster now, he might never get another chance.

He had to bring the creature down by any means necessary, before it recovered its original strength.

But what awaited Cheongpung’s descending sword as it cut through the wind was another group of monsters, known by a different name: fanatics.

“Stop him!”

“Heaven above and earth below; all demons—!”

*Sh-sh-sh-shhk! Slice!*

Purple Force flowed along the sword and cut through flesh and bone without hesitation.

Thirty-Six Plum Blossom Swords.

Huashan’s proudest technique filled the space. Along the path traced by his blade, the Force of the Zaha Divine Technique blossomed and scattered like petals.

Beautiful, and yet tragic.

And more than anything, utterly brutal.

*Thud! Fwoosh!*

He cut, and cut, and cut again.

They fell, and fell, and fell again.

But—

*They’re not backing down……*

Cheongpung’s face turned deathly pale.

Before long, everything around him was stained red.

Blood poured out without pause, washing away the fragrance of his sword technique and obscuring the purple Force.

And that wasn’t all.

The defenders who had joined the fight were swinging their weapons with the resolve to die, but even so, the wall of fanatics held firm.

To them, death—the thing every living person feared—was a sacred martyrdom.

“The great Lord of Heaven’s power has descended upon this land! We will give our lives to protect His Apostle!”

“Lord of Heaven, lead us!”

The fanatics’ spirits had never been higher than after witnessing the Blood Lord survive.

No—now it was something beyond madness.

To some, it was a strange and terrible calamity. But to the fanatics, it was a miracle proving their faith had been right all along.

And amid that whirlpool of madness and death, Cheongpung saw it clearly.

A monster slowly retreating from the jaws of death, absorbing the blood of friend and foe pouring in from every direction.

*Rustle.*

First, new flesh began growing from the body that had been charred black.

*Crack.*

Melted bone and muscle regenerated.

*Plop. Plop.*

Lips that had stuck together came apart, revealing sharp, white teeth.

Along with a long, blood-red tongue that flicked hungrily, driven by an unbearable thirst.

“……More. Give me more.”

The moment a voice like scraping metal slipped from the monster’s parched lips, Cheongpung felt the blood in his whole body turn cold.

*Already?*

It was a sight too bizarre to describe—and a recovery far too fast.

It was well beyond what he and the other allies had expected.

So much so that he wondered if they should retreat right now, even if only to delay the monster’s recovery for a little while.

But even in that fleeting moment, the mindless monster was regaining its original strength at an astonishing rate.

“More!”

The Blood Lord’s sudden cry sent a shiver down Cheongpung’s spine.

Was it because his voice had become much clearer and sharper?

No.

It was the majestic internal energy carried in that cry—something Cheongpung hadn’t been able to feel just moments ago.

*No!*

As a scream rang out in his heart, Cheongpung thrust his sword forward with all his strength.

*Sh-sh-sh-shhk!*

Force brighter and more powerful than ever tore through the space.

The fanatics blocking his way, endlessly chanting their eight-character incantation, were cut to pieces and scattered.

A breakthrough aimed at a single point.

Following close behind Cheongpung came Jeong Hogun and the Embroidered Uniform Guards under his command, who had joined the fight.

“Wipe out the rebels!”

“Long live His Majesty the Emperor!”

They were the Great Nation’s finest troops in name and reality, their ranks made up of martial artists from at least Supreme First Rate to Peak.

They had cast aside the golden armor and helmets bestowed by the Son of Heaven, but their dazzling pride and vows still shone. Their sword points were all aimed in one direction.

At the Blood Lord.

*Fwoooosh! Boom!*

A deafening crash sent a thick spray of blood surging through the air.

And a tiny crack began to form in the ranks of the countless fanatics, which had seemed like an unbreakable iron wall.

*Slice! Thud-thud-thud!*

Even with Temporary Strength Pills, they could not close the gap in martial enlightenment.

Dozens of Huashan’s finest techniques poured from Cheongpung’s blade, while the Embroidered Uniform Guards, led by Jeong Hogun, drove into the fanatics’ formation like an awl.

Before another enemy could fill the gap.

So they could get one step closer, one moment sooner, to the Blood Lord.

*If this keeps up, we can do it.*

No—they had to do it.

It wasn’t only Cheongpung who thought so.

They all thought so, and they were all prepared to die.

The Kunlun Sect Daoist who, even with a sword buried in his chest, used his last strength to grab hold of a fanatic.

The young, nameless soldier behind him, squeezing his eyes shut as he thrust his spear.

The middle-aged Embroidered Uniform Guard, pressing his spilling entrails back into his split abdomen as he advanced, clad in a pride brighter than his armor.

Every one of them instinctively knew.

If they let this chance Jin Taekyung had created slip away, they might never be able to bring that monster down.

If the West Gate fell, not only would they be slaughtered—the hundreds of thousands of people sheltering in the Inner City would be massacred, too.

Their unshakable, desperate resolve shot toward the wall of fanaticism like the spear of someone kneeling behind them.

“Now!”

At Cheongpung’s shout, every ally who had pushed deep into enemy lines squeezed out their remaining strength and lunged forward.

A life-or-death charge that might be their last—but one none of them would regret.

*Crack-crack-crack!*

Fountains of blood burst into the air.

Cries of pain spilled from every direction, and the bodies of allies and enemies alike tangled together as they crumpled.

But that was enough.

Countless fanatics still surrounded them, but at this moment, Cheongpung had only one target.

*Crunch. Crunch.*

The monster, chewing on something unknown—something he didn’t want to know—suddenly turned its head to look at Cheongpung.

It had two arms and two legs like a human, but could no longer be called human. In its red hand was a corpse with no head.

No—dozens of bodies already lay at the monster’s feet.

The fanatics’ corpses, dried up like mummies.

“Who are you?”

His expression and tone made it seem as though he truly wanted to know.

Cheongpung didn’t know why the monster couldn’t remember him, but one thing was certain.

*He still hasn’t fully recovered.*

Watching his reflection in those blood-red pupils, Cheongpung spat out his answer.

His voice held more hostility than ever.

“You don’t deserve to hear my name.”

And at that moment—

*Flash.*

Purple light burst from Cheongpung’s fingertips, which moved faster than sound.

*Slice!*

Skin split, and blood flew.

The Blood Lord stared at Cheongpung in bewilderment, then blinked as he noticed the deep gash across his chest.

“Ah, ah……?”

Along with the pain, forgotten memories began to rise slowly to the surface.

And with them came anger.

“You……”

His hand reached out as if he were entranced.

But before he could recover his memories, Cheongpung was already moving without hesitation.

*Slice, slice, slice!*

They moved at a speed like streaks of light, their bodies tangling and crossing. Each time they did, blood sprayed into the air.

More precisely, the Blood Lord’s blood.

*Drip-drip-drip.*

Watching his own blood spatter across the ground, the Blood Lord’s eyes widened.

“……No.”

It wasn’t the pain.

Thirst.

The more blood he lost, the more that terrible thirst—briefly quenched—tightened around him once again.

*Sh-sh-sh-shhk!*

Even as a storm of sword strikes rained down, the Blood Lord felt his thirst growing stronger and looked around.

*I need it. Blood. I need more.*

But despite that desperate desire, Cheongpung was squeezing out the last of his strength with every attack, giving him no time to quench his thirst.

*Thud! Crack!*

Blood was flowing everywhere as the battle went on, but it wasn’t nearly enough.

It could only patch up the large and small wounds appearing across his body, one after another.

But he had remembered something else he’d briefly forgotten.

Something very important to him—another source of blood that could quench his thirst.

*Right. That’s right.*

The Blood Lord grinned, unable to contain his joy.

Then he raised both hands toward the sky and cried out in an eager voice.

“Come! Hurry!”

At that instant—

*Whoosh!*

The purple Force Cheongpung had sent flying grazed the Blood Lord’s arm, frozen for a moment.

No—it cut through it.

*Slice!*

Both arms shot high into the air. At the same time, pain and thirst surged through him.

But even after losing the arms he had barely regenerated, the Blood Lord’s smile didn’t fade.

He knew.

The countless shadows plunging down toward him would quench his thirst. They blocked even the heavy rain pouring over his head at that moment, blotting out the already dark sky until it turned utterly black.

*Kiiieeet!*

At the bloodcurdling sound that suddenly rang out from the air, Cheongpung instinctively looked up.

And he saw.

No. Everyone saw it clearly.

Countless flying beasts—too many to count—plunged toward the battlefield, their blood-red eyes flashing.

And at the center, at the very end of them all, was one being.

*Flap-flap-flap!*

A wave of monsters that could neither be blocked nor avoided.

Beyond the thunder of countless wings beating as they poured down and covered the space, the voice of the monster who had finally regained all his strength and memories pierced Cheongpung’s ears.

“I remember your name.”

“……!”

“And the debt I owe that bastard, Mae Jonghak, the Sword Saint.”

At that moment—

*Crack-crack-crack!*

With a horrible sound of flesh and bone tearing, sticky blood painted Cheongpung’s vision red.
```
