<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1069.txt",
      "sha256": "f0d5e584ce1fe206bcacf7bffddbe64f92463d41aab6dff64254163bb1e06050",
      "bytes": 12350
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3063ab543198cd8cc6f9953de58d90ef5822cb8955d487b8126b1c9d9254cd7f",
      "bytes": 1073
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2732e564b29748d27703f6f9fa741b08e869fe6ffc1aab99000bc0b5edca2776",
      "bytes": 242256
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3fbe198cad55c61532fc6af31dbeb56593116cd4ab32ea2a1149a8ad15ee8efe",
      "bytes": 1502
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "59a2577dac6ec7bbb4e9881523d2b0375a68235833c1ac1e4570332604779954",
      "bytes": 700
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "1c44ebf5b163ed00f9d69045238de718cb32bdcf3e978145e4e28f42a716491b",
      "bytes": 974
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "3a6adf661c67d8c21f7f941ebad88049de04071831c32fdfb742d493bf1a5c5b",
      "bytes": 700
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "0413ed7a645b698829beff9384c8399fd0d605e01bcbd978600e97cca8f64e41",
      "bytes": 673
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "9b4892eca365c7ff181b7d8ffc829e5cbdffcbd7c67855119e3803aad6840747",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "8241ac066db300f9309c220845d949891f2fee255d9789fddf88c8852b83dbc7",
      "bytes": 980
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7df8b2357d0faa08e63a571debd66c331206f8c9af0b11d116826f4c7dad2ad4",
      "bytes": 284375
    }
  ],
  "estimated_tokens": 10069
}
-->

# Durable State Update — Chapter 1069

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
1 and safe_through 1069. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1069. Profile updates may replace only one
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
  "chapter": 1069,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1069,
    "continuity_sources": [1069],
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
    "Jin’s allied force was pursued by hundreds of reanimated enemies after marching without proper rest; Jin killed the pursuers, but the fate of the watching crow is unknown.",
    "Ma Sanbao serves the Blood Lord and was covertly watching Jin’s force; the surveillance was detected, first by Great Sir in Ningxia.",
    "The East Depot’s network had shared its view with Dark Heaven through the Eastern Heaven Demon Lord.",
    "The Grand Mage suspects Hyeoncheon and the Kongtong survivors went to Great Sir."
  ],
  "continuity_sources": [
    1068
  ],
  "open_questions": [
    "Who is Great Sir, and what is his connection to Hyeoncheon and the surviving Kongtong Disciples?",
    "Did Jin’s sword strike kill or otherwise affect the watching crow?",
    "Are Dark Heaven’s forces broadly composed of reanimated corpses, and has Ma Sanbao spread the Corpse Art to others?",
    "What is the Lord of Heaven seeking through Jin, and when will he appear?"
  ],
  "safe_through": 1068,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 궁성     | **Bow Saint**                 | —              |
| 곤륜파    | **Kunlun Sect**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 상태               | **Status**                     |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 노부      | **this old man / I**                                            |
| 소저      | **Young Lady**                                                  |
| 도사      | **Daoist**                                                      |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마중걸 | **Ma Junggeol** |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 석가 | **Shakyamuni** | Buddhist figure invoked by Hong Dao in his earlier conversation with Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 제니 | **Jenny** | East Asian news anchor interviewing Jacob. |
| 마방 | **horse caravans** | Descendants of northern mounted tribes who traveled ancient trade routes between the Outer Lands and the Central Plains. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 마중걸 | 적천강 | visiting horse-caravan chief to legendary martial master | Great Hero Jeok Cheongang | polite and deferential | Recognizes Jeok as the Fire King. |
| 마중걸 | 주화란 | fellow combatant addressing the young bureau head | Young Lady | polite and hesitant | Addresses her as 소저 while trying to speak up about his injuries. |

