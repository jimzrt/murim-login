<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1022.txt",
      "sha256": "ccba32c7823f97bc999e1f04d3fb63489b132d1789bc6e3773520ee05c182752",
      "bytes": 13488
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "18f19c74860a3f7943c8001dad01a2a663df1c610175f254ac50c0ca1c230cd1",
      "bytes": 1372
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0dafd418aa393e495962bfa62c9107ec29bc8b93a7018fc838daf88d8b83fce0",
      "bytes": 238757
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "6ad45538588618319919aa50af634253dddac9581b239f33fc08418cb5df7bfc",
      "bytes": 927
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a20e9cef1f8e89507ba92243045cb63815dfe46059e0ce0f61b1372b6128f54e",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "c70f97dfc92ff78a64c3b9868bb31b56677028c70176bf2b51c0e589d847e517",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "912ebf7322726f78d8831d2d8b5b99d5bf5941326f37d91636b10260f2f2da4c",
      "bytes": 1502
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "5ba7d1c6d2b00df5f41489a6d87fc74d3c31d25bcc65746f4c462d847d1343c3",
      "bytes": 974
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "692551a20505db85c5a88d3b71ae485e610fb1e74e4dd2417b8f400ee2878237",
      "bytes": 673
    },
    {
      "path": "characters/Namho.md",
      "sha256": "07c351c9961a9c137d6c9dc6c085efb1d99bf97eb7fd721fcd1c6d02603fe945",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "eb6037b0d9189c49566da30453a34283f505383c50a3bbd0c646bf32b6c7a22c",
      "bytes": 1069
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "1466d5ed6e7b24d4d33666f45335a1b979b3d35be2ea91d850888d15b7e7d79b",
      "bytes": 778
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "3cf825bb374f49183907efdd781c722742762ef5d71afb905afec046b09507e7",
      "bytes": 742
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "15f2d2bedc0f95bbfd98fd6ccc2764077f1429bfd15da23d3aa28f27e2104f7e",
      "bytes": 980
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "507b0fe7baa2fbe88cd266588cf80fe0017827f7315f54f4cb4544ce93792695",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "107226d29d3a00596e274bb32d326b67d072d4bda85484b408975b0987bfdde5",
      "bytes": 277335
    }
  ],
  "estimated_tokens": 14116
}
-->

# Durable State Update — Chapter 1022

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
1 and safe_through 1022. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1022. Profile updates may replace only one
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
  "chapter": 1022,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1022,
    "continuity_sources": [1022],
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
    "Jin Taekyung ordered the Gansu leaders to gather all forces from the Qilian Mountains at the Great Snow Mountain; Sima Gong agreed, and Zhongnan consented.",
    "Sama Pyo has returned to Taekyung’s group under Sima Gong’s order to watch their every move; Taekyung believes Pyo is now acting as a spy.",
    "Sima Gong says he seeks the Black Dragon Demon Gate’s resurgence and Pyo’s eventual rule over Gansu; he says their goal is unchanged despite setbacks.",
    "Dark Heaven captured Dunhuang after breaching the Jade Gate Pass and is advancing toward the Great Snow Mountain; the defense of Dunhuang suffered catastrophic losses.",
    "The Kongtong Sect Leader escaped Dunhuang, but his whereabouts and the fate of the other survivors remain unknown.",
    "A secret letter received by Sama Pyo was suspected to have come from Gansu or Qinghai; its sender, contents, and purpose remain unknown."
  ],
  "continuity_sources": [
    1021
  ],
  "open_questions": [
    "Who sent Sama Pyo the secret letter, what did it say, and what was its purpose?",
    "Where is the Kongtong Sect Leader, and what became of Dunhuang’s surviving troops?",
    "Who or what does Sima Gong consider the other tiger, and what is the full scope of his unchanged plan?"
  ],
  "safe_through": 1021,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 사마공    | **Sima Gong**      |
