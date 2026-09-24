<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1002.txt",
      "sha256": "6d9785bfbbe5e0bb686a88dbc361c4bc6fe946f14838efd55642a45cdd88b234",
      "bytes": 13536
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8e9b8f4541121309a482edba248b84acb299f411950ab91153f3b0d35f6b255c",
      "bytes": 1490
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "de9067f7d03eeb676863896370f0bfc283ae9ad4035a92d1e6d43c0baf36248f",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "04d36ecffec9edda2fc45e4c1372ca1c236b8b38284c18a3720b5acdd21083be",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "06b82e3d964e6e6755782467b6e5b9a8cfedbad073030e387ebb890e9fbe26f7",
      "bytes": 1408
    },
    {
      "path": "characters/Namho.md",
      "sha256": "a96d153ff5d91a94e16d48f00b4c909804b2f19a4730cd0259c44a235a2c0aa5",
      "bytes": 1091
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "204fed78c14cfd25c6f9cb14feff0eaf601efde620c2645175f3140c0796542e",
      "bytes": 1446
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "c3734173469b049e381e6c9fef44e3168e7d912668e705c2273f707980a2383c",
      "bytes": 2457
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "afeffb3ea305c8845f5db1934d4fead68351bfc1c1b8648c3085723dff7f2d83",
      "bytes": 274761
    }
  ],
  "estimated_tokens": 11721
}
-->

# Durable State Update — Chapter 1002

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
1 and safe_through 1002. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1002. Profile updates may replace only one
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
  "chapter": 1002,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1002,
    "continuity_sources": [1002],
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
    "Taekyung’s group and the Zhongnan party, now numbering roughly a thousand, are traveling toward Gansu and have reached a village near the Shaanxi–Gansu border.",
    "The villagers feared the approaching crowd because they thought it was a gang of mounted bandits; the bandits’ identity and whereabouts remain unknown.",
    "Taekyung and the Zhongnan Sect have made an outward reconciliation for mutual benefit, though underlying resentment remains.",
    "Dark Heaven’s advancing army has an unknown destination; its Moving Formations may enable surprise attacks, but their number and locations remain unknown.",
    "The Demon-Sealing Formation may be able to neutralize Moving Formations; Zhuge Feng’s clan used it to contain the rift at Dongting Lake.",
    "Sama Pyo’s Black Dragon Demon Gate in Gansu may be threatened by Dark Heaven’s advance through Xinjiang.",
    "The Nanman Beast Palace is defending Sichuan alongside the still-intact Qingcheng and Emei Sects."
  ],
  "continuity_sources": [
    1000,
    1001
  ],
  "open_questions": [
    "Where will Dark Heaven’s advancing army strike, and what is its objective?",
    "What caused the System malfunction, and is it connected to the Lord of Heaven?",
    "Why did Sama Pyo’s father order him to return immediately?",
    "Who are the mounted bandits feared by the villagers, and where are they?"
  ],
  "safe_through": 1001,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 월화     | **Wolhwa**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 본문      | **our sect / this sect**                                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 은자 | **silver nyang** | Silver currency unit. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 하오문도 | **Lower District Sect member** | Member of the Lower District Sect. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1001
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1001
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1001
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 996
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 973
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest; had fled from the steppe and commanded nearly four hundred subordinates before his death
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 992
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear; has negotiated a mutually beneficial alliance with Jin Wikyung and the Jin Family

## Korean source

