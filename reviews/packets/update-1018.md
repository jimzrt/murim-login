<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1018.txt",
      "sha256": "667aa4d31267e618c41f6657c5886dfc24a130a232263a3f6087a2fc7a95f544",
      "bytes": 12588
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "caa9df12a1b579c5a332cd6c4652d6f0e01d3c4ebede5fd854656763fb972f13",
      "bytes": 1731
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "611b5144e394205d82ab664a36e903511377554b9737ac63e0571a7866e56564",
      "bytes": 238256
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a522b280bb5116cea5843e6a5409ad1d9ad968c5437e24137330c467b23faa4e",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "43781226a4201695851f3e77adf3e0cc7af5af7bb62222c8f012d57916518132",
      "bytes": 1408
    },
    {
      "path": "characters/Namho.md",
      "sha256": "d0fa24c1c3c0021501eb7154ce064b42a113d2c697291add2477e320d238439b",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "237b779ee24a32e95d0391a39e4c545223d0e09c0e2c30b9442f760d00a1ffaa",
      "bytes": 904
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "99f5249d9c551bcec0238857f0ede185c333b4f4080776c0d13094bbeca2d7fc",
      "bytes": 778
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "ae018fc95f02f66d7fa1b18eee17010cc5fae473af29c8c23ccd74364cf53690",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "107226d29d3a00596e274bb32d326b67d072d4bda85484b408975b0987bfdde5",
      "bytes": 277335
    }
  ],
  "estimated_tokens": 10436
}
-->

# Durable State Update — Chapter 1018

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
1 and safe_through 1018. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1018. Profile updates may replace only one
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
  "chapter": 1018,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1018,
    "continuity_sources": [1018],
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
    "Gansu Murim’s leaders upheld the decision to leave forces on the rear front to delay Dark Heaven if it uses the Moving Formation; the Kongtong Sect opposed the decision.",
    "Taekyung agreed to let Gansu Murim’s decision stand for now and has not yet used the item in his Inventory.",
    "Namho reported that Sama Pyo was burning a secret letter shortly before the group left the Jin Family of Taiyuan; Taishan was with him, and its contents and recipient are unknown.",
    "Sima Gong warned Taekyung that releasing the horse caravans could be a serious mistake; Taekyung believes there will be no problem if his expectations are correct.",
    "Six Baekma Bang men left to fetch the Lord within five days of the march’s halt; Ma Junggeol remains with Taekyung’s group.",
    "Namho has an important matter he said he could only disclose to Taekyung at that time.",
    "Sama Pyo disobeyed Sima Gong’s order to return to Gansu; consequences are unknown.",
    "Sima Gong ordered two martial artists dealt with for making a taboo remark about Sama Pyo’s succession."
  ],
  "continuity_sources": [
    1016,
    1017
  ],
  "open_questions": [
    "Who is the Lord, and what are his motives and connection, if any, to Dark Heaven?",
    "Will the six Baekma Bang men return with the Lord within Taekyung’s deadline?",
    "What was in the secret letter Sama Pyo burned, and to whom was it addressed?",
    "What is Dark Heaven’s full strength and objective, and will it use the Moving Formation to attack the rear?",
    "What consequences, if any, will Sama Pyo face for disobeying Sima Gong’s order?"
  ],
  "safe_through": 1017,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 일신     | **One God**         |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1016
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1017
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1017
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1017
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1017
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1017
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1018화



“아무도 모르게 홀로 밀서(密書)를 태우고 있었다라.”

입술 사이로 흘러나온 나지막한 뇌까림.

나를 응시하는 적천강의 눈빛은 어느덧 침잠하게 가라앉아 있었다.

“남호가 착각했을 가능성은?”

“그건…….”

말을 잇는 대신 조용히 입을 닫자, 적천강이 얕은 한숨을 내쉬었다.

“빌어먹을. 사실인 모양이로군.”

