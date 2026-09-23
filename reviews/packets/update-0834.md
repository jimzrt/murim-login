<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0834.txt",
      "sha256": "1d2681d93e6021fd5e30d528593bdf76947b53f4aaeaffe18af4a2559771c0d2",
      "bytes": 13778
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7376983479b3946b99ad88b86a3004ac5928d007d12fb550289c4befb0b0a538",
      "bytes": 2043
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ad6965cfcc54bdbb79c84cfefd2d5c0b76d1e8fdd3994cdc0d6cd2934374048b",
      "bytes": 226906
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8a408747de4e637218c9ab679e7e8c831bfd0768d931d39955e46c8777ac6c6f",
      "bytes": 723
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "0c72887805eedfc0d6ee94422b9ba395a64366e1abf7b6fc94bf2fd04e0c21ac",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a3c6f1b6d9fe10b2d200a3385a2b4edb71d922a9b332a7f25e1caebb473ffe57",
      "bytes": 1848
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ff885b6e17490dfec4e7483d0a4f5ad8edaf50a28704fa89faff896a35d85bf6",
      "bytes": 1853
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5368678cb916c6320edf14a330c6f52008b5df2f24e94611fc0682b1eed8d7f5",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "e0a8ced7eb5086878733e7931798f9023e1280ffeac8b9e949e6c3483bb766b4",
      "bytes": 937
    },
    {
      "path": "characters/Namho.md",
      "sha256": "0bc5f9e6a95f99cf41996c347fca2eef91c02d8fd4847eb5cc39a0d86a31f842",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "c6f48c8a526da7243ed59d350c8010d83fa4eb6aefa89234a7a9bc40adf22305",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "af29838178ea6fb66b10e4fc72a64896812ae49dfe13d26ad70f70c725dde068",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "a25f7065fd07dcc69876bd885b13a45f2d25d172c17fd879ddcde2e4a7a7d020",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "fb9c012fd9b3442f8592966a0b9754c88d820dac64706476408626e95065909d",
      "bytes": 787
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "892a1e8800765d30eb8a5996d56898ddd711286f305c320782ea235764ddac18",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9efad41a2b865bcf5c939bc36568267e2332e7ce051f57c19cbf5cf82b65cc36",
      "bytes": 251423
    }
  ],
  "estimated_tokens": 15356
}
-->

# Durable State Update — Chapter 834

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
1 and safe_through 834. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 834. Profile updates may replace only one
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
  "chapter": 834,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 834,
    "continuity_sources": [834],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "Jin erased the Doppelganger, but Main Quest [Cataclysm] and its “Stop the Summoning” mission failed.",
    "The Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System transferred Jin to Murim while he was unconscious; he has now awakened in Nanman.",
    "The System’s Status Window is currently inaccessible; Jin suspects an update may be responsible.",
    "Jin saw a vision in which Ahomed’s ritual summoned a black-haired man who killed Ahomed and unleashed a destructive storm of magical power; whether the vision was real remains unknown.",
    "Jin believes the summoned man is not Asmodeus, but does not know his identity.",
    "The Prophet’s remaining mage disciples completed their prepared ritual, and Ahomed was the mage who led it."
  ],
  "continuity_sources": [
    832,
    833
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?",
    "What changed in the System update, and when will its functions return?"
  ],
  "safe_through": 833,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 남만야수궁  | **Nanman Beast Palace**          |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 무인     | **martial artist**                               | Default term                                          |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 수강 | **Palm Force** | Force generated through a palm technique. |
| 추혼객 | **Soul-Chasing Guest** | Song Ilseom’s former epithet; he was known by it ten years earlier. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 대지모신 | **Earth Mother Goddess** | New deity proclaimed by Jin Taekyung as Nanman's One God. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 모신천국 | **Mother Goddess Heaven** | Slogan used by followers of the Earth Mother Goddess. |
| 불신지옥 | **Unbeliever Hell** | Slogan threatening unbelievers with damnation. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 833
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 833
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 833
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 833
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 833
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 717
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 724
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 716
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 716
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 716
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 802
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 725
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃834화



