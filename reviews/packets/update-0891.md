<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0891.txt",
      "sha256": "6f07f4d6b35a89a858c22b969913b368df377d12e6480c7a0bbba668be64a930",
      "bytes": 12697
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "74b6aadd0b97454144a0a4fe90daf4ba48ede79716db055aaca76c6890a6fdd3",
      "bytes": 1612
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "42391788f53c6c5ac3e1dcd23d6389823b2c8658da1a82bb5b05e797a4f8f5b6",
      "bytes": 230370
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "71da9953a2285b7657b3baecc884a3599cbbfa720f0c73369198ae1d0c18c623",
      "bytes": 927
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a06a8eaa722889792f8826cd100984bbebf015104166f3def71511df8da7601b",
      "bytes": 759
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "92d4f46a64a2ca6db8ce92b2642fa5ab0676dff9bf3e4f902891635b5059d60e",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "ea93c02c4b9ede9a2c75cfb4242a51d2e388d10c3d6be1ba1519b4ba45ea867f",
      "bytes": 1432
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "63a3853555a1826413a62f52bf4874b23cb753cdc3b38d669817ea5812e94a3c",
      "bytes": 1511
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "27e9f93d630b2b4d5b61e2160a64d4e83ac7926d53aa0281e9be82abbb2d3afa",
      "bytes": 973
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "d5adf3625d28d65df926800cdaeaf5e64bea44e72ef039bdd567569ca29863cf",
      "bytes": 815
    },
    {
      "path": "characters/Namho.md",
      "sha256": "fe06fda30d724540064efcc3448371fa81e4333650bff6b5a891f66cbbb03e13",
      "bytes": 973
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "af755ca06e333c14b3c3af890275c684bfe92c958145cdef001fb9b1aabe7962",
      "bytes": 936
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "7f4258f05ae6ed40152e2b9dfb06afcaca802d897620740c63663ba110dd5ea5",
      "bytes": 900
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "ae2f68201caa83ab4cc61c0b3f5007885801d5905d2731c417e1e14c59a84ff5",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "3707708d156a52116d1bbe6679218ac3ecfe3d78d491592e1b28fddf56c70e89",
      "bytes": 1074
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "5805ae7d870ce48847c40c12f40779ed52ce20c37cf3d3b52ac2ac8b4319d083",
      "bytes": 715
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "8713494a6fe9c012e3b60b28f2f90dca15db17fe1c91ef5bb06131be461d52b0",
      "bytes": 685
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "316109bbe3b069eaf51f374d4009e61d4ccec06834f1a7f2dc8137653500551a",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "48ddcbbc20bbd83a294df54034c4472ba72cc667bc095f1c343ef75d9c343115",
      "bytes": 260366
    }
  ],
  "estimated_tokens": 14794
}
-->

