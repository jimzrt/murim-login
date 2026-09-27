<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1113.txt",
      "sha256": "43e0d984079679238f424f3f570115d472773d43d0418534ee46eafb8b469766",
      "bytes": 12442
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bbb9aee318e8c9421bb3afd4ad7dea21414b909c81e9dec81b8549233676c7d1",
      "bytes": 1430
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b11a3900716c29bbb12566605a5b2b29b815bc855f6d7ff2496ddb57f4d9e13b",
      "bytes": 244401
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "bce7167050d07122571f9202108c8d57fb797008e92d82d1100c5bfb3935d5dc",
      "bytes": 915
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "145f19754c2960216a2abee4d02885ed3fa86cd2d168ef0168265695eba3c871",
      "bytes": 1230
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ddd5d7721e984c4b0b319b36e3a4741e690ad38c144b3495c3aed62605c2a86e",
      "bytes": 760
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "fc6ebaa60c6318161456fadb4228e41364a280970f985a6c8527ef16fd8bd651",
      "bytes": 738
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e5600cd7d9631fe2400320fb6baaf51bff9a7518943878730eea86b8134c4ddc",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1d3d06adc9be37aede8add53bb2583ba1ba65c0e38f9aeb7811bdaea4b391edc",
      "bytes": 623
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "5ce9c4f02c37fd2ed1c062f2a61d634d687a5d39ce4ec7c6b783300de8870ebf",
      "bytes": 700
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "81e3c508f36bdbbfec37f028da5e1c420204474ec94d34d895078f395893cbb1",
      "bytes": 288671
    }
  ],
  "estimated_tokens": 10792
}
-->

# Durable State Update — Chapter 1113

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
1 and safe_through 1113. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1113. Profile updates may replace only one
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
  "chapter": 1113,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1113,
    "continuity_sources": [1113],
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
    "Jin Taekyung and Cheongpung are badly injured in the Inner City; Taekyung may not survive.",
    "The Slaughter Saint remains at the South Gate to support its defense; the Bow Saint’s motives are unclear.",
    "Jeok Cheongang killed the Dalai Lama at the North Gate; Jeok is badly injured, and Perfected Being Hyeoncheon is alive but barely conscious.",
    "The Potala Palace’s vendetta against the Fire Gate Clan began with Songhak’s destruction of its forces more than two hundred years ago; the Dalai Lama allied with Dark Heaven to seek revenge.",
    "The Blood Lord is heading to the Inner City to kill Taekyung."
  ],
  "continuity_sources": [
    1111,
    1112
  ],
  "open_questions": [
    "Will Jin Taekyung survive his injuries, and can he receive treatment from the Divine Physician?",
    "What is the Bow Saint hiding, and why did she accept the possibility of Taekyung’s death?",
    "Can the South Gate hold against the Grand Mage and the four Black Ghosts?",
    "Will the Blood Lord reach Taekyung before he can be treated?"
  ],
  "safe_through": 1112,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 청풍     | **Cheongpung**     |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 생도     | **cadet**                                    |
| 은인     | **Benefactor**                               |
| 소협      | **Young Hero**                                                  |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 서문 | **West Gate** | One of the Nanman Beast Palace's gates. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 천호 | **Thousand Captain** | Rank held by Jeong Hogun in the Embroidered Uniform Guard. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 정호군 | 진태경 | imperial officer responding to the Marquis of Shangshan | Marquis of Shangshan | formal and deferential | Accepts the command with a formal acknowledgment of Taekyung’s title. |
| 천주 | 대술사 | master to servant | you | commanding and authoritative | Addresses her through mind-voice, ordering her to report, raise her head, and depart. |
| 대술사 | 천주 | servant to master | Lord of Heaven | extremely deferential | Uses reverent titles and self-abasing language while reporting and pleading. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1111
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and learns from past mistakes; his confidence in his overwhelming power is genuine rather than bluster, and he remains devoted to the Lord of Heaven despite resenting being treated as disposable and Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and suspects the Lord wants Jin Taekyung above all else; he recognizes Cheongpung and remembers a debt to Sword Saint Mae Jonghak.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1111
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1112
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1110
- **Aliases:** None
- **Role:** Jeong Hogun was a Thousand Captain of the Embroidered Uniform Guard and a skilled martial artist who led roughly three hundred surviving guards in a final charge against the Blood Lord.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1111
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1111
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1110
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