사실 처음에만 하더라도 나는 이 모든 것이 그저 단순한 착오라고 생각했다.

사마표를 불러서 직접 몇 마디 대화를 나누면 깔끔하게 해결되는, 뭐 그런 사소한 해프닝.

하지만…….

“이미 확신하고 있었습니다. 남 노인은.”

“그렇겠지. 이제야 네 녀석에게 이야기를 꺼냈다는 것은, 지금까지 그만큼 깊이 생각했다는 뜻일 테니.”

“네. 처음에는 그도 긴가민가했던 모양입니다. 이를 뒷받침할 만한 마땅한 증거가 없는 상황이기도 했고요.”

늙어 간다는 것은 그만큼 감각이 무뎌진다는 뜻.

그래서 남호 역시 고민에 고민을 거듭했다고 했다.

은영각 요원으로서 지긋하리만치 맡아 온 익숙한 그 냄새가, 사마표의 방에 감돌던 것과 같은 종류의 것인지.

자신의 무뎌진 감각이 괜한 오해를 불러일으키는 것은 아닌지.

그리고 이 늙은 은영각 요원이 칠 주야가 넘게 고민한 끝에 도출한 결론은 하나뿐이었다.



‘그건 분명 유지(油紙)가 타들어 가는 냄새였어. 이제는 확신할 수 있네.’



유지. 즉 기름을 먹인 종이다.

전서를 주고받을 때는 쉽게 젖거나 찢어지는 것을 방지하기 위하여 기름에 적시는 것이 상식인데, 당연하게도 건조한 상태의 종이와는 탄내부터가 달랐다.



‘종이에 기름을 먹이는 또 다른 이유는 태우기가 쉽다는 걸세. 발각되면 안 되는 서신일수록 빠른 증거 인멸이 필수거든.’



아득한 세월을 정보원으로 살아온 남호다.

비록 방 안에 감돌던 미세한 탄내 이외에는 그 어떤 흔적도 없었지만, 그는 그 순간부터 사마표와 태산을 향한 의심의 끈을 놓지 않았다고 했다.



‘산서성을 떠나던 그 날부터 줄곧 지켜봤지만, 불과 며칠 전까지만 하더라도 내 판단을 확신할 수 없었지. 정말 그것이 유지가 타는 냄새였는지, 그렇다면 어디의 누구에게서 받은 것인지.’



그리고 남호로 하여금 판단을 망설이게끔 만든 가장 큰 이유는 따로 있었다.

“향이 독특했다더군요.”

“향? 종이 탄내를 말하는 것이냐?”

“예. 남 노인이 알고 있는 여러 종류의 탄내와는 상당히 달랐다고 합니다.”

“종이 타는 냄새가 다 거기서 거기지, 그게 무슨…….”

“어느 지방이냐에 따라 저마다의 특색이 있다고 들었습니다. 풍습도, 음식도, 그리고 기름의 원료가 되는 동물도.”

내가 나직이 덧붙인 뒷말에, 적천강이 문득 미간을 좁혔다.

“잠깐. 혹시?”

“남 노인의 말에 의하면 감숙과 청해에서만 볼 수 있는 동물이 있다고 하던데, 맞습니까?”

“낙타……!”

억눌린 탄성을 토해 낸 적천강이 고개를 끄덕였다.

“그거였군. 그 독특한 향의 정체가.”

“일평생 중원과 남만(南蠻)에서만 머물렀으니, 남 노인으로서도 쉽게 분간할 수 없었을 겁니다.”

“그래. 그 희한하게 생긴 놈들은 청해와 감숙 서부에만 서식하는 탓에 접하기 힘들지.”

더군다나 현시대의 무림에서는 소, 말, 양, 돼지를 이용한 동물성 기름을 사용하는 것이 보통.

하지만 우리가 처음으로 감숙성에 진입했던 그날, 다른 화룡각 대원들과 함께 잠시 휴식을 취하던 남호는 뜻하지 않은 실마리를 얻을 수 있었다고 했다.