# Durable State Update — Chapter 891

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
1 and safe_through 891. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 891. Profile updates may replace only one
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
  "chapter": 891,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 891,
    "continuity_sources": [891],
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
    "The imperial banquet is three days away; So Gyo says the coming battle may be fiercer than the one over a decade ago.",
    "So Gyo believes Jin Taekyung may be the person she seeks and the person foretold by “that person,” but has not confirmed it; only she and the Emperor know the secret she withheld from Baek Yeon.",
    "So Gyo wears two matching, curved saber-like objects recovered from the flower garden; their purpose is unknown.",
    "Prince Shangshan remains in the enemy’s grasp, and Taekyung believes confrontation cannot be avoided.",
    "Ma Sanbao noticed Taekyung hiding near the Inner Palace and warned him to proceed carefully; he plans to contact Taekyung later.",
    "Taekyung has reached Jeok Cheongang’s pavilion in the Outer Palace.",
    "Taishan is staying with the group in the Outer Palace and has an enormous appetite for five-spice pork."
  ],
  "continuity_sources": [
    889,
    890
  ],
  "open_questions": [
    "Who is the person So Gyo seeks, and who foretold them?",
    "What secret do So Gyo and the Emperor share, and why might Jeok Cheongang joining Taekyung’s side be preferable to So Gyo?",
    "What will happen at the imperial banquet?",
    "What is the purpose of So Gyo’s two curved saber-like objects?",
    "Why, and by what process, were Murim assassins drawn into the conflict?"
  ],
  "safe_through": 890,
  "temporary_decisions": [
    "Retain “that person” for 그분; the foreteller is unidentified.",
    "Render 곡도 descriptively as “curved saber,” not as a proper name."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 마교     | **Demonic Cult**                                 |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 반박귀진 | **Returning to Simplicity** | Supreme Peak technique or phenomenon used by Jeok Cheongang. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 역용술 | **disguise technique** | Technique used by the Third Fiend to conceal his identity. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 887
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 889
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 886
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 889
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 890
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 883
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 890
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and Supreme Peak martial artist, leading the Depot in place of its bedridden leader, Cang Gong.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 884
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 883
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 889
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 878
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 878
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 888
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 890
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 888
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃891화



해후(邂逅)라고 표현하기에는 불과 며칠 정도 떨어져 있었을 뿐이지만, 그래도 반가운 건 반가운 거다.

그리고 말이 며칠이지, 체감상으로는 몇 달처럼 느껴졌던 것도 크게 한몫했고.

‘굵직한 일들이 하도 많았어야지.’

그래도 뭐랄까. 익숙한 얼굴들을 마주하니 낯선 곳이지만 잠시 집에 온 듯한 기분이 들어 좋다.

나는 순식간에 몰려든 일행들을 향해 웃으며 손을 흔들었다.

“이야, 다들 되게 오랜만에 보는 것 같네. 잘 지냈어요?”

반응은 즉각적이었다.

적천강은 이미 몇 시진 전에 봐 놓고 왜 유난이냐며 아무렇지 않은 척 콧방귀를 뀌었고, 사마표와 송일섬은 묵묵히 고개를 끄덕였으며, 내 갑작스러운 등장에 석상처럼 굳어 있던 주화란은 어느 순간 빛살처럼 계단을 내려오더니 안절부절못하는 목소리로 이렇게 말했다.

“으, 어. 은인. 아니, 각주님. 어디 성한 곳은 없으세요?”

“예?”

“아니, 아니에요. 말이 헛나왔어요. 그러니까 제 말은…….”

“다친 곳 없냐고요?”

“앗. 네!”

어느새 가까이 다가온 신의가 허허 웃으며 입을 열었다.

“크게 고초를 겪으신 것 같지 않아 다행입니다. 여기 계신 주 소저께서도 이제 한 시름 놓겠군요.”

주화란이 흠칫 몸을 떨었다.

“제가요?”

“아닙니까? 의원인 저보다 더 신경 쓰시던데요.”

“그…… 화룡각의 일원으로서 각주님의 신변을 걱정하는 건 당연한 거 아닌가요?”

“아, 그야 당연한 일이지요. 그렇고 말고요.”

손녀 말에 맞장구쳐 주는 할아버지처럼 고개를 끄덕인 신의가 나를 향해 눈을 찡긋했다.

“그렇다고 합니다.”

“어…….”

이 상황에서는 도대체 무슨 말을 해야 하나.

괜히 이상한 기분이 된 내가 다급하게 할 말을 찾고 있던 그때, 문득 머리 위로 어둠이 드리워짐과 동시에 축축한 무언가가 정수리에 닿았다.

툭. 투둑.

순간 천장에서 비가 샌 줄 알았다. 등 뒤에서 느껴지는 거친 호흡과 그 끈적거리는 타액을 느끼기 전까지는.

‘아. 이 십새.’

굳이 보지 않아도 정체를 알 것 같다. 고개를 슬쩍 들어 위를 바라보니 예상했던 한 사람이 침을 뚝뚝 흘리고 있었다.

“태산이는각주를다시만나서너무너무기쁘고반갑다.”

미친놈인가. 말 빨라진 것 봐.

“각주잘지냈나태산이는잘지냈다오향장육도먹고오향장육도먹고오향장육도먹었다.”

실컷 처먹기만 했단 소리다.

물론 지금 이 순간에도 녀석은 바로 앞에 있는 내가 아니라 한구석에 산더미처럼 쌓인 접시들을 응시하고 있었다.

“태산이는각주를도울만반의준비를끝마쳤다명령만내려라.”

“…….”

확실히 오향장육을 먹을 만반의 준비를 끝마친 것 같아서, 나는 해탈한 목소리로 명령을 내려 주었다.

“알겠으니까 식기 전에 처먹어.”

“태산이. 각주의 명을 받든다!”

어느 때보다 의욕 넘치는 대답과 함께, 육중한 몸을 날린 태산이 오향장육을 학살하기 시작했다.

그 끔찍한 살육의 현장을 흐린 눈으로 바라보던 나는 문득 잊고 있던 한 사람을 떠올렸다.

“잠깐. 남 노인은 어디 있어요?”

“여기 있다.”

허리를 붙잡고 어기적어기적 계단을 내려온 남호가 우울한 얼굴로 말을 이었다.

“잠깐 쉬고 있었다. 늙어서 그런지 몸이 예전 같지 않군.”

“아니, 어쩌다가 다쳤어요?”

“측간에 갔다가 그만.”

“저런. 미끄러지셨나 보네.”

“황궁이라 그런지 측간에까지 기름칠을 잘 해 놨더군. 천장 기둥을 붙잡고 있는데 힘이 빠지지 뭐냐.”

“천장 기둥이요? 바닥이 아니라?”

의아해하는 내게 신의가 속삭였다.

“측간에 숨어 태산 소협을 기습하려고 했던 것 같습니다.”

“…….”

“곧 괜찮아질 겁니다. 나이만 드셨지 몸은 아주 정정하셔서.”

지랄 났다. 진짜.

한숨을 푹 내쉰 나는 어느새 둥그렇게 주위를 둘러싼 사람들을 둘러보았다.

정상인도, 비정상인도 있었지만 그래도 나를 위해 황궁이라는 호굴(虎窟)까지 따라와 준 사람들이다.

임무의 위험성을 알았음에도 자신들의 하나뿐인 목숨을 걸었으니, 일을 논의함에 있어서 조금의 숨김이나 거짓이 있어서는 안 된다.

“생각만큼 오랫동안 자리를 비울 수 없으니까, 빠르게 말할게요.”

작게 심호흡한 나는 이야기를 시작했다.

아니, 시작하려고 했다.

쿰척. 쿰척. 파오후.

“…….”

제발 그만 좀 처먹어.



* * *



내가 지난 며칠간의 상황을 쉴 새 없이 쏟아낸 직후, 전각 내부는 고요한 적막에 휩싸였다.

사실 그럴 만도 하다.

이미 동창을 통해 일련의 상황을 알고 있었겠지만, 그들로서는 이 자리에서 처음 듣는 이야기도 있었으니까.

그리고 가장 먼저 침묵을 깨트린 사람은 바로 적천강이었다.

“일 한번 더럽게 꼬였군.”

작게 중얼거린 그의 눈빛은 침잠하게 가라앉아 있었다.

“초절정 고수만 여섯에 그 정도 수준의 금의위들까지…… 이래서 대국(大國)이라고 불리는 것인가?”

나는 무거운 마음으로 적천강의 말을 정정해 주었다.

“제가 직접 확인한 것만 그 정도입니다. 아직 숨겨 놓은 고수들이 있을 수도 있어요.”

“허.”

무림과 관은 언뜻 철저하게 분리되어 있는 것처럼 보이지만, 실상은 다르다.

대국은 곧 대륙이다. 황도에 웅크린 전력은 적천강조차도 신음할 만큼 강대하기 이를 데 없었다.

더군다나 예상치 못한 복병까지 있었으니까.

“우선 소교라는 그 여인에 대해 더 자세히 말해 보거라. 용모와 말투. 어떤 무기를 쓰고 어찌 움직이는지.”

적천강은 그 누구보다 소교의 존재를 경계하는 듯했고, 나는 내가 직접 보고 느낀 모든 것을 알려 주었다.

짧은 격돌이 이루어졌을 당시. 그녀가 보인 움직임까지 자세히 설명해 가면서.

그러나 강호에서 최소 세 손가락 안에 들어가는 연배의 적천강도, 식견이라면 어디에서도 떨어지지 않는 남호도 이렇다 할 대답을 내놓지 못했다.

“말투야 딱히 특정 지을 수 없으니 어쩔 수 없다 치더라도, 그런 용모에 연검을 쓴다는 고수에 대해서는 딱히 들은 바가 없다.”

“저 역시 노 선배의 말에 동감합니다. 암천의 주구 노릇을 하는 것을 보면 필시 사마외도(邪魔外道)에 속한 인물일 터인데…… 정마대전 당시 은영각이 파악했던 마두들 중에서도 그 정도의 여고수는 매우 드물었습니다.”

근심 어린 목소리로 대꾸한 남호가 나를 향해 고개를 돌렸다.

“혹시 이상한 점은 없었나? 정교한 인피면구나 역용술(易容術)을 사용했을 가능성도 무시할 수 없으니.”

나는 잠시 기억을 떠올려 봤지만, 이내 고개를 저었다.

무공의 경지가 깊어질수록 예리해지는 것이 눈썰미다.

인피면구를 아무리 잘 만든다 해도 한계가 있고, 역용술을 유지하는 데에도 끊임없는 공력 유지가 필요한 법인데 내가 본 바로는 조금의 기시감도 느껴지지 않았다.

“아닙니다. 적어도 느낀 바에 의하면 그런 수법과는 거리가 멀었어요.”

“하지만 혹시 모를 가능성이…….”

“그만. 저 녀석이 그렇다면 그런 것이다.”

이미 오래전부터 나와 같은 길을, 그리고 그보다 더 먼 곳까지 다다른 사람의 이해력은 무공을 익히지 않은 남호에 비할 바가 아니다.

남호의 말을 단호하게 끊어 낸 적천강이 천천히 턱을 쓰다듬었다.

“극상승의 보법에 반박귀진(返璞歸眞)의 경지라, 연배가 어느 정도라고?”

“아마도 서른쯤? 많이 쳐줘야 삼십 대 중반 정도로 보였습니다.”

“이립(而立) 어림에 그 정도의 무위를 갖춘다는 건 불가능……”

나와 눈이 마주친 적천강이 말꼬리를 흐렸다.

“……하진 않지만, 실로 불가능에 가깝다.”

“아니, 이야기 중에 왜 제 눈치를 보세요.”

“노부가 언제!”

“지금요.”

“지금 줘 터지고 싶으냐?”

“아뇨.”

“그럼 입 다물고 있어라.”

“옙.”

혁무진이 이런 기분이었구나.

‘미안하다. 돌아가면 잘해 줄게.’

나는 내심 반성하며 입을 다물었고, 찬물을 단숨에 들이킨 적천강은 입맛을 다셨다.

“제기랄. 둘 중 하나군. 천주가 어느 천고의 기재를 제자로 들여 지금까지 키웠거나, 아니면 반박귀진을 넘어 반로환동에 이른 노괴(老怪)거나.”

“개인적으로는 후자일 것 같긴 합니다. 남천마후도 마찬가지였고요.”

“그럴 가능성이 높겠지. 정마대전으로 천하가 뒤흔들릴 때도 심산유곡(深山幽谷)에 은거하던 이들이 있었다. 당장 노부도 그중 한 명이었으니 그 소교라는 계집도 아닐 거라는 보장이 없지.”

충분히 가능성 있는 이야기다.

마교의 낡은 하늘이 닫히고, 암천이라는 새로운 하늘이 열린 지 무려 반세기에 가까운 시간이 흘렀다.

현재에 이르러 암천의 휘하에서 모습을 드러낸 이들 중 상당수는 이른바 대마두(大魔頭)라 불리던 전대의 노고수였지만, 혈주와 서천마군. 그리고 남천마후와 같은 핵심 인물들은 오히려 세간에 알려지지 않은 인물들이었다.

‘소교도 그들과 같은 부류라고 보는 것이 맞겠지.’

하지만 소교의 정체를 알아내는 것보다 중요한 것은 따로 있었다.

충분히 제압 가능한 상황에서도 나를 풀어준 이유.

그것에 대한 의문만큼은 아무리 생각해도 쉽게 해결되지 않았다.

“모르겠습니다. 소교, 그 여자가 굳이 왜 그런 선택을 했는지.”

말없이 이야기를 듣고 있던 주화란이 불쑥 입을 열었다.

“저도 줄곧 그게 이해가 되지 않았어요. 각주님께는 실례가 될 수도 있는 말이지만…… 이미 그물에 걸린 물고기를 도로 풀어놓을 이유가 있나 싶어서.”

“아무래도 한 번에 일망타진하려는 의도가 아니겠소? 곧 열릴 대연회에서 말이오.”

옆자리에 있던 송일섬의 대꾸에 주화란이 고개를 내저었다.

“정보가 새어 나가면 도리어 곤란해지는 것은 그쪽이에요. 저들이 이렇게 나온 이상 우리 역시 혼신을 다해 결전을 치르지 않겠어요?”

맞는 말이다.

차라리 이 자리에 모인 사람들이 아군 측 전력의 전부라면 이해할 수 있겠지만, 마삼보를 중심으로 십 년이 넘는 세월 동안 준비해 온 반정군(反正軍)의 전력 역시 만만치 않을 것이다.

‘전력에서 승산이 없었다면, 애초에 반정은 꿈도 꿀 수 없었을 테니까.’

그렇다면 적들은 이 사실을 까맣게 모르고 있을까?

그럴 리가.

작금의 황제는 역모의 성공과 동시에 동창의 권한을 점차 축소시켰고, 이는 지금과 같은 상황을 우려하여 계속해서 견제해 왔다는 뜻이나 다름없다.

‘금의위 역시 무력이나 정보력에서 동창에 비해 결코 떨어지지 않는 집단이니, 철저한 감시도 해 왔겠지.’

적어도 내가 직접 겪은 황제는 그런 사람이었다.

철두철미하고, 심계가 깊으며, 훗날 화가 될 우환은 반드시 뿌리 뽑아야 하는 사람.

냉정하고도 잔혹한 지배자. 그만한 힘을 가진 대륙의 주인.

그런 그가 이 사태를 방관했다는 것은 도무지 설명하기 어렵다.

단 하나의 경우가 아니라면.

‘확신하고 있는 거야. 우리가 무슨 수를 쓴다 해도, 아무리 죽을힘을 다해 싸운다 해도 결과는 달라지지 않는다고.’

잡초는 밟고, 또 밟아도 시들지 않는다.

하지만 단번에, 모든 뿌리를 뽑는다면 잡초는 비로소 사라진다.

‘빌어먹을.’

공기가 무겁게 가라앉았다.
```

## Final English reading copy

```markdown
# Chapter 891

It had only been a few days—not long enough to call this a reunion—but it was still good to see everyone again.

And “a few days” was only on paper. It had felt more like a few months.

*There’d been so much going on.*

Still, how should I put it? Seeing familiar faces made this strange place feel, for a moment, like home. I liked that.

I smiled and waved at the group that had rushed over to me.

“Wow, it feels like ages since I’ve seen you all. How’ve you been?”

The reactions came at once.

Jeok Cheongang snorted as if nothing had happened, asking why I was making such a fuss when he’d already seen me a few shichen ago. Sama Pyo and Song Ilseom silently nodded. Ju Hwaran, who’d frozen like a statue when I suddenly appeared, came flying down the stairs in a flash. Her voice unsteady, she said,

“Y-You… Benefactor. No, Pavilion Master. Are you hurt anywhere?”

“Huh?”

“N-No, that’s not it. I misspoke. What I mean is…”

“You’re asking if I’m hurt?”

“Ah. Yes!”

The Divine Physician had come closer without my noticing. He chuckled warmly.

“I’m glad you don’t seem to have suffered too much. Young Lady Ju here can finally breathe a little easier, too.”

Ju Hwaran flinched.

“Me?”

“Is that not so? You seemed more worried than I was, and I’m the physician.”

“Th-That’s… As a member of the Fire Dragon Pavilion, isn’t it only natural that I’d worry about the Pavilion Master’s safety?”

“Ah, of course it is. Quite right.”

The Divine Physician nodded like a grandfather agreeing with his granddaughter, then winked at me.

“So she says.”

“Uh…”

What on earth was I supposed to say in this situation?

I felt strangely awkward and was frantically searching for something to say when a shadow suddenly fell over me. At the same time, something damp touched the crown of my head.

Plop. Plop.

For an instant, I thought rain was leaking through the ceiling. That was before I heard the rough breathing behind me and felt the sticky saliva.

*Oh. You bastard.*

I didn’t need to look to know who it was. I glanced up, and there he was, drooling exactly as I’d expected.

“Taishan is very, very happy and glad to see the Pavilion Master again.”

Was this lunatic for real? Look how fast he was talking.

“Pavilion Master doing well Taishan doing well Taishan ate five-spice pork and ate five-spice pork and ate five-spice pork.”

So all he’d done was stuff his face.

Even now, he wasn’t looking at me. He was staring at the mountain of plates piled in one corner.

“Taishan has finished preparing everything to help the Pavilion Master just give the order.”

“……”

He’d clearly finished preparing to eat five-spice pork, so I gave the order in a voice drained of all hope.

“Fine. Eat it before it gets cold.”

“Taishan will obey the Pavilion Master’s command!”

With an answer more enthusiastic than ever, Taishan hurled his massive body forward and began slaughtering the five-spice pork.

I watched the horrific scene through half-lidded eyes, then suddenly remembered someone I’d forgotten.

“Wait. Where’s Elder Namho?”

“I’m here.”

Namho came clomping down the stairs, one hand on his lower back, his face gloomy.

“I was resting for a moment. Maybe it’s because I’m old, but my body’s not what it used to be.”

“What happened? Did you hurt yourself?”

“I went to the privy, and then…”

“Oh no. Did you slip?”

“Palace privy or not, the place might as well have been greased. I was hanging on to a ceiling beam when my strength gave out.”

“The ceiling beam? Not the floor?”

The Divine Physician whispered to me as I stared at him in confusion.

“I believe he hid in the privy to ambush Young Hero Taishan.”

“……”

“He’ll be fine soon. He may be old, but he’s in excellent shape.”

This was a complete shitshow. Seriously.

I let out a deep sigh and looked around at the people gathered in a circle around me.

Some were normal, some weren’t, but they’d all followed me into the imperial palace—a tiger’s den—for my sake.

They knew how dangerous this mission was, and they’d risked their one and only lives. When discussing what to do, I couldn’t hide or lie about a single thing.

“I can’t stay away from my post as long as I’d like, so I’ll keep this quick.”

I took a quiet, deep breath and began to speak.

Or, I tried to.

Chomp. Chomp. *Pah-ooh.*

“……”

Please, stop eating.

* * *

As soon as I finished pouring out everything that had happened over the past few days, a hushed silence settled over the pavilion.

It made sense.

They’d already learned about some of it through the East Depot, but there were things they were hearing for the first time here.

The first to break the silence was Jeok Cheongang.

“This has gotten one hell of a mess.”

He muttered under his breath, his gaze sinking darkly.

“Six Supreme Peak masters, and Embroidered Uniform Guards of that caliber… Is this what they mean when they call it a Great Nation?”

I corrected him with a heavy heart.

“That’s only what I saw for myself. They could have other masters hidden away.”

“Hah.”

Murim and the government might look as though they were kept completely separate, but the truth was different.

A Great Nation meant a continent. The forces hunkered down in the imperial capital were so powerful that even Jeok Cheongang had to groan.

And there was another unexpected wild card.

“First, tell us more about that woman called So Gyo. Her appearance, her way of speaking. What weapon she uses and how she moves.”

Jeok Cheongang seemed more wary of So Gyo than anyone else. I told them everything I’d seen and felt myself, even going into detail about her movements during our brief clash.

Yet even Jeok Cheongang, who was among the three oldest in the martial world, and Namho, whose knowledge was second to none, couldn’t offer a clear answer.

“Her manner of speaking doesn’t give us much to go on. But I’ve never heard of a master with that appearance who uses a flexible sword.”

“I agree with Senior Jeok. If she’s serving Dark Heaven, she must be one of the demonic or heterodox martial artists. But even among the fiends the Hidden Shadow Pavilion identified during the Great Faction War, women of that caliber were very rare.”

Namho replied in a worried voice, then turned to me.

“Did you notice anything strange? We can’t rule out the possibility that she was using a finely crafted human-skin mask or a disguise technique.”

I tried to recall what I’d seen, then shook my head.

The higher one’s martial arts realm, the sharper one’s eye became.

No matter how well made a human-skin mask was, it had its limits. And maintaining a disguise technique took a constant supply of internal energy. From what I’d seen, I hadn’t felt the slightest trace of anything like that.

“No. At least, from what I felt, it didn’t seem like she was using either of those methods.”

“But we can’t rule out the possibility…”

“Enough. If that boy says so, then that’s how it is.”

Jeok Cheongang had walked the same path I had, and gone farther down it. His understanding was beyond anything Namho, who hadn’t learned martial arts, could match.

After cutting Namho off firmly, Jeok Cheongang slowly stroked his chin.

“She has a supreme footwork technique and has reached Returning to Simplicity. How old did you say she was?”

“Maybe thirty? She looked no older than her mid-thirties at most.”

“To reach that level of martial prowess around thirty is impossi—”

Jeok Cheongang met my eyes and trailed off.

“—not impossible, but about as close to it as you can get.”

“Why are you looking at me like that while we’re talking?”

“When did this old man do that?”

“Just now.”

“Do you want to get your ass kicked?”

“No.”

“Then shut up.”

“Yes, sir.”

So this was how Hyuk Mujin felt.

*Sorry. I’ll treat you better when we get back.*

I kept quiet, chastened, and Jeok Cheongang downed a cup of cold water in one go before clicking his tongue.

“Damn it. It’s one of two things. Either the Lord of Heaven took some once-in-a-millennium prodigy as his Disciple and raised her all this time, or she’s an old monster who’s gone beyond Returning to Simplicity and Returned to Youth.”

“Personally, I think it’s the latter. The Southern Heaven Demon Empress was the same.”

“That’s probably more likely. Even when the world was shaken by the Great Faction War, there were people living in seclusion in remote mountains and valleys. This old man was one of them. There’s no guarantee that the woman called So Gyo wasn’t, too.”

It was a perfectly plausible explanation.

Nearly half a century had passed since the old sky of the Demonic Cult closed and a new one, Dark Heaven, opened.

Many of the people who’d emerged under Dark Heaven’s command in the present day were old masters from a previous generation, the kind known as fiends. But key figures like the Blood Lord, the Western Heaven Demon Lord, and the Southern Heaven Demon Empress were people the world hadn’t known about at all.

*So it makes sense that So Gyo belongs in the same category.*

But there was something more important than discovering So Gyo’s identity.

Why had she let me go when she could have subdued me?

No matter how much I thought about it, I couldn’t find an easy answer.

“I don’t know. Why did So Gyo go out of her way to make that choice?”

Ju Hwaran, who’d been listening without a word, suddenly spoke up.

“I haven’t been able to understand it either. This may be rude to the Pavilion Master, but… why let a fish that’s already been caught in the net go free?”

“Perhaps they intend to catch us all at once at the grand banquet that’s coming up.”

Song Ilseom, seated beside her, answered. Ju Hwaran shook her head.

“If the information got out, it would be a problem for them instead. Now that they’ve made this move, wouldn’t we fight the decisive battle with everything we have?”

She was right.

It would’ve made sense if the people gathered here were the entirety of our side’s forces. But the restoration army that had spent more than a decade preparing under Ma Sanbao’s leadership was no joke either.

*If they didn’t have a chance of winning with their forces, they never would’ve dreamed of staging a coup in the first place.*

So did the enemy know nothing about this?

Of course not.

The current Emperor had gradually reduced the East Depot’s authority as soon as the rebellion succeeded. That was practically proof that he’d kept it in check because he’d been worried about a situation like this.

*The Embroidered Uniform Guard is no weaker than the East Depot in either force or intelligence. They must have been keeping a close watch, too.*

At least, that was the impression I’d gotten of the Emperor.

Thorough, calculating, and someone who would always uproot a future source of trouble.

A cold and ruthless ruler. The master of a continent with the power to match.

It was hard to explain why someone like that had stood by and let all this happen.

Unless there was only one possibility.

*He’s certain. No matter what we try, no matter how desperately we fight, the outcome won’t change.*

You could trample weeds again and again, and they still wouldn’t wither.

But pull out every root in one go, and the weeds would finally be gone.

*Damn it.*

The air sank heavily around us.
```