## Listed compact profiles

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1068
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1067
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1056
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1067
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1065
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** Though timid by nature, he is earnest and protective of his sworn brothers, loyal to the benefactor who helped them reform, and willing to bear personal risk for their mission.
- **Voice:** Not established
- **Relationships:** He leads six sworn brothers who, with him, are known as the Seven Masters of Baekma Bang, and trusts the benefactor they call the Lord.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1065
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1056
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

## Korean source

```text
1069화




원래 사람이 한순간에 돌변하면 주변인들은 알 수 없는 불안감을 느끼는 법이다.

그것이 쫓고 쫓기는 추격전 속에서 벌어진 일이라면 더더욱.

“흡……!”

불현듯 침묵을 깨트린 대인의 침음성에, 주위의 공기가 급속도로 얼어붙었다.

벌써 세 번째로 뒤쫓아온 추격대를 뿌리친 지 일각도 되지 않은 시점.

야트막한 언덕과 갈대숲에 몸을 숨긴 채 은밀하고도 신속하게 이동하던 아군들은 반사적으로 병장기를 움켜쥐었고, 그중에는 적천강 또한 포함되어 있었다.

“무슨 일이냐?”

낮게 가라앉은 적천강의 물음과 함께, 나를 포함한 모두의 시선이 대인을 향해 쏠렸다.

어느샌가 딱딱하게 굳어있는 얼굴.

그의 정신 상태를 의미하듯 언제나 살짝 풀려 있던 동공은 급속도로 팽창해 있었고, 이마에서는 식은땀 한 방울이 또르륵 굴러떨어졌다.

“느낌이, 느낌이 좋지 않소. 그것도 엄청나게.”

만약 이곳이 감숙성이었다면 저 인간이 이번엔 무슨 미친 소리를 지껄일까 하고 넘겼을지도 모른다.

그러나 제아무리 정신이 오락가락하더라도 대인은 명실상부한 초절정 고수고, 우리가 있는 이곳은 온갖 위협이 도사린 적지(敵地)였으며, 우연이라고는 해도 날짐승을 이용한 적들의 감시를 가장 먼저 알아차린 그의 말은 단순히 흘려들을 수 없는 종류의 것이었다.

타고난 육감(六感)이란 무공의 높고 낮음과는 다른 문제니까.

“느낌이 좋지 않다?”

심각하게 되묻는 적천강을 향해 대인이 고개를 끄덕였다.

“그렇소.”

“좀 더 자세히 말해 보거라. 맞아 뒈지기 싫으면 공손하게 존댓말 쓰고.”

“알겠소.”

대인의 대답을 듣고 허허 웃은 적천강이 나를 향해 고개를 돌렸다.

“노부가 저 미친놈을 손 봐줘도 되겠느냐?”

“되겠습니까?”

“아마 안 되겠지.”

“아시면서 왜 물어보세요.”

“혹시나 해서 물어봤다. 여하튼 그래서 정말 안 된다는 게냐?”

“손금 봐주는 것 정도는 괜찮은데, 손 봐주는 건 안 됩니다.”

“염병할. 강호의 도리가 아주 땅에 떨어졌구먼.”

하늘을 우러러 탄식한 적천강이 반쯤 포기한 얼굴로 대인을 바라보았다.

“그래, 일단 알겠으니까 우선 하려던 말이나 계속 씨불여 보거라. 정확히 무슨 느낌이라고?”

“이게 뭐랄까, 마치 보이지 않는 손이 뱃속을 쥐어 짜내는 느낌이오.”

“그리고?”

“자꾸만 속이 울렁거리고 식은땀이 나오.”

“어떤 이유로 그러는지 짐작이 가는 바가 있느냐?”

“그걸 모르겠소. 왠지 모르게 익숙한 감각 같기는 한……. 으헙!”

말을 끝마치기도 전에 다시 한번 터져 나오는 침음성.

동시에 얼굴이 창백하게 질린 대인이 누가 말릴 틈새도 없이 움직였다.

쉬익!

흐릿한 잔영까지 남기며 쾌속하게 뻗어 가는 신형.

삽시간에 빽빽한 갈대숲 사이로 사라지는 대인의 뒷모습에, 나와 적천강을 포함한 초절정 고수들은 황급히 그의 뒤를 쫓았다.

아니, 정확히는 쫓으려 했다.

막 발걸음을 뗀 그 순간, 갈대숲 사이로 선명하게 울려 퍼지는 어떤 소리를 듣기 전까지는.

푸득, 푸다다닥!

“……?”

아니, 뭔데 시벌.

모두가 설마 하는 마음이 된 그때, 짐작을 확신으로 바꿔 주는 대인의 목소리가 들려왔다.

“어흐으, 시원타…….”

“……!”

“……!”

죽음과도 같은 침묵이 내려앉은 공간 속, 믿을 수 없다는 눈빛으로 나를 바라보던 적천강이 굳게 닫혀 있던 입술을 뗐다.

“정말 안 되겠느냐?”

“…….”

“죽이지는 않고 한 군데만 부러트리겠다. 다리 말고 팔이나 뭐 그런 곳.”

적천강의 간절한 부탁에, 일그러진 얼굴로 코를 막고 있던 궁성이 코맹맹이 소리로 중얼거렸다.

“팔 정도면 괜찮을지도…….”

솔직히 살짝 갈등하긴 했다.

하지만 초인적인 인내심으로 마음속 충동을 참아 낸 나는 고개를 내저으며 생각했다.

‘육감은 개뿔이.’

여기서 더 육갑 떨지나 않으면 다행이지, 제 이름도 모르는 인간한테 뭘 기대했나 싶다.

‘그래도 일 인분 이상은 톡톡히 해 주니까.’

내심 한숨을 삼키던 그때, 요란하기 그지없던 볼일을 끝마친 대변. 아니, 대인이 세상 편안한 얼굴로 모습을 드러냈다.

“후우. 느낌이 좋군.”

“……아까는 느낌이 엄청나게 안 좋다면서요?”

“내가? 그럴 리가 있나. 자네가 착각한 거겠지.”

“진짜 개빡치네.”

“응? 지금 뭐라고 했나?”

“아닙니다. 그냥 혼잣말이에요.”

“흠. 안 좋은 버릇이 있군. 나야 상관없지만 조속히 고치도록 하게. 혼잣말을 자주 하면 주위 사람들이 정신 나간 사람으로 볼 수도 있거든.”

“…….”

아마도 잠시 이성의 끈이 끊어졌던 것 같다.

순간 눈앞이 흐려진다 싶더니, 어느새 웬 흉악한 얼굴이 내 앞을 가로막고 있었으니까.

“어어. 참으시오, 참으시오!”

“놔, 안 놔? 가뜩이나 못생긴 얼굴인데 여기서 더 엉망진창이 되고 싶어?”

얼떨결에 여기까지 따라오게 된 마적단의 수괴. 아니, 이제는 마방으로 업종을 변경한 마중걸이 슬픈 눈빛으로 나를 바라보았다.

“……그건 말이 너무 심하지 않소.”

“아, 미안합니다. 너무 흥분해서.”

이성을 되찾은 내 사과에 살짝 슬픔이 가신 마중걸이 대답했다.

“화를 좀 가라앉히시오. 대인께서 뭔가 악의적인 의도로 한 말이 아니라는 건 알고 있지 않소.”

물론 알고 있다.

사실 그 순수함 때문에 더 열이 받는 것일지도 모른다.

이 긴박하고도 위급한 상황에서 한껏 어그로를 끌더니 그 결과가 고작 쾌변이라니.

설령 내가 아니라 석가모니라 할지라도 아미시벌 관세음뒤짐을 외치며 목탁으로 대인의 뚝배기를 깼을 것이다.

‘그렇다고 어디에 버려두고 갈 수도 없고.’

순수 악이 있다면 그게 바로 대인이 아닐까.

땅이 꺼져라 한숨을 내쉰 나는, 모두가 볼 수 있도록 손을 들어 출발하라는 수신호를 전달했다.

당장 촌각이 아쉬운 상황에 벌써 일각에 가까운 시간을 허무하게 날려 버렸으니, 더욱 신속한 이동이 필요한 시점이었다.

‘이대로라면 목적지에 도달할 때까지 꼬박 며칠이 더 걸릴지도 몰라.’

산맥을 완전히 내려오기도 전에 있었던 첫 습격을 시작으로, 이미 세 번이나 적들의 추격을 허용한 상황.

그때마다 나를 비롯한 초절정 고수들이 앞장서서 성공적으로 추격대를 섬멸시켰지만, 중요한 것은 적들이 따라붙는 그 속도와 끈질김에 있었다.

‘놈들에게는 우리를 감시할 수 있는 눈과, 한시도 쉬지 않고 추격해도 지치지 않는 괴물들이 있으니까.’

죽음도, 고통도, 피로도 잊은 괴물들.

언데드(Undead)의 진정한 무서움은 바로 그 점에 있다.

죽음에서 다시 태어나며 감정을 빼앗겼고, 죽지 않았으나 이미 죽은 것이나 다름없는 존재이기에 감각도 잊었으며, 그와 같은 이유로 피로조차 느끼지 못한다.

‘산맥을 내려온 지 얼마 되지도 않았다. 그런데 이런 식으로 계속해서 발목이 잡힌다면…….’

순간 마음속에 떠오른 포위와 전멸이라는 단어를, 나는 조용히 씹어 삼켰다.

처음부터 패배를 생각하는 자는 결국 패배자가 될 수밖에 없다.

수천, 혹은 수만.

아니 설령 십만의 언데드가 숨통을 조여 오더라도, 나는 모두를 이끌고 이 촘촘한 그물을 찢으며 나아가야 했다.

우리의 목적지, 곤륜파를 비롯한 청해성의 아군들이 머무르고 있을 저 머나먼 동쪽으로.

그리고 이런 내 마음을 알아차린 듯, 재차 이동을 시작한 사람들 사이에서 빠져나온 주화란이 다가와 말했다.

“동쪽의 청해호(靑海湖)까지만 다다른다면 놈들도 쉽게 쫓아오지 못할 거예요.”

언제나 늘 그렇듯, 그림자처럼 주화란의 곁에 붙어 있던 송일섬이 불쑥 입을 열었다.

“틀린 말은 아니오. 단, 그곳에 청해성의 모든 전력이 집결해 있고 저 괴물들이 총력을 다해 우리를 뒤쫓지 않는다는 가정하에서만.”

“……송 호위.”

“아닙니다. 주 소저. 맞는 말이에요.”

어떻게 보면 찬물을 끼얹는 발언이었지만, 송일섬의 판단은 냉정하면서도 정확했다.

가슴 한구석에는 희망을 간직하더라도 머리로는 모든 것을 부정해야 한다.

최악을 기반으로 최선을 추구하는 것.

그것이야말로 생존과 승리를 위한 가장 중요한 요소였다.

“청해호까지 남은 거리는 어떻게 됩니까?”

“모든 여력을 쥐어짠다면 앞으로 이틀이에요. 지도를 샅샅이 살펴보아도 그 이상 단축할 수 있는 길은 없어요.”

지금 이 순간 주화란의 손에 들려 있는 저 낡은 지도는 결코 평범한 것이 아니다.

표왕(鏢王)이라고까지 칭해졌던 조부에게서 물려받은 것이며, 천하 각지에 은밀하게 숨겨진 길과 각 지역의 특징이 자세히 적혀 있다.

그러나 이곳은 청해성.

특히 끝없는 광야와 분지로 이루어진 북서부는 드문드문 늘어선 초목과 갈대숲만이 존재하는, 현재의 우리로서는 최악의 악조건으로 가득한 지형이었다.

‘반면 놈들에게는 최적의 지형이고.’

앞서 주화란은 말했다.

모든 여력을 쥐어짜도 청해호까지는 이틀이 걸린다고.

이는 추격자들이 계속해서 따라붙는다면 사흘, 나흘, 혹은 보름이 넘어도 이상하지 않다는 뜻이다.

‘놈들의 추격이 생각 이상이다. 은밀함과 신속함. 둘 중 하나는 포기해야 해.’

그렇다면, 내 선택은 하나뿐이다.

동시에 가장 먼저 해야 할 일도 매우 명확했다.

“벗어.”

불현듯 속도를 높이며 던진 한마디.

이에 최대한 몸을 수그린 채, 금의위들의 후미를 맡아 이동하던 정호군이 반사적으로 되물었다.

“뭐?”

“다시.”

“뭐……라고 하셨습니까?”

“당장 벗으라고.”

순간 동공 지진을 일으키는 정호군의 모습에, 나는 괜한 오해를 풀기 위한 부연설명을 덧붙였다.

“더러운 상상 하지 마라. 그 염병할 갑옷 얘기니까.”

특유의 광택을 지우기 위해 진흙으로 치덕치덕 문댄 갑옷을 가리키자, 정호군이 눈살을 찌푸렸다.

“그럴 수는 없소. 이건 황제 폐하께서 금의위 모두에게 직접 하사하신 거요.”

“싫다?”

“그렇소. 제아무리 상산후의 명령이라 해도 이 갑옷에는 황실의 권위와 명예가 담겨 있소.”

“그래서, 그 권위와 명예를 지키다가 뒈져도 좋다?”

“그건…….”

“그래, 뭐 그러면 입고 다녀. 나중에 뒤처졌을 때 버리고 가면 그만이니까.”

짧은 침묵이 흐른 뒤, 정호군이 대답했다.

“생각해보니, 폐하께서 상산후의 명을 가장 우선시하라고 하셨던 것 같구려.”

“변명치고는 좀 추한데.”

“젠장.”

“벗겠다는 뜻으로 받아들이지. 괜히 꾸물대지 말고 지금 당장 아랫놈들한테 명령…….”

문득 말꼬리를 흐린 나는, 어느새 내려앉은 흐릿한 어둠 속을 노려보았다.

그리고 이내 한숨을 내쉬며 막 투구를 벗은 정호군에게 말했다.

“아직 벗지 마라.”

그 순간.

드드득.

지금까지의 추격대와는 비교도 안 되는 진동이, 저 너머에서 들끓기 시작했다.
```