‘실로 기막힌 우연이었지. 도통 입맛도 없고 해서 혼자 생각에 잠겨 있었는데, 어디서 한번 맡아 본 냄새가 솔솔 풍겨 오지 뭔가. 이게 뭔가 싶어서 물어보니 낙타 고기라더군.’



실마리는 그렇게 이어졌고, 비로소 확신을 굳히게 된 남호는 내게 이 사실을 전했다.

사마표가 누군가에게 밀서(密書)를 받았으며, 그 밀서가 보내진 곳이 감숙 혹은 청해가 틀림없다는 말과 함께.

그리고 밀서를 보낸 그 누군가의 정확한 정체에 대해서는, 이미 이 사실을 아는 모두가 어렴풋이 짐작하고 있었다.

남호가 감숙에 이어 청해를 언급한 것은 단순한 가능성에 불과할 뿐, 수천 리에 달하는 머나먼 산서성으로 밀서를 보낼 만한 인물은 한 사람뿐이니까.

“흑야왕(黑夜王) 사마공…….”

혼잣말처럼 흘러나온 내 뇌까림에, 적천강이 거칠게 침을 뱉었다.

“많이 컸군. 정말로.”

“밀서에 무슨 내용이 적혀 있었을까요?”

“예상하는 바가 있느냐?”

“있긴 합니다.”

“말해 보거라.”

“최소한 우리 아들 밥은 잘 먹고 다니냐, 뭐 그런 내용은 아니라는 것 정도.”

순간, 적천강의 관자놀이에 실핏줄이 솟았다.

“그걸 지금 말이라고 하느냐? 그건 태산인가 강산인가 하는 그놈도 알겠다.”

“태산이라면 모를 수도 있어요.”

“……솔직히 그 부분만큼은 노부로서도 부정하기 힘들군. 그러고 보니 그 덩치만 큰 놈은 오는 길에 어땠다더냐?”

“며칠간 남 노인이 지켜본 바로는 확실히 이상하긴 했다더라고요. 감숙성에 가까워질수록 밥도 깨작깨작 먹고, 온종일 침울해하고.”

물론 깨작깨작 먹었다는 것에는 약간의. 아니, 상당한 어폐가 있다.

그 와중에도 꾸준히 하루 다섯 끼를 처먹었는데 그게 어떻게 깨작깨작인가. 배불배불이지.

하지만 평상시 태산의 식사량을 생각한다면 하루 다섯 끼는 사실상 간헐적 단식이나 다름없었다.

더군다나 감숙성을 향한 거리가 좁혀질수록 죽상이 되어 가던 녀석의 모습을 생각한다면, 확실히 이상한 점이 한둘이 아니다.

‘내가 알고 있는 사마표라면 태산이에게도 함구했을 가능성이 크긴 하지만.’

어찌 되었건 현재의 상황에서 가장 중요한 것은 하나다.

산서성에 머무를 당시 두 부자(父子) 사이에 어떤 은밀한 내용이 담긴 밀서가 오갔고, 그것은 결코 우리에게 있어 희망차고 긍정적인 흐름이 아니라는 것.

이런 생각까지는 하고 싶지 않지만, 만에 하나 정말 최악의 사태가 벌어진다면…….

“음.”

내가 고개를 내저어 머릿속의 생각을 애써 떨쳐 내려던 그때였다.

그런 내 모습을 물끄러미 바라보던 적천강이 불쑥 입을 연 것은.

“걱정되느냐?”

“뭐가요?”

“사마표와 태산. 그 두 녀석을 네 손으로 직접 베게 될까 봐.”

“……!”

저벅.

나도 모르게 불현듯 멈춰 버린 발걸음.

반쯤은 기계적으로 걷고 있던 나는 그 자리에 우뚝 선 채, 적천강을 말없이 응시했다.