```text
＃1002화



“누구긴 누굽니까요. 그 흉악하기 짝이 없는 마적단 놈들이지.”

사내의 대답이 들려온 순간, 나와 적천강은 반사적으로 서로를 바라볼 수밖에 없었다.

그도 그럴 것이, 이 시점에 등장하기에는 너무 뜬금없는 존재였으니까.

마적단(馬賊團).

뜻 그대로 말 탄 도적놈들을 의미한다.

장강의 지류마다 장강수로맹의 수채가 있고, 길이 놓인 산기슭마다 녹림맹의 산채가 존재하는 것처럼 너른 고원(高原)과 평야가 많은 지역에는 바로 마적단이 있었다.

‘풍양이 두목으로 있던 적풍단(赤風團)도 그중 하나였고.’

광활하기 그지없는 북방의 대초원은 비단 유목민들만의 터전이 아니었다.

장성(長城)을 넘어 흘러들어 온 인간 군상들의 피신처인 동시에, 유일한 안식처였다.

그리고 각자의 신세로 돌아갈 수 없는 도망자 신세가 된 그들에게는 두 가지 선택지가 주어졌다.

잡아먹거나, 혹은 잡아먹히거나.

당연하게도 그들 중 대다수는 전자를 택했다.

먹잇감이 되느니 포식자로 살아남는 것이 백 배, 천 배는 나을 테니까.

아마도 풍양 역시 비슷한 전철을 밟았을 것이다.

도대체 어떠한 경로로 잠력단을 손에 넣고 절기라 불릴 법한 마공(魔功)을 익혔는지는 모르겠으나, 놈은 포식자로서 상당한 두각을 드러냈다.

무려 수백이나 되는 수하를 이끌고 장성을 넘는 간 큰 행보를 보일 정도였으니.

하지만 결국 그런 풍양과 적풍단조차 항산검문에서 뼈를 묻었다.

제아무리 규모를 갖추었다 해도 결국은 도적 집단.

중원에 비하면 변방 촌구석 취급받는 산서성이라 해도, 일개 마적단에게 주어진 한계는 명백했다.

‘그런데, 고작 마적단 따위가 이 근방을 어슬렁거려? 그것도 감숙과 섬서의 경계선에?’

아무리 정신 나간 놈들이어도 누울 자리를 보고 발을 뻗는 법.

감숙에는 공동파와 흑룡마문이, 섬서에는 화산파와 종남파가 떡하니 버티고 있는 마당에 마적단이 깝죽거린다는 건 상식에서 벗어나는 일이다.

‘뭔가 있다. 분명히.’

적천강 역시 나와 같은 생각을 떠올렸음이 틀림없다.

미간을 좁힌 채 생각에 잠겨 있는 그를 대신해, 나는 사내를 향해 입을 열었다.

“그 얘기, 더 자세히 들어 볼 수 있겠습니까?”

“마적단 놈들에 관해서 말입니까요?”

“예. 정확한 위치나 규모, 만약 잘 모르신다면 단순한 소문도 괜찮습니다.”

심상치 않은 분위기를 읽은 듯, 말없이 눈만 껌뻑거리던 사내가 문득 입을 열었다.

“얼마 주시렵니까?”

“예?”

“은자 넉 냥. 그 정도면 충분할 듯한데.”

“……?”

아니, 이 아저씨 갑자기 왜 이래?

황당해진 내가 뭐라 대답하기도 전에, 사내가 멋쩍은 얼굴로 뺨을 긁적였다.

아니, 정확히는 긁적이는 척하며 자신의 뺨에 글자를 그렸다.

이곳에 없는, 그러나 결코 잊을 수 없는 누군가의 이름을.

‘월……화. 잠깐. 월화(月華)?’

비로소 그 의미를 깨닫고 멍하니 입을 벌린 나를 향해, 사내. 아니 하오문도가 눈을 찡긋하며 입을 열었다.

“아직 갈 길이 바쁘신 듯한데, 가면서 말씀 나누시는 건 어떻습니까요?”

“……!”

잠시 잊고 있었다.

하오문의 눈과 귀는 어디에나 있다는 것을.

아무 일도 없었다는 듯, 능청스러운 사내의 모습에 낮게 실소를 흘린 내가 입을 열었다.

“무진아.”

말이 떨어지기 무섭게 후다닥 달려온 혁무진이 대답했다.

“옙. 조장님. 무슨 일로 부르셨습니까.”

“이분에게 은자 넉 냥, 아니 열 냥 드려라. 말 한 필도 내어드리고.”

시원시원한 한 마디와 함께 돌아서려던 그때, 혁무진의 중얼거림이 귓전에 닿았다.

“아니, 미리 전낭이라도 던져 주고 저런 소릴 하던지. 그리고 저 양반한테 말 주면 난 뭐 타라고.”

“……큼.”

“저 봐, 들었으면서 괜히 모르는 척하는 거. 진짜 내가 드러워서 때려치우던가 해야…….”

“크흐흐흠!”

“어, 왜 그러십니까. 혹시 따로 더 지시하실 거라도?”

언제 그랬냐는 듯 눈을 똘망똘망하게 뜬 혁무진을 짜게 식은 눈빛으로 응시하던 나는, 지금 막 인벤토리에서 꺼낸 전낭을 던져 주었다.

“어이쿠, 뭘 또 이런 걸다. 그냥 돈 쓰는 족족 제 월봉에서 까고 모자란 건 집안에 손 벌려도 되는데. 아니면 구걸을 하거나.”

“내가…… 미안하다.”

“조장님께서 미안하실 게 뭐가 있습니까. 혁가 포목점 기둥뿌리가 흔들려도 제 사정이죠. 안 그래요?”

“알겠으니까 그만 좀 해. 여하튼 그걸로 됐지?”

“말은요?”

“……!”

“말까지 내어 주면 저는 뭐, 돌아가신 조상님이 태워 줍니까?”

할 말이 없어진 나는, 대답 대신 슬그머니 고개를 돌려 가까이에 있는 종남파 제자를 응시했다.

정확히는 그가 타고 있는 준마를.



* * *



마치 폭풍과도 같은 연쇄 삥 뜯기가 끝난 후, 모두가 만족할 만한 결과를 얻은 우리는 다시 감숙성으로 발걸음을 향했다.

물론 그 과정에서 종남파 제자 한 명은 안락한 말안장 위에서 내려 튼튼한 두 다리로 이동하게 됐지만, 내 알 바는 아니었다.

내게 있어 중요한 건, 하오문도가 가진 정보였으니까.

“모두 당분간은 이 근방에 머무르는 것이 좋겠소. 아니, 아예 얼씬도 말고 섬서 쪽으로 가시구려. 흉악한 마적 놈들이 언제 쳐들어올지 모르니.”

하오문도는 남아 있는 양민들에게 몇 번이고 신신당부하며 말에 올랐고, 풍운검군은 그런 그들을 위해 십여 명의 제자를 남겨주었다.

혹시 모를 위험한 상황을 대비하여, 양민들을 섬서로 안전히 이끌어 줄 목적이었다.

그리고 이동을 시작하자마자 하오문도가 꺼낸 첫마디는, 모두의 뒤통수를 얼얼하게 만들기에 충분했다.

“솔직히 말씀드리자면, 마적단은 없습니다.”

“……?”

“……?”

잠깐의 침묵이 흐른 뒤, 혁무진이 허리춤에 건 검파를 만지작거리며 말했다.

“은자 열 냥. 좋게 말할 때 당장 뱉어내쇼.”

“갈! 입 다물지 못할까. 같은 아군을 겁박하다니. 네놈이 사마외도(邪魔外道)의 무리와 무엇이 다르단 말이냐!”

준엄하게 혁무진을 꾸짖은 적천강이, 순간 겁을 집어먹은 하오문도를 향해 보기 드문 친절한 어투로 입을 열었다.

“저놈은 괘념치 말고 계속 말해 보게. 그깟 은자 열 냥, 저승길 가는 노잣돈이라고 생각하면 그만이니.”

“…….”

개무섭네. 진짜.

오가는 말만 들어보면 무림맹이 아니라 마림맹이라고 해도 되겠다.

공력이라고는 한 줌도 느껴지지 않는 하오문도는 압박감으로 창백해진 얼굴이 되어 더듬더듬 입을 열었다.

“정확히는 있었는데, 없어졌습니다.”

“오호. 있었는데 없어졌다라.”

적천강이 탄성과 함께 사람 좋은 미소를 지었다.

“현재 상황에 대입해 보니 이해가 쏙 되는군. 자네도 곧 이 세상에서 없어질 테니.”

“히이익!”

“은자는 아홉 냥만 받겠소. 한 냥은 떠날 때 갖고 가시든지.”

“으헉!”

“그만, 다들 그만!”

결국 내가 나선 직후에야 숯불 위 가마솥처럼 들끓던 민심은 겨우 진정되었고, 불쌍한 하오문도는 허겁지겁 자세한 이야기를 풀어놓았다.

“그러니까, 녕하성(寧夏省)의 마적단이 심상치 않은 움직임을 보이기 시작한 건 사실이다. 그겁니까?”

“예, 예에.”

“그럼 마을에 모여 있던 그 많은 사람은…….”

“일부러 소문을 과장해서 흘린 겁니다. 당장 머지않아 서쪽 일대에서 난리가 벌어질 테니, 최대한 양민들의 피해를 줄이려고요.”

“암천은 멀고, 마적단은 가까우니까?”

“바로 그겁니다. 녕하성은 제법 가까우니 사막 너머의 암천보다는 더욱 위협적이죠. 더군다나 저처럼 무공을 익히지 않은 몸이라면 오죽하겠습니까.”

그때, 말머리를 나란히 한 채 이동하고 있던 풍운검군이 문득 눈살을 찌푸리며 끼어들었다.

“잠깐. 녕하가 한때 마적단의 무법천지였던 것은 사실이지만, 놈들이라면 이미 오래전에 토벌되었을 텐데?”

이건 또 무슨 소린가.

뜻밖의 정보에 모두의 시선이 쏠리자, 한차례 헛기침을 내뱉은 풍운검군이 말을 이었다.

“처음부터 차근차근 말하자면, 과거의 녕하는 우리에게 있어 오랜 골칫거리였네. 크고 작은 수백여 개의 마적단이 난립하는 곳이라, 관군조차 딱히 통제할 수 없는 지경이었지.”

“관군조차 나서지 않는다면, 녕하성에 살고 있던 양민들은요?”

“썩은 개울에 물고기가 남아 있겠나? 양민들 대부분이 떠나거나, 그들 중 일부가 되었지.”

“초원과 다를 게 없군요.”

“사실상 또 하나의 초원이라고 보는 게 맞을 걸세. 녕하는 감숙과 섬서의 사이에 위치해 있지만, 북쪽에서 흘러들어온 유목민과 중원에서 배척당한 소수민족들의 마지막 행선지이기도 하니까. 물론 그중에서도 화룡점정(畵龍點睛)은…….”

“도망자들. 씻을 수 없는 죄를 짓고 도망쳐 온.”

불쑥 끼어든 남호가 자연스럽게 말을 이어받았다.

“그렇기에 녕하는 지금껏 중원의 무림 문파에게 있어 계륵(鷄肋)과도 같은 존재였지. 땅은 좁고 황량한데 남아 있는 사람들이라고는 온갖 흉악한 놈들뿐이었으니. 설령 피해를 감수하고 영역을 확보하더라도 그 이후가 문제였을 터. 맞소?”

작게 입맛을 다신 풍운검군이 고개를 끄덕였다.

“인정하긴 싫지만…… 부정할 수 없구려. 정마대전 이전에는 서로의 눈치를 볼 수밖에 없었고, 이후에는 극심한 피해를 입어 회복에만 전념해야 했으니.”

대충 가닥이 잡힌다.

구파일방과 오대세가.

그들은 정파 무림을 대표하는 의기의 상징이지만, 동전의 뒷면을 들여다보면 아득한 세월 동안 힘과 이권을 독점해 온 지배층이기도 했으니까.

당장 근래의 혈사를 일으킨 모용세가가 다른 마음을 품기 시작한 것도, 정마대전 이전의 치열한 힘겨루기 속에서 이민족이라 배척받은 탓도 있었다.

‘물론 어차피 배신자의 변명에 불과하지만.’

내심 중얼거린 나는, 부끄러운 민낯을 인정하며 얼굴이 붉어진 풍운검군을 향해 가장 중요한 것을 물었다.

“하지만 앞서 녕하성의 마적단은 이미 오래전에 토벌되었다고 하셨는데. 그 일은 어느 문파가 주도한 겁니까?”

그리고 다음 순간 들려온 풍운검군의 대답은, 실로 뜻밖이었다.

“그 누구도 나서지 않았네.”

“예?”

“아니, 못 했지. 그때의 녕하는 이미 무법천지였고, 본문은 물론 인근의 모든 무림 방파는 이제 겨우 정마대전의 여파를 추스른 상태였어.”

“그렇다면 도대체 어떻게.”

“자세한 사정은 모르겠지만, 현재 녕하성이 안정될 수 있었던 이유는 단 한 사람의 존재 때문이었다고 들었네. 어느덧 십 년 가까이 된 일이지.”

“……!”

구파일방 같은 거대 방파가 아니라, 개인이었다고?

생각지도 못한 대답에 모두가 눈을 크게 떴다.

당연하다.

지금까지의 사정만 들어 보면 과거의 녕하성은 그야말로 무법천지.

이쯤 되면 웨스턴 무림이라고 칭해도 부족할 지경인데, 수백여 개나 되는 마적단을 토벌했다는 건…….

“고수로군. 최소 초절정의 경지에 도달한.”

말없이 이야기를 듣고만 있던 적천강이 짤막한 한 마디를 툭 내뱉었고, 이는 곧 내 생각과도 일치했다.

‘지금으로부터 십여 년 전, 수많은 마적들을 쓸어버리고 녕하성을 평정한 의문의 초절정 고수라…….’

수상한 것은 그뿐만이 아니다.

문제는 강산이 한 차례 뒤바뀔 시간 동안 잠잠하던 그 녕하성의 마적단이, 심상치 않은 움직임을 보이기 시작했다는 것에 있었다.

‘도대체 뭐지?’

눈살을 찌푸린 채 묵묵히 말을 몰아 나아가던 그때, 누군가의 입술 사이로 침묵을 깨트리는 한 마디가 울려 퍼졌다.

“감숙. 감숙입니다!”

태원진가에서부터 쉴 새 없이 말을 몰아 내달린 지 어언 나흘.

험준한 산맥 뒤에 가려진 그곳에는, 실로 광활한 고원이 펼쳐져 있었다.

감숙.

지금 눈앞에 보이는 저 대지가 죽음의 땅이 될지, 또 다른 전장으로 향하는 교두보가 될지는 아무도 알 수 없었다.

그 누구도.
```