## Korean source

```text
＃1113화



희생 없이 얻을 수 있는 것은 아무것도 없다.

법도와 인의 따위는 개나 줘 버린 야만의 시대 속, 전쟁이라는 가장 끔찍한 폭력의 수단으로 승리를 쟁취하고자 하는 이들에게는 더욱더.

하지만 그 잔인한 현실을 알고 있다 하더라도, 결코 익숙해질 수 없는 종류의 것이 있다.

이를테면, 불과 얼마 전까지만 하더라도 웃으며 말을 주고받던 누군가의 부재를 깨닫게 됐을 때라든지.

“……그래, 결국 그렇게 됐나.”

의식을 잃은 직후에 일어난 일을 들은 진태경은, 혼잣말과도 같은 뇌까림과 함께 조용히 눈을 감았다.

그리고 동시에, 문득 떠올렸다.

비록 긴 시간은 아니었으나, 신뢰가 담긴 눈빛으로 자신을 바라보았던 그 수많은 눈동자를.

그와 더불어, 어느샌가 익숙해진 누군가의 무뚝뚝한 얼굴과 음성을.



‘그대가 누구인지는 상관없다. 금의위는 오직 황상 폐하의 명만을 따를 뿐. 황명에 반하여 앞길을 막아선다면 죽이겠다.’

‘호패도 없는 무림인이라 그런지, 무례하기 짝이 없군.’

‘고맙소. 우리를, 황실을 지켜 주어서.’



아스라이 눈과 귀를 스쳐 지나가는 찰나의 순간들.

그 기억의 끝에는, 언제나 흔들림 없이 나아가던 누군가의 모습이 있었다.



‘금의위 천호(千戶) 정호군, 상산후의 명을 받드나이다!’



이제는 두 번 다시 들을 수 없게 된 그의 음성을 떠올리며, 말없이 눈을 뜬 진태경은 가슴 깊은 곳에서 울컥 치미는 무언가를 억눌렀다.

멍청할 만큼 우직했던 무관(武官)은 늘 담담했고, 또한 당당했다.

비록 정호군의 최후를 목격하기도 전에 정신을 잃었으나, 분명 그러했으리라 진태경은 확신할 수 있었다.

그는 그런 사람이었으니까.

지난 석 달의 시간 동안 함께했던 휘하의 금의위들도, 목숨을 걸고 싸웠을 서문의 수비군들도 마찬가지였을 것이다.

그들 모두는 타인을 지키기 위해 싸웠고, 장렬하게 산화(散花)했다.

그리고 그런 이들의 희생이 있었기에, 자신을 포함한 적잖은 이들이 살아남을 수 있었다는 사실을 진태경은 영원히 기억할 터였다.

그의 곁에서 고개를 떨구고 눈물을 흘리는 한 사람 역시도.

“……미안해요, 은인. 제가 부족했어요.”

물기 어린 눈과 파르르 떨리는 목소리.

스스로를 자책하는 청풍의 모습에, 진태경은 담담한 어조로 입을 열었다.

“맞아, 부족했지. 청 소협도, 나도.”

“아니에요. 은인은 최선을 다했어요. 만약 제가 조금 더 강했더라면…….”

“청 소협.”

“네?”

“만약 혈주가, 아니 천주가 처음부터 태어나지도 않았다면 참 좋았을 텐데. 안 그래?”

“……!”

“만약, 어쩌면, 혹시…… 그런 병신 같은 생각들은 머릿속에서 지워. 죽은 사람들한테 미안하고, 살아남은 스스로가 미칠 듯이 원망스러워도 참아.”

까득.

내성(內城)의 성벽에 기대어져 있던 몸뚱어리를 조금씩 움직이며, 진태경은 자신도 모르게 이를 악물었다.

마치 세포 단위로 전해지는 듯한 끔찍한 고통 때문에.

그리고 의식을 되찾은 그 순간부터 온 힘을 다해 억누르고 있는, 그럼에도 계속해서 가슴 깊은 곳에서 솟구치는 분노와 자책 때문에.

스륵.

불현듯 실 끊어진 인형처럼 풀어지는 다리.

가까스로 성벽을 붙잡으며 비틀거리는 진태경의 모습에, 청풍이 황급히 손을 뻗어 그를 부축했다.

아니, 정확히는 부축하려 했다.

그 도움의 손길이 닿기도 전, 진태경이 단호하게 고개를 가로젓기 전까지는.

“으, 은인.”

흔들리는 청풍의 눈동자에 억지로 몸을 일으켜 세우는 진태경의 모습이 비쳤다.

어느새 이마를 타고 흘러내리는 구슬땀과 창백하기 그지없는 안색.

그러나 겉으로 보이는 것만이 전부가 아니다.

지금 그의 신체 내부가 생각했던 것 이상으로 처참하게 망가져 있다는 사실을, 공력을 불어넣어 힘을 더했던 장본인인 청풍은 누구보다 잘 알고 있었다.

앞서 그가 흘린 눈물의 일부는, 진태경의 죽음을 막지 못할 것이라는 불길한 예감 때문이기도 했으니까.

하지만.

턱.

진태경은 결코 멈추지 않았다. 포기하지 않았다.

온 힘을 다해 고통을 참고, 가슴 한구석에서 용암처럼 들끓는 수많은 감정을 억누르며 성벽을 잡고 다시금 일어났다.

천천히. 동시에 끈질기게.

그리고 일 초가 십 년처럼 느껴지는 그 아득함 속에서, 목소리를 쥐어 짜냈다.

“우리가 살아남은 이유를, 그들이 우리를 살리기 위해 목숨까지 내던져야 했던 이유를 생각해.”

그럴 수는 없다. 그래서는 안 된다.

이대로 무너지면, 포기해 버리면 모든 것이 물거품이 되어 버릴 테니까.

앞서 목숨 바쳐 퇴로를 연 이들의 희생도.

지금 이 순간에조차도 죽어가고 있을 또 다른 이들의 희생도.

“죽은 사람들에 대한 사과도, 질질 짜는 것도 할 일을 전부 끝마친 뒤에 하라고.”

비단 청풍에게만 하는 말이 아니었다.

절박함, 혹은 패배감에 물든 얼굴로 고개를 늘어뜨린 주위의 모두를 향해 진태경은 꿋꿋이 말을 이었다.

이미 지칠 대로 지친 육신과 정신으로 인해 잠시 잊고 있었던, 그들의 의무를.

“오직 그것만이…… 우리가 할 수 있는 최선의 예의이자 사명이다.”

저벅.

마지막 한 마디를 토해 낸 진태경이 비로소 발걸음을 내디딘 그 순간.

“……!”

“……!”

주의의 공기가 찌르르 울렸다.

보이지 않는 격동과 열기가 한 몸이 되어 피어올랐다.

한 걸음.

고작 한 걸음을 옮겼을 뿐이다.

혈인(血人)이나 다름없는 몰골을 한, 지금 당장 쓰러져도 이상하지 않을 어느 젊은이의 초라한 모습이었다.

하지만 어째서일까.

그저 지켜보는 것만으로도 심장이 요동쳤다.

전신을 지배하고 있던 짙은 패배감이 서서히 걷혀 가고, 그 빈자리를 뜨거운 무언가가 채웠다.

쿵. 쿵. 쿵.

누가, 어디서부터 시작되었는지 모를 울림이 고요한 연못의 파문(波紋)처럼 번지기 시작한다.

내성 밖, 점점 더 급박해지는 전고(戰鼓) 소리는 죽음이 다가오고 있다는 것을 뜻했으나 상관없었다.

적어도 지금만큼은.

도산검림을 헤쳐 나가는 무림인이자 대국의 열후이며, 더 나아가 이 광활한 천하에서 살아가는 한 사람의 백성인 그와 함께하는 한은.

잠시나마 잊을 수 있었다.

잊고 있던 무언가를 다시금 되새길 수 있었다.

콰아아앙!

저 멀리서 들려오는 굉음과 함께, 영원토록 울려 퍼질 것 같던 전고 소리가 멎었음에도.

두두두두!

어느새 대로(大路)를 휩쓸며 내성으로 다가오는 수많은 적들의 발걸음에서 터져 나오는 진동과.

차차차창!

거센 강철의 소음을 따라 처절한 비명이 온 사방에 흘러넘쳐도.

쿵쿵쿵쿵!

그들은 온 힘을 다해 발을 구르고, 병장기를 내리찍으며, 아직 꺼지지 않은 함성의 불씨를 피워 올렸다.

내성 깊은 곳에 웅크린 채 떨고 있을 수많은 백성들을 떠올리며.

뜨거운 열기를 띤 눈동자에 한 사람의 모습을 담아내며.

“모두 기억해라.”

어느덧 선명해진 목소리와 함께 천천히 들어 올려지는, 은백색의 창날을 응시하며.

“우리가 무엇을 위해 지금껏 살아 있는지.”

스릉.

씹어뱉는 듯한 그 한 마디와 동시에 창날이 서릿발 같은 기세를 내뿜은 그 순간.

스아아아아.

철탑처럼 우뚝 선 진태경의 등 뒤에서, 올올이 피어오른 자줏빛 섬광이 횃불보다 강한 빛으로 어둠을 밝혔다.

그리고 해 질 녘 노을처럼 번져 가는 자하신공(紫霞神功)의 기운에 뒤덮인 한 사람의 눈가는, 더 이상 젖어 있지 않았다.

어느 때보다 깊게 가라앉은, 그의 음성 역시도.

“해낼게요. 반드시.”

전투는, 아직 끝나지 않았다.



* * *



붉다. 붉었다.

적어도 지금 한 사람의 시야에 들어온 모든 풍경은, 온통 시체와 피에 잠겨 있었다.

서걱!

심호흡 한 번에 사라지는 생명의 숫자가 몇일까.

곳곳에서 목이 솟구치고, 팔다리가 날아가며, 혹은 고통에 의해 천천히 죽어 가는 이도 있다.

그들은 한때 신선처럼 고아한 자태로 새하얀 도포를 휘날리던 도사요, 나라의 녹을 받아먹고 사는 관군이며, 무림인이자 백성이기도 했으나 지금은 제대로 된 분간이 불가능했다.

머리부터 발끝까지 피를 뒤집어쓴 채, 서녕의 대로변에 그려진 이 참혹한 지옥도(地獄道)의 일부가 되어 갈 뿐이니까.

그리고 이 지옥도의 첫선을 그려 낸 동시에, 마지막 방점(傍點)을 찍을 장본인은 자신의 눈 앞에 펼쳐지고 있는 학살을 관망하고 있었다.

‘미련한 것들 같으니.’

그로서는 도무지 이해할 수 없는 일이었다.

저들은 도대체 무엇을 위해 싸우는가.

고작 혈통 하나만으로 자격을 얻은 황제를 위해서?

아니면 형체조차 존재하지 않는, 정의(正意)라는 낯간지러운 말을 위해서?

‘우습군.’

아마 저들 중 대부분은 황제의 얼굴조차 본 적 없을 것이며, 중원의 무림인들이 그토록 죽고 못 사는 정의란 결국 저들의 울타리 속에서만 만들어진 것에 불과했다.

하지만 천주(天主)는, 그분만큼은 달랐다.

한 자리에 있는 것만으로도 몸이 떨려올 만큼 강대한 권능과 위압감.

힘이 곧 정의인 세상에서, 이보다도 적합한 주인이 어디에 있단 말인가.

‘이 충실한 종복이, 당신의 염원을 이뤄드리겠나이다.’

천주를 향해서인지, 아니면 스스로를 위함인지 모를 다짐과 함께 혈주는 신형을 내뻗었다.

쉭!

소름 끼치도록 낮은 파공성이 울려 퍼진 다음 순간.

투두두둑.

저항을 포기하지 않고 내성을 향해 뻗은 대로변을 가로막고 있던 수비군의 전열(前列)이 힘없이 허물어졌다.

실 끊긴 인형들처럼 쓰러지는 일백의 신형들 위로 높이 솟구치는, 짙은 피 분수와 함께.

푸화아악!

온 사방에 흩뿌려지는 핏방울.

그 믿을 수 없는 광경을 두 눈으로 목격한 수비군들 사이로, 파르르 떨리는 음성이 흘러나왔다.

“괴, 괴물…….”

“그래, 너희에겐 그렇게 보이겠지.”

웃으며 대꾸한 혈주가 손을 뻗었다.

퍼어엉!

핏빛 섬광이 부풀어 오르며 폭발한다. 굉음이 비명을 집어삼키고, 뜯겨나간 뼈와 살점이 비산했다.

“허나, 그분께서 천하를 손에 넣으신 후에는 누가 나를 괴물이라 부르겠느냐.”

힘이 곧 정의가 되는 세상이다.

피에 미친 괴물이, 하늘이 내린 신장(神將)으로 불릴 날도 머지않았다.

비록 그 위대한 대업을 위해 반드시 사라져야 할 한 사람의 목숨을 취하지는 못했으나.

“길을 열어라. 이 하잘것없는 부나방들아.”

서걱! 푸푸푹!

지금의 혈주에게 있어, 그 모든 것은 시간 문제에 불과했다.

어느덧 내성은 눈에 보일 만큼 가까워졌고, 나머지 세 면의 성벽에서 치열한 전투가 이어지는 한 자신의 앞길을 막을 수 있는 자는 아무도 없었으니까.

‘대술사, 네년만큼은 끼어들지 말거라. 아무리 그래도 내 손으로 그분이 아끼시는 종년을 죽이고 싶진 않으니.’

마음속 뇌까림과 함께, 혈주가 도륙을 이어가려던 그 순간이었다.

쉬이이잉, 쾅!

예리하고도 눈부신 섬광이, 도무지 멈출 것 같지 않던 괴물의 발걸음을 가로막은 것은.
```