“할 말이 많아 보이는 표정이로구나.”

“…….”

“네 녀석이 꿀 먹은 벙어리가 된 김에, 노부가 한 가지 재미있는 이야기를 들려주마.”

나는 대답하지 않았고, 적천강은 대답을 기다리지 않았다.

“정마대전으로 인해 천하가 불타오르던 시절, 군자도(君子刀)라는 자를 알게 됐다.”

우리는 다시 걷기 시작했고, 나는 복잡한 목소리로 대꾸했다.

“별호 한번 멋지네요.”

“멋지긴 쥐뿔이. 처음에는 손가락이 오그라들다 못해 부러질 것 같은 별호를 지닌 탓에 썩 마음에 들지는 않았지. 한데 한동안 같이 마교 놈들의 모가지를 따며 겪어 보니 제법 쓸 만한 놈이었다.”

“쓸 만했다면, 어떤 의미로 말씀하시는 겁니까?”

“둘 다였다. 사람으로서도, 무인으로서도.”

“대단한 호평이네요. 다른 누구도 아닌 노야께서 그렇게 말씀하실 정도면.”

“세간의 평가는 더 좋았지. 비록 몰락하긴 했지만 뼈대 있는 무가 출신에, 일신의 무위와 의기(意氣)도 뛰어나 그 어떤 위험한 상황에서도 앞장섰고 결코 물러섬이 없었다.”

그야말로 협객(俠客)의 표본이었다는 소리다.

가장 먼저 돌격하고, 가장 늦게 퇴각하며, 살신성인의 정신을 온몸으로 실천하는.

그러나 갑작스럽게 시작된 이 이야기의 결말을, 나는 이미 마음속으로 짐작하고 있었다.

“어째서인지 말씀하시는 게 전부 과거형이네요. 꼭 지난날을 후회하시는 것처럼.”

적천강의 입가에 씁쓸한 미소가 스쳤다.

“이 눈치 빠른 녀석 같으니.”

“배신자였습니까?”

“그래, 마교의 하수인이었지. 그러나 처음부터는 아니었다.”

“그 말씀은…….”

“노부가 군자도의 출신에 대해 말한 것, 기억하느냐?”

“예. 청해성에서도 뼈대 있는 무가 출신이었다고.”

“사실 다른 문파와의 전쟁으로 가문이 완전히 와해 되었으니, 차라리 풍비박산이라는 표현이 옳을 것이다. 갓난쟁이였던 군자도를 젖동냥해 가며 키운 늙은 가복(家僕)이 그가 알고 있던 유일한 가족이었으니까.”

알고 있던, 이라.

그제야 문득 알 것 같았다.

이름도, 얼굴도 모르는 과거의 협객이 왜 마교의 그늘 아래로 들어갔는지.

“살아남은 혈족이 있었군요.”

“맏형이었다더군. 소가주였음에도 멸문지화(滅門之禍) 속에서 살아남았으니 천운을 타고난 게지. 바로 그 천운과 그보다 더한 복수심으로 사막을 넘어 마교에 의탁했고……. 이후의 일은 눈치 빠른 네 녀석이라면 충분히 짐작할 수 있을 것이다.”

마치 눈앞에서 태극기가 펄럭이는 듯한 이 기분은 뭘까.

오래전에 봤던 고전 명작 영화가 문득 떠올랐지만, 그것도 잠시뿐이었다.

눈물 콧물 다 쏟았던 그 영화와는 달리, 이 이야기는 결말부터가 다를 테니까.

그리고 그 결말에 담긴 의미가, 적천강이 좋지 않은 옛 추억을 끄집어 낸 이유일 테니까.

“군자도는 죽었겠군요.”

적천강이 나지막한 음성으로 대답했다.

“그래, 맞다. 노부가 직접 그를 처단했지.”

“그 선택을, 후회하십니까?”

“후회라. 너라면 어떨 것 같으냐?”

“……!”