| 종남파    | **Zhongnan Sect**                |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 신법     | **movement technique**                           |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사매     | **Junior Sister**                            |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 감숙     | **Gansu**              |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 마중걸 | **Ma Junggeol** |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 검룡 | **Sword Dragon** | Epithet of Nangong Ok; one of the Ten Dragons and Phoenixes. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 사백 | **Senior Martial Uncle** | Zhongnan Sect title used for a senior of the speaker’s Master’s generation. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
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
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 마중걸 | 적천강 | visiting horse-caravan chief to legendary martial master | Great Hero Jeok Cheongang | polite and deferential | Recognizes Jeok as the Fire King. |
| 마중걸 | 사마공 | visiting group leader to sect leader | Sect Leader Sima | polite and respectful | Addresses him as 사마 문주 while explaining Ningxia and Baekma Bang. |
| 사마공 | 마중걸 | sect leader to visiting group leader | you | formal and probing | Uses 자네 while questioning Ma Junggeol about following Dark Heaven. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 986
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1021
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1020
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1021
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1015
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1017
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** Though timid by nature, he is earnest and protective of his sworn brothers, loyal to the benefactor who helped them reform, and willing to bear personal risk for their mission.
- **Voice:** Not established
- **Relationships:** He leads six sworn brothers who, with him, are known as the Seven Masters of Baekma Bang, and trusts the benefactor they call the Lord.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1018
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1021
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he is protective of Taishan and pragmatic in combat; he recognizes that his father's ruthless, survival-driven worldview shaped him, even as its influence weighs on him.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir; his father's ruthless treatment of family shaped his rise and remains a source of inner constraint. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, and Sima Gong has now ordered him to spy on Taekyung's group. He was Ju Hwaran's former fiancé in a political engagement and is openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1021
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1016
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1016
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1018
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1022화



물경 오천을 아우르는 인마는 그야말로 죽을힘을 다해 내달렸다.

한 근이라도 무게를 가볍게 하고자 최소한으로 지니고 있던 식량과 물자도 버렸고, 말들의 체력 안배도 신경 쓰지 않은 채 채찍을 휘둘렀다.

혹여 말이 거품을 물고 쓰러지기라도 하면 두 발로 뛰었고, 모든 공력을 쏟아부어 경신법을 펼쳤다.

제법 수련을 쌓은 무인이라 할지라도, 극도의 피로를 느낄 수밖에 없는 강행군.

특히 감숙 무림인들과는 달리, 두어 번의 짧은 휴식이 고작이었던 종남파와 화룡각 대원들에게는 마지막 한나절 동안의 시간이 마치 십 년처럼 느껴졌을 것이다.

하지만 모두의 한계를 극한까지 끌어올린 짧은 강행군 덕분에, 우리는 등 뒤에서 비쳐오는 서광(曙光)과 함께 모습을 드러낸 새하얀 설산을 확인할 수 있었다.

‘대설산(大雪山).’

명칭에 담긴 의미 그대로, 새벽의 여명을 받아 빛나는 눈 덮인 산맥은 눈이 부시도록 희었고 그만큼 이질적이었다.

아니, 어쩌면 가장 이질적인 것은 이 변덕스러운 기후일지도 몰랐다.

‘분명히 한 시진 전까지만 하더라도 주위가 온통 사막이었는데.’

언제 그랬냐는 듯, 함박눈을 펑펑 쏟아내는 하늘을 힐끗 바라본 나는 이내 다시 대설산을 바라보았다.

구름과 맞닿은 수십여 개의 높은 봉우리와 굽이진 산맥.

아직 완전히 벗겨지지 않은 어둠에 잠겨 있는 거대한 자연의 장벽은 고요했고, 서서히 속도를 늦추며 가까워지는 오천의 인마 사이로는 경계와 불안감이 감돌았다.

당연한 일이었다.

지금으로부터 한나절 전, 공동파를 중심으로 형성되어 있던 돈황(敦煌)의 최전선이 처참하게 무너졌다는 소식은 이제 모르는 이가 없었으니까.

