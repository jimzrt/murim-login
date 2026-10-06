<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1025.txt",
      "sha256": "d2abca785c9f42ce0af4461200a7e70179112746d6ddb8503abbec4000b4469d",
      "bytes": 13438
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fa1c6d85db218a7cc83d3908d074586705caf7a2dc11bd35a56a6f3448442af8",
      "bytes": 2137
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0821386659bc3addb778ca5fcefcff90bf100119ece13916b00f44e929e9de3b",
      "bytes": 248927
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "93a13c611efa0b21aea808493f603982cd1888d380682107f627e71022f4aa79",
      "bytes": 844
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "6b40f1dd9f993566f9bd0827215942c9ada4baa7491fc75217148916c8cd641a",
      "bytes": 1802
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "dd40da4170be019e901ee81c7f7d0301527dd4c581d5c377178037666bb35ce1",
      "bytes": 1550
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "33d767e689f83cad086c9b6bc71e7a7bf3b46191f4f2ae2e75f56faa53843343",
      "bytes": 623
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "1e4c39655a2d4a8b8c8c96a6ea78e15ba11924e51e8b5899fca33b7d40745449",
      "bytes": 877
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "b823bdc68f5e4fb9b1397d3a4ac806710cc76b4d468c0e55928ebca776f38c96",
      "bytes": 716
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9eaab60f46f2aef1d1e2f3da649cc6a65fa83cb2204db89723cca64979c16987",
      "bytes": 296103
    }
  ],
  "estimated_tokens": 12268
}
-->