시름을 잊는 방법은 사람마다 다르다.

누군가는 독서와 음악으로 슬픔을 달래고, 맛있는 음식과 술 한잔으로 분노를 털어낸다.

몸을 움직이는 것도 좋은 방법이다. 숨이 턱에 찰 때까지 뛰고, 격렬하게 운동을 하다 보면 어중간한 잡생각 따위는 머릿속에서 깨끗하게 지워져 있으니까.

그런 의미에서 5kg대 우량아로 태어나며 동네 산부인과의 역사를 새로 쓴 나는, 늘 마지막 방법을 선호하는 편이었다.

“격렬한 움직임. 그것만큼 좋은 게 없지. 무진이 너도 그렇게 생각하지 않니?”

고양이 발바닥처럼 부드럽게 건넨 목소리에, 내 ‘시름 이겨 내기’ 강론을 듣고 있던 혁무진이 굳게 닫혀 있던 입을 열었다.

“아닌데요.”

“아니야?”

“예.”

“왜?”

“때리실 거잖아요.”

“누가 그래? 난 아직 아무 말도 안 했는데.”

“조장님 주먹이요. 거의 울부짖고 있는데요.”

떨리는 시선으로 나를, 정확히는 불끈 움켜쥔 주먹을 바라보는 혁무진을 향해 나는 순순히 고개를 끄덕였다.

“그래, 맞아.”

“……이렇게 쉽게 인정하셔도 됩니까?”

“인정해야지. 그게 현실이니까.”

“한 번만 살려 주시면 안 됩니까?”

“지금 그 질문은 약간 오해의 여지가 있네. 누가 들으면 내가 너 죽이는 줄 알겠다.”

“죽이진 않아도 죽일 것처럼 때리셨잖아요.”

“내가 언제?”

그 순간, 믿을 수 없다는 눈빛으로 나를 바라본 혁무진이 발악하듯 외쳤다.

“어제! 그제! 작년부터! 항상! 비가 오나 눈이 오……!”

뻑!

“어흑!”

사람이 처맞는 데에는 다 이유가 있는 법.

그리고 시동이 걸린 내가 한동안 신나게 혁무진을 두들겨 패며 현실의 시름을 잊어 가던 그때.

빠르게 가까워지는 인기척과 함께, 익숙한 목소리들이 굳게 걸어 잠근 격자 창문의 틈새로 들려왔다.

“왜 마차를 멈춰 세웠…… 잠깐, 왜 길잡이들뿐이지? 혁무진은?”

“태산 소협도 보이지 않아요!”

젊은 남녀의 다급한 목소리에 이어 들려오는 늙수그레한 노인의 외침까지.

“뭣이! 태산이 그놈이 사라졌단 말이냐!”

“네. 분명히 혁 소협이나 다른 길잡이들과 함께 각주님을 지키고 있어야 하는데.”

“세상에, 감사합니다. 천지신명이시여. 그 새끼 만난 후부터 뒷골이 당겨서 오늘내일하고 있었는데, 앞으로 이십 년은 더 살 수 있겠군.”

“아니, 그건 말이 심하지 않소!”

“말이 심하긴 니미럴. 심한 건 태산인지 금수강산인지 하는 네 수하 놈 식성 아니냐? 지난 수십 년간 노부가 남만에 머무르면서 온갖 해괴한 금수들을 다 봤지만, 세상에 코끼리보다 많이 처먹는 놈이 있을 거라고는 상상도 못 했다.”

“이보시오! 남 노인!”

“어어, 아니 그런데 아까부터 이 어린 노무 새끼가…… 마, 너 적 선배 앞에서 이렇게 굴 수 있어? 대가리에 피도 안 마른 놈이 어디 어른 앞에서 언성을 높여!”