‘물론 거리와 시간을 따져봤을 때, 대설산이 이미 암천의 손아귀에 떨어졌을 가능성은 적지만…….’

전쟁은 확률로 수식할 수 없는, 그야말로 변화무쌍한 괴물이다.

단순히 사술(邪術)이라는 단어로 정의하기 힘든 기이한 힘을 사용하는 적들과 맞서 싸워야 한다면 더더욱.

‘아무리 그래도 공동파가 이렇게 쉽게 무너질 줄은 몰랐지만.’

물론 냉정하게 말하자면 공동파의 전력은 구파일방 중에서도 수위에 꼽힐 만큼은 아니다.

그러나 장문인을 필두로 무려 세 명의 초절정 고수를 보유했고, 핵심 전력이라 할 수 있는 본산 제자들의 무공 역시 출중하다는 것이 호사가들의 평가.

그런데도 며칠은커녕 불과 한나절도 버티지 못했다니, 이미 암천과 여러 번에 걸쳐 충돌했던 나조차도 놈들의 전력을 쉽사리 가늠하기 힘들 정도였다.

‘분명 사전의 방비도, 전력도 충분했을 텐데.’

공동파 그 자체라 할 수 있는 세 명의 초절정 고수와 일천의 제자들. 그런 그들을 중심으로 결집한 물경 일만의 아군.

마중걸이 가져온 정보 덕분에 암천의 대군세가 최소 삼만에 달한다는 것은 알고 있었지만, 수성(守城)과 공성(攻城)의 차이는 어마어마하다.

그리고 나는 암천이 그 정도의 격차를 뛰어넘어 이렇게까지 일방적으로 아군을 짓뭉갰다는 소식에, 문득 한 가지 짐작을 떠올릴 수밖에 없었다.

‘놈들 중에 최소 세 명 이상의 초절정 고수가 존재한다. 만약 그게 아니라면…… 엄청난 고수가 있겠지. 그것도 압도적인 무위로 전장을 지배할 수 있을 정도의.’

전자라면 다행이지만, 후자의 경우라면 힘겨운 싸움이 될 것이다.

무림인이라고 해서 다 같은 무림인이 아니듯, 이른바 초인(超人)이라 불리는 이들 역시 마찬가지니까.

산 밑에 있는 이들은 모른다.

저 거대한 산자락에 몇 그루의 나무가 있고, 얼마나 가파른 협곡이 존재하는지.

멀리서 보았을 때는 그저 엇비슷하게만 느껴지는 수십여 개의 산봉우리들이, 가까이에서 지켜보면 얼마나 제각각의 높낮이를 지녔는지.

공동파를 포함하여 일만에 달하는 아군이 궤멸에 가까운 타격을 입고 퇴각할 수밖에 없었던 것은, 바로 그런 초인들의 격차 때문일 것이다.

‘물론 우리 역시 엄청난 전력이지만, 과연 암천이 이 사실을 모르고 감숙성에 수만의 대군을 쏟아부었을까?’

나와 적천강. 종남파의 세 노도사와 흑야왕 사마공까지.

당장 이 자리에 있는 초절정 고수만 무려 여섯이고, 감숙 일대를 가로지르는 수천의 인마는 어디에서나 눈에 띄기 마련.

결국 내가 내린 결론은 하나였다.

‘놈들이 감숙으로 진격한 이유는, 충분히 승산이 있다고 생각했기 때문이겠지.’

그렇다면 네 명의 마군과 마후를 잃었음에도 그토록 자신할 수 있는 이유는 무엇일까.

소림혈사 이후 종적을 감추었던 혈주(血主)?

아니면 지금껏 암천이 드러내지 않았던 또 다른 전력?

그것도 아니라면…….

‘천주(天主)?’

나도 모르게 입술을 비집고 흘러나온 그 두 글자에, 본능처럼 등골이 서늘해진 바로 그 순간이었다.

