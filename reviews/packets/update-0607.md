<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0607.txt",
      "sha256": "f42af2d14dfb114ef0921d4c2098ee61696dc4a4e77cf49a9b577ac9540ec5ad",
      "bytes": 12700
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "36ab924d981273949acc29f679701de4cf93f64a95a9e56ffb2814f220ebfe68",
      "bytes": 2371
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "db6adc6ee958a6360a233d06147ec7744fe48660fd0a1bf1270135ba8595d75d",
      "bytes": 187933
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "ee64055e6e2249f55af046dcc6530496adcd53b2556462f856a4c9e95071f3b5",
      "bytes": 711
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "24fc9a712ee5c6b383aca3ad882776622a28dd59aa850c3b0f8217f4df415d52",
      "bytes": 667
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "a3ea16cad3ed286d47f95359f983f33464e233e88fc9e0fd1fcd0a0e1e52984c",
      "bytes": 698
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7c5467a48525c1978e87df3b2268486842d4fa9080eaa9c2457785888ce7b5ed",
      "bytes": 1797
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "683ecb63ddd3d97c9b409804512d411c5665540455f284c0ea53028c7398902c",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fcdb2901fecb3622d78a079ef6b868fd56891017870b6909bb9538fe812a5d8f",
      "bytes": 188415
    }
  ],
  "estimated_tokens": 9945
}
-->