듣기만 해도 어질어질해지는 대화가 이어지던 그때, 바닥에 쓰러져 꿈틀거리던 혁무진이 외쳤다.

“저, 저 여기 있습니다! 살려 주세요!”

그 순간, 짧은 침묵 끝에 동시다발적인 외침이 터져 나왔다.

“암천! 암천의 습격이오!”

“혁 소협은 괜찮을 테니, 각주님부터 먼저 구하세요!”

“빌어먹을, 길잡이들도 한통속이었나! 그럼 태산이도……!”

“노부의 날카로운 식견으로 간파한 바에 의하면 태산이 그놈도 한통속이다! 나타나면 죽여! 제발 죽여!”

차차차창!

칼 뽑히는 소리와 겁에 질린 남만 길잡이들의 비명을 들으며, 나는 문득 생각했다.

‘아, 엄마 보고 싶다.’

무림, 역시 쉽지 않다.



* * *



멀쩡하게 마차에서 내린 나를 목격한 사람들의 반응은 가지각색이었다.

“살았다!”

“아아, 대지모신의 사도시여!”

“모신천국! 불신지옥!”

한순간에 암천의 주구로 몰려 변명 한마디 못하고 죽을 뻔한, 남만야수궁 소속의 길잡이들은 그대로 주저앉았고.

“어?”

“어?”

묻지도 따지지도 않고 우선 한 놈부터 썰고 보려던 추혼객(抽魂客) 송일섬과 흑룡도(黑龍刀) 사마표는 마치 데칼코마니처럼 동시에 움직임을 멈췄으며.

“열화신룡 진태경이…… 알고 보니 암천?”

정마대전 이후부터 수십 년간 남만에 머무르던 은영각(隱影閣) 요원 남호는 마침내 치매 증상을 보였고.

“은인!”

마지막으로 표왕(驃王)의 손녀이자 용봉표국의 소국주인 주화란은 비명 같은 외침과 함께 내게 달려들었다.

와락!

음, 역시 무림 오길 잘했어.

하지만 나는 어떤 상황에서도 공과 사를 철저히 구분하는 남자. 억지로 입꼬리에 힘을 주며 진중한 목소리로 입을 열었다.

“샴푸 뭐 쓰세요?”

“진짜 무슨 일이라도 생긴 줄 알고 깜짝 놀…… 네?”

“아, 아무것도 아닙니다.”

잠깐 정신이 혼미해졌던 모양이다.

다시 한번 마음을 가다듬기 위해 심호흡하던 그때, 주화란이 걱정 가득한 목소리로 물었다.

“정말 괜찮으신 거 맞아요?”

“저야 눈이 오나 비가 오나 벼락이 치고 우박이 내려도 사시사철 괜찮죠. 그런데 진짜 샴푸 뭐 쓰세요.”

“어떡해. 머리 다치셨나 봐.”

“……죄송합니다. 머리를 다친 게 아니라 잠깐 혼란이 와서 그래요.”

의식의 흐름, 이거 만만히 볼 게 아니다.

현실에서 막 돌아오기도 했고, 아직 잠이 덜 깼는지 제멋대로 움직이는 혓바닥 때문에 내가 정상이라는 걸 입증하기까지는 약간의 시간과 노력이 필요했다.

그러니까, 어느 늙고 괴팍한 은영각 요원에게 검증 과정을 거쳐야 했다는 뜻이다.

“노부의 이름이 무엇이냐?”

“아니, 왜 이런 것까지 해야 하는데요.”

“묻는 말에만 대답해라. 다시 한번 묻지. 이름은?”

“미치겠네.”

“노부는 미 씨가 아니다.”

“와, 돌아 버리겠네.”

“와 씨도 아니다.”

환장하겠다고 말하려다가 포기한 내가 대답했다.

“남호.”

“그렇다면 신분은?”

“은영각.”

“틀렸다.”

“예?”

“노부는 그냥 은영각 요원이 아니라, 은영각 최고의 요원이다.”

“그냥 최고령 요원 아니에요?”