쐐애애액!

불현듯 울려 퍼진 날카로운 파공성. 소리를 쫓아 고개를 돌리자, 대설산의 깊은 산자락에서 차례대로 솟구치는 불꽃이 시야에 들어왔다.

펑, 펑, 퍼벙!

한 번, 두 번. 그리고 마지막 세 번.

짧은 시간 차를 두고 연달아 허공을 물들이는 폭죽과 함께, 새하얀 옷을 뒤집어쓰고 있던 산자락 위로 붉은 선이 그어졌다.

‘저건.’

신호다.

대설산을 점령한 아군이 폭죽과 횃불을 통해 보내는 신호.

그와 동시에 한껏 촉각을 곤두세우고 있던 사람들 사이에서 안도의 한숨이 흘러나왔다.

당장이라도 뽑아 들 것처럼 검파에 손을 얹고 있던 혁무진과 송일섬, 굳은 얼굴로 전방을 주시하던 주화란과 남호도 마찬가지였다.

그러나 그들 중 단 한 사람 예외가 있다면, 그건 한나절 전부터 다시 화룡각에 합류한 사마표였다.

‘……저 녀석.’

당장이라도 묻고 싶었다.

왜 줄곧 아무런 말도 하지 않는지.

모두가 긴장하고 경계할 수밖에 없던 와중에도, 마치 이럴 줄 알았다는 것처럼 당연하게 신색을 유지할 수 있는지.

하지만 묻지 않았다. 물을 수 없었다.

아직까지도 의기소침한 태산과 함께 말머리를 나란히 한 채 달리는 사마표의 모습을 복잡한 눈빛으로 바라보던 나는, 이내 말없이 고개를 돌렸다.

최근에 들었던 적천강의 물음을 다시금 떠올리며.



‘사마표와 태산. 그 두 녀석이 사마공의 밀명으로 일을 꾸미고 있다면, 그리고 그 밀명이 암천과 연관이 있다면…… 너는 어찌하겠느냐.’



글쎄. 어찌해야 할까.

아직도 정확한 답을 찾지 못한 마음속 의문과 함께, 나는 조용히 말고삐를 힘주어 움켜쥐었다.

눈앞의 현실과 달리, 동쪽에서 번져오는 여명은 대설산을 환하게 물들이고 있었다.



* * *



“커……헉.”

울컥, 검붉은 핏물을 토해 낸 사내는 입술을 떨었다.

눈처럼 새하얗던 도포(道袍)는 피와 먼지로 더럽혀 진지 오래였고, 초점이 흐릿한 눈동자는 시야도 제대로 분간하지 못했다.

하지만 그럼에도 불구하고, 사내는 손에 쥔 검을 놓지 않았다. 도저히 놓을 수 없었다.

‘아직, 아직 끝나지 않았다.’

언제나 듬직하던 대사형도, 호랑이 같았던 사백도, 조카나 다름없이 생각했던 어린 사매도 이제는 곁에 없다.

죽었다. 단 한 사람도 빠짐없이 그들 모두가.

목이 잘려서. 심장이 관통당해서. 혹은 흔적도 찾아볼 수 없이 산산조각으로 흩어져서.

그렇기에 일어나야 했다. 복수해야 했다.

으득.

온 힘을 다해 악문 잇새 사이로 핏물이 터졌다.

감각이 마비된 탓에 비릿한 혈향조차 느껴지지 않는 상태.

사내는 자신의 핏물을 생명수처럼 받아 마셨다.

비틀거리는 두 다리를 애써 일으켜 세우고 과거 스승으로부터, 사문(師門)으로부터 하사받은 애검을 눈앞의 적을 향해 휘둘렀다.

그 어느 때보다 처절한 기세로. 마지막 남은 한 조각의 힘조차 쥐어 짜내어.

“으. 으아아아!!!”