“사마표와 태산. 그 두 녀석이 사마공의 밀명으로 일을 꾸미고 있다면, 그리고 그 밀명이 암천과 연관이 있다면……. 넌 어찌하겠느냐.”

나는 침묵했다.

고작 일 년.

깊은 정을 쌓기에는 짧은 시간이다. 살아온 환경도 다르고, 성격도 다르다.

하지만 어째서일까.

꽉 닫힌 입술 사이로, 그 어떤 대답도 쉽게 흘러나오지 않았다.

분명 망설임 없이 답해야 하는 질문이었음에도 불구하고.

너라면 어찌하겠느냐.

적천강의 그 물음이, 끝없이 부딪치는 메아리가 되어 귓가를 울리고 있었다.



* * *



며칠을 쉼 없이 내달린 끝에 기련산에 다다른 삼천의 군세가 짧지만 달콤한 휴식을 취하고 있을 그 무렵.

빛 한줄기 들어오지 않는 칠흑 같은 밀실(密室)에서는 세 사람이 서로를 마주하고 있었다.

“일이 틀어졌소. 그것도 아주 많이.”

“화왕, 그 빌어먹을 노괴(老怪)가 어찌 이곳에 있는 거요?”

자리에 앉자마자 기다렸다는 듯이 날아드는 두 줄기의 음성에, 상석(上席)을 차지한 누군가가 대답했다.

“이미 엎질러진 물. 상황이 바뀌었으니 새로운 대책을 세우기 위해 두 분을 모셨소.”

“시작부터 보기 좋게 엇나갔거늘, 한마디 변명 없이 자신감만 넘치시는구려.”

“이번만큼은 우리를 납득시켜 줘야 할 거요, 사마 문주.”

“……납득이라.”

상석의 누군가. 아니, 흑야왕 사마공의 안광이 돌연 번뜩였다.

어둠 속에서 자신을 응시하는 두 노도사(老道士)를 향해.
```

## Final English reading copy

```markdown
# Chapter 1018

“He was burning a secret letter alone, without anyone knowing.”

The words slipped from my lips in a low murmur.

Jeok Cheongang’s gaze, fixed on me, had grown dark and still.

“Could Namho have been mistaken?”

“That…”

I closed my mouth instead of finishing the sentence. Jeok Cheongang let out a quiet sigh.

“Damn it. So it’s true.”

At first, I’d thought the whole thing was just a simple misunderstanding.

A minor incident we could clear up by calling Sama Pyo over and talking to him directly.

But…

“Elder Nam was already certain.”

“I thought so. If he’s only just brought it up with you, he must have given it a great deal of thought until now.”

“Yes. At first, even he wasn’t sure. There wasn’t any solid evidence to back it up, either.”

Growing old meant the senses grew dull.

Namho had said he’d agonized over it again and again.

Whether the familiar smell he’d encountered over and over as an agent of the Hidden Shadow Pavilion was the same kind as the one that had lingered in Sama Pyo’s room.

Whether his dulled senses were leading him to make a baseless accusation.

And after more than seven days and nights of worry, this old Hidden Shadow Pavilion agent had reached only one conclusion.

*“It was definitely the smell of oiled paper burning. I’m certain now.”*

Oiled paper—paper treated with oil.

It was customary to soak missives in oil to keep them from getting wet or torn, and naturally, they smelled different when burned from dry paper.

*“Another reason to oil paper is that it burns easily. The more a letter must not be discovered, the more important it is to destroy the evidence quickly.”*

Namho had spent decades as an intelligence agent.

Though he’d found no trace of anything beyond the faint smell of something burning in the room, from that moment on he never let go of his suspicions about Sama Pyo and Taishan.

*“I watched them closely from the day we left Shanxi Province, but until just a few days ago, I still couldn’t be sure. Whether it really was oiled paper burning—and, if so, who had sent it, and from where.”*

But there was another, more important reason Namho had hesitated to reach a conclusion.