“…….”

말없이 나를 노려보는 남호의 모습에, 간신히 진실의 마차에서 빠져나와 몸을 추스르고 있던 혁무진이 중얼거렸다.

“일단 기억이나 판단력 쪽에는 아무런 문제도 없는 것 같은데요.”

“갈! 네놈이 뭘 안단 말이냐!”

“깜짝이야. 왜 그렇게 화를 내세요?”

“노부도 다 계획이 있다. 지금 눈앞의 이놈이 열화신룡 진태경의 탈을 뒤집어쓴 암천의 주구라면 어찌할 테냐!”

“노환이 의심되긴 하는데, 일단 아닙니다. 제 목을 걸죠.”

“근거는?”

“다들 오시기 전에 제가 맞아 봤는데, 주먹맛이 딱 조장님이에요.”

“…….”

“주먹이 제 살갗에 아주 쩍쩍 달라붙습니다. 제 몸이, 영혼이 기억해요. 이런 느낌은 조장님께 맞았을 때만 받을 수 있어요.”

혁무진이 슬픈 미소를 지으며 나를 바라보았다.

“깨어나셔서 기쁩니다, 조장님. 제가 지난 사흘 동안 많이 걱정했어요.”

앞으로는 좀 덜 때려야 하나, 곰곰이 생각하고 있던 나는 그 말을 듣고 눈살을 찌푸렸다.

“지금 뭐라고?”

“네? 뭐가요?”

“아니, 사흘이라고 하지 않았냐?”

“아. 모르셨어요? 사흘 전에 잠깐 깨어나셨다가, 그 후로 쭉 앓는 소리에 땀까지 흘리시며 주무셨는데.”

“……당연히 모르지. 자고 있던 놈이 어떻게 아냐.”

혁무진이 머쓱하게 머리에 난 혹을 문질렀다.

“죄송합니다. 여하튼 그것 때문에 다들 난리였어요. 남 노인은 약초라도 구해야 한다고 다른 분들과 함께 주위를 샅샅이 뒤지셨고, 적천강 대협은 곧장 사천으로 향하신다며 떠나셨습니다.”

“노야, 아니 스승님이 사천으로?”

“네. 그렇게 다급해하시는 모습은 난생처음 봤다니까요.”

“그런데 사천에는 왜…… 아.”

미처 말을 잇기도 전에, 문득 어떤 생각이 머릿속을 스쳤다.

‘사천당가(四川唐門).’

비록 몇 달 전 서천마군에 의해 막대한 타격을 입었던 사천당가지만, 무림 세가로서의 저력은 하루아침에 사라지는 것이 아니다.

더군다나 주로 암기와 독을 다루는 사천당가는 천하에서 손꼽히는 의가(醫家)이기도 하니까.

게다가…….

‘사천에는 신의(神醫)가 있지.’

엄밀히 따지자면 천하에 알려진 신의의 진짜 정체는 살성(殺星)이지만, 스승과 달리 사천에 남은 제자도 신의라 부르기에 조금의 부족함도 없는 명의다.

적천강은 바로 그 새로운 신의를 데려오기 위해 먼저 떠난 거였고.

‘굳이 그렇게까지 하지 않아도 됐을 텐데.’

당장 만나지 못한다는 아쉬움과 함께 마음 한구석이 뭉클해지던 그때, 나는 몸 깊숙한 곳에서 찌르는 듯한 통증을 느꼈다.

‘이건…….’

틀림없다.

시스템 업데이트와는 별개로 여전히 남아있는 [부서진 신체]의 영향이었다.

레벨 업으로도 회복하지 못한 그 흔적이, 하단전 어림을 쿡쿡 쑤시고 있었다.

‘음.’

흘러나려는 침음성은 애써 삼켰지만, 미약하게나마 찌푸려지는 미간은 어쩔 수 없다.

그렇지 않아도 내게 시선을 집중하고 있던 사람들은 그 모습을 놓치지 않았다.