목의 핏줄이 도드라질 만큼 맹렬한 기합과 함께 검을 내리그은 그 순간. 사내는 불현듯 기이한 감각에 사로잡혔다.

스륵.

마치 시간이 멈춘 듯했다.

피부에 와닿는 공기도, 어디선가 불어오던 바람도, 그리고 사내의 손끝을 따라 내리그어지는 검신도.

모든 것이 느려졌고, 동시에 선명했다.

‘이건.’

사내는 전율했다.

삼십여 년의 짧지 않은 인생을 통틀어, 단 한 번 느껴 보았던 감각.

뼈를 깎는 수련 끝에 마침내 절정의 경지에 오르던 그 날, 깨달음을 얻기 직전의 자신이 그랬다.

무아(無我).

무인이라면 누구나 바라마지 않는, 잠시나마 스스로의 존재마저 잊은 채 더 높은 경지를 향해 나아가는 깨달음의 순간.

‘아. 아아.’

사내의 눈동자가 잘게 떨렸다.

어느덧 되돌아온 초점과 함께 또렷해진 시야 너머로, 느려진 시간 속에 갇혀 버린 한 중년인이 보였다.

아니, 단신으로 일백이 넘는 사문의 식구들을 몰살시켜 버린 괴물이.

하지만 이제는 아니었다.

조금 전까지만 하더라도 눈으로 좇을 수도 없을 만큼 빨랐던 괴물은 지금 이 순간 옴짝달싹하지 못한 채 그 자리에 굳어 있었고, 사내의 검은 느려진 시간 속에서 놈의 정수리를 향해 떨어져 내리는 중이었다.

‘죽어라.’

사내는 확신했다.

지금의 깨달음으로 자신의 무위가 눈부실 정도로 진일보했다는 것을.

오랫동안 앞을 가로막고 있던 벽을 허물어트리고, 마침내 팔성(八成)의 경지에 오른 복마검(伏魔劍)이 눈앞의 괴물을 베어 가르리라는 것을.

그리고 다음 순간.

쐐액! 턱.

빛살처럼 손을 뻗어 검신을 움켜잡은 괴물의 모습에, 사내는 비로소 깨달았다.

이 모든 것이 착각이었음을.

느려진 것은 시간이 아니라, 오직 자기 자신뿐이었다는 것을.

콰드득!

산산조각이 난 애검과 함께 사내를 둘러싼 비몽(悲夢)이 깨져 나간다. 넋 나간 그의 눈동자에 웃고 있는 괴물의 모습이 비쳤다.

“혼자서 허우적대는 꼴이 제법 볼만하던데. 어때, 혹시 모르니 한 번 더 기회를 줄까?”

사내는 멍하니 눈앞의 적을 바라보았다.

처음으로 가까이에서 본 괴물의 얼굴은, 전신에 피를 뒤집어썼다는 것을 제외한다면 너무나도 평범한 중년인이었다.

아마도 그래서였을 것이다.

이미 그 실체를 뼈저리게 느꼈음에도, 말이 통하지 않을 상대라는 사실을 알고 있음에도 애써 목소리를 쥐어 짜낸 것은.

“왜, 왜 이런 짓을…….”

“뭐?”

괴물, 아니 중년인이 눈살을 찌푸렸다.

“왜 이런 짓을 하냐니. 그런 한심한 질문이 어디 있나? 차라리 어부에게 왜 물고기를 잡냐고 물어보는 게 낫겠군.”

“……!”

“그리고 이건 모두 자네들이 자초한 거야. 얌전히 투항하면 지금 당장은 살려 준다고 그렇게 말했는데 꼭…… 하여간 말코 도사 새끼들은 피를 봐야 말을 듣는다니까.”

한숨을 푹 내쉰 중년인이 딱하다는 눈빛으로 사내를 바라보았다.

“보아하니, 자네에게도 원하는 대답을 듣기에는 글러먹은 것 같군.”