“He said the scent was unusual.”

“The scent? You mean the smell of the paper burning?”

“Yes. He said it was quite different from the various kinds of burning smells he knew.”

“Burning paper smells like burning paper. What does that—”

“I’ve heard each region has its own particular traits. Its customs, its food, and even the animals whose fat is used to make oil.”

At my quiet addition, Jeok Cheongang suddenly furrowed his brow.

“Wait. Could it be?”

“Elder Nam said there are animals found only in Gansu and Qinghai. Is that right?”

“Camels…!”

Jeok Cheongang gave a muffled gasp and nodded.

“So that’s what it was. The source of that unusual scent.”

“Since he’d spent his whole life in the Central Plains and Nanman, it wouldn’t have been easy for Elder Nam to tell the difference.”

“That’s right. Those oddly shaped beasts are hard to come across, since they live only in Qinghai and western Gansu.”

Besides, in Murim these days, it was common to use animal fats from cows, horses, sheep, and pigs.

But the day we first entered Gansu Province, Namho had been resting for a while with the other members of the Fire Dragon Pavilion when he stumbled upon an unexpected clue.

*“It was an incredible coincidence. I’d lost my appetite and was sitting by myself, lost in thought, when a familiar smell started wafting over. I asked what it was, and they told me it was camel meat.”*

That was how the clues came together. Once Namho had finally become certain, he told me what he’d found.

Sama Pyo had received a secret letter from someone, and it had almost certainly been sent from Gansu or Qinghai.

As for the exact identity of the person who had sent it, everyone who knew about the letter had already formed a vague guess.

Namho had mentioned Qinghai as well as Gansu only as a possibility. There was only one person who might send a secret letter all the way to Shanxi Province, thousands of *li* away.

“The Black Night King, Sima Gong…”

At my murmur, which sounded almost like I was talking to myself, Jeok Cheongang spat roughly.

“You’ve gotten bold. You really have.”

“What do you think the letter said?”

“Do you have a guess?”

“I do.”

“Then tell me.”

“At the very least, I’m pretty sure it wasn’t something like, ‘Is my son eating well?’”

In an instant, a vein bulged at Jeok Cheongang’s temple.

“You call that an answer? Even that Taishan—or Gangsan, whatever his name is—could tell you that.”

“Taishan might not.”

“……Honestly, I can’t argue with you on that one. Speaking of that oversized fool, how was he on the way here?”

“Elder Nam said he was definitely acting strange, based on what he’d observed over the last few days. The closer we got to Gansu, the less he ate, and he stayed gloomy all day.”

Of course, there was a slight—no, a considerable—problem with saying he ate less.

He was still stuffing his face five times a day. How was that eating less? That was eating plenty.

But considering how much Taishan usually ate, five meals a day was basically intermittent fasting.

And the closer we got to Gansu, the more miserable he looked. There was no shortage of things that seemed strange.

*Knowing Sama Pyo, he might’ve kept it from Taishan, too.*

Whatever the case, only one thing mattered most right now.

While they were still in Shanxi Province, a secret letter containing some hidden message had passed between father and son. And whatever it said, it certainly wasn’t a hopeful or positive development for us.

I didn’t want to think this way, but if the absolute worst happened…

“Hmm.”

I shook my head, trying to force the thought from my mind.

Jeok Cheongang had been watching me closely. Then he abruptly spoke.

“Are you worried?”

“About what?”

“About having to cut down Sama Pyo and Taishan with your own hands.”

“……!”

*Step.*

Without realizing it, I stopped walking.

I’d been walking almost mechanically, but now I stood stock-still, staring silently at Jeok Cheongang.

“You look like you have a lot to say.”

“……”

“Since you’ve clammed up, let this old man tell you an interesting story.”

I didn’t answer, and Jeok Cheongang didn’t wait for one.

“During the Great Faction War, when the world was going up in flames, I came to know a man called the Junzi Saber.”