“저어, 조장님. 혹시 무슨 문제라도…….”

“아냐. 그냥 생각할 게 좀 있어서.”

틀린 말은 아니었다.

내가 입은 부상에 대해, 그리고 사흘 전 이를 눈치챘을 적천강에 대해 생각하고 있었으니까.

‘노야가 신의를 찾아간다는 건, 당신의 능력으로는 나를 치료할 수 없다는 사실을 알았기 때문이겠지.’

단언하건대, 화왕(火王) 적천강은 위대한 무인이자 좋은 스승이다.

그러나 시스템으로도 치유할 수 없는 내 부상은, 그런 적천강에게도 해결할 수 없는 난제(難題)처럼 여겨졌을 것이다.

‘시바, 처음에만 해도 1금융권 대출인 줄 알았는데, 이제와서 보니 햇살론이었네.’

마치 도박판에서 이기기 위해 사채까지 끌어쓰다 인생 말아먹은 도박꾼이 된 기분이다.

하지만 이렇게 된 이상 별수 있나.

설령 그 순간으로 돌아가도 같은 선택을 허리라는 사실을 알기에 나는 그저 쓴웃음만 지어 보였다.

어쩔 수 없는 일이었다.

그 몇 번의 도박에 걸려 있던 것은 금괴나 수표 따위가 아니라, 나 자신과 또 다른 누군가의 목숨이었으니.

내가 처했던 그 위기의 순간마다 일섬(一殲)을 사용하지 않았다면, 지금까지 살아 있지도 못했을 것이다.

‘덕분에 숨통이 트였으니, 빚을 갚을 때가 온 거겠지.’

얼굴을 마주한 채 대화를 나눌 수 있는 사람도 아니고, 시스템에게 투정 부릴 생각 따위는 없다. 이미 과할 만큼 큰 선물을 받았고 여러 번 경고도 들었다.

지금껏 걸어온 그 모든 길이, 오직 내 선택이었다.

‘그럼 된 거지. 뭐.’

그 한 마디로 머릿속 복잡한 생각을 지워 냈다.

지금 당장은 혼자서 아무리 생각해 봤자 당장 나아지는 것도 없을뿐더러, 주위 사람 기분도 좀 생각해야 하니까.

내가 이 정도로 배려심이 깊은…… 아니, 그런데 잠깐만.

“그럼 태산이 놈은 어디 간 건데?”

“어?”

“어?”

불쑥 던진 내 물음에 모두가 눈을 깜빡이던 그때, 남만야수궁에서 붙여 준 길잡이 중 하나가 엉거주춤 다가와 입을 열었다.

“그…… 덩치 큰 분께서는 뭐 좀 가지러 가셨습니다.”

남호가 어리둥절한 표정으로 되물었다.

“가지러 가?”

“예.”

“아니, 도대체 뭘?”

“그게, 그.”

길잡이가 뭐라 말하려던 그 순간.

파사사사삭!

오십여 장 밖에 있던 풀숲이 흔들리며, 저게 사람이 맞나 싶을 정도의 거구가 뛰쳐나왔다.

“태산이! 가져왔다!”

그리고 손에 든 거무튀튀한 물체를 번쩍 치켜들었다.

“태산이가 세상에서 제일 좋아하는, 아니 아픈 각주를 치료할 명약!”

그 광경을 멍하니 바라보던 사람들이 중얼거렸다.

“꿀이네요.”

“맞소. 꿀통이오.”

“말씀하시는 중에 죄송한데, 저건 꿀통이 아니라 벌집 아닙니까?”

“그것도 맞지.”

위이이이이잉!

태어나서 처음 봤다.

저렇게 큰 벌은, 그리고 저렇게 큰 벌이 수천 마리나 뭉쳐져 있는 광경은.

“……원시천존이시여. 천지신명이시여.”

슬픔에 젖은 남호의 목소리를 뒤로 하고, 나를 비롯한 모두는 조용히 마차에 올랐다.