이미 회광반조(回光返照)의 문턱에 접어든 사내가 흐릿한 목소리로 대답했다.

“처, 천벌을 받을 것이다.”

“뭐? 천벌? 지금 천벌이라고 했나?”

눈을 동그랗게 뜬 중년인이 돌연 낄낄거리며 웃었다. 그리고 어느 순간, 흐릿해진 그의 손이 사내의 가슴을 관통했다.

콰직!

뼈와 살이 으스러지는 격통에 활처럼 휘는 허리. 사내는 조금씩 까맣게 물들어가는 시야 속에서, 아무 일도 없는 것처럼 조각구름이 흘러가는 하늘을 보았다.

마지막으로 귓가를 파고드는 음성과 함께.

“보이나? 새로운 하늘이.”

“……!”

콰드득, 털썩!

뽑혀져 나오는 손과 함께 허물어지는 신형.

공동파 제일의 후기지수라 불리는 공동검룡(崆峒劍龍)의 시체를 짓밟은 중년인은, 문득 고개를 돌려 저 멀리 펼쳐진 거대한 산맥을 바라보았다.

대설산.

곧 무수한 핏물로 붉게 물들 그곳은, 떠오르는 햇빛을 받아 눈부시게 빛나고 있었다.

“자, 어디 한번 한바탕 놀아 볼까.”

빙긋 미소 짓는 중년인의 등 뒤로, 거대한 울림이 대지를 떨어 울리기 시작했다.
```

## Final English reading copy

```markdown
# Chapter 1022

The five thousand men and horses pushed themselves to the limit as they raced forward.

They threw away even the food and supplies they’d been carrying in the barest quantities, trying to lighten their loads by even a single *geun*. They whipped their horses on without a thought for pacing them.

If a horse foamed at the mouth and collapsed, they ran on foot, pouring all their internal energy into their movement techniques.

It was a forced march that would leave even a well-trained martial artist utterly exhausted.

For the Zhongnan Sect and Fire Dragon Pavilion members, who had managed only a couple of brief rests unlike the martial artists of Gansu, the final half day must have felt like ten years.

But thanks to the short forced march that had pushed everyone to their limits, we spotted the snow-white mountain range appearing alongside the first light shining over our backs.

*The Great Snow Mountain.*

True to its name, the snow-covered peaks glowed in the dawn light, dazzlingly white and utterly alien.

No—perhaps the strangest thing of all was this fickle weather.

*It was nothing but desert all around us just two hours ago.*

I glanced up at the sky, which was dumping great flakes of snow as if it had never been otherwise, then looked back at the Great Snow Mountain.

Dozens of high peaks met the clouds, and the range wound between them.

The colossal barrier of nature still shrouded in darkness was silent. Wariness and unease spread among the five thousand men and horses as they gradually slowed and drew closer.

It was only natural.

By now, everyone had heard the news that the front line at Dunhuang, built around the Kongtong Sect, had been utterly crushed half a day ago.

*Of course, given the distance and the time, it’s unlikely the Great Snow Mountain has already fallen to Dark Heaven…*

War was a monster too changeable to be reduced to probabilities.

Especially when we had to fight enemies who wielded bizarre powers that were hard to define with the simple term *dark arts*.

*Still, I never thought the Kongtong Sect would fall this easily.*

To be fair, the Kongtong Sect’s strength wasn’t among the highest of the Nine Sects and One Gang.

Even so, according to the gossips, it had three Supreme Peak masters, including its Sect Leader, and its main disciples—the core of its strength—were also accomplished martial artists.

Yet it hadn’t held out for days. It hadn’t even lasted half a day. Even I, despite having clashed with Dark Heaven several times, had trouble gauging their strength.

*The Kongtong Sect must have had enough time to prepare, and enough strength to defend itself.*

Three Supreme Peak masters who embodied the Kongtong Sect, a thousand disciples, and a force of no less than ten thousand gathered around them.