We started walking again, and I replied, my voice troubled.

“That’s quite a title.”

“Like hell it is. At first, I didn’t care for it much. The title was so embarrassingly grand it made my fingers curl up—and nearly break. But after spending some time with him, cutting down Demonic Cult bastards, I found he was a pretty useful fellow.”

“What do you mean, useful?”

“Both as a person and as a martial artist.”

“That’s quite a compliment. Especially coming from you, Old Master.”

“People thought even more highly of him. He came from a once-prominent martial family, though it had fallen into decline. His personal skill and sense of justice were exceptional, and he always led the way in even the most dangerous situations. He never backed down.”

In other words, he’d been the very model of a chivalrous hero.

The first to charge in, the last to retreat, living out the spirit of self-sacrifice with his whole body.

But I already had a feeling how this story, which had come out of nowhere, would end.

“Why are you talking about him entirely in the past tense? You sound like you regret what happened.”

A bitter smile passed over Jeok Cheongang’s lips.

“You’re a sharp one.”

“Was he a traitor?”

“Yes. He was a Demonic Cult lackey. But he hadn’t been one from the beginning.”

“You mean…”

“Do you remember what I told you about the Junzi Saber’s origins?”

“Yes. He was from a prominent martial family in Qinghai.”

“In truth, his family had been completely destroyed in a war with another sect. ‘Scattered to the winds’ would be more accurate. The only family he knew was an old retainer who’d raised the infant Junzi Saber by begging for breast milk.”

The only family he *knew*.

It suddenly made sense.

Why that chivalrous hero from the past had ended up under the Demonic Cult’s shadow.

“There was a surviving relative.”

“His eldest brother, apparently. He was the Lesser Family Head, yet survived the family’s destruction. You’d have to call him blessed by fate. He crossed the desert and sought refuge with the Demonic Cult, armed with that luck—and a thirst for revenge even greater than it. …You’re sharp enough to guess what happened next.”

Why did it feel like I could see the Korean flag waving before my eyes?[^1]

A classic movie I’d seen long ago came to mind—but only for a moment.

[^1]: *Taegukgi* (“Korean flag”) is the Korean title of a film about brothers caught up in the Korean War.

Unlike that movie, which had made me cry my eyes out, this story’s ending would be different.

And that ending was why Jeok Cheongang had dredged up an unpleasant memory from his past.

“The Junzi Saber must’ve died.”

Jeok Cheongang answered in a low voice.

“Yes. I killed him myself.”

“Do you regret that choice?”

“Regret it? What would you have done?”

“……!”

“If Sama Pyo and Taishan are plotting something on Sima Gong’s secret orders—and those orders are connected to Dark Heaven… what would you do?”

I fell silent.

A mere year.

It wasn’t long enough to form a deep bond. We’d lived in different circumstances, and we had different personalities.

But why?

No answer came easily through my tightly pressed lips.

Though it was a question I should have answered without hesitation.

*What would you do?*

Jeok Cheongang’s question echoed in my ears, colliding again and again without end.

* * *

Around the time the three thousand troops, after several days of nonstop marching, reached the Qilian Mountains and were taking a brief but sweet rest—

In a pitch-black secret chamber where not a single ray of light could enter, three people faced one another.

“Things have gone wrong. Very wrong.”

“The Fire King—that damned old monster—what’s he doing here?”

Two voices came flying at once as soon as the others had taken their seats. The person occupying the seat of honor answered.

“What’s done is done. The situation has changed, so I’ve summoned the two of you to come up with a new plan.”

“Things have gone badly from the start, yet you’re brimming with confidence without offering a single excuse.”

“This time, Sect Leader Sima, you’ll have to give us a reason to accept this.”

“……Accept it.”

The eyes of the person in the seat of honor—no, the Black Night King, Sima Gong—suddenly gleamed.

He stared into the darkness at the two old Daoists facing him.
```