무림. 역시 쉽지 않다.
```

## Final English reading copy

```markdown
# Chapter 834

Everyone has their own way of forgetting their troubles.

Some people soothe their grief with books and music. Others shake off their anger with good food and a drink.

Getting physical is another good option. Run until you’re gasping for breath, work out hard enough, and all those half-baked thoughts get wiped clean from your mind.

In that sense, having been born a chubby baby weighing over eleven pounds and made history at the local maternity clinic, I’d always preferred the last method.

“Nothing beats a good workout. Don’t you think so too, Mujin?”

At my voice, soft as a cat’s paw, Hyuk Mujin—who’d been listening to my lecture on “overcoming your troubles”—finally opened his tightly shut mouth.

“No.”

“No?”

“Yes.”

“Why not?”

“Because you’re going to hit me.”

“Who says? I haven’t even said anything yet.”

“Your fist, Captain. It’s practically howling.”

Hyuk Mujin’s eyes trembled as he looked at me—or, more precisely, at the fist I had clenched tight. I nodded readily.

“Yeah. You’re right.”

“……You’re admitting it that easily?”

“I have to. That’s reality.”

“Could you spare me just this once?”

“People could misunderstand that question. Anyone listening might think I’m trying to kill you.”

“You may not kill me, but you hit me like you’re trying to.”

“When did I do that?”

At that, Hyuk Mujin stared at me in disbelief and shouted as if his life depended on it.

“Yesterday! The day before! Since last year! All the time! Rain or snow—”

Wham!

“Urgh!”

There’s always a reason someone gets beaten up.

And while I was getting warmed up and happily beating Hyuk Mujin for a while, forgetting my troubles in the process, familiar voices came through the slats of the tightly shut carriage window, accompanied by footsteps drawing closer.

“Why did the carriage stop—wait, why are there only guides here? Where’s Hyuk Mujin?”

“I don’t see Young Hero Taishan either!”

After the urgent voices of a young man and woman came the shout of an old man.

“What! That Taishan brat has disappeared?”

“Yes. He should definitely be with Hyuk Mujin and the other guides, protecting the Pavilion Master.”

“Oh, thank you, gods of heaven and earth. Ever since I met that bastard, the back of my head’s been throbbing, and I thought I’d kick the bucket any day now. Looks like I’ve got another twenty years in me.”

“Now that’s going too far!”

“Going too far, my ass. What’s going too far is the appetite of that underling of yours—Taishan, Scenic Mountain, whatever his name is. I’ve spent decades in Nanman and seen every kind of strange beast there is, but I never imagined there’d be a man who eats more than an elephant.”

“Now, listen here, Elder Nam!”

“Hey, hang on. This little shit’s been mouthing off at me for a while now… You think you can act like this in front of Senior Jeok? You’re still wet behind the ears—how dare you raise your voice at an elder!”

As that dizzying conversation went on, Hyuk Mujin, who’d been sprawled on the floor and twitching, called out.

“I-I’m right here! Help me!”

A short silence followed. Then everyone shouted at once.

“Dark Heaven! It’s an attack by Dark Heaven!”

“Young Hero Hyuk will be fine—save the Pavilion Master first!”

“Damn it, were the guides in on it too? Then Taishan must’ve—!”

“By this old man’s keen eye, that Taishan brat’s in on it too! If he shows up, kill him! Please, kill him!”

Clang, clang, clang!

As swords were drawn and the Nanman guides screamed in terror, I found myself thinking:

*Ah. I miss Mom.*

Murim really wasn’t easy.

* * *

The people who saw me step out of the carriage in perfect health reacted in all sorts of ways.

“We’re saved!”

“O Apostle of the Earth Mother Goddess!”

“Mother Goddess Heaven! Unbeliever Hell!”

The guides from the Nanman Beast Palace, who’d been branded Dark Heaven’s lackeys and nearly killed without a chance to explain themselves, sank to the ground.

“Huh?”