Thanks to the information Ma Junggeol had brought, we knew Dark Heaven’s army numbered at least thirty thousand. But there was an enormous difference between defending a fortress and attacking one.

Hearing that Dark Heaven had overcome such an advantage and crushed our forces so one-sidedly brought one possibility to mind.

*There must be at least three Supreme Peak masters among them. If not… then they have one monstrously powerful master. Powerful enough to dominate the battlefield with sheer martial might.*

The first possibility would be fortunate. The second would make for a hard fight.

Just as not every martial artist was alike, neither were the people called superhuman.

Those at the foot of the mountain didn’t know how many trees stood on its vast slopes or how many steep gorges cut through it.

The dozens of peaks that looked much the same from afar had heights and shapes that varied wildly when you saw them up close.

That difference between superhumans was why the force of ten thousand, including the Kongtong Sect, had suffered near-annihilation and been forced to retreat.

*Our force is formidable too. But did Dark Heaven really pour tens of thousands of troops into Gansu without knowing that?*

Jeok Cheongang, myself, the three old Daoists of the Zhongnan Sect, and Sima Gong, the Black Night King.

There were six Supreme Peak masters right here, and the thousands of men and horses crossing Gansu were bound to be noticed wherever they went.

In the end, I reached one conclusion.

*They must have advanced into Gansu because they believed they had a good chance of winning.*

Then what could make them so confident despite losing four Demon Lords and a Demon Empress?

The Blood Lord, who had vanished after the Shaolin Bloodshed?

Or some other force Dark Heaven had yet to reveal?

Or…

*The Lord of Heaven?*

Just as those two words slipped from my lips without my realizing it, a chill ran down my spine by instinct.

Whoosh!

A sharp whistle suddenly rang out. I turned toward the sound and saw flames rising one after another from deep in the Great Snow Mountain.

Boom. Boom. Boom!

Once, twice. Then three times in a final burst.

The fireworks burst across the sky in quick succession, and a red line appeared along the mountain slope, still blanketed in white.

*That’s…*

A signal.

The forces who had taken the Great Snow Mountain were signaling with fireworks and torches.

A sigh of relief passed among the people who’d been on edge.

Hyuk Mujin and Song Ilseom, their hands resting on their sword hilts as if ready to draw at any moment, were no exception. Neither were Ju Hwaran and Namho, watching ahead with tense expressions.

But there was one exception among them: Sama Pyo, who had rejoined the Fire Dragon Pavilion half a day earlier.

*…That guy.*

I wanted to ask him right then and there.

Why had he been silent the whole time?

How could he keep his composure as if he’d expected this, even while everyone else had been forced to stay tense and wary?

But I didn’t ask. I couldn’t.

I watched Sama Pyo riding alongside the still-dejected Taishan, my gaze tangled with conflicting thoughts, then quietly turned away.

Jeok Cheongang’s question from recently came back to me.

*“If Sama Pyo and Taishan are up to something on Sima Gong’s secret orders, and those orders are connected to Dark Heaven… what would you do?”*

*Hell if I know. What should I do?*

With that question still unanswered in my heart, I silently tightened my grip on the reins.

Unlike the reality before me, the dawn spreading from the east was bathing the Great Snow Mountain in light.

* * *

“Guh… ack.”

The man’s lips trembled as he vomited a mouthful of dark red blood.

His Daoist robe, once as white as snow, had long since been stained with blood and dust. His unfocused eyes could barely make out what was in front of him.

And yet, he didn’t let go of the sword in his hand. He couldn’t.

*Not yet. It isn’t over.*

His ever-reliable Senior Brother, his tiger-like Senior Martial Uncle, and the young Junior Sister he’d thought of as a niece were no longer by his side.

They were dead. Every last one of them.

Their heads had been cut off. Their hearts pierced. Or their bodies blown apart so completely that not a trace remained.

That was why he had to rise. He had to take revenge.

Crack.

Blood burst between his clenched teeth.