## Final English reading copy

```markdown
# Chapter 1069

When someone suddenly changes, the people around them can’t help feeling uneasy.

Especially when it happens in the middle of a chase.

“Hh…”

At Great Sir’s sudden groan, the silence shattered—and the air around us froze.

It hadn’t even been fifteen minutes since we’d shaken off the third group of pursuers.

Our allies had been moving quickly and quietly, keeping low among the shallow hills and reeds. Now they reflexively tightened their grips on their weapons. Jeok Cheongang was among them.

“What is it?”

At Jeok Cheongang’s low, grave question, everyone—including me—turned toward Great Sir.

His face had gone rigid without anyone noticing. His pupils, usually a little unfocused, had suddenly dilated, as if reflecting his state of mind. A bead of cold sweat rolled down his forehead.

“I have a bad feeling. A really bad one.”

If we’d been in Gansu, I might’ve just wondered what crazy thing he was going to say this time and let it pass.

But no matter how unhinged he was, Great Sir was an undisputed Supreme Peak master. We were in enemy territory, with threats lurking everywhere. And though it might’ve been a coincidence, he was the first to notice the enemy using birds to spy on us. His words weren’t something we could simply brush aside.

A person’s innate sixth sense had nothing to do with how advanced their martial arts were.

“A bad feeling?”

Jeok Cheongang asked gravely. Great Sir nodded.

“That’s right.”

“Explain in more detail. And be polite if you don’t want to get beaten to death.”

“Understood.”

Jeok Cheongang chuckled at Great Sir’s answer, then turned to me.

“Would it be all right if this old man taught that lunatic a lesson?”

“Would it?”

“Probably not.”

“Then why ask?”

“I thought I’d check. Anyway, so it really isn’t all right?”

“You can read his palm, but you can’t lay a hand on him.”

“Damn it. The code of the martial world has fallen to the ground.”

Jeok Cheongang sighed up at the sky, then looked at Great Sir with a half-resigned expression.

“Fine. I understand. Now keep talking. What exactly does this feeling feel like?”

“How should I put it? Like an invisible hand is squeezing my insides.”

“And?”

“My stomach keeps churning, and I’m breaking out in a cold sweat.”

“Any idea what’s causing it?”

“I don’t know. Somehow, it feels familiar…”

“Ulp!”

Before he could finish, Great Sir groaned again.

His face went pale. He moved before anyone had a chance to stop him.

*Whoosh!*

His figure shot away so quickly it left a blur behind. Great Sir vanished among the dense reeds in an instant. Jeok Cheongang, the other Supreme Peak masters, and I hurried after him.

Or, more precisely, we were about to.

Until a certain sound rang out clearly from the reeds.

*Flap, flap-flap-flap!*

“…?”

What the hell was that?

Just as we all began to dread the answer, Great Sir’s voice confirmed our suspicions.

“Ahhh, that’s better…”

“……!”

“……!”

A deathly silence settled over the area. Jeok Cheongang stared at me in disbelief, then finally parted his tightly shut lips.

“Are you sure it’s not all right?”

“……”

“I won’t kill him. I’ll just break one thing. His arm or something, not his leg.”

At Jeok Cheongang’s earnest plea, Bow Saint muttered through her pinched nose.

“An arm might be all right…”

I’ll admit, I was tempted.

But I resisted the urge through superhuman self-control and shook my head.

*Sixth sense, my ass.*

If he could just refrain from acting like a complete idiot for once, that’d be a miracle. What had I expected from someone who didn’t even know his own name?

*Still, he more than pulls his weight.*

I swallowed a sigh. Great Sir—who’d just finished taking care of business with a racket that was anything but discreet—emerged looking completely at ease.

“Whew. I feel great.”

“……A minute ago, you said you felt really bad.”

“Me? I don’t believe I did. You must’ve misunderstood.”

“You’re pissing me off.”

“Hm? What was that?”

“Nothing. Just talking to myself.”

“Hm. That’s a bad habit. It doesn’t bother me, but you should break it soon. If you talk to yourself too often, people might think you’ve lost your mind.”

“……”

I must’ve lost my grip on reason for a moment.

My vision blurred, and when it cleared, a fierce-looking face was blocking my view.

“Whoa! Take it easy, take it easy!”

“Let go! Let go! That ugly face of yours is already bad enough. Want me to make it even worse?”

Ma Junggeol—the chief of the mounted bandits who’d somehow ended up following us this far, and now the head of a horse-caravan business—looked at me sadly.

“……That was a bit harsh.”

“Ah, sorry. I got carried away.”

My apology eased some of the sadness from Ma Junggeol’s face.

“Calm down. You know Great Sir didn’t mean anything by it.”

Of course I knew.

Maybe that was why his innocence made me even angrier.

He’d been a complete nuisance at a critical moment, and all that fuss had been over a satisfying bowel movement.

Even Shakyamuni himself would have shouted, “Amitabha, fuck this! Guanyin, drop dead!” and cracked Great Sir’s skull with a wooden fish.

*But I can’t exactly leave him behind somewhere.*

If pure evil existed, maybe Great Sir was it.

I sighed deeply and raised a hand for everyone to get moving.

Every moment mattered, and we’d already wasted nearly fifteen minutes for nothing. We needed to pick up the pace.

*At this rate, it could take us several more days just to reach our destination.*

The first attack had come before we’d even made it all the way down from the mountain range. By now, the enemy had caught up with us three times.

Each time, the Supreme Peak masters, including me, had led the charge and wiped out the pursuers. But the important thing was how quickly and relentlessly the enemy caught up to us.

*They have eyes to keep watch on us—and monsters that can chase us without resting for even a moment.*

Monsters that had forgotten death, pain, and fatigue.

That was what made the undead truly terrifying.

They’d been reborn from death with their emotions stripped away. They hadn’t died, yet they were already as good as dead. They’d forgotten sensation, and for the same reason, they couldn’t even feel fatigue.

*We haven’t been down from the mountains for long. But if they keep slowing us down like this…*

The words *surrounded* and *wiped out* rose in my mind. I quietly swallowed them.

Anyone who thought about defeat from the start was bound to lose in the end.

Thousands, or tens of thousands.

Even if a hundred thousand undead came to close their hands around our throats, I had to lead everyone through this dense net and keep moving.

Toward our destination far to the east, where our allies in Qinghai—including the Kunlun Sect—should be waiting.

As if she’d sensed what I was thinking, Ju Hwaran broke away from the people moving out and came over.

“If we can make it as far as Qinghai Lake, they won’t be able to pursue us so easily.”

Song Ilseom, who—as always—stayed close beside Ju Hwaran like a shadow, spoke up unexpectedly.

“You’re not wrong. But that’s only if all of Qinghai’s forces have gathered there, and those monsters aren’t pursuing us with everything they have.”

“……Captain Song.”

“No, Young Lady Ju. He’s right.”

In a way, it was a discouraging thing to say, but Song Ilseom’s judgment was cold and accurate.

You could keep hope in a corner of your heart, but your mind had to question everything.

Build for the worst, then strive for the best.

That was the most important thing when it came to survival and victory.

“How far is it to Qinghai Lake?”

“If we push ourselves to the limit, two days. I’ve gone over the map in detail, and there’s no route that would get us there any faster.”

The old map in Ju Hwaran’s hands was anything but ordinary.

She’d inherited it from her grandfather, who’d even been called the Escort King. It contained detailed notes on secret roads hidden throughout the land and the features of each region.

But this was Qinghai Province.

Especially in the northwest, with its endless open plains and basins, only sparse vegetation and reed beds grew. The terrain was full of obstacles for us.

*But perfect for them.*

Ju Hwaran had said that even if we pushed ourselves to the limit, it would take two days to reach Qinghai Lake.

If the pursuers kept catching up, that could mean three days, four days, or even more than a fortnight.

*They’re pursuing us harder than I expected. Stealth or speed—we’ll have to give up one of them.*

That left me with only one choice.

And the first thing I needed to do was obvious.

“Take it off.”

I abruptly picked up the pace and tossed out the order.

Jeong Hogun, who was hunched low at the rear of the Embroidered Uniform Guard, reflexively asked, “What?”

“Say that again.”

“……What did you say?”

“I said take it off right now.”

At the sight of Jeong Hogun’s eyes practically shaking, I added an explanation to head off any misunderstanding.

“Don’t get any dirty ideas. I’m talking about that damn armor.”

I pointed at the armor, which had been thoroughly smeared with mud to hide its distinctive shine. Jeong Hogun frowned.

“I can’t. His Majesty personally bestowed this on every member of the Embroidered Uniform Guard.”

“You don’t want to?”

“That’s right. No matter what orders the Marquis of Shangshan gives, this armor carries the authority and honor of the imperial family.”

“So you’d rather die protecting that authority and honor?”

“That’s…”

“Fine. Keep wearing it, then. When you fall behind, we can just leave you behind.”

After a brief silence, Jeong Hogun answered.

“On second thought, I believe His Majesty did tell us to put the Marquis of Shangshan’s orders first.”

“That’s a pretty ugly excuse.”

“Damn it.”

“I’ll take that as agreement. Don’t waste time—give the order to your men right now…”

I trailed off and stared into the hazy darkness that had settled around us.

Then I sighed and spoke to Jeong Hogun, who’d just taken off his helmet.

“Don’t take it off yet.”

At that moment—

*Rumble.*

A tremor unlike anything the previous pursuers had caused began to churn in the distance.
```