## Final English reading copy

```markdown
# Chapter 1002

“Who else would it be? Those vicious mounted bandits.”

The moment I heard the man’s answer, Jeok Cheongang and I reflexively looked at each other.

And for good reason. They were far too unexpected to show up at a time like this.

Mounted bandits.

Just what the name said: bandits on horseback.

Just as the Yangtze River Channel League had strongholds along every branch of the Yangtze, and the Green Forest Alliance had mountain strongholds on every mountainside with a road, mounted bandits could be found in regions with broad plateaus and plains.

*Pung Yang’s Red Wind Band had been one of them.*

The vast northern Great Steppe wasn’t home to nomads alone.

It was a refuge for all kinds of people who’d crossed the Great Wall—and, at the same time, their only place of rest.

And for those who could never return to the lives they’d left behind, there were two choices.

Eat or be eaten.

Naturally, most of them chose the former.

It was a hundred, a thousand times better to survive as a predator than to become prey.

Pung Yang had probably followed a similar path.

I had no idea how he’d come into possession of a Temporary Strength Pill or learned demonic martial arts worthy of being called a secret technique, but he’d proven himself a formidable predator.

He’d even had the nerve to lead hundreds of subordinates across the Great Wall.

But in the end, Pung Yang and the Red Wind Band had both met their end at the Mount Heng Sword Sect.

No matter how large they grew, they were still just a band of bandits.

Even in Shanxi Province, dismissed as a backwater compared with the Central Plains, there were clear limits to what a mere band of mounted bandits could do.

*And now a bunch of mounted bandits are hanging around here? Right on the border between Gansu and Shaanxi?*

Even the craziest bastards knew to check whether they had somewhere to lie down before stretching out their legs.

With the Kongtong Sect and the Black Dragon Demon Gate standing firm in Gansu, and Huashan and the Zhongnan Sect in Shaanxi, it made no sense for mounted bandits to swagger around here.

*Something’s going on. It has to be.*

Jeok Cheongang must have been thinking the same thing.

He was frowning in thought, so I spoke to the man for him.

“Could you tell us more about them?”

“You mean the mounted bandits?”

“Yes. Their exact location and numbers, if you know them. If not, even a rumor would be useful.”

The man had been blinking at us in silence, apparently picking up on the serious mood. Then he suddenly spoke.

“How much will you pay?”

“What?”

“Four silver nyang. That should be enough.”

“……?”

What was this guy’s deal all of a sudden?

Before I could come up with a reply, the man awkwardly scratched his cheek.

Or rather, he pretended to scratch it as he traced out letters on his cheek.

The name of someone who wasn’t here—but whom I could never forget.

*Wol…hwa. Wait. Wolhwa?*

I finally understood. My mouth fell open as the man—or rather, the Lower District Sect member—winked at me.

“You seem to be in a hurry to get where you’re going. Why don’t we talk on the way?”

“……!”

I’d almost forgotten.

The Lower District Sect’s eyes and ears were everywhere.

I let out a quiet laugh at the man’s shameless act, as though nothing had happened, then called out.

“Mujin.”

Hyuk Mujin came hurrying over and answered at once.

“Yes, Captain. What do you need?”

“Give this gentleman four silver nyang—no, ten. And provide him with a horse.”

I was turning away after delivering the order when Hyuk Mujin’s muttering reached my ears.

“You could at least toss him the money before saying that. And if you give him a horse, what am I supposed to ride?”

“……Ahem.”

“See? You heard me, but you’re pretending you didn’t. I’m so fed up, I ought to just quit—”

“Ahem!”

“Uh, what is it? Did you have another order for me?”

Hyuk Mujin’s eyes went wide and bright as if he’d never said a thing. I gave him a cold look and tossed him the money pouch I’d just taken out of my Inventory.

“Oh my, you really shouldn’t have. You can just deduct whatever you spend from my monthly pay, and if it’s not enough, I can ask my family for more. Or beg for it.”

“I’m… sorry.”

“What do you have to apologize for, Captain? Even if the pillars of the Hyuk Family Textile Shop start shaking, that’s my problem. Right?”

“I get it. Just stop already. That should cover it, right?”

“What about the horse?”

“……!”

“If you give away the horse too, what am I supposed to ride? My ancestors are dead—they’re not going to give me a lift.”

Out of answers, I quietly turned my head and looked at the nearby Zhongnan Sect Disciple.

More specifically, at the fine horse he was riding.

* * *

After the whirlwind shakedown was over, we got an outcome everyone could be satisfied with and set off toward Gansu Province again.

Of course, one Zhongnan Sect Disciple had to climb down from his comfortable saddle and travel on his own two sturdy legs. But that wasn’t my problem.

The only thing that mattered to me was the information the Lower District Sect member had.

“Everyone should stay around here for the time being. No—better yet, don’t come anywhere near. Head toward Shaanxi. Those vicious mounted bandits could attack at any moment.”

The Lower District Sect member repeated his warnings to the villagers who’d stayed behind, then mounted his horse. The Wind-and-Cloud Sword Lord left a dozen or so Disciples behind to help them, just in case danger arose, and lead them safely to Shaanxi.

As soon as we set off, the Lower District Sect member’s first words were enough to leave everyone feeling as if they’d been smacked in the back of the head.

“To be honest, there are no mounted bandits.”

“……?”

“……?”

After a brief silence, Hyuk Mujin fiddled with the sword at his waist and said,

“Ten silver nyang. Spit it back out right now, while I’m still asking nicely.”

“Enough! Hold your tongue! Threatening an ally—how are you any different from those demonic, heterodox villains?”

Jeok Cheongang sternly rebuked Hyuk Mujin, then turned to the Lower District Sect member, who was visibly frightened, and spoke with an unusually kind tone.

“Don’t mind that fool. Go on. Ten silver nyang is a small price to pay for your fare on the road to the afterlife.”

“…….”

God, he’s terrifying.

Just from listening to them, you’d think we were the Demonic Path Alliance, not the Murim Alliance.

The Lower District Sect member, who didn’t seem to have an ounce of internal energy, had gone pale from the pressure. He stammered out his explanation.

“To be precise, there were mounted bandits, but they’ve disappeared.”

“Oh? They were there, and now they’re gone.”

Jeok Cheongang let out an appreciative sound and smiled kindly.

“That makes perfect sense, given the situation. You’ll soon disappear from this world, too.”

“Eek!”

“I’ll take nine silver nyang. Keep one for the trip.”

“Gah!”

“Enough, all of you!”

Only after I stepped in did the people’s anger, which had been boiling like a cauldron over a charcoal fire, finally settle down. The poor Lower District Sect member hurriedly explained the details.

“So what you’re saying is, the mounted bandits in Ningxia Province really have started acting strangely?”

“Y-Yes.”

“Then all those people gathered in the village…”

“I deliberately spread an exaggerated rumor. Trouble is about to break out in the western region, so we wanted to keep the civilians from getting caught up in it as much as possible.”

“Dark Heaven is far away, but the mounted bandits are close?”

“Exactly. Ningxia Province is pretty close, so the mounted bandits there are a greater threat than Dark Heaven beyond the desert. All the more so for someone like me, who hasn’t learned martial arts.”

The Wind-and-Cloud Sword Lord had been riding alongside me. Now he frowned and cut in.

“Wait. Ningxia was once a lawless land ruled by mounted bandits, but weren’t they put down a long time ago?”

What was this now?

Everyone turned toward him at the unexpected information. The Wind-and-Cloud Sword Lord cleared his throat and continued.

“To start from the beginning, Ningxia used to be a longstanding headache for us. Hundreds of mounted-bandit groups, large and small, were spread across the region, to the point that even the government troops couldn’t control them.”

“If even the government troops wouldn’t step in, what happened to the civilians living in Ningxia Province?”

“Would any fish remain in a polluted stream? Most of the civilians either left or became one of them.”

“So it was no different from the steppe.”

“In practice, you could call it another steppe. Ningxia lies between Gansu and Shaanxi, but it was also the final destination for nomads who’d come down from the north and minority peoples who’d been driven out of the Central Plains. And the final touch among them all was…”

“Fugitives. People who came running after committing unforgivable crimes.”

Namho cut in, smoothly picking up where he’d left off.

“That’s why Ningxia had always been a prize the Murim sects of the Central Plains couldn’t quite bring themselves to claim. The land was small and barren, and the people left there were all sorts of vicious bastards. Even if a sect took losses securing the territory, dealing with it afterward would be another problem. Am I right?”

The Wind-and-Cloud Sword Lord clicked his tongue softly and nodded.

“I don’t like admitting it, but I can’t deny it. Before the Great Faction War, we could only watch one another. Afterward, we suffered such heavy losses that we had to focus entirely on recovering.”

I was starting to get the picture.

The Nine Sects and One Gang.

The Five Great Families.

They were symbols of the orthodox faction’s honor, but if you looked at the other side of the coin, they were also an entrenched ruling class that had monopolized power and influence for ages.

Even the Murong Family, which had recently brought about a bloodbath, had started harboring other ambitions partly because it had been treated as a foreign people and excluded during the fierce power struggles before the Great Faction War.

*Though, in the end, that’s nothing but an excuse from a traitor.*

I muttered inwardly, then asked the Wind-and-Cloud Sword Lord, who’d admitted the shameful truth with reddened cheeks, about the most important thing.

“But you said the mounted bandits in Ningxia Province were put down a long time ago. Which sect led that effort?”

The Wind-and-Cloud Sword Lord’s answer was truly unexpected.

“No one stepped forward.”

“What?”

“No, they couldn’t. Ningxia was already lawless, and not only our sect but every martial faction in the surrounding area had only just recovered from the aftermath of the Great Faction War.”

“Then how on earth…”

“I don’t know the details, but I heard that Ningxia Province was able to stabilize because of one person alone. That was nearly ten years ago.”

“……!”

Not a major sect like the Nine Sects and One Gang, but a single individual?

Everyone’s eyes widened at the answer they’d never expected.

Understandable.

From what we’d heard so far, Ningxia Province had once been a lawless land.

It was practically the Wild West of Murim. To have put down hundreds of mounted-bandit groups—

“A master, then. At least someone who’d reached the Supreme Peak realm.”

Jeok Cheongang had been listening in silence. He tossed out the brief remark, which matched my own thoughts exactly.

*A mysterious Supreme Peak master who swept away countless mounted bandits and pacified Ningxia Province ten years ago…*

That wasn’t the only suspicious thing.

The problem was that the mounted bandits in Ningxia Province had started acting strangely after remaining quiet for a whole decade—long enough for the mountains and rivers to change.

*What the hell is going on?*

I was frowning and silently urging my horse onward when a voice broke through the silence.

“Gansu. It’s Gansu!”

Four days had passed since we’d galloped without rest all the way from the Jin Family of Taiyuan.

Beyond the rugged mountain range, a vast plateau spread out before us.

Gansu.

No one could know whether the land before our eyes would become a place of death or a staging ground for another battlefield.

No one.
```