“Huh?”

Soul-Chasing Guest Song Ilseom and Black Dragon Saber Sama Pyo had been ready to cut someone down first and ask questions later. They both froze at the same time, like mirror images.

“Blazing Flame Divine Dragon Jin Taekyung… was Dark Heaven’s lackey all along?”

Namho, a Hidden Shadow Pavilion agent who’d lived in Nanman for decades since the Great Faction War, finally started showing signs of dementia.

“Benefactor!”

Last of all, Ju Hwaran—the Escort King’s granddaughter and the Young Bureau Head of the Yongbong Escort Bureau—ran over to me with a shriek.

She threw her arms around me.

Well, coming to Murim really had been the right call.

But I was a man who kept business and pleasure strictly separate, no matter the circumstances. I fought to keep the corners of my mouth from rising and spoke in a solemn voice.

“What shampoo do you use?”

“I was so worried something had really happened to you, I was terrified—what?”

“N-Nothing.”

I must have been a little out of it.

As I took a deep breath to get a hold of myself, Ju Hwaran asked in a voice full of concern, “Are you really all right?”

“I’m fine in every season—whether it’s snowing, raining, thundering, or hailing. But seriously, what shampoo do you use?”

“Oh no. You must have hit your head.”

“……I’m sorry. I didn’t hit my head. I’m just a little confused.”

The stream of consciousness is no joke.

I’d only just returned from the modern world, and maybe I was still half asleep. It took a little time and effort to prove I was in my right mind, thanks to my tongue doing whatever it wanted.

Which meant I had to go through a test administered by a certain old, eccentric Hidden Shadow Pavilion agent.

“What is this old man’s name?”

“Why do I have to do something like this?”

“Answer the question. I’ll ask again. What’s the name?”

“This is driving me nuts.”

“This old man’s not named Mi.”

“Wow, I’m going to lose my mind.”

“This old man’s not named Wa, either.”

I was about to say I was going crazy, but gave up and answered.

“Namho.”

“Then what’s your affiliation?”

“Hidden Shadow Pavilion.”

“Wrong.”

“What?”

“This old man isn’t just a Hidden Shadow Pavilion agent. He’s the Pavilion’s finest agent.”

“Wouldn’t you be its oldest agent?”

“……”

Namho glared at me without a word. Hyuk Mujin, who’d finally escaped the Truthful Carriage and was getting back on his feet, muttered,

“His memory and judgment seem fine to me.”

“Bah! What do you know, you fool!”

“Whoa. Why are you getting so mad?”

“This old man has a plan, too. What would you do if the fellow in front of you were a Dark Heaven lackey wearing Blazing Flame Divine Dragon Jin Taekyung’s face?”

“I suspect infirmities of old age, but no, he isn’t. I’ll stake my neck on it.”

“What’s your evidence?”

“I got hit before everyone came over. That punch felt exactly like the Captain’s.”

“……”

“His fist sticks to my skin like glue. My body remembers it. My soul remembers it. I only get that feeling when the Captain hits me.”

Hyuk Mujin looked at me with a sad smile.

“I’m glad you woke up, Captain. I was really worried these past three days.”

I’d been wondering if I ought to hit him a little less from now on. But at that, my brow furrowed.

“What did you just say?”

“Huh? What about?”

“Did you say three days?”

“Oh. You didn’t know? You woke up briefly three days ago, then slept the whole time after that, groaning and sweating.”

“……Of course I didn’t know. How would someone who was asleep know?”

Hyuk Mujin rubbed the bump on his head, looking sheepish.

“Sorry. Anyway, everyone was in an uproar over it. Elder Nam searched everywhere nearby with the others, saying they had to find some medicinal herbs. Great Hero Jeok left right away, saying he was heading to Sichuan.”

“Old Master—no, my Master went to Sichuan?”

“Yes. I’ve never seen him so hurried.”

“But why Sichuan… Oh.”

Before I could finish the question, a thought suddenly crossed my mind.

