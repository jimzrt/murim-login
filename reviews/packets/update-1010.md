<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1010.txt",
      "sha256": "77cbbaeec253741a79e723024c625da2b9e00baa9673cc510a0ba9b8113c9323",
      "bytes": 12626
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "cd713e4da57ff58a16cd9afbecbe3312bab9c93f756d79912504c5b151f2e125",
      "bytes": 871
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b104545771a66a8fc3a9ca63e7f5e7da6a886d5b28c68d12d55267b0309741d3",
      "bytes": 237440
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a9da793a64f798d655c7983725258c0ce8e0c6cbbd885646861ae89cc0d74dc2",
      "bytes": 1408
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4028c4ce290afa8201f0767dbb91be49e4ff4506338504d58bbc6b87165d112e",
      "bytes": 1614
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0d9d28acac0e1e0b40e62aa2ebdc4abb5086aaabe7e9f5d33b15637923636f7b",
      "bytes": 623
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "a49edca76efb13f967ef8166d9b565ed7e6f94af591f27e2f8704aadcca34c44",
      "bytes": 563
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "91011c42991384cf62a4375bb76f17c620aaadb6ab1aeb12c39baa47650647e2",
      "bytes": 733
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8a36c21af3e33ce8297d5a41a312212a7b74793dcd26a6bf5d9ca9c9372e2ef2",
      "bytes": 276653
    }
  ],
  "estimated_tokens": 10491
}
-->