## Final English reading copy

```markdown
# Chapter 1113

Nothing can be gained without sacrifice.

That was even more true for those seeking victory through war—the most terrible form of violence—in an age of savagery that had thrown law and benevolence to the dogs.

But even knowing that cruel reality, there were some things one could never get used to.

Like realizing that someone who had been laughing and talking with you only moments ago was gone.

“……So, it ended that way after all.”

After hearing what had happened immediately after he lost consciousness, Jin Taekyung quietly closed his eyes, muttering to himself.

And at the same time, someone came to mind.

Though they had shared little time, so many pairs of eyes had looked at him with trust.

Along with them came the stony face and voice of someone whose presence had gradually become familiar.

*“It doesn’t matter who you are. The Embroidered Uniform Guard obeys only His Majesty the Emperor’s command. If you stand in our way in defiance of his imperial decree, I’ll kill you.”*

*“Perhaps it’s because you’re a martial artist without even an identity tag, but your manners are atrocious.”*

*“Thank you. For protecting us—for protecting the imperial family.”*

Fleeting moments brushed past his eyes and ears, faint as mist.

And at the end of those memories was always the figure of someone who had pressed forward without wavering.

*“Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, answers the command of the Marquis of Shangshan!”*

Remembering the voice he would never hear again, Jin Taekyung opened his eyes without a word and forced down something rising up from deep in his chest.

The officer had been so stubbornly steadfast it was almost foolish. He had always been calm, and always stood tall.

Taekyung had lost consciousness before witnessing Jeong Hogun’s final moments, but he was certain they had gone that way.

Because that was the kind of man he was.

The Embroidered Uniform Guards who had served under Jin Taekyung over the past three months must have been the same. So must the defenders at the West Gate, who had fought with their lives on the line.

They had all fought to protect others, and gone up in a blaze of glory.

Jin Taekyung would remember forever that, thanks to their sacrifice, no small number of people—including him—had survived.

So would the person beside him, head bowed as he shed tears.

“……I’m sorry, Benefactor. I wasn’t good enough.”

His eyes glistened, and his voice trembled.

Looking at Cheongpung as he blamed himself, Jin Taekyung spoke in a calm voice.

“You’re right. We weren’t good enough. Neither you nor I.”

“No. You did everything you could. If only I’d been a little stronger……”

“Young Hero Cheongpung.”

“Yes?”

“If only the Blood Lord—or no, the Lord of Heaven—had never been born in the first place. Wouldn’t that have been nice?”

“……!”

“Those stupid thoughts—what if, maybe, if only—get them out of your head. Even if you feel terrible for the dead, even if you hate yourself like crazy for surviving, bear it.”

His teeth ground together.

Jin Taekyung slowly shifted his body, which had been propped against the Inner City wall. He clenched his jaw without meaning to, against the terrible pain that seemed to reach every cell in his body.

And against the fury and self-reproach he had been trying with all his might to hold back since regaining consciousness, though they kept surging up from deep within him.

His legs suddenly gave way like a puppet with its strings cut.

Jin Taekyung managed to grab the wall, but he staggered. Cheongpung reached out in alarm to support him.

Or, more precisely, he tried to.

Until Jin Taekyung firmly shook his head before that helping hand could reach him.

“B-Benefactor.”

In Cheongpung’s unsteady eyes, Jin Taekyung forced himself upright.

A sheen of sweat had begun to run down his forehead, and his face was deathly pale.

But what showed on the outside was not the whole story.

Cheongpung, who had poured his internal energy into Jin Taekyung to lend him strength, knew better than anyone that his insides were in even worse shape than they seemed.

Some of the tears he had shed earlier had come from a terrible premonition: that he would be unable to stop Jin Taekyung from dying.

But—

Thump.

Jin Taekyung did not stop. He did not give up.

Bearing the pain with everything he had and tamping down the emotions boiling like lava in a corner of his chest, he gripped the wall and stood up again.

Slowly. And stubbornly.

Then, through a distance so vast that each second felt like ten years, he forced the words out.

“Think about why we survived. Why they had to give up their lives to save us.”

They couldn’t let that happen. They mustn’t.

If they fell apart now, if they gave up, everything would have been for nothing.

The sacrifice of those who had given their lives to open a path of retreat.

The sacrifice of others who might even now be dying.

“Save your apologies to the dead and your sobbing until after we’ve finished everything we have to do.”

He wasn’t speaking only to Cheongpung.

Jin Taekyung kept speaking resolutely to everyone around him. Their heads hung low, their faces marked by desperation or defeat. Exhausted in body and mind, they had briefly forgotten their duty.

“That’s the only way…… we can show them the respect they deserve. It’s our duty.”

Step.

The moment Jin Taekyung finally took a step after forcing out those last words—

“……!”

“……!”

The air around them rang.

An invisible surge and heat rose as one.

One step.

He had moved only one step.

He looked wretched—a young man covered in blood, who wouldn’t have seemed out of place if he collapsed right then and there.

But why?

Just watching him made their hearts pound.

The oppressive defeat that had taken hold of their whole bodies slowly lifted, and something hot filled the space it left behind.

Thump. Thump. Thump.

A pulse whose source no one could name began to spread like ripples across a still pond.

Outside the Inner City, the war drums grew more urgent, signaling death’s approach. But it didn’t matter.

At least not now.

As long as they stood with him—a martial artist who had crossed a mountain of sabers and a forest of swords, a Great Nation’s marquis, and, beyond that, one of the people living in this vast world.

For a moment, they could forget.

They could remember something they had forgotten.

KABOOM!

Even when a thunderous crash sounded in the distance and the war drums that had seemed destined to ring forever fell silent.

But the tremors of countless enemy footsteps swept down the avenue toward the Inner City.

The clash of steel rang out, and desperate screams filled the air.

Still, they stamped their feet with all their strength and brought their weapons down, fanning the embers of a battle cry that had yet to die.

Thinking of the countless people huddled in the depths of the Inner City, trembling.

Holding the image of one man in their heated eyes.

“Remember this, all of you.”

They watched the silver-white spearhead slowly rise, his voice now clear.

“What we’ve been alive for all this time.”

Shing.

At that moment, the spearhead gave off a frosty aura, and Jin Taekyung spat out his words.

Swoosh.

Behind him, standing tall as an iron tower, strands of violet light rose and blazed brighter than torches, illuminating the darkness.

And beneath the energy of the Zaha Divine Technique spreading like the sunset at dusk, the corner of one person’s eye was no longer wet.

His voice, sunk deeper than ever, was the same.

“I’ll do it. I promise.”

The battle was not over yet.

* * *

Red. Everything was red.

At least, every part of one person’s view was submerged in corpses and blood.

Slice!

How many lives vanished with a single deep breath?

Heads flew everywhere. Limbs went sailing. Some died slowly, writhing in agony.

Some had been Daoists in fluttering white robes, as refined as immortals; others had been government soldiers living on the nation’s payroll. They had been martial artists and common people, too. Now it was impossible to tell them apart.

Drenched in blood from head to toe, they had become part of the hellscape painted across Xining’s main road.

The man who had drawn the first strokes of this hellscape and would put the final touch to it watched the slaughter unfold before his eyes.

*What a bunch of fools.*

He couldn’t understand it.

What were they fighting for?

For an emperor who had earned his place through nothing but his bloodline?

Or for that embarrassing word, “justice,” which had no shape or form?

*Ridiculous.*

Most of them had probably never even seen the Emperor’s face. And the justice the Central Plains martial artists were so willing to die for was nothing more than something made within their own little walls.

But the Lord of Heaven was different. The Lord alone.

His power and presence were so overwhelming that just being near him made one tremble.

In a world where might made right, what ruler could be more fitting?

*This loyal servant will fulfill your wish.*

With a vow he couldn’t tell whether he made to the Lord of Heaven or to himself, the Blood Lord shot forward.

Whoosh!

A moment after the horrifyingly low whistle of air, the front line of defenders—still refusing to give up the fight as they blocked the main road to the Inner City—crumpled helplessly.

A hundred bodies collapsed like puppets with their strings cut, and a torrent of dark blood burst high into the air.

Splatter!

Blood sprayed in every direction.

Among the defenders who witnessed the unbelievable sight, a trembling voice escaped someone’s lips.

“A-a monster……”

“Yes. I suppose that’s what I look like to you.”

The Blood Lord smiled as he replied, then reached out.

Boom!

A flash of blood-red light swelled and exploded. The blast swallowed their screams, scattering torn flesh and bone.

“But after he takes the world, who will call me a monster?”

It was a world where might made right.

It wouldn’t be long before the blood-mad monster was hailed as a divine general sent by Heaven.

Though he had failed to take the life of one man whose death was necessary for that great undertaking—

“Open the way, you worthless moths.”

Slice! Thud-thud-thud!

To the Blood Lord, all of it was only a matter of time.

The Inner City was already close enough to see clearly. And while fierce battles continued at the other three walls, there was no one who could block his path.

*Grand Mage, you bitch, stay out of this. Even I don’t want to kill a servant girl the Lord of Heaven favors with my own hands.*

The Blood Lord was about to continue his slaughter, muttering to himself—

Whoooooosh! Boom!

A sharp, dazzling flash blocked the monster’s steps, which had seemed impossible to stop.
```