*The Sichuan Tang Clan.*

Although the Sichuan Tang Clan had suffered a devastating blow at the hands of the Western Heaven Demon Lord a few months ago, the strength of a great family didn’t disappear overnight.

Besides, the Sichuan Tang Clan, which mainly dealt in hidden weapons and poison, was also one of the most renowned medical families in the world.

And on top of that…

*The Divine Physician is in Sichuan.*

Strictly speaking, the Divine Physician known to the world was actually the Slaughter Saint. But unlike his master, the Disciple had stayed in Sichuan, and he was a physician every bit as worthy of the title.

Jeok Cheongang had left ahead of us to bring that new Divine Physician back.

*He didn’t have to go that far.*

I felt a pang of regret that I wouldn’t get to see him right away, and a warmth stirred in one corner of my heart. Then a stabbing pain rose from deep inside my body.

*This is…*

There was no doubt.

Separate from the System update, the effects of [Broken Body] remained.

That damage, which even leveling up hadn’t healed, was needling me around the lower dantian.

*Mm.*

I swallowed the groan, but I couldn’t stop my brow from furrowing just a little. The people who’d already been focused on me noticed.

“C-Captain. Is something wrong?”

“No. I’ve just got something on my mind.”

That wasn’t a lie.

I was thinking about my injuries—and about Jeok Cheongang, who’d noticed them three days ago.

*Master must have gone to find the Divine Physician because he realized there was nothing he could do to treat me.*

I could say this without a doubt: Fire King Jeok Cheongang was a great martial artist and a good Master.

But my injury, which the System couldn’t heal, must have seemed like a problem even Jeok Cheongang couldn’t solve.

*Fuck. At first I thought I’d gotten a loan from a regular bank, but now I find out it was a Sunshine Loan.*

I felt like a gambler who’d borrowed from loan sharks to keep playing, only to ruin his life.

But there was no point dwelling on it now.

Even if I could go back to that moment, I knew I’d make the same choice. All I could do was give a bitter smile.

It couldn’t be helped.

The stakes in those few gambles hadn’t been gold bars or checks. They’d been my life—and someone else’s.

If I hadn’t used One Annihilation at each of those moments of crisis, I wouldn’t still be alive.

*I’ve finally got some breathing room. I guess it’s time to pay my debt.*

I couldn’t sit down face-to-face and talk with the System, and I had no intention of whining at it. I’d already received more than enough of a gift, and it had warned me plenty of times.

Every path I’d walked until now had been my own choice.

*That’s enough. It is what it is.*

With those words, I cleared the jumble of thoughts from my mind.

Thinking about it on my own wouldn’t make anything better right now. I had to think about how the people around me felt, too.

I’m really a considerate person, aren’t I? No, wait a second.

“Then where’d that Taishan bastard go?”

“Huh?”

“Huh?”

Everyone blinked at my sudden question. One of the guides from the Nanman Beast Palace shuffled over and spoke.

“Um… the big fellow went to get something.”

Namho asked in bewilderment, “Went to get something?”

“Yes.”

“What on earth?”

“Well, um…”

The guide was about to say something when—

*Rustle, rustle, rustle!*

The bushes some fifty jang away shook, and a huge figure burst out. He was so massive you had to wonder if he was human.

“Taishan! Brought it!”

He raised the dark, murky thing in his hand.

“Taishan’s favorite thing in the world—no, a miracle cure for the sick Pavilion Master!”

The people watching stared blankly and murmured.

“That’s honey.”

“Right. A pot of honey.”

“Sorry to interrupt, but isn’t that a beehive, not a pot of honey?”

“That’s true, too.”

*Bzzzzzzzz!*

It was the first time I’d ever seen it.

Bees that big—and thousands of them all swarming together.

“……Primordial Heavenly Venerable. Gods of heaven and earth.”

Leaving Namho’s sorrowful voice behind, the rest of us quietly climbed back into the carriage.

Murim really wasn’t easy.
```