# Durable State Update — Chapter 1025

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
1 and safe_through 1025. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1025. Profile updates may replace only one
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
  "chapter": 1025,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1025,
    "continuity_sources": [1025],
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
    "Jeok Cheongang and Jin Taekyung cleared mutated Gate Forest of Death-I in the Tianshan Mountains; the Black Ghosts and monsters there were defeated.",
    "Mutated Gates Forest of Death-II through -VI were destroyed when Taekyung cut through hidden barriers between spaces; he gained the Door Opener title and leveled up, restoring his injuries and fatigue.",
    "Taekyung’s use of the Mind’s Eye caused severe physical harm and status effects, and deepened his insight into the ability; the System warns its use can be fatal.",
    "The separated companions reappeared, but the Great Sir was absent after the final rift closed.",
    "The Bow Saint briefly displayed intense emotion after emerging from her rift; its cause is unknown.",
    "The last Black Ghost said that “that person” was waiting for Taekyung; the figure’s identity and purpose remain unknown.",
    "The Lord of Heaven has awakened and regained strength, but says the process is incomplete; the Grand Mage awaits a command.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported Alpha’s awakening; what Alpha is and what its awakening means remain unknown.",
    "Taekyung has experienced unexplained chest pain and difficulty sleeping; whether he used his full strength while affected by the fasting pill remains unresolved."
  ],
  "continuity_sources": [
    1191,
    1190
  ],
  "open_questions": [
    "Who is “that person” waiting for Taekyung, and what do they want?",
    "Where is the Great Sir, and why did he not emerge with the others?",
    "What caused Taekyung’s chest pain and sleeplessness, and did he use his full strength while affected by the fasting pill?",
    "What remains to be completed for the Lord of Heaven, and what command will he give the Grand Mage?",
    "What is Alpha, and what does its awakening mean?"
  ],
  "safe_through": 1191,
  "temporary_decisions": [
    "Render 진인사대천명 as “Do all that man can, then await Heaven’s will.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 경험치              | **EXP**                        |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 검룡 | **Sword Dragon** | Epithet of Nangong Ok; one of the Ten Dragons and Phoenixes. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 십만마도 | **Hundred Thousand Demonic Disciples** | The earlier force used as a comparison for Dark Heaven’s army. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 공동검룡 | **Kongtong Sword Dragon** | Epithet of the Kongtong Sect’s renowned rising martial artist killed in the flashback. |
| 천산삼노 | **Three Elders of Tianshan** | The three former Demonic Cult fiends serving the Blood-Sword Demon Lord. |
| 호법원주 | **Guardian Court Chief** | Title of a Kongtong Sect official reported among the dead. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 진태경 | 사령관 | captor to captive undead commander | you | casual, mocking, and dismissive | Taekyung addresses the Skeleton Warlord informally while rejecting its pleas to turn back. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |
| 풍운검군 | 진태경 | martial artist to fellow martial artist | Daoist Friend Jin | respectful and familiar | Thinks of Jin as 진 도우 when recognizing him as a possible turning point in the battle. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |
| 적천강 | 혈주 | hostile_opponents | you | blunt and threatening | Jeok Cheongang blocks the Blood Lord’s final attack on Taekyung and rebukes him. |
| 노인 | 진태경 | older opponent to younger opponent; no family relation established | you | calm, familiar speech | The old man addresses Taekyung as 자네 while testing him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1176
- **Aliases:** None
- **Role:** Deceased young-seeming high-ranking Dark Heaven figure who claimed command of its army after killing the Grand Mage.
- **Personality:** Cunning and controlling, he trusts his overwhelming power and relishes opponents who survive and resist him; he resents the Lord of Heaven’s attention to Taekyung and rationalizes his intended murder as loyalty, yet believes his choice is right.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He served the Lord of Heaven, killed the Grand Mage, and died after Jin Taekyung defeated him; at death, he recognized that the Lord had never valued his loyalty.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1191
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, later cast him out, and regards their failings toward each other as a debt to settle in another life; he was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1191
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1191
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1065
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet capable of risking himself for a moment of conscience, he values his heir’s future and repaying a debt to Jeok Cheongang.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; Sima Gong chose him as heir and approved his plan to answer the Gate’s betrayal. Sama Pyo returned to remain with him as he died. Sima Gong aided Jeok Cheongang despite their history.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 1105
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

## Korean source

```text
＃1025화



불과 십여 명밖에 되지 않는 그들이 수만의 적들 사이에서도 단연 눈에 띌 수 있었던 것은, 총 세 가지 이유 때문이었다.

첫째. 하늘을 찌를 듯이 높게 들어 올린 백기.

둘째. 그런 백기와 상반되는 새카만 갈기를 휘날리며 맹렬하게 달려가는 거대한 흑마(黑馬).

그리고 마지막 셋째. 무리의 선두를 차지한 세 명의 노인.

‘저 늙은이들은 누구지?’

기감으로도 파악할 수 없을 만큼 먼 거리였지만, 그럼에도 불구하고 본능적으로 느껴지는 범상치 않은 기세.

내가 말없이 미간을 좁히던 그때, 어느덧 산 밑자락에 다다른 그들 사이에서 깊은 울림이 터져 나왔다.

“무림맹의 개들은 듣거라!”

심후한 공력과 함께 산맥 곳곳으로 뻗어 나가는 음성.

무슨 이유 때문인지 상의가 피범벅으로 물들어 있는 한 노인의 외침에, 적천강이 나를 바라보며 눈을 깜빡였다.

“거참, 희한하군. 지금 노부가 이상한 환청을 들은 것 같은데.”

“아닐걸요.”

“뭐라? 그럼 저 미친놈이 정말 엎드려 부복하라고 했단 말이더냐? 다른 사람도 아닌 노부에게?”

“그 정도까지 콕 집어서 말한 건 아니지만, 뭐 당장은 무림맹 소속이시잖아요.”

“그렇지. 일단은.”

“무림맹의 개라고 했으니까, 그럼 맞네요. 일단은.”

“그래, 노부가 제대로 들은 게 맞다 이거지.”

뭔가를 곰곰이 생각하던 적천강이 말을 이었다.

“그럼 하나 묻자. 어디서 굴러먹다 왔는지 모를 개뼈다귀 같은 놈들이 하늘과도 같은 스승을 모욕할 때, 하나뿐인 제자, 아니 뭐 그 비슷한 녀석은 어찌 행동해야겠느냐?”

“…….”

제자면 제자지. 그 비슷한 녀석은 또 뭐야.

아직까지도 끈질기게 컨셉을 유지하고 있는 적천강의 모습에, 나는 작게 혀를 차며 대답했다.

말이 아닌, 행동으로.

쉭, 탁.

“어, 어어?”

순식간에 빈손이 되어 어리둥절해하는 무인을 뒤로한 채, 나는 그에게서 빌린 창을 한껏 뒤로 젖혔다.

아니, 빌렸다는 표현에는 약간의 어폐가 있다.

나는 이 창을 돌려주지 못할 테니까.

스윽.

활처럼 휘어지는 허리와 수축하는 근육. 부드럽게 이완되는 관절이 이어져 하나의 동선을 그린다.

그리고 창날이 겨누어진 방향의 끝에는, 저 멀리 백기를 든 채 외침을 이어 가는 일단의 무리가 있었다.

“지금 즉시 무기를 버리고 투항한다면……!”

화아악!

마침내 손을 떠난 창이 대기를 찢어발긴다.

맹렬한 파공성마저 앞질러 나아간 그것이 한 줄기의 섬광이 되어 표적에 닿기까지 걸린 시간은, 그야말로 찰나에 불과했다.

퍼엉!

선홍빛 핏물이 터져 나왔다.

단말마도 지르지 못한 채 몸뚱어리가 터져 나간 흑마가 썩은 고목처럼 허물어지고, 말도 안 되는 개소리를 힘차게 이어 가던 노인이 표횰한 움직임으로 지면에 떨어져 내렸다.

‘초절정 고수.’

험준한 산맥을 타고 전해질 만큼 심후한 공력을 선보였을 때부터 짐작했지만, 노인 역시 초인이라 불릴 자격이 충분한 자였다.

비록 상당한 거리가 있었다 하더라도, 어마어마한 힘과 속도가 실린 창을 그리 어렵지 않게 피해 냈으니까.

그리고 저 무리 중 이와 같은 무위를 지닌 것은, 비단 그 한 사람뿐만이 아니었다.

“환영 인사가 제법 거칠구나, 아해(兒孩)야.”

“백기를 든 상대에게 선제공격이라니, 네놈들이 그토록 지껄여 대던 강호의 도리는 땅에 떨어졌느냐?”

나직하면서도 선명한 음성.

잎사귀 하나 붙어 있지 않은 수많은 나뭇가지 사이로, 다른 두 명의 노인은 나를 똑바로 응시하고 있었다.

“그래, 너로군. 말로만 듣던 그 어린놈이.”

“열화신룡 진태경. 맞느냐?”

나 역시 공력을 실어 대답했다.

“아닌데?”

“……?”

“……?”

“농담이야. 사실 맞아.”

“……!”

“……!”

언제 봤다고 알은척부터 했던 두 노인은 물론, 앞서 쏘아 보낸 투창에 교통수단을 잃어버린 예의 노인까지 당혹스러운 기색으로 서로를 바라보았다.

이유는 아마 두 가지일 것이다.

첫째. 이 어린놈의 새끼가 뭘 잘못 먹었는지 초장부터 헛소리를 지껄여서.

둘째. 그 어린놈의 새끼가, 뭘 얼마나 잘 처먹었는지 헛소리에 담긴 공력이 엄청나서.

그리고 나는 저 노망난 늙은이들에게 지금까지 얼마나 많은 경험치를 처먹었는지 일일이 설명해 줄 생각 따위는 조금도 없었다.

다만 이 엄청난 전력을 바탕으로 돈황마저 깨부수고 온 마당에 항복을 권유하는 놈들의 저의가 궁금할 따름이었다.

물론 그전에, 어디서 굴러먹다 온 개뼈다귀인지는 알아야겠지만.

“나도 말해 줬으니 기왕 이렇게 된 거 서로 통성명은 해야지? 댁들이 말한 강호의 도리라는 게 있는데.”

세 명 중 중심에 선, 얼굴이 곰보 자국으로 뒤덮인 노인이 순순히 대답했다.

“핏덩이 주제에 혓바닥이 짧군. 좋다, 노부들은 천산삼노(天山三老)라 한다.”

순간, 나는 눈을 부릅떴다.

“천산삼노……!”

두 번째, 뚱뚱한 배불뚝이 노인이 그럴 줄 알았다는 듯이 고개를 끄덕였다.

“역시 들어 본 모양이군.”

“세상에, 당신들이 바로 그 천산삼노라니.”

내 탄성에 마지막 세 번째, 서열상 막내임이 분명한 고봉밥 정수리 노인이 피식 웃었다.

“정마대전 이전부터 전해져 내려온 우리에 관한 이야기는 익히 들었을 터, 이제야 제대로 이야기를 할 마음이 드나?”

내가 놀란 얼굴로 대답했다.

“아니.”

“후회할 짓 하지 말고 지금이라도…… 뭐?”

“아니라고. 별호도 오늘 처음 들었는데, 무슨. 그리고 노는 좀.”

“뭐라?”

“그냥 이러면 알아서 씨부릴 것 같아서 놀란 척해 봤지. 아, 혹시 천산삼노라고 들어 보셨어요?”

고개를 돌려 살아 있는 무림 대백과 사전, 적무위키를 바라보자 머지않아 대답이 흘러나왔다.

“천산에 떠돌이 개 세 마리가 어슬렁거린다는 이야기는 오래전부터 익히 들었지.”

“아하.”

“천성이 개라 그런지, 정마대전 때는 마교에 붙어 중원에서 온갖 개지랄을 떨었다. 노부도 한번 손 봐주려고 벼렸었고.”

“그래서요?”

“그래서는 뭔 놈의 그래서. 노부가 작심했는데도 저놈들이 아직까지 숨통이 붙어 있는 이유가 무엇이겠느냐?”

“전장에서 마주치진 못했군요.”

“타고난 개새끼들이라 코 하나는 좋더군. 기가 막히게 내빼는 통에 그림자도 구경 못 해 봤다.”

“아.”

짧은 대화를 통해 결론을 도출한 나는 혼잣말처럼 중얼거렸다.

물론, 모두가 다 들을 수 있도록 공력을 실어서.

“좆밥이었구나.”

“……!”

“……!”

“……!”

주위의 공기가 파르르 떨렸다.

하지만 보이지 않는 분노로 뜨겁게 끓어오르는 산 밑의 적들과 달리, 산등성이를 따라 길게 진을 친 아군들의 반응은 달랐다.

천산삼노가 누구인가.

정마대전의 한 자락을 장식한 전대의 초절정 고수이자 모두가 두려워 마지않았던 대마두들이다.

한데 그런 그들을 굽어보며 적천강과 나는 말했다.

그저 한낱 개새끼들이라고. 좆밥이라고.

그리고 이런 말도 안 되는 폭언과 기행은, 아군에게 있어 놀라움과 동시에 안도감을 선사하기에 충분했다.

‘그게 내가 노렸던 거고.’

치열한 혈투를 앞둔 지금.

나는 말 몇 마디만으로 상대를 도발하는 것뿐만 아니라 아군의 사기까지 끌어 올렸다.

고작 이 정도로 불리한 전세가 단번에 뒤집히지는 않겠지만, 기세(氣勢)라는 것은 무엇보다 중요하다.

물론…….

‘만약 이 자리에 천주(天主)가 와 있다면, 기세 따위는 아무런 소용도 없겠지만.’

십만마도의 새로운 하늘.

도무지 그 끝을 알 수 없을 만큼 거대한 힘을 지닌 악(惡), 그 자체.

모두에게 보여 주기 위해 말아 올린 입꼬리와는 달리, 단 한번도 대면한 적 없던 절대자의 존재를 떠올리자 가슴 한구석이 무거워진다.

‘천산삼노를 한낱 사자(使者)로 부릴 정도라면, 놈들을 이끄는 건 도대체 누구일까.’

그리고 마치 내 마음속에 자리 잡은 의문을 읽은 듯, 무시무시한 안광으로 이쪽을 노려보던 천산삼노 중 첫째로 짐작되는 곰보 노인이 입을 열었다.

“더 이상의 긴말은 필요 없겠군. 마군(魔軍)께서 너희를 보고자 하신다.”

“……뭐?”

마군이라니.

순간 눈살을 찌푸린 나는 적천강을 비롯한 수뇌부들과 눈빛을 교환했다.

이 자리의 모두가 알고 있듯이, 마군이라 불릴 만한 자들은 이미 모조리 죽었다.

각각 동, 서, 북을 상징하는 세 명의 마군과 남만야수궁에서 끝끝내 죽음을 맞이한 남천마후까지.

‘그런데, 또 한 명의 마군이 남아 있다고?’

이 새끼들이 설마 치사하고 멋대가리 없게 동서마군, 서북마후 뭐 이딴 거라도 만들었나 생각하던 그때.

문득 한 사람에게 생각이 미쳤다.

‘혹시, 혈주(血主)?’

근무 중 사망처리 된 직장 동료의 빈자리를 놈이 채우기라도 한 걸까.

적들을 이끄는 총사령관의 존재를 두고 수뇌부들 사이에 낮은 속삭임이 오가려던 찰나, 산 밑에서 재차 외침이 울려 퍼졌다.

“마군께서 이르시길, 안전은 보장할 테니 이 제의에 응하라 하셨다!”

다른 누구도 아닌 암천이 안전을 보장한다니.

당연히 말도 안 되는 개소리다.

수뇌부 전체는 물론, 나 역시도 저 터무니 없는 말에 헛웃음을 흘렸다.

다음 순간, 천산삼노의 손짓에 그를 따르던 암천의 무인 하나가 말안장에 매달린 무언가를 꺼내 건네기 전까지는.

후우웅, 툭.

높게 솟구쳐 산 중턱에 떨어진 그것은 아군을 통해 곧장 수뇌부에게 전해졌고, 나는 피범벅이 된 그 커다란 보따리를 열어 보기도 전에 안의 내용물이 무엇인지 알아차릴 수 있었다.

아니, 우리 모두가.

쿵. 쿠궁.

“흡……!”

제법 육중한 소리를 내며 굴러떨어지는 수십여 개의 수급(首級)에 곳곳에서 침음성이 터져 나온 것도 잠시, 그중 낯익은 얼굴을 알아본 사마공이 낮게 중얼거렸다.

“공동검룡(崆峒劍龍)이로군.”

본 적은 없으나, 그 별호는 들어 봤다.

공동파 장문인의 직계 제자이자 중원에는 십봉룡(十鳳龍)의 일원으로 잘 알려진 최고의 후기지수 중 한 명.

그리고…… 스승인 장문인과 함께 살아남아 돈황을 탈출했다던 바로 그였다.

“자, 장로이신 두 진인(眞人)도 여기 계십니다.”

“호법원주께서도 유명을 달리하셨군. 도대체 어찌하여…….”

이미 사망이 확실시 된 이들은 물론, 살아남았다고 알려진 자들까지 한낱 수급이 되어 돌아왔다.

그것도 공동파의 주축이라 할 수 있는 핵심 수뇌부가.

“그렇다면 설마.”

쉽게 말을 잇지 못하고 입을 다문 나를 향해, 풍운검군이 무겁게 고개를 가로저었다.

“다행히도 장문인께서는 놈들의 손아귀를 벗어난 모양일세. 이걸…… 다행이라고 해야 할지는 모르겠지만.”

돈황에서의 전투가 끝이 아니었다.

끈질긴 추적이 있었고, 끔찍한 살육이 있었다.

그리고 지금, 들어본 적 없는 새로운 마군은 어떤 이유에서인지 우리를 보고자 한다.

단순한 위협이 아닌, 천산삼노를 보내어 협박을 곁들이면서까지.

“아쉽군. 거리가 더 가까웠으면 네놈들의 표정을 똑똑히 볼 수 있었을 텐데.”

조금 전까지만 해도 분노하던 세 늙은이는, 낄낄 웃으며 말을 이었다.

“고작 이 정도가 끝이라고 생각하는 건 아니겠지. 응?”

적천강이 가라앉은 목소리로 입을 열었다.

“그게 무슨 개소리냐.”

과거의 두려움이 떠올라서일까, 적천강의 존재감에 잠시 움찔한 천산삼노가 이내 더욱 힘을 실은 음성으로 답했다.

“일천. 아직 일천의 포로가 더 남아 있다.”

“……!”

“네놈들이 앞서 했던 제의를 승낙한다면, 놈들 중 일부를 돌려보내줄 용의가 있지.”

입 안이 텁텁하다. 나는 위장이 뒤틀리는 것 같은 통증을 느끼며 물었다.

“거절한다면?”

세 마리의 개새끼가 소리내어 웃었다.

“해보겠느냐?”

빌어먹을.

그것으로, 내 대답은 정해진 것이나 다름없었다.
```

## Final English reading copy

```markdown
# Chapter 1025

There were only a dozen or so of them, yet three things made them stand out even among tens of thousands of enemies.

First, a white banner held high enough to pierce the sky.

Second, a massive black horse charging fiercely, its jet-black mane flying in stark contrast to that banner.

And third, the three old men at the front of the group.

*Who are those old men?*

They were so far away that even my Qi Sense couldn’t pick them up. And yet I could instinctively feel their extraordinary presence.

Just as I narrowed my eyes in silence, a deep voice boomed from the group, now reaching the foot of the mountain.

“You dogs of the Murim Alliance, listen!”

His voice, backed by profound internal energy, spread across the mountain range.

For some reason, the front of the old man’s clothes was soaked in blood. As he shouted, Jeok Cheongang looked at me and blinked.

“Goodness, how strange. I think this old man just heard a bizarre hallucination.”

“I doubt it.”

“What? Then that madman really did tell us to prostrate ourselves? And to no one else but this old man?”

“Not quite that specifically, but you are with the Murim Alliance right now.”

“That I am. For now.”

“He called us dogs of the Murim Alliance, so he’s right. For now.”

“So this old man did hear correctly.”

Jeok Cheongang thought about it for a moment, then continued.

“Then let me ask you something. When some dog-boned nobody, who knows where they crawled out of, insults his heaven-like Master, how should his one and only Disciple—no, someone more or less like a Disciple—act?”

“…”

If you’re a Disciple, you’re a Disciple. What was this “more or less like one” business?

Still stubbornly keeping up the act, Jeok Cheongang drew a quiet click of my tongue. I answered not with words, but with action.

Whoosh. Clack.

“H-Huh?”

Leaving the martial artist who’d suddenly been left empty-handed staring in confusion, I drew back the spear I’d borrowed from him as far as I could.

Though “borrowed” wasn’t quite the right word.

I wouldn’t be able to give this spear back.

My waist bent like a bow, my muscles contracted, and my joints relaxed in sequence, all flowing together into a single motion.

At the far end of the direction the spearhead pointed, the group carrying the white banner continued shouting.

“If you drop your weapons and surrender this instant—!”

Whoosh!

The spear finally left my hand, tearing through the air.

It outran even the fierce whistle of its passage, becoming a streak of light. The time it took to reach its target was no more than an instant.

Boom!

Bright red blood burst into the air.

The black horse, its body blown apart before it could even whinny, crumpled like a rotten tree trunk. The old man who’d been loudly spouting the most ridiculous nonsense dropped lightly to the ground.

*Supreme Peak master.*

I’d suspected as much when he’d displayed enough internal energy for his voice to carry across the rugged mountain range. The old man, too, was worthy of being called a superhuman.

Even from a considerable distance, he’d managed to evade a spear driven by tremendous force and speed without much difficulty.

And he wasn’t the only one among them with that level of skill.

“That’s quite a rough welcome, child.”

“Launching a preemptive attack on someone carrying a white banner? Has the code of the martial world you’ve been going on about fallen to the ground?”

Their voices were low, yet clear.

Among the countless branches of the leafless trees, the other two old men stared straight at me.

“So it’s you. The young brat we’ve heard so much about.”

“Blazing Flame Divine Dragon Jin Taekyung, is that right?”

I sent my answer back with internal energy.

“Nope.”

“…”

“…”

“Kidding. It is.”

“……!”

“……!”

The two old men, who’d acted like we were old acquaintances despite never having met, and the one who’d lost his means of transportation to my spear all looked at one another in bewilderment.

There were probably two reasons.

First, this young brat had started spouting nonsense right out of the gate. Maybe he’d eaten something bad.

Second, that young brat had eaten so well that his nonsense was backed by an absurd amount of internal energy.

I had no intention of explaining to those senile old men just how much EXP I’d eaten up until now.

I was simply curious why, after using their overwhelming forces to crush even Dunhuang, they were urging us to surrender.

But before that, I wanted to know what kind of dog-boned nobodies they were.

“I’ve introduced myself, so we might as well exchange names, right? You were the ones talking about the code of the martial world.”

The old man in the middle, whose face was covered in pockmarks, answered without protest.

“You’ve got no manners for a brat still wet behind the ears. Fine. We’re called the Three Elders of Tianshan.”

My eyes widened.

“The Three Elders of Tianshan…!”

The second old man, a fat, potbellied fellow, nodded as if he’d expected that reaction.

“So you have heard of us.”

“Good heavens. You’re the Three Elders of Tianshan?”

At my exclamation, the third old man—clearly the lowest-ranking of the three, with a crown like a heaping bowl of rice—gave a short laugh.

“Surely you’ve heard the tales about us, passed down since before the Great Faction War. Are you finally ready to talk to us properly?”

I answered, looking surprised.

“No.”

“Don’t do something you’ll regret. Even now, you could—what?”

“I said no. I’ve never even heard that title before today. And cut the ‘Elder’ stuff.”

“What?”

“I just pretended to be surprised because I figured you’d start blabbing on your own. Oh, have you ever heard of the Three Elders of Tianshan?”

I turned to the living Murim encyclopedia, Jeok Wiki. Before long, an answer came.

“I’ve heard for a long time that three stray dogs wander around Tianshan.”

“Ah-ha.”

“Born dogs, it seems. During the Great Faction War, they sided with the Demonic Cult and caused all kinds of hell in the Central Plains. I’d been itching to teach them a lesson myself.”

“And?”

“And what? What do you think is the reason those fellows are still breathing, even though this old man had made up his mind?”

“You never ran into them on the battlefield.”

“They were born sons of bitches, but they had good noses. They were so damn good at running away I never even caught a glimpse of them.”

“Oh.”

Drawing a conclusion from our brief conversation, I murmured as if to myself.

Of course, I made sure everyone could hear me by putting internal energy behind it.

“They were weak as shit.”

“……!”

“……!”

“……!”

The air around us trembled.

But unlike the enemy at the foot of the mountain, whose rage was boiling hot despite being invisible, the allies lined up along the ridge reacted differently.

Who were the Three Elders of Tianshan?

They were fiends from a bygone era, Supreme Peak masters who’d made their mark during the Great Faction War and struck fear into everyone.

And yet Jeok Cheongang and I looked down at them and called them nothing but a bunch of dogs. Weaklings.

Those outrageous insults and absurd antics were enough to fill our allies with both astonishment and relief.

*That was what I was going for.*

With a fierce battle just ahead, I’d provoked the enemy with a few words while also boosting our allies’ morale.

This alone wouldn’t turn the tide of such an unfavorable battle in an instant, but momentum mattered more than anything.

Of course…

*If the Lord of Heaven is here, then momentum won’t mean a damn thing.*

The new Heaven of the Hundred Thousand Demonic Disciples.

Evil itself, with power so immense its limits were impossible to grasp.

The corner of my mouth had curled up for all to see, but the thought of that absolute being—someone I’d never once met—left a heaviness in my chest.

*If someone can use the Three Elders of Tianshan as mere messengers, who the hell is leading them?*

As if he’d read the question in my mind, the pockmarked old man—who seemed to be the eldest of the Three Elders of Tianshan—glared at us with a terrifying light in his eyes and spoke.

“There’s no need for any more talk. The Demon Lord wishes to see you.”

“…What?”

The Demon Lord?

I frowned and exchanged glances with Jeok Cheongang and the other leaders.

As everyone here knew, all those worthy of being called Demon Lords were already dead.

The three Demon Lords who represented the East, West, and North, and even the Southern Heaven Demon Empress, who had met her end at the Nanman Beast Palace.

*But there’s another Demon Lord left?*

Had these bastards come up with something tacky and ridiculous, like the East-West Demon Lord or the Northwest Demon Empress?

Just then, someone came to mind.

*Could it be the Blood Lord?*

Had he filled the vacancy left by a coworker who’d been marked dead on the job?

Before the leaders could trade quiet whispers about the identity of the enemy commander, another shout rang out from the foot of the mountain.

“The Demon Lord says your safety will be guaranteed if you accept this offer!”

Dark Heaven guaranteeing our safety?

That was obviously complete bullshit.

The whole leadership—including me—let out a laugh at the outrageous claim.

At least, we did until one of the Dark Heaven martial artists following the Three Elders of Tianshan reached into his saddlebag and handed them something at a signal from the eldest.

Whoosh. Thud.

It soared high, then landed halfway up the mountain. Our allies immediately carried it to the leaders. Before I even opened the large blood-soaked bundle, I knew what was inside.

No—we all did.

Thump. Thump-thump.

“Ugh…”

Dozens of severed heads rolled down with heavy thuds. Groans rose from all around us. Among them, Sima Gong recognized a familiar face and murmured,

“The Kongtong Sword Dragon.”

I’d never seen him before, but I’d heard the title.

A direct Disciple of the Kongtong Sect Leader, and one of the greatest young prodigies in the Central Plains, known as one of the Ten Dragons and Phoenixes.

And he was the very one who was said to have escaped Dunhuang alive alongside his Master, the Sect Leader.

“T-the two Perfected Ones who served as Elders are here, too.”

“The Chief of the Protectorate Court has also met his end. How could this have happened…?”

The dead were here, as expected, but so were those who’d supposedly survived.

They were all just severed heads now.

And they belonged to the Kongtong Sect’s core leadership.

“Then could it be…”

I trailed off, unable to continue, and Wind-and-Cloud Sword Lord gravely shook his head.

“Fortunately, it seems the Sect Leader escaped their grasp. Though I don’t know if we should call that fortunate.”

The fighting at Dunhuang hadn’t been the end.

There had been a relentless pursuit, and there had been a horrific slaughter.

And now, for some reason, a new Demon Lord we’d never heard of wanted to see us.

Not with a simple threat, either. They’d sent the Three Elders of Tianshan to deliver a threat backed by force.

“It’s a shame you’re so far away. If you were closer, I could’ve gotten a good look at your faces.”

The three old men, who’d been furious just a moment ago, continued with a cackling laugh.

“You don’t think this is all we have, do you? Hm?”

Jeok Cheongang spoke in a low voice.

“What kind of dogshit is that supposed to mean?”

Perhaps some old fear had surfaced. The Three Elders of Tianshan flinched at Jeok Cheongang’s presence, but soon answered, putting even more force into their voices.

“A thousand. We still have another thousand prisoners.”

“……!”

“If you accept the proposal you made earlier, we’re willing to return some of them.”

My mouth felt dry. Pain twisted through my stomach as I asked,

“And if we refuse?”

The three sons of bitches laughed aloud.

“Want to find out?”

Damn it.

That left me with little doubt about my answer.
```