# Durable State Update — Chapter 1010

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
1 and safe_through 1010. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1010. Profile updates may replace only one
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
  "chapter": 1010,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1010,
    "continuity_sources": [1010],
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
    "Baekma Bang is the largest group in Ningxia and is opening a trade route west toward Xinjiang.",
    "Baekma Bang scouts saw at least a thousand Dark Heaven tents in the western desert, on a route closer to Gansu than Qinghai.",
    "Ma Junggeol's group followed the force for a day and a half at a distance of one hundred li before returning with its report.",
    "Ma Junggeol says Baekma Bang has important information about Dark Heaven and came to offer help."
  ],
  "continuity_sources": [
    1008,
    1009
  ],
  "open_questions": [
    "Who was the unknown master who helped reform the Ningxia bandit leaders?",
    "What is Dark Heaven's full strength and objective in the western desert?"
  ],
  "safe_through": 1009,
  "temporary_decisions": [
    "Render 곡차 in this drinking scene as grain liquor."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 하오문    | **Lower District Sect**          |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 초식     | **form**                                         | Numbered technique movement                           |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 상태               | **Status**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마중걸 | **Ma Junggeol** |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 계인 | **Buddhist precept seals** | Seals carved into the foreheads of Shaolin martial monks. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 하오문도 | **Lower District Sect member** | Member of the Lower District Sect. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 마방 | **horse caravans** | Descendants of northern mounted tribes who traveled ancient trade routes between the Outer Lands and the Central Plains. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 녕하성 | **Ningxia Province** | Region between Gansu and Shaanxi. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 진태경 | 마중걸 | Murim Alliance member to visiting horse-caravan chief | Junggeol | casual | Initially addresses him familiarly, then apologizes and shifts to polite speech. |
| 마중걸 | 진태경 | visiting horse-caravan chief to young Murim Alliance member | young man | polite and deferential | Initially calls him a pretty little gigolo as an insult, then uses a respectful address. |
| 마중걸 | 적천강 | visiting horse-caravan chief to legendary martial master | Great Hero Jeok Cheongang | polite and deferential | Recognizes Jeok as the Fire King. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |
| 마중걸 | 사마공 | visiting group leader to sect leader | Sect Leader Sima | polite and respectful | Addresses him as 사마 문주 while explaining Ningxia and Baekma Bang. |
| 사마공 | 마중걸 | sect leader to visiting group leader | you | formal and probing | Uses 자네 while questioning Ma Junggeol about following Dark Heaven. |

## Listed compact profiles

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1009
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1005
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1005
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1009
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** He is initially confrontational under pressure but becomes formal and earnest when explaining his group’s purpose.
- **Voice:** Not established
- **Relationships:** He leads six associates who, with him, are known as the Seven Masters of Baekma Bang.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1009
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating, yet outwardly gentle; he uses persuasive sophistry and a calming manner to justify hard choices.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1010화



“결국, 그리 결정한 것이냐?”

적천강의 물음에 나는 고개를 끄덕였다.

“예. 아무래도 이곳에 남아 있어야 할 것 같습니다.”

아마도 마중걸과 그 수하들이 반나절만 늦게 도착했다면, 나는 이미 화룡각 대원들과 함께 청해성으로 향하고 있었을 것이다.

‘현재로서도 감숙성의 전력은 충분했으니까.’

공동파와 종남파.

각각 구파일방에 속한 두 거목이 버티고 있는 데다가 사마공이 이끄는 흑룡마문 또한 결코 그에 못지않다.

흑룡마문의 휘하에 몰려든 흑도와 사파는 질적인 면에서 떨어질지 몰라도, 단순히 그 머릿수만으로도 엄청난 전력이다.

하지만 이제는 상황이 달라졌다.

최소 수만에 이를 것으로 추정되는 암천의 대군세도 문제지만, 내가 감숙에 남기로 결정한 가장 큰 이유는 다름 아닌 시간이었다.

놈들이 이곳까지 들이닥치는 시간.

“녕하로 돌아온 시점이 정확히 언제였습니까?”

마중걸이 대답했다.

“사흘 전이었소. 오밤중에 도착했으니 이틀 전이라고 해도 무방하겠구려.”

“사흘 전?”

불쑥 끼어든 적천강이 눈살을 찌푸리자, 마중걸이 황급히 말을 이었다.

“다, 당장 위급한 것은 저희 역시 마찬가지라, 녕하 곳곳에 급보를 전하고 수하들을 움직이느라 정신이 없었습니다.”

앞선 반응을 이미 사흘 전에 도착했던 놈이 왜 이제야 찾아왔냐고 해석한 모양이지만, 나는 적천강이 왜 눈살을 찌푸렸는지 알고 있었다.

‘딱 그 무렵이군.’

문득 뇌리를 스치는 기억이 있다.

그리 멀지 않은 곳에서 마적단 놈들이 활보하고 있다며 두려움에 떨고 있던 수백여 명의 사람들.

그들에게 있어 녕하성은 아직까지도 무법천지로 인식되어 있었을 테니, 마중걸이 전한 급보로 인해 난리통이 된 분위기가 마적단들의 습격쯤으로 여겨졌을 것이다.

워낙 최근에 벌어진 일이라 섬서지부 소속인 하오문도 역시 자세한 사정을 모르기는 매한가지였을 테고.

‘결국 이것 때문이었나.’

세상일은 돌고 돌며, 동시에 하나로 이어지는 법.

어떤 사건의 결과는 또 다른 한 사건의 발단이 되고, 결국 지금에 이르렀다.

그리고 사흘 전에 도착했다는 마중걸의 대답은 모두의 머릿속을 복잡하게 만들기에 충분했다.

“하면, 돌아오는 데까지 소요된 시일은 어느 정도인가?”

풍운검군의 물음에 마중걸이 손가락을 꼽았다.

“어디 보자. 사막을 빠져나오는 것만 칠주야, 또 초원을 다시 가로지르는 것에 그보다 하루가 더 걸렸으니까…… 약 달포 정도입니다.”

“잠깐. 조금 전에는 가는 데에만 스무날이 걸렸다고 하지 않았나? 거기에 더해 하루하고도 반나절 동안 암천을 추적했었고.”

“그랬지요. 하지만 초행길을 처음 지날 때와 다시 돌아올 때의 사정은 다릅니다. 저희가 괜히 마적, 아니 마방(馬房)이겠습니까?”

“……음.”

부정할 수 없는 반론이다.

초절정 고수인 풍운검군이 일부 초식만 보고도 상대의 수준과 어떤 종류의 무공을 익혔는지 짐작할 수 있듯이, 가장 빠른 길을 찾아 이동하는 것에는 마적과 마방을 따라올 자들이 없다.

“신중함도 과하면 독이 되는 법. 진정 중요한 것은 따로 있지.”

쉽사리 말문을 잇지 못하는 풍운검군을 제지한 적천강이 마중걸을 응시했다.

“만약 네가 수만의 대군을 이끌고 있다면, 이곳까지 도달하기까지 어느 정도의 시일이 필요하겠느냐?”

“그, 그것은.”

뭔가를 골똘히 생각하던 마중걸이 이내 한숨을 내쉬었다.

“쉽게 답하기 어렵습니다. 하지만…….”

“하지만?”

“낙타와 사막마는 물론 모든 물자가 충분히 갖추어진 상태라는 전제하에, 그리고 전원이 엄청난 강행군을 버틸 만큼의 무공을 익힌 이들이라면…… 예. 아무리 지체된다고 해도 한 달입니다.”

“한 달. 고작 한 달이라.”

“물론, 경우에 따라 그보다 훨씬 단축될 수도 있지요.”

눈치를 살피며 덧붙인 마중걸의 한 마디에, 이야기를 듣고 있던 사마공의 얼굴이 딱딱하게 굳었다.

“어떤 경우를 말하는 것인가?”

“잊으셨습니까? 저희야 초원을 가로지르느라 필요 이상의 시일이 지체되었던 것이지, 당시 파악한 놈들의 위치는 감숙과 그리 멀지 않았습니다. 그 엄청난 병력을 감안하더라도…….”

말꼬리를 흐린 마중걸이, 마른침을 꿀꺽 삼키며 말을 이었다.

“한, 스무 날 정도면 충분할 겁니다.”

“……!”

“……!”

회의실 안의 공기가 차갑게 식었다.

아니, 식은 것을 넘어 빙하처럼 얼어붙었다.

마중걸의 한마디에 잠시 잊고 있었던 사실을 깨달은 사람들은 부릅뜬 눈으로 서로를 바라보았다.

맞다.

최대한 신속하게 왔던 길로 되돌아와야 했던 마중걸과는 달리, 암천에게는 또 다른 선택지가 있었다.

바로 진격이다.

초원을 경유하는 것이 아닌, 압도적인 힘으로 곧장 전방을 무너트리고 돌파하는 선택지.

그리고 만약 놈들이 정면 돌파를 선택했다면, 전투가 벌어지기까지 남아 있는 시간은 그야말로 한 줌에 불과했다.

‘앞으로 하루, 혹은 이틀.’

물론 최악의 상황을 가정했을 때의 이야기다.

마중걸이 떠난 직후 암천의 대군세가 며칠을 더 그 자리에 머물렀을지, 혹은 지금도 여전히 그곳에 머무르고 있을지는 아직 누구도 모른다.

하지만 지금은 늘 최악의 상황을 염두에 두고 움직여야 한다.

그것이 바로 전쟁이니까.

“더 이상의 탁상공론은 개나 줘 버려야 할 것 같군. 다들 그렇게 생각하지 않나?”

침묵을 깨트리는 적천강의 나직한 음성 위로, 현재의 상황과는 어울리지 않은 맑은 종소리가 덧씌워졌다.

띠링.



* * *



드드드득.

마치 작은 산이 움직인다면 이런 광경일까.

흑룡마문과 종남파.

그리고 사마공이 인근에서 징발한 수백의 무인들까지 더하자 이천을 넘어 삼천에 가까운 머릿수가 모였고, 등 뒤로 끝없이 펼쳐진 인마(人馬)의 물결을 응시하던 나는 문득 허공으로 시선을 돌렸다.

정확히는, 허공 어딘가에 떠 있는 반투명한 홀로그램 창을 향해.



- 진행 중인 퀘스트 조건이 충족되었습니다!

- 서쪽으로 향하기 (완료)

- 퀘스트, [사막의 아지랑이]를 성공적으로 완료했습니다!

- 퀘스트 보상이 지급됩니다!

- 대량의 경험치와 명성을 획득했습니다!

- [사막의 아지랑이]가 완료됨에 따라, 새로운 연계 퀘스트가 생성되었습니다.

- 신규 퀘스트를 확인하시겠습니까?



고작 한 식경.

삼천에 달하는 대병력이 모든 준비를 끝마치고 출격하기까지 걸린 시간치고는 너무나도 촉박했고, 새롭게 생성된 연계 퀘스트를 확인할 시간 따위는 있을 리 만무했다.

‘물론 이미 얼추 예상되는 내용이라 굳이 급하게 확인할 필요도 없었지만.’

나는 힘차게 달려가는 말고삐를 고쳐 쥐며, 마음속으로 명령어를 읊었다.

‘퀘스트 창 오픈.’

띠링.



퀘스트



[피의 길]



아득한 과거, 대륙과 대륙을 잇는 교역로였던 이 땅은 오늘날에 이르러 중대한 위기에 처하고 말았습니다.

생소한 이목구비를 지닌 이국(夷國)의 상인들도, 수레 한가득 비단을 싣고 사막을 넘어 이국으로 향하던 이들도 더는 존재하지 않습니다.

광활한 사막의 지배자들은 중원을 풍요롭게 만드는 교역로를 끊었고, 이제는 장성 안의 전부를 원합니다.

비단이 흘러넘치던 옛 시절은 이미 케케묵은 과거가 되었습니다.

무수히 많은 강철과 피. 그리고 시체만이 이 땅의 현재이며 미래가 될 것입니다.

부디 무운을 빕니다.



등급 : 초절정

제한 : 진태경

임무 : 감숙성 일대 적 섬멸 (미완료)

보상 : 대량의 경험치와 명성

 선택에 따른 연계 퀘스트

실패 : [암천]의 승리

 감숙성 지배권 상실





‘역시나.’

어느 정도는 예상했던 내용이다.

아니, 실패하면 저 정도로 끝나지 않으리라는 것도 충분히 알 수 있었다.

‘감숙성의 전선이 붕괴한다면, 그때는 서부 전체가 위태로워지겠지.’

전쟁은 곧 도미노와 다름없다.

제아무리 처음부터 끝까지 신중하고 치밀하게 준비한다 해도, 단 한 번의 실수로 지금껏 쌓아 올린 모든 것이 단숨에 허물어지고 만다.

‘더 늦기 전에 막아야 해.’

그나마 다행인 것은 감숙 무림의 대처가 철저하다는 것이었다.

무려 삼중에 걸친 전선과 중요성에 따라 차등 배치한 삼만여 명의 병력.

그리고 그 삼중 전선 중, 가장 최전선에 배치된 돈황(敦煌)은 전력을 다한다면 사흘 안에 주파할 수 있는 거리였다.

비단길.

현대의 세계인들에게는 실크로드(Silk road)라는 이름으로 더 잘 알려진 이 일대는, 그야말로 평야와 황야의 끝없는 연속이었으니까.

폭이 좁은 길을 지나느라 속도를 줄일 필요도, 말을 버릴 만큼 험준한 지형도 없다.

그저 말이 지쳐 쓰러질 때까지 쉬지 않고 달리면 그만이었다.

문제는…….

‘암천. 그놈들도 마찬가지라는 거지.’

그것이 단 촌각도 지체할 수 없는 이유다.

낙타와 사막마가 있다 해도 사막에서의 이동 속도는 어느 정도 한계가 있지만, 모래가 아닌 흙과 풀에 뒤덮인 땅으로 접어든다면 이야기가 달라진다.

돈황은 첫 번째로 쓰러지는 도미노가 될 테고, 수만의 적들은 이내 메뚜기 떼처럼 감숙성을 뒤덮을 것이 분명…….

“뭘 그리 빤히 보고 계시오?”

“……!”

“뭐, 구름 모양이라도 살피시나?”

거짓말이 아니라, 정말 소스라치게 놀랐다.

갑작스럽게 들려온 목소리 때문이 아니라, 고개를 돌리자마자 시야를 가득 메운 흉악한 인상 때문에.

“아이, 씨. 깜짝이야. 갑자기 뭡니까?”

전직 마적이자 현직 마방답게, 거세게 들썩이는 말안장 위에서도 흔들리지 않는 편안함을 보여 주고 있던 마중걸이 대답했다.

“별건 아니고. 아까부터 허공만 뚫어져라 바라보고 있길래 말 좀 걸어 봤소.”

“내가 어디를 보건 무슨 상관이에요. 그리고 우리가 그렇게 친한 사이는 아닌 것 같은데?”

“당연히 아니지. 나한테 화살비를 퍼붓게 만든 장본인이잖소 그것도 무려 세 번이나.”

가뜩이나 흉악하게 생긴 얼굴을 잔뜩 찌푸리는 마중걸을 향해, 나는 심드렁하게 대꾸했다.

“그래서요?”

“……양심이란 게 없소? 그리고, 두 번까지야 그렇다 치더라도 마지막 세 번째는 도대체 무슨 생각으로 발사 명령을 내린 거요?”

“그냥. 두 번 하면 정 없어 보일까 봐.”

“……?”

“끝. 됐죠?”

대충 던진 대답에, 마중걸이 미친놈 보듯이 입을 딱 벌렸다.

“되긴 뭐가 돼. 사람 맞소?”

“그건 내가 해야 할 말 같은데.”

“……지금 그거, 무슨 뜻이오?”

무슨 뜻이긴. 다 알면서.

하지만 생긴 것 가지고 팩트 폭행을 하기에는 내 마음이 너무나도 여리다.

말없이 어깨를 으쓱해 보인 나는 마중걸을 보며 문득 생각했다.

‘그나저나, 확실히 생긴 거랑은 영 딴판이란 말이지.’

얼굴만 보면 세상을 파멸로 몰아넣고도 남을 흉신악살이 따로 없는데, 하는 짓이나 드문드문 드러나는 성격을 보면 의외로 멍청한 구석이 있다.

아직 마중걸을 비롯한 마방들을 향한 의심을 거두지 않은 몇몇 수뇌부들의 강력 주장으로 반쯤 볼모가 된 지금에도, 저리 태평한 모습을 보이고 있으니.
```

## Final English reading copy

```markdown
# Chapter 1010

“So, that’s what you’ve decided?”

At Jeok Cheongang’s question, I nodded.

“Yes. I think I need to stay here after all.”

If Ma Junggeol and his men had arrived half a day later, I’d probably already be on my way to Qinghai with the Fire Dragon Pavilion members.

*Gansu had enough forces as things stood.*

The Kongtong Sect and the Zhongnan Sect.

Two towering powers belonging to the Nine Sects and One Gang stood firm here, and the Black Dragon Demon Gate, led by Sima Gong, was every bit their equal.

The dark-path figures and unorthodox factions gathered under the Black Dragon Demon Gate might have been inferior in quality, but their sheer numbers made them an enormous force.

But now the situation had changed.

The massive Dark Heaven army—estimated to number at least tens of thousands—was a problem. But the biggest reason I’d decided to stay in Gansu was time.

The time it would take them to reach us.

“When exactly did you return to Ningxia?”

Ma Junggeol answered.

“Three days ago. We arrived in the middle of the night, so I suppose you could say it was two days ago.”

“Three days ago?”

Jeok Cheongang cut in abruptly, furrowing his brow. Ma Junggeol hurriedly continued.

“W-we were in a hurry, too. We were so busy sending urgent messages throughout Ningxia and getting our men moving that we couldn’t think of anything else.”

He’d apparently interpreted Jeok Cheongang’s reaction as, *You arrived three days ago, so why are you only coming to us now?* But I knew why Jeok Cheongang had frowned.

*That was right around the time.*

A memory suddenly came to mind.

Several hundred people had been trembling with fear, saying that mounted bandits were roaming not far away.

Ningxia Province must still have seemed lawless to them. So, with Ma Junggeol’s urgent message causing an uproar, they’d probably assumed the mounted bandits were attacking.

It was hardly surprising that even the Lower District Sect member from the Shaanxi branch knew nothing about the details. It had all happened so recently.

*So that’s what it was.*

The events of the world turn in circles, and they’re all connected at the same time.

One incident’s aftermath becomes the beginning of another, and eventually it all leads to the present.

And Ma Junggeol’s answer—that they’d arrived three days ago—was enough to leave everyone with plenty to think about.

“How long did it take you to get back?”

At the Wind-and-Cloud Sword Lord’s question, Ma Junggeol counted on his fingers.

“Let’s see. It took seven days and nights just to get out of the desert, and crossing the grasslands again took another day longer than that… About a month, I’d say.”

“Wait. Didn’t you say earlier that it took twenty days just to get there? And then you spent another day and a half following Dark Heaven.”

“That’s right. But there’s a difference between traveling a route for the first time and making the return journey. Do you think we’re mounted bandits—no, horse caravans—for nothing?”

“...Hmm.”

It was an argument he couldn’t refute.

Just as the Wind-and-Cloud Sword Lord, a Supreme Peak master, could get a sense of an opponent’s level and the kind of martial arts they practiced after seeing only a few forms, no one could match mounted bandits and horse caravans when it came to finding the fastest route.

“Too much caution can become a poison. There’s something more important here.”

Jeok Cheongang stopped the Wind-and-Cloud Sword Lord before he could respond, then fixed his gaze on Ma Junggeol.

“If you were leading an army of tens of thousands, how long would it take you to reach here?”

“W-well…”

Ma Junggeol thought hard for a moment, then let out a sigh.

“That’s hard to answer. But…”

“But?”

“Assuming we had enough camels, desert horses, and supplies—and everyone had trained enough to endure an extreme forced march… Yes. Even if there were delays, it would take a month at most.”

“One month. Just a month.”

“Of course, depending on the circumstances, it could be much shorter.”

At Ma Junggeol’s addition, delivered as he gauged the room, Sima Gong’s face stiffened.

“What circumstances do you mean?”

“Have you forgotten? We lost more time than we needed to because we crossed the grasslands. The location we’d found them in wasn’t all that far from Gansu. Even taking that enormous force into account…”

Ma Junggeol trailed off, then swallowed hard before continuing.

“A-about twenty days should be enough.”

“……!”

“……!”

The air in the meeting room turned cold.

No—it froze like a glacier.

Everyone who’d briefly forgotten that fact now realized it and looked at one another with wide eyes.

That was right.

Unlike Ma Junggeol, who had to hurry back the way he’d come, Dark Heaven had another option.

They could advance.

Instead of detouring across the grasslands, they could break through the front by sheer force.

And if they chose a direct assault, the time left before a battle began would be next to nothing.

*One day, or maybe two.*

Of course, that was the worst-case scenario.

No one knew whether Dark Heaven’s army had remained there for several more days after Ma Junggeol left—or whether they were still there now.

But at a time like this, we had to plan for the worst.

That was war.

“I think we can throw any more armchair strategizing out the window. Don’t you all agree?”

Above Jeok Cheongang’s low voice, which broke the silence, rang a clear chime that didn’t fit the situation at all.

*Ding.*

* * *

*Rumble, rumble.*

Would this be what it looked like if a small mountain were moving?

With the Black Dragon Demon Gate and the Zhongnan Sect—and the hundreds of martial artists Sima Gong had conscripted from nearby—the force had grown to more than two thousand, close to three thousand. As I looked at the endless wave of people and horses stretching out behind me, I suddenly glanced up.

More precisely, I looked toward the translucent holographic window floating somewhere in the air.

> **System**  
> The conditions for the current Quest have been met!  
> **Head West** — Complete  
> Quest **Desert Mirage** successfully completed!  
> Quest rewards have been granted!  
> Gained a large amount of EXP and Fame!  
> A new linked Quest has been generated upon completion of **Desert Mirage**.  
> Would you like to view the new Quest?

Barely half an hour.

That was far too little time for a massive army of three thousand to finish all preparations and set out. There was no way I’d have time to check the newly generated linked Quest.

*Though I had a rough idea what it would say, so there was no need to check in a hurry.*

I tightened my grip on the reins of my galloping horse and silently gave the command.

*Open Quest window.*

*Ding.*

> **System**  
>   
> **Quest**  
>   
> **Road of Blood**  
>   
> Long ago, this land was a trade route linking one continent to another. Today, it has fallen into grave peril.  
>   
> The foreign merchants, with their unfamiliar features, are gone. So are those who used to cross the desert, heading for foreign lands with wagons piled high with silk.  
>   
> The rulers of the vast desert have cut off the trade routes that once brought prosperity to the Central Plains. Now they want everything within the Great Wall.  
>   
> The old days, when silk flowed in abundance, have already become a distant, dusty past.  
>   
> Endless steel, blood, and corpses will be the present and future of this land.  
>   
> May fortune be with you.  
>   
> **Grade:** Supreme Peak  
> **Restriction:** Jin Taekyung  
> **Mission:** Annihilate hostile forces in the Gansu region — Incomplete  
> **Reward:** A large amount of EXP and Fame  
> **Linked Quest determined by your choice**  
> **Failure:** **Dark Heaven** wins  
> — Lose control of the Gansu region

*As expected.*

That was more or less what I’d expected.

Actually, I knew full well that if we failed, it wouldn’t end there.

*If the Gansu front collapses, the entire western region will be in danger.*

War was just like a line of dominoes.

No matter how carefully and thoroughly you prepared from beginning to end, one mistake could bring everything you’d built crashing down in an instant.

*I have to stop them before it’s too late.*

The one thing we had going for us was that Gansu Murim had prepared thoroughly.

Three successive defensive lines, with thirty thousand troops deployed according to each line’s importance.

And Dunhuang, the foremost of those three lines, was close enough to reach in three days if we pushed ourselves to the limit.

The Silk Road.

This area, better known to people of the modern world as the Silk Road, was one endless stretch of plains and wilderness.

There was no need to slow down for a narrow path, no rugged terrain that would force us to abandon our horses.

All we had to do was keep riding until the horses collapsed from exhaustion.

The problem was…

*Dark Heaven could do the same.*

That was why we couldn’t afford to lose even a moment.

Even with camels and desert horses, there was a limit to how fast they could travel through the desert. But once they reached land covered in soil and grass instead of sand, that would change.

Dunhuang would be the first domino to fall, and tens of thousands of enemies would soon swarm across Gansu like locusts—

“What are you staring at so intently?”

“……!”

“Checking the shape of the clouds or something?”

I wasn’t exaggerating when I said I nearly jumped out of my skin.

It wasn’t the sudden voice that startled me. It was the menacing face that filled my vision as soon as I turned around.

“Ah, damn. You scared me. What’s with you all of a sudden?”

Ma Junggeol, who looked perfectly comfortable even on a saddle bouncing violently beneath him—a former mounted bandit, current horse-caravan chief—answered.

“Nothing much. You’ve been staring into the air for a while, so I thought I’d talk to you.”

“What’s it to you where I’m looking? And I don’t think we’re close enough for you to just chat me up.”

“Of course we’re not. You’re the one who had them rain arrows down on me. Three times, no less.”

I answered Ma Junggeol, who was scowling so hard his already vicious face looked even worse.

“So?”

“...You’ve got no conscience, do you? And even if I can understand the first two times, what on earth were you thinking when you ordered them to fire that third time?”

“Just thought stopping at two would make me look cold.”

“……?”

“That’s it. Happy?”

At my offhand answer, Ma Junggeol gaped at me as if I were insane.

“What do you mean, ‘that’s it’? Are you even human?”

“Feels like that’s a question I should be asking you.”

“...What’s that supposed to mean?”

What did it mean? He knew perfectly well.

But I was too tenderhearted to hit him with the facts about his looks.

I silently shrugged, then looked at Ma Junggeol and suddenly thought:

*Still, he really is nothing like he looks.*

Judging by his face alone, he looked like some evil spirit who could plunge the world into ruin. But from the way he acted, and the bits of his personality that showed through now and then, he seemed surprisingly stupid.

Even now, at the strong insistence of a few leaders who still suspected Ma Junggeol and the other horse-caravan men, he was practically being held hostage. Yet he seemed utterly carefree.
```