# Durable State Update — Chapter 607

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 607. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 607. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 607,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 607,
    "continuity_sources": [607],
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
    "Cheon Taemin remains unconscious after more than twenty years and has been moved in his hibernation capsule from Ares Guild's Area A to his former mansion.",
    "Magic Johnson has heavily fortified and concealed Taemin's mansion with layered magic, though additional work is still needed.",
    "Magic Johnson suspects another Grand Mage may know who created the Area A secret space and its magic, and plans to consult the other Grand Mages.",
    "Lee Jungryong and Song Cheonwoo tried and failed to awaken Taemin in the past.",
    "Jin Taekyung, Team Leader Choi, Magic Johnson, and the Skeleton King are keeping Taemin's survival and current location secret.",
    "Team Leader Choi is privately spending time with Taemin after their reunion of more than twenty years.",
    "There are only three Grand Mages in the world.",
    "The Texas incident was an attempted terrorist use of an unpurified A-grade Magic Gem, not a Mutated Gate; the B-rank perpetrator exploded and caused no significant casualties.",
    "Worldwide identity checks and Magic Gem inspections have tightened, while terrorist organizations are experimenting with Gates and Magic Gems in Africa and the Middle East.",
    "The Pentagon has requested Jin's advice and assistance, and Magic Johnson, Jin, and Team Leader Choi are preparing to go there.",
    "Jin has been preparing an undisclosed course of action for himself and others, but the terrorist threat has made him hesitate."
  ],
  "continuity_sources": [
    606
  ],
  "open_questions": [
    "What caused Cheon Taemin's unconscious state and how can he be awakened?",
    "Who created the Area A secret space and its unusually advanced magic?",
    "Did another Grand Mage know about or assist with Taemin's confinement?",
    "What debt does Go Se-won intend to repay to Jin Taekyung, and how will the authorities resolve Jin's charges?",
    "What course of action has Jin been preparing, and will the terrorist threat change his decision?"
  ],
  "safe_through": 606,
  "temporary_decisions": [
    "Use maternal grandfather for 외조부 and 외할아버지.",
    "Use Team Leader Choi for 최 팀장.",
    "Use Mutated Gate for 변이 게이트.",
    "Use Pentagon for 펜타곤 and retain Ppoppo as Korean baby-talk for a kiss.",
    "Use Grand Mage for 대마도사."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 사부     | **Master**                                   |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 청해     | **Qinghai**            |
| 도사      | **Daoist**                                                      |
| 방장      | **Abbot**                                                       |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 북한 | **North Korea** | Country referenced in Taekyung's comparison. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 대통령 | **President** | Title for Korea's head of state. |
| 도람프 | **Doramp** | Parodic name for the U.S. president in a forum headline. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 오각 | **Five Pavilions** | Inner Hall organizational grouping. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 펜타곤 | **Pentagon** | Headquarters of the United States Department of Defense and source of intelligence about terrorist experiments. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 605
- **Aliases:** Slayer
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 605
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 558
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 605
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license; his Middle Dantian is partially activated at 10%, slightly improving the efficiency of his martial arts and internal energy.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 605
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃607화



펜타곤(Pentagon).

거대한 오각형의 형상을 한 이 건물은 그야말로 난공불락(難攻不落)에 가까웠다.

한 사람 한 사람이 상위 헌터로 이루어진 천여 명의 경비대. 그리고 건물의 내, 외부를 둘러싸고 있는 아득한 마나의 흐름만으로도 펜타곤의 위상을 알 수 있었다.

「대단하지?」

크게 뜨인 눈으로 주위를 둘러보는 나와 최 팀장의 모습에, 막 인증 절차를 끝마친 매직 존슨이 알만하다는 표정으로 씩 웃었다.

「세계 2차 대전 당시 처음 건설된 이래, 펜타곤이 공격받은 건 단 두 차례뿐이야. 9.11테러. 그리고 대격변. 결과가 어떻게 되었는지는 두 사람 다 알 테고.」

최 팀장이 고개를 끄덕였다.

“마왕 아스모데우스와 몬스터 군단의 대공세에도 끝끝내 무너지지 않았습니다.”

「맞아. 내 인생을 통틀어 두 번째로 치열했던 전투였지. 첫 번째는 말할 것도 없이 ‘승리의 날’이었고, 그때마다 한 사람 덕분에 죽을 고비를 넘겼어.」

미국인이 아니라, 지구인이라면 누구나 아는 사실이다.

이 땅 위에 강림한 악마, 마왕 아스모데우스를 막을 수 있었던 사람은 대격변 당시에도, 그 이후에도 오직 한 사람이 유일했으니까.

「천태민. 미국인들이 스카이(Sky)라고 부르는 네 외조부가 아니었다면 지금의 나도, 이 펜타곤도 없었겠지.」

매직 존슨이 마치 뭔가를 떠올리듯, 흐릿해진 시선으로 최 팀장을 바라보던 그때였다.

「나와 같은 생각이군, 존슨.」

불쑥 들려온 목소리의 주인은 나도, 최 팀장도. 당연하게도 인벤토리 안에 숨어 있는 스켈레톤 킹도 아니었다.

뚜벅. 뚜벅.

거친 구둣발 소리. 주름진 청바지와 셔츠 복장에 온통 헝클어지고 뒤엉킨 흰 머리카락.

얼굴 한쪽이 심하게 일그러진 노년의 백인은 거침없는 걸음으로 다가와 불쑥 양손을 내밀었다.

「두 사람 중 누구한테 먼저 악수를 청해야 할지 모르겠으니, 한꺼번에 하지. 척 헤이글이네. 편하게 척이라고 부르면 되겠군.」

첫인사부터 텍사스 상남자의 기운이 느껴지다 못해 흘러넘친다.

나는 왠지 모르게 익숙한 척 헤이글의 얼굴을 빤히 응시하며 그의 손을 붙잡았다.

“진태경입니다. 그런데 혹시…….”

「바로 그 척 헤이글이냐고? 맞아. 자네만큼 유명하진 않지만 나도 왕년에 몬스터 깨나 썰고 다녔지.」

“오오. 오오오.”

보면서도 설마 했는데, 눈앞의 노인은 일명 엉클 척(Uncle Chuck)이라 불리던 전 세대의 S급 헌터였다.

어릴 때 좋아했던 대격변의 전쟁 영웅을 이렇게 마주하게 될 줄이야. 나는 탄성과 함께 그의 손을 힘차게 위아래로 흔들었다.

“팬입니다. 진짜 팬이에요. 초등학교 때 당신 헌터 카드도 모았었는데.”

「헌터 카드? 그걸 사우스 코리아에서도 팔았나?」

“그건 북한에서도 팔았을걸요. 저도 용돈 받을 때마다 꼬박꼬박 사 모았죠.”

「호. 내게 막대한 개런티를 선물해 준 멍청한 꼬꼬마가 여기 한 명 더 있었군. 물론 그때 들어온 개런티는 다섯 번의 이혼 위자료로 다 썼지만.」

단숨에 내 어린 시절의 추억을 박살 낸 척 헤이글이 흐뭇하게 웃으며 말을 이었다.

「나중에 내 카드 가진 것 있으면 가져와 보게. 원한다면 사인도 해 주지.」

“아, 그건 전부 교환했는데요.”

「왓?」

“열 장 모은 다음에 친구가 가진 천태민 카드랑 교환했어요. 솔직히 엉클 척 카드는 그닥 희귀하진 않아서.”

「…….」

웃음기가 싹 사라진 척 헤이글이 한숨을 내쉬었다.

「빌어먹을. 교환 대상이 다른 사람도 아니라 미스터 스카이라니. 이건 뭐라 할 수도 없겠군.」

“희소성이나 가치가 비교도 안 되죠. 원래 스무 장 달라는 걸 제가 깎고 깎아서…….”

「……알겠어. 알겠으니까 이제 그만해.」

고개를 절레절레 내저은 척 헤이글이 최 팀장과 악수를 하며 말했다.

「외조부를 쏙 빼닮았군. 만나서 반갑네, 최.」

“반갑습니다. 미스터 헤이글.”

「편하게 척이라고 부르라니까. 머리에 똥만 가득 차 있는 다른 얼간이들이라면 모를까. 자네나 자네 옆의 변절자는 충분히 그럴 만한 자격이 있어.」

카드 좀 팔았다고 바로 변절자 취급하는 것 보소. 내가 내심 중얼거리던 그때, 최 팀장이 침착한 어조로 대답했다.

“이해해 주십시오, 미스터 헤이글. 펜타곤의 책임자이자 미합중국의 국방장관을 그렇게 부르기에는 제 마음이 편치 않습니다.”

「흠. 그런가? 생각해 보니 자네도 사람들의 눈이 신경 쓰이긴 하겠군. 아무래도 거대 길드를 두 개나 맡게 되었으니 말이야.」

두 사람의 대화를 듣던 내가 눈을 깜빡였다.

“펜타곤의 책임자? 국방장관?”

「음? 몰랐나?」

“몰랐죠. 당연히.”

「그래? 다른 사람들은 다 알던데. 난 최소한 존슨이 알려 줬다고 생각했지.」

국방장관의 시선에 차세대 국밥부장관 당선이 유력한 대마도사가 턱을 긁적였다.

「나도 당연히 아는 줄 알았지. 진. 정말 몰라?」

이쯤 되니 내가 멍청이가 된 기분이다. 나는 떨떠름한 목소리로 대꾸했다.

“진짜 몰랐는데요. 혹시 며칠 전에 부임하셨어요? 아하. 내가 그래서 몰랐었구나?”

척 헤이글의 짧고 굵은 대답이 돌아왔다.

「올해로 8년째일세.」

“……아.”

「뭐, 굳이 알아야 할 필요까지는 없지. 이제부터 할 이야기에 비하면 딱히 중요한 것도 아니고. 자, 이제 다들 따라오게.」

자연스럽게 정복 앞주머니에서 시가를 꺼내어 문 척 헤이글이 앞장섰고, 우리는 그의 뒤를 따라 걸음을 옮겼다.

척 헤이글이 시가를 뻑뻑 피워 댈 때마다 뿜어져 나온 매캐한 연기가 천장에 닿자, 경고음과 함께 붉은빛이 깜빡거린다.

위잉! 위이잉!

- 화재 위험! 화재 위험!

쾅!

일말의 망설임도 없이 경고등을 박살 내 버린 척 헤이글이 중얼거렸다.

「퍽킹 사이렌.」

상남자와 좀생이를 넘어 미친놈이 따로 없다. 인벤토리에 숨어 검색 보안대를 무사 통과한 스켈레톤 킹이 속삭였다.

- 인간 맞나? 몬스터가 아니라?

나도 상당히 의구심이 들긴 하는데, 어릴 적 수집했던 헌터 카드에 적혀 있던 설명과 정확히 일치한다.

텍사스 출신에 카우보이가 꿈이었고, 실제로 미노타우르스를 주먹으로 길들여 타고 다녔다는 믿지 못할 얘기와 기타 등등.

뚜벅. 뚜벅.

거침없이 나아가는 척 헤이글의 앞을 막아서는 간 큰 인물은 아무도 없었다.

펜타곤 소속으로 보이는 연구원 및 헌터, 직원들은 재앙을 마주한 것처럼 좌우로 갈라졌고, 지팡이 대신 시가를 문 모세는 굴뚝처럼 연기를 뿜어내며 그 사이를 가로질렀다.

물론 중간중간 트래쉬 토크를 하는 것도 잊지 않았다.

「이 빌어먹을 복도는 도대체 언제 넓어지는 거야? 볼 때마다 박살을 내 버리고 싶군.」

「헤이, 스미스. 좋게 말할 때 그 전자 담배 치워. 한 번만 더 내 앞에서 개 같은 스트로베리 향을 풍겼다가는 순직자 명단에 올려 주지. 대신 시가는 괜찮아.」

「고든. 3구역에 경고등이 박살 났으니 가서 복구해. 누가 깨트렸냐고? 잘 들어. 네 퍽킹 직속 상관이다.」

마치 성난 황소처럼 날뛰는 척 헤이글을 막을 수 있는 사람은 아무도 없었다.

5분 남짓한 이동 시간 동안 불쌍한 스미스는 전자 담배 액상을 강제로 교체당했고, 죄 없는 고든은 경고등을 수리하러 발에 불이 나도록 뛰어갔으며, 구름처럼 피어오르는 시가 연기에 화재 위험을 경고한 일곱 개의 경고등이 추가로 박살 났다.

그리고 아마 저 경고등도 고든이 수리해야 할 거다.

“…….”

이거 진짜 제정신이 아니구만.

도대체 누가 저 인간을 국방장관 자리에 앉히는 미친 생각을 했을까 고민하던 그때, 매직 존슨이 넌지시 속삭였다.

「헤이. 게이즈. 요즘 척이 테러리스트 문제 때문에 예민해서 그래. 본성은 착한 친구니까 이해해 줘.」

그의 말이 끝나기가 무섭게 척 헤이글이 벽면을 후려쳤다.

「이 개 같은 복도! 복도! 복도! 복도 좀 넓히라고 하지 않았나!」

쾅! 쾅! 콰아앙!

넓어지는 복도를 물끄러미 바라본 최 팀장이 진심을 담아 물었다.

“정말 착한 것 맞습니까?”

「……아마도. 저래 보여도 국방장관으로서의 능력이나 추진력 하나는 끝내줘.」

당연히 끝내주겠지. 척 헤이글의 심기에 조금이라도 거슬렸다가는 그 사람의 인생이 끝날 테니까.

부쩍 자신감이 없어진 매직 존슨의 대답과 함께, 마나 인식 장치를 통과한 척 헤이글이 굳게 닫힌 문을 가리키며 말했다.

「벌써 다 왔군. 자, 여러분. 이곳은 5동이다.」

“5동?”

「E-Ring이라고 불리는 곳이지. 참고로 한 가지 말해 주자면, 내가 알기로 이곳에 외국인이 출입한 건 25년 만이야.」

최 팀장을 바라본 척 헤이글이 씩 웃으며 한 마디를 덧붙였다.

「이곳을 자유롭게 드나들 수 있었던 외부인은 지구상에 오직 한 사람뿐이었어. 미스터 스카이. 그는 미합중국의 대통령과 같은 대우를 받았지.」

다른 부분을 제쳐 두고서라도, 다른 누구도 아닌 저 척 헤이글이 꼬박꼬박 미스터라는 호칭을 붙이는 것으로도 천태민의 위상은 입증된다.

「그리고 이제 그 외손자와 젊은 영웅이 바통을 이어받았군. 자네들 모두…… 5동에 온 것을 환영하네.」

척 헤이글의 말이 끝나기가 무섭게, 문 전체에서 환한 빛이 쏟아졌다.

화아악!

아니, 이건 빛이 아니라 마법이다.

나는 전신을 훑는 마나의 흐름을 거부하지 않고 받아들였다.

시야를 물들이는 눈 부신 빛과 함께 주위를 둘러싼 공간이 일그러졌다.

‘이건…….’

이 익숙한 감각의 정체가 텔레포트(Teleport)라는 것을 깨달음과 동시에, 눈을 깜빡인 나는 완전히 낯선 새로운 공간에 도착했음을 깨달았다.

빠르게 돌아온 시야 속, 오각형의 테이블을 중심으로 앉아 있는 사람들이 보였다.

「그럼 중동 전선에 투입될 전력은…… 이런. 드디어 손님들께서 오셨군요.」

삑.

기계음과 함께 어두운 밀실을 밝히던 홀로그램이 사라지고, 상석에 앉아 있던 멀끔한 인상의 중년인이 말을 멈추고 자리에서 일어났다.

더없이 익숙한 얼굴이다.

온갖 미디어에 쉴 새 없이 노출되는 신분을 가진 그는 TV에서 봤을 때보다 더 나이 들어 보였고, 신문에서 본 것 이상의 카리스마를 뿜어내고 있었다.

「생각보다 늦었군요, 헤이글 장관. 또 애꿎은 경고 장치를 박살 낸 건 아니었길 바랍니다.」

웃음 섞인 중년인의 말에, 벌겋게 달아올라 있는 시가 끄트머리를 손가락으로 분지른 척 헤이글이 대답했다.

「내 봉급에서 까면 될 거 아닙니까.」

「그렇지 않아도 재무부 장관이 전해 달라더군요. 이미 이번 달 봉급은 당신이 부순 펜타곤 수리비로 다 나갔다고.」

「빌어먹을. 또? 이러다가 위자료가 무서워서 이혼도 못 하겠군.」

한숨 섞인 중얼거림을 내뱉은 척 헤이글이 우리를 향해 고개를 돌렸다.

「소개는 필요 없겠지?」

적어도 이번에는 필요 없다.

최 팀장도, 나도. 심지어는 스켈레톤 킹 조차도 저 중년인이 누구인지 알고 있었으니까.

- 간악한 인간이여. 저 늙은 인간이 혹시…….

맞다. 작게 고개를 끄덕인 나는 절제된 걸음으로 다가오는 중년인의 이름을 마음속으로 중얼거렸다.

‘도널드 도람프 주니어.’

이름보다 유명한 직함은, 미합중국 대통령이다.
```

## Final English reading copy

```markdown
# Chapter 607

The Pentagon.

This massive building, shaped like a giant pentagon, was practically impregnable.

More than a thousand guards, every one of them a high-ranking Hunter. The immense flows of mana surrounding the inside and outside of the building alone were enough to convey the Pentagon’s stature.

“Impressive, isn’t it?”

Magic Johnson had just finished the authentication process. Seeing Team Leader Choi and me looking around with our eyes wide, he flashed us a knowing grin.

“Since it was first built during World War II, the Pentagon has only been attacked twice. The 9/11 terrorist attacks and the Great Cataclysm. You both know how those turned out.”

Team Leader Choi nodded.

“Even the Demon King Asmodeus and his monster army’s all-out assault couldn’t bring it down.”

“That’s right. It was the second fiercest battle of my life. The first was obviously the Day of Victory. And both times, one person helped me narrowly escape death.”

Any person on Earth, not just an American, knew that fact.

During the Great Cataclysm and afterward, only one person had ever been able to stop the demon who had descended upon this world—the Demon King Asmodeus.

“Cheon Taemin. If your maternal grandfather—the man Americans called Sky—hadn’t been there, neither I nor this Pentagon would exist today.”

Magic Johnson gazed at Team Leader Choi with distant eyes, as if remembering something, when a voice suddenly rang out.

“I see you’re thinking the same thing as me, Johnson.”

The owner of that voice was neither Team Leader Choi nor me. Naturally, it wasn’t the Skeleton King hiding inside my Inventory, either.

Clomp. Clomp.

Heavy footsteps approached.

The old white man wore wrinkled jeans and a shirt, and his white hair was thoroughly tangled and disheveled. One side of his elderly face was severely distorted.

He strode toward us without hesitation and abruptly held out both hands.

“I don’t know which of you two I should shake hands with first, so I’ll do both at once. I’m Chuck Hagel. You can just call me Chuck.”

His first greeting didn’t merely carry the air of a tough Texan. It overflowed with it.

For some reason, Chuck Hagel’s face looked familiar. I stared at him as I took his hand.

“I’m Jin Taekyung. But, by any chance…”

“You’re wondering if I’m that Chuck Hagel? I am. I may not be as famous as you, but I used to cut down my fair share of monsters back in the day.”

“Oh. Ooooh.”

I’d suspected as much just from looking at him, but the old man before me really was a previous-generation S-rank Hunter known as Uncle Chuck.

I had never imagined I would meet one of the war heroes from the Great Cataclysm whom I had admired as a child. With a cry of delight, I vigorously shook his hand up and down.

“I’m a fan. A real fan. I even collected your Hunter cards when I was in elementary school.”

“Hunter cards? They sold those in South Korea?”

“They probably sold them in North Korea, too. I bought them religiously whenever I got my allowance.”

“Huh. So there was another stupid little brat here who gave me a fortune in royalties. Of course, I spent all the royalties I made back then on alimony from five divorces.”

Chuck Hagel smiled contentedly, instantly destroying one of my childhood memories.

“If you still have any of my cards, bring them to me sometime. I’ll even sign them if you want.”

“Ah, I traded all of them.”

“What?”

“After collecting ten, I traded them for a Cheon Taemin card a friend had. Honestly, Uncle Chuck cards weren’t all that rare.”

“…”

All traces of laughter vanished from Chuck Hagel’s face. He sighed.

“Damn it. And it wasn’t just anyone’s card. It was Mr. Sky’s. I can’t even say anything about that.”

“There’s no comparison in rarity or value. My friend originally wanted twenty cards, but I haggled him down and down until…”

“…I understand. I understand, so stop now.”

Chuck Hagel shook his head repeatedly, then shook hands with Team Leader Choi.

“You look exactly like your maternal grandfather. Nice to meet you, Choi.”

“Nice to meet you, Mr. Hagel.”

“I told you to call me Chuck. If you were one of those other idiots with nothing but shit in their heads, maybe not. But you and the traitor beside you have earned the right.”

*Look at him calling me a traitor just because I sold some cards.*

While I grumbled inwardly, Team Leader Choi answered in a calm voice.

“Please understand, Mr. Hagel. I don’t feel comfortable addressing the person in charge of the Pentagon and the Secretary of Defense of the United States that way.”

“Hm. Is that so? Come to think of it, I suppose you do have to worry about what people think. You’re in charge of two massive Guilds now, after all.”

I blinked as I listened to them.

“The person in charge of the Pentagon? The Secretary of Defense?”

“Hm? You didn’t know?”

“No, I didn’t. Obviously.”

“Really? Everyone else seemed to know. I assumed Johnson had at least told you.”

At the Secretary of Defense’s words, the Grand Mage—widely expected to be elected the next Secretary of Gukbap[^1]—scratched his chin.

“I assumed you knew, too. Jin. You really didn’t know?”

At this point, I felt like I had somehow become an idiot. I replied with some reluctance.

“I really didn’t know. Were you appointed a few days ago? Ah. That must be why I didn’t know.”

Chuck Hagel gave me a short, blunt answer.

“This is my eighth year.”

“…Oh.”

“Well, it’s not as if you particularly need to know. Compared to what we’re about to discuss, it isn’t especially important. Now, everyone, follow me.”

Chuck Hagel naturally pulled a cigar from the breast pocket of his dress uniform and put it between his lips. He took the lead, and we followed behind him.

Every time Chuck Hagel puffed on his cigar, acrid smoke billowed up to the ceiling, setting off an alarm as red lights flashed.

Wee-oo! Wee-oo!

> Fire hazard! Fire hazard!

Bang!

Without a moment’s hesitation, Chuck Hagel smashed the warning light and muttered,

“Fucking siren.”

He had gone beyond being a tough guy or a petty-minded bastard. He was simply insane.

The Skeleton King, who had safely passed through the security checkpoint while hiding in my Inventory, whispered,

“Is he even human? Not a monster?”

I had plenty of doubts myself, but the man matched the description printed on the Hunter cards I had collected as a child.

He was from Texas and had dreamed of becoming a cowboy. There were even unbelievable stories about him taming a minotaur with his bare fists and riding it around, among other things.

Clomp. Clomp.

No one was brave enough to stand in Chuck Hagel’s way as he marched forward without hesitation.

Researchers, Hunters, and employees who appeared to belong to the Pentagon split to either side as if facing a disaster. Moses, who had a cigar in his mouth instead of a staff, crossed between them while spewing smoke like a chimney.

Of course, he didn’t forget to talk trash along the way.

“When is this damn hallway going to get wider? Every time I see it, I want to smash it to pieces.”

“Hey, Smith. Put that electronic cigarette away while I’m asking nicely. If you waft that shitty strawberry scent in front of me one more time, I’ll put you on the list of people who died in the line of duty. Cigars are fine, though.”

“Gordon. A warning light was smashed in Section Three. Go fix it. Who broke it? Listen carefully. Your fucking direct superior.”

No one could stop Chuck Hagel as he rampaged around like an enraged bull.

During the roughly five-minute walk, poor Smith was forced to change his e-cigarette liquid, innocent Gordon ran off with his feet on fire to repair the warning light, and seven more warning lights were smashed after they warned of the fire hazard caused by the clouds of cigar smoke.

Gordon would probably have to repair those, too.

“…”

This guy was seriously out of his mind.

I was wondering who had come up with the insane idea of putting that man in the position of Secretary of Defense when Magic Johnson leaned toward me and whispered,

“Hey, guys. Chuck’s touchy because of the terrorist problem these days. He’s a good guy at heart, so try to understand him.”

The moment he finished speaking, Chuck Hagel slammed his fist into the wall.

“This goddamn hallway! Hallway! Hallway! Hallway! Didn’t I tell you to make the hallway wider?”

Bang! Bang! Kraaang!

Team Leader Choi stared blankly at the hallway as it widened, then asked with complete sincerity,

“Is he really a good person?”

“…Probably. Even if he looks like that, his abilities and drive as Secretary of Defense are second to none.”

Of course they were. Anyone who got even slightly on Chuck Hagel’s nerves would have their life ended.

Along with Magic Johnson’s suddenly much less confident answer, Chuck Hagel passed through a mana-recognition device and pointed toward a firmly closed door.

“We’re here already. Now, everyone. This is Building Five.”

“Building Five?”

“It’s called the E-Ring. And, for what it’s worth, as far as I know, this is the first time a foreigner has entered this place in twenty-five years.”

Chuck Hagel looked at Team Leader Choi and added with a grin,

“There was only one outsider on Earth who could freely come and go here. Mr. Sky. He was treated the same way as the President of the United States.”

Even setting aside everything else, Cheon Taemin’s status was proven by the fact that Chuck Hagel—of all people—referred to him as “Mister Sky” every single time.

“And now his maternal grandson and a young hero have taken up the baton. Both of you… welcome to Building Five.”

The instant Chuck Hagel finished speaking, brilliant light poured out from the entire surface of the door.

Whoosh!

No. This wasn’t light. It was magic.

I accepted the flow of mana sweeping over my entire body instead of resisting it.

Along with the dazzling light filling my vision, the space around us warped.

*This is…*

The moment I realized that this familiar sensation was Teleport, I blinked and found myself in a completely unfamiliar new space.

As my vision rapidly returned, I saw people seated around a pentagonal table.

“Then the forces being deployed to the Middle East front will be… Oh. It seems our guests have finally arrived.”

Beep.

With a mechanical sound, the hologram illuminating the dark conference room vanished. A neat-looking middle-aged man seated at the head of the table stopped speaking and rose from his seat.

His face was more than familiar.

He was a man whose position kept him constantly exposed in every form of media. He looked older than he had on television and radiated even more charisma than he had in the newspapers.

“You’re later than I expected, Secretary Hagel. I hope you haven’t smashed another innocent warning device.”

At the middle-aged man’s amused remark, Chuck Hagel snapped off the glowing end of his cigar with his fingers and answered,

“They can deduct it from my salary.”

“The Secretary of the Treasury asked me to tell you that, as it happens, your entire salary for this month has already gone toward repairing the Pentagon damage you caused.”

“Damn it. Again? At this rate, I’ll be too afraid of alimony to get divorced.”

Chuck Hagel let out a sighing mutter, then turned toward us.

“I suppose introductions aren’t necessary?”

At least this time, they weren’t.

Team Leader Choi knew who the middle-aged man was. So did I. Even the Skeleton King knew.

“Wicked human. Could that old human perhaps be…”

That was right.

I gave a small nod. As the middle-aged man approached with measured steps, I murmured his name in my head.

*Donald Doramp Jr.*

His title was more famous than his name.

He was the President of the United States.

[^1]: *Gukbap* is rice served in hot soup. Jin is deliberately replacing *bang* (“defense”) in *gukbang-bu-jang-gwan*, “Secretary of National Defense,” with *bap*, creating the nonsensical title “Secretary of Gukbap.”
```