His senses had gone numb; he couldn’t even smell the metallic tang of blood.

The man drank his own blood as if it were the elixir of life.

He forced his unsteady legs upright and swung the beloved sword he’d received long ago from his Master, from his sect, at the enemy before him.

With more desperation than ever. Squeezing out even the last scrap of strength he had left.

“Ugh. Aaargh!”

At the moment he brought his sword down with a ferocious shout that made the veins in his neck stand out, the man was suddenly seized by a strange sensation.

*Whoosh.*

It was as if time had stopped.

The air against his skin, the wind blowing from somewhere, even the sword blade falling with the movement of his hand—

Everything slowed, and at the same time, everything grew clear.

*This is…*

The man shuddered.

In all his thirty-some years of life, he had felt this sensation only once before.

It had happened on the day he finally reached the Peak realm after grueling training, just before he gained enlightenment.

*No-self.*

The moment of insight every martial artist longed for: a brief instant when they forgot even their own existence and advanced toward a higher realm.

*Ah. Aah.*

The man’s eyes trembled.

His focus returned, and beyond his now-clear vision he saw a middle-aged man trapped in the slowed flow of time.

No—a monster who had slaughtered more than a hundred members of his sect all by himself.

But not anymore.

The monster, who had been too fast for him to follow with his eyes only moments ago, was now frozen in place, unable to move. The man’s sword was falling through the slowed time, toward the crown of the monster’s head.

*Die.*

The man was certain.

This enlightenment had made his martial might advance by leaps and bounds.

He had broken through the wall that had held him back for so long. His Demon-Subduing Sword had finally reached eight-tenths mastery, and it would cut down the monster before him.

And then—

*Whoosh! Clack.*

The monster reached out at the speed of light and caught the blade in his hand.

Only then did the man understand.

It had all been an illusion.

It wasn’t time that had slowed. It was only him.

Crack!

The man’s nightmare shattered along with his beloved sword. In his vacant eyes, he saw the monster smiling.

“You flailing around by yourself was quite a sight. How about I give you another chance, just in case?”

The man stared blankly at the enemy before him.

The monster’s face, seen up close for the first time, belonged to such an ordinary-looking middle-aged man—if you overlooked the blood covering him from head to toe.

Maybe that was why, even after feeling the truth of what he was down to his bones, even knowing that he was beyond reason, the man forced his voice out.

“Why… why are you doing this?”

“What?”

The monster—no, the middle-aged man—furrowed his brow.

“Why am I doing this? What a pathetic question. You might as well ask a fisherman why he catches fish.”

“……!”

“And this is all your own fault. I told you I’d spare you for now if you surrendered quietly, but you had to… Honestly, those damned Daoist bastards don’t listen until they see blood.”

The middle-aged man let out a deep sigh and looked at the man with pity.

“From the looks of it, you won’t be able to give me the answer I want either.”

The man, already at the threshold of his final rally, answered in a faint voice.

“Heaven… Heaven will punish you.”

“What? Heaven’s punishment? Did you just say Heaven’s punishment?”

The middle-aged man’s eyes widened. Then he suddenly chuckled. At some point, his blurred hand pierced the man’s chest.

Crack!

His back arched with the agony of bone and flesh being crushed. Through his vision, slowly turning black, the man saw clouds drift across the sky as if nothing had happened.

Then a voice pierced his ears for the last time.

“Can you see it? The new Heaven.”

“……!”

Crack. Thud!

The man’s body crumpled as the hand was pulled free.

The middle-aged man stepped on the corpse of the Kongtong Sect’s most renowned rising martial artist, the Kongtong Sword Dragon, and turned his head toward the vast mountain range in the distance.

The Great Snow Mountain.

It would soon be stained red with countless streams of blood, but for now it shone brilliantly in the rising sunlight.

“Come on, let’s have ourselves a little fun.”

Behind the middle-aged man’s smile, a tremendous rumble began to shake the earth.
```
