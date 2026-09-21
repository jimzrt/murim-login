<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0612.txt",
      "sha256": "8e51ed9e24d2e10681596b65c5a6272c3194983b8cae8efe9cf614b063ff3eda",
      "bytes": 13403
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0355e8ef739b1f88a58f1e054ce8c2c329ecba05480b663ad494f572b08dffeb",
      "bytes": 2031
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a0e8bb6a839cb19391d0cc6bfe48fa153e29045b143cbe99b1dc301112380b1f",
      "bytes": 189948
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "79251d4fe5b7d229b3861b923cc43dd8a83e79bb57c11a43f4cf07177b595f6a",
      "bytes": 667
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "58e01f10ab16fa79347671b10f88571cdba4ce2864656b69f51910e2cbbe8751",
      "bytes": 646
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "541eb5e7482e231b98e96604bd18ffdd8590796eddda9f733ca0824bc0d2e366",
      "bytes": 1886
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "bb3e55a927a4c2921c2f7e8839f7ca0006209d300ab16e93261ba28731c28325",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "a629eecd44aff8dc7a1b43a6e3c69248da760e0f9584609e8378866081440671",
      "bytes": 689
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "379c06d2cf7b83932ccb9b66df4d8839806cc05fa225b884db3089c85a799f08",
      "bytes": 191616
    }
  ],
  "estimated_tokens": 10046
}
-->

# Durable State Update — Chapter 612

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 612. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 612. Profile updates may replace only one
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
  "chapter": 612,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 612,
    "continuity_sources": [612],
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
    "Al Diab Jawahiri, the leader of Al-Qaeda, remains in the Skeleton King's custody.",
    "The Skeleton King is an undead named monster who has fought alongside Jin Taekyung and is accepted by Chuck Hagel as an ally.",
    "Al-Qaeda possesses a large Magic Gem research laboratory that appears to have operated for at least ten years.",
    "Choi and Magic Johnson are investigating the Al-Qaeda laboratory and its research results.",
    "Restricted supplies found among the terrorists indicate that someone is supporting or supplying them from within established military, political, or smuggling networks.",
    "The masked group has spent the past week destroying terrorist leadership and headquarters while concealing its identities.",
    "The group's unknown identities and overwhelming force have created a significant deterrent against further terrorist action.",
    "Freed prisoners have publicly described the atrocities they witnessed, bringing renewed international attention to global terrorism and the masked group.",
    "Jin Taekyung intends to return after resolving the final matter he has deliberately postponed."
  ],
  "continuity_sources": [
    611
  ],
  "open_questions": [
    "Who supplied Al-Qaeda with the restricted equipment, weapons, artifacts, and military goods?",
    "What results, if any, did Al-Qaeda obtain from its long-running Magic Gem experiments?",
    "What fate will the Skeleton King ultimately assign to Al Diab and the remaining terrorists?",
    "Where is Jin Taekyung actually returning, and what final matter must he resolve first?"
  ],
  "safe_through": 611,
  "temporary_decisions": [
    "Use Al Diab Jawahiri as the full English rendering of 알 디아브 자와히리.",
    "Retain Crazy Korean as Chuck Hagel's address for the masked protagonist.",
    "Preserve the chapter's weeds metaphor with pull out weeds and pull them out by the roots.",
    "Keep Magic Gem laboratory for 마정석 관련 비밀 실험실."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 로그인              | **Login**                      |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 키라라 | **Kirara** | Worker at Tokyo-ru referenced in Taekyung's joke. |
| 진호 | **Jin-ho** | Jin Taekyung's older male friend, addressed as Jin-ho hyung. |
| 아프리카 | **Africa** | Region where terrorist organizations are reportedly conducting Gate and Magic Gem experiments. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 진호 | 태경 | Older male friend addressing a younger male friend in a close hyung relationship | Taekyung | Informal and familiar | Jin-ho addresses Taekyung as 태경아 in recalled advice; Taekyung refers to him as Jin-ho hyung. |
| 진태경 | 김화종 | younger_ally_to_older_butler | Butler Kim | respectful and formal | Asks about Kim Hwajong before entering the morgue and later bids him farewell. |

## Listed compact profiles

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 607
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 600
- **Aliases:** Butler Kim
- **Role:** Hwa-jong was Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong served Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 609
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license; his Middle Dantian is partially activated at 10%, slightly improving the efficiency of his martial arts and internal energy.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 609
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 600
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong was a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Gentle and composed as Butler Kim, but retains a fiery temperament and a habit of swearing.
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and served Choi Minwoo as butler and personal escort, becoming Choi's only family.

## Korean source

```text
＃612화



“나와.”

착 가라앉은 목소리. 어둠 속에서 날카롭게 빛나는 눈동자.

그러나 나는 대답하는 대신 침착하게 그를 지켜봤다. 잠깐의 침묵이 흐른 뒤 딸칵, 하는 소리와 함께 거실이 환해진다.

스윽.

조심스럽게 걸음을 옮긴 남자가 힘주어 재차 입을 열었다.

“숨어 있는 거 다 알고 있으니까 나오라고. 너 내가 누군지 알아?”

당연히 알고 있다. 그의 이름과 얼굴, 심지어는 나이와 고향까지. 집에 돌아오자마자 이런 짓을 할 줄은 몰랐지만.

“좋아, 마지막이다. 셋 셀 때까지 안 나오면 내 친한 동생 부른다. 걔 엄청 세고 잘나가는 헌터야. 하나. 둘…….”

셋까지 다 세고 나면 무슨 일이 벌어질까 궁금하긴 했지만, 이미 볼 장 다 본 마당에 더 지켜보는 것도 낯부끄럽다.

나는 한숨처럼 입을 열었다.

“설마 그 친한 동생이라는 사람이 나는 아니지?”

“……!”

“얼씨구. 맞나 보네.”

충격으로 석상처럼 굳어 있던 남자, 진호 형이 부릅뜬 눈으로 나를 바라봤다.

“뭐, 뭐야. 네가 왜 거기서 나와.”

“어차피 부를 거, 알고 미리 왔다. 됐냐?”

잠시 침묵하던 진호 형이 무거운 표정으로 입을 열었다.

“어디서부터 어디까지 봤냐.”

“나와, 할 때부터.”

“아, 씨바…….”

“멋있더라. 포스가 너무 지려서 나도 모르게 나올 뻔했잖아.”

“지금 놀리냐?”

“응.”

한 치의 망설임도 없는 당당한 대답에 나를 빤히 노려보던 진호 형이, 문득 실소를 흘렸다.

“새끼. 하나도 안 변했네.”

별것 없어 보이는 저 한 마디에, 이토록 반갑고 고마운 기분이 드는 것은 왜일까. 나는 그를 따라 웃으며 대답했다.

“배고프다. 라면 끓여 줘.”



* * *



김이 모락모락 나는 냄비를 사이에 두고 마주 앉으니, 일 년 전쯤으로 돌아온 기분이다.

물론 지금은 나도, 진호 형도 그때와는 많이 달라졌지만.

“형이 정장 입은 건 처음 보네. 맨날 누더기 같은 추리닝만 걸치고 다니더니.”

“인마, 누더기 같다니. 그거 꽤 비싼 메이커야.”

“언제 샀는데?”

“음. 고등학교 때?”

진호 형이 몇 살이었더라. 잠깐 생각하던 내가 고개를 끄덕였다.

“누더기 같은 게 아니라 누더기였네. 나 물 좀. 아니다. 혹시 소주 있어?”

“차라리 고깃집에 가서 고기 있냐고 물어봐라.”

“……보아하니 곧 단명하겠구만.”

“김 계장 그 새끼만 아니었어도 진작 끊었다. 그 시발롬은 나이 차이도 얼마 안 나면서 사사건건 시비 걸고 지랄이야.”

넥타이를 거칠게 풀어헤친 진호 형은 소주 석 잔을 연거푸 들이켰다.

작년 말, 드디어 오랫동안 준비했던 공무원 시험에 합격한 그였다.

“그래도 형이 공무원이 되긴 하네. 세상 참 말세다.”

“이 새끼 말본새 보소. 그럼 안 될 줄 알았냐?”

“아니. 되는 건 둘째치고 난 형이 조만간 야동 보다가 복상사할 줄 알았지.”

“……음. 제법 일리가 있는 말이긴 한데.”

부정하지 않는 걸 보니 그나마 아직 한 줄기 양심은 남아있군.

만약 정부 정식 부처 중에 야동부가 있었다면 장관까지 올라가고도 남을 인간이다.

야동부 차관직에 소라 아오이, 대변인으로는 키라라 아스카를 두고 폰허브를 호령했겠지.

하지만 애석하게도 그런 정신 나간 부처는 존재하지 않았고, 특채 시험을 통해 합격한 진호 형은 알짜배기로 소문난 헌터 및 게이트 관리 부서에 발령 났다.

물론 나와의 개인적인 친분이 보이지 않는 가산점을 부여했다는 것은 나도 내심 짐작하는 바였다.

꼴꼴꼴.

소주 잔을 가득 채운 진호 형이 불쑥 입을 열었다.

“그런데 웬일이냐?”

“잊으셨나 본데, 여기 내 집이야. 지금은 쓰레기 처리장인지 오피스텔인지 헷갈리긴 하지만.”

“집주인이 두세 달 넘게 코빼기도 안 비추니까 하는 소리 아냐, 인마.”

“그거라면 뭐 형 얼굴도 볼 겸해서 왔지. 가져갈 물건도 있었고.”

“가져갈 물건? 옷 말하는 거면 그냥 하나 사지 그러냐. 돈도 썩어 나는 놈이.”

“돈이 있어도 못 사. 파는 곳이 없어서.”

“그런 게 어디 있어?”

의아한 표정으로 되묻던 진호 형이 이내 짧은 탄성을 흘렸다.

“아. 혹시 그 고물 캡슐?”

“응, 그거. 다행히 안 버렸더라.”

“버리면 죽여 버린다며.”

“그래서 다행인 거지. 버렸으면 진짜 죽였을 텐데, 휴.”

“……농담이지? 농담이라고 해 줘, 제발.”

맨 처음 나를 무림으로 인도했던 게임 캡슐은 별다른 쓸모 없이 이곳에 방치되어 있었다.

시스템이 허락한 덕분에 캡슐이 없어도 자유자재로 로그인과 로그아웃을 할 수 있게 되었으니까.

하지만 그렇다 해서 애물단지 취급할 수는 없는 법이다.

그 고물 캡슐이야말로 지금의 나를 만들어 준 일등 공신이며, 가치를 매길 수 없는 보물이니까.

“내가 식탁은 안 닦아도 그 캡슐은 일주일에 한 번씩 닦는다. 그런데 그거 여전히 작동 안 되던데. 뭐 하러 가져가?”

“그냥. 장식용이지, 뭐.”

“귀신 들린 물건 아니냐? 전에 왜, 희망 고시원 살았을 때 네가 저 캡슐에서 잤다가 이상한 악몽 꿨다고…….”

그러고 보니 그랬던 적이 있었지.

처음 로그아웃했을 때의 이야기를 꺼내는 진호 형의 모습에, 나는 황급히 화제를 돌렸다.

“혹시 그 뉴스 봤어? 이번에 중동이랑 아프가니스탄 쪽 난리 났던데.”

“어? 갑자기 그 얘기를 왜 꺼내?”

“아니, 봤냐고.”

“당연히 보기야 봤지. 어제 중동 테러 단체랑 아프가니스탄 반군 세력들이 공동 성명서도 발표했잖아. 앞으로 테러 자제하고 밑에 놈들 단속 잘하겠다고. 사실상 쫄아서 항복 선언 한 거지.”

“안심하면 안 돼. 어차피 잠깐일 테니까.”

“그래도 진짜 대단한 사람들 아니냐? 그 이상한 복면 쓴 5인조.”

다행히 화제 돌리기는 그럭저럭 먹혀 든 모양이다. 나는 내심 안도의 한숨을 내쉬며 고개를 끄덕였다.

“그렇지.”

“뭐, 어쨌든.”

후루룩 면발을 빨아들인 진호 형이 소주로 입가심을 하며 말을 이었다.

“고생 많았다. 새해 밝자마자 몬스터 웨이브에, 몬스터보다 더한 인간에, 이젠 사막이랑 아프리카까지 다녀오고.”

“뭘 또 고생씩이나. 그냥 해야 할 일이니까 한 것…….”

순간 멈칫한 나는 말꼬리를 흐렸다. 잠깐만. 이 인간이 지금 무슨 말을 하는 거야.

“아니, 뭐라고?”

“뭐긴 뭐야. 네가 들은 대로지. 혹시나 해서 찍어 봤는데 대충 맞았네.”

“……!”

“인마. 전 세계에 그럴 만한 짓을 할 사람이 몇 명이나 있다고. 다들 테러리스트 죽어 버렸으면 좋겠다. 반군 새끼들 꼴도 보기 싫다. 하면서도 막상 복면 뒤집어쓰고 실행에 옮길 사람이 누가 있겠냐? 아니, 애초에 그걸 실현할 수 있는 능력이 없지, 능력이.”

눈을 동그랗게 뜬 내 모습에 진호 형이 피식 웃었다.

“몇몇 사람들도 내심 짐작하면서도 쉬쉬하고 있을걸. 어차피 증거도 없는 데다가 탓할 일도 아니니까. 다만 어떤 말단 공무원은 운 좋게 그 복면인이 어떤 성격인지도 알고, 라면도 끓여 먹는 사이라 이렇게 슬쩍 떠볼 수 있는 거고.”

나는 왠지 모르게 얼얼해진 뒤통수를 어루만졌다.

내가 유력한 용의자로 지목될 거라는 사실은 짐작했지만, 이렇게 어이없을 만큼 쉽게 걸려들 줄은 몰랐다.

“나, 나 진짜 아닌데?”

“그래. 뭐 그렇다고 치자. 그래서 언제 돌아온 거야?”

“…….”

젠장. 이미 나가리다. 한숨을 푹 내쉰 나는 소주잔을 채우며 대답했다.

“사흘. 아니다, 나흘 전.”

“좋아. 이제 좀 고분고분해졌군.”

“어디 가서 입 벙긋하지 마. 기밀인 건 둘째치고, 그때는 형이 위험해져.”

나나 최 팀장. 그리고 가족들은 늘 보이지 않는 경호에 둘러싸여 있지만, 진호 형은 아니다.

내 말의 의미를 찰떡처럼 알아들은 진호 형이 입맛을 다셨다.

“으음. 뭔가 거물이 된 기분인데.”

“거물이 되기 전에 폭발물이 먼저 배달 올지도 몰라.”

“글쎄. 걔들은 다 알아도 나 못 건드릴걸? 진태경이 빡 돌면 무슨 일 벌일지 모르니까. 캬, 이거야말로 언터처블(Untouchable) 아니냐?”

태평하게 웃은 진호 형이 말을 이었다.

“그나저나 요새는 얼마나 바쁘게 지내길래, 언제 돌아왔는지도 헷갈려?”

“음.”

얼마나 바쁘냐고?

어느덧 덥수룩하게 자란 턱수염을 긁적이던 내가 대답했다.

“그냥 밤낮없이 훈련해. 가족들이랑 같이 식사하고, 계속해서 다시 훈련.”

“훈련? 너 정도씩이나 되는 놈이 왜 훈련을 해?”

“형은 명문대 나왔는데도 십 년 가까이 또 공부만 했잖아. 비슷한 거지.”

“이 새끼가 아픈 곳을 찌르네. 그리고 너랑 나랑 같냐? 분야 차이가 아니라 아예 노는 레벨이 다른데.”

그것도 그렇다. 진호 형이 나온 명문대는 연간 수백 명이 입학하고, 그와 비슷한 숫자가 졸업하니까.

하지만 지금의 내게도 훈련은 필요했다.

배움에는 끝이 없고, 공부(工夫)라는 단어는 학문에만 적용되는 것이 아니다.

‘정확히는 새로운 뭔가를 배운다기보단, 천천히 되새긴다고 봐야겠지.’

그런 의미에서 내가 하고 있는 훈련은 복습이라고 봐야 했다.

나를 위한 공부이기도 하고, 이 세상을 위한 공부이기도 했다.

아쉽게도 아직 완전한 결과물을 만들지는 못했지만.

“으, 표정 진지한 거 봐. 뺨 한 대만 치고 싶다.”

“……거, 한창 진지한데 그 아가리를 좀.”

“입장 바꿔서 한번 생각해 봐라. 너 같으면 어떨지.”

“음. 그건 그렇네. 한잔해.”

우리는 사이좋게 술잔을 부딪쳤다. 소주를 한입에 털어 넣고, 다 식어 버린 면발을 뒤적거리던 진호 형이 묻는다.

“그래서, 훈련은 잘 되어 가고?”

“그럭저럭. 한 달쯤 전부터 준비했던 거라 슬슬 마무리 단계긴 한데…… 이게 쉽지가 않네.”

이건 결코 엄살이 아니다.

지금의 나는 마치 1만 피스로 이루어진 퍼즐을 맞춰야 하는 어린아이와 같았다.

하나하나를 확인하고 짜 맞추는 과정에서 스스로에 대한 아쉬움과 부족함을 느꼈고, 이제는 마지막 남은 한 조각을 찾지 못해 어둠 속을 더듬거리고 있다.

그리고 내 눈 앞을 가린 이 어둠의 이름을, 나는 이미 알고 있었다.

‘심마(心魔).’

마음에 낀 먹구름은 쉽게 흩어지지 않았다.

무림과 현대. 두 세계에 대한 고민과…… 그래, 무엇보다 김화종의 마지막 모습이 자꾸만 떠오른다.

금방이라도 꺼질 것 같던 그의 목소리가. 피로 뒤덮인 붉은 눈밭에서 서서히 감기던 눈동자가 생각났다.

어쩌면 내가 이 자리에 온 이유는, 캡슐을 가져가기 위해서라 아니라 편안함을 느끼고 싶어서였는지도 모른다.

사랑하는 가족도, 함께 하는 동료도 아닌 전혀 다른 세상에서 자신만의 삶을 사는 친구를 만나 옛날처럼 술잔을 부딪치고 싶어서였을 것이다.

‘그래, 그런 거였어.’

나는 문득 마음이 편안해지는 것을 느꼈다.

비록 심마를 완전히 떨쳐 낸 것은 아니지만, 모든 상황과 고민을 인정하고 받아들이는 것만으로도 무거웠던 마음 한구석이 홀가분해진다.

더불어 지금 내가 있어야 할 곳이 여기가 아니라는 것도 깨달았다.

“나 간다.”

“라면 다 식었는데. 안주로 두부김치 만들…… 갑자기?”

“어. 할 일 생각났어. 술 혼자 먹어.”

“미친놈이냐?”

“아니, 집주인인데. 이번 달부터 월세 낼래?”

험악한 표정을 짓고 있던 진호 형이 넙죽 허리를 숙였다.

“조심히 들어가십시오, 사장님.”

“오냐.”

피식 웃으며 현관문으로 향하는 내 뒤로, 진호 형의 다급한 목소리가 울려 퍼졌다.

“야, 야! 캡슐은?”

“다음에. 다음에 가져갈게.”

그렇게 대답하면서도 나는 알고 있었다.

어쩌면 이다음에도, 나는 똑같은 대답과 함께 캡슐을 가져가지 않을 것이라는 걸. 오늘처럼 술잔만 부딪칠 것이라는 걸.

“그래, 힘내라. 인마.”

귓가에 닿은 자그마한 누군가의 중얼거림과 함께, 나는 걸음을 옮겼다.
```

## Final English reading copy

```markdown
# Chapter 612

“Come out.”

His voice was low and steady. His eyes gleamed sharply in the darkness.

Instead of answering, I calmly watched him. After a brief silence, the living room suddenly brightened with a click.

The man cautiously stepped forward and spoke again, his voice firm.

“Come out. I know you’re hiding there. Do you know who I am?”

Of course I did. I knew his name and face, even his age and hometown. I just hadn’t expected him to pull something like this the moment I came home.

“All right, this is the last warning. If you don’t come out by the time I count to three, I’m calling my close younger friend. He’s an incredibly strong and successful Hunter. One. Two…”

I was curious about what would happen after he counted to three, but after seeing everything there was to see, continuing to watch felt embarrassing.

I spoke with a sigh.

“Don’t tell me that close younger friend is me?”

“……!”

“Well, would you look at that. Guess I was right.”

The man who had frozen like a statue in shock stared at me with wide eyes.

“What the hell? Why are you coming out of there?”

“I knew you were going to call me anyway, so I came before you could. Happy now?”

After a brief silence, Jin-ho hyung spoke with a heavy expression.

“How much did you see?”

“From when you said, ‘Come out.’”

“Ah, fuck…”

“You looked pretty cool. Your presence was so intense I almost came out on my own.”

“Are you making fun of me right now?”

“Yes.”

At my shameless answer, Jin-ho hyung stared at me for a moment before suddenly letting out a quiet laugh.

“You bastard. You haven’t changed at all.”

Why did such a simple remark make me feel so happy and grateful to see him?

I smiled along with him and answered.

“I’m hungry. Make me some ramyeon.”

* * *

Sitting across from each other with a steaming pot between us made me feel as though I had gone back about a year.

Of course, both Jin-ho hyung and I had changed considerably since then.

“This is the first time I’ve seen you in a suit. You used to wear nothing but ragged-looking tracksuits.”

“Hey, don’t call it ragged. It’s a pretty expensive brand.”

“When did you buy it?”

“Hmm. High school?”

How old had Jin-ho hyung been then? After thinking for a moment, I nodded.

“So it wasn’t ragged-looking. It was actually ragged. Get me some water. No, wait. Do you have any soju?”

“You might as well go to a barbecue restaurant and ask if they have any meat.”

“……Judging by that, you’re probably going to die young.”

“I would’ve quit ages ago if it weren’t for that asshole Section Chief Kim. That fucking bastard isn’t even that far from me in age, but he picks fights over every little thing and acts like a complete jackass.”

Jin-ho hyung roughly loosened his tie and downed three shots of soju in a row.

At the end of last year, he had finally passed the civil service exam he had been preparing for so long.

“So you really did become a civil servant. The world really is coming to an end.”

“Listen to this bastard’s attitude. Did you think I wouldn’t?”

“No. Becoming one is beside the point. I thought you’d drop dead in the act while watching porn before you ever got there.”

“……Hmm. That does make a fair amount of sense.”

Since he didn’t deny it, at least one thread of his conscience must still have remained.

If there had been a Pornography Department among the government’s official ministries, this man would have climbed all the way to minister.

With Sora Aoi as deputy minister and Asuka Kirara as spokesperson, he would have ruled Pornhub from the top.

Unfortunately, no such deranged ministry existed. After passing through a special recruitment exam, Jin-ho hyung had been assigned to the Hunter and Gate Management Department, a division known for being a plum assignment.

Of course, I had a vague suspicion that our personal relationship had earned him a few invisible bonus points.

Glug, glug, glug.

After filling his soju glass to the brim, Jin-ho hyung suddenly spoke.

“What brings you here?”

“You seem to have forgotten, but this is my house. Though at this point, I’m starting to confuse it with a garbage dump or an officetel.”

“Isn’t that because the owner hasn’t shown his face in two or three months?”

“If that’s what you mean, I came partly to see your face. I also had something to pick up.”

“Something to pick up? If you mean clothes, why not just buy some? You’ve got money coming out of your ears.”

“I can’t buy it even if I have the money. There’s nowhere that sells it.”

“What kind of thing is that?”

Jin-ho hyung looked puzzled, then suddenly let out a short exclamation.

“Ah. You mean that old capsule?”

“Yeah, that one. Luckily, you didn’t throw it away.”

“You said you’d kill me if I did.”

“That’s why it’s lucky. If you’d thrown it away, I really would have killed you. Phew.”

“……You’re joking, right? Please tell me you’re joking.”

The game capsule that had first led me to the Murim had been left here, abandoned without any real purpose.

Thanks to the System’s permission, I could now freely use Login and Logout without the capsule.

But that didn’t mean I could treat it like an unwanted piece of junk.

That old capsule was the greatest contributor to making me who I was. It was a priceless treasure.

“I don’t wipe the dining table, but I clean that capsule once a week. It still doesn’t work, though. Why are you taking it?”

“Just because. It’s decoration or something.”

“Isn’t it haunted? You know, back when you lived at Hope Goshiwon, you slept in that capsule and had a weird nightmare…”

Come to think of it, that had happened.

As Jin-ho hyung began bringing up what happened after my first Logout, I hurriedly changed the subject.

“Did you see the news? Things got pretty crazy in the Middle East and Afghanistan this time.”

“Huh? Why are you bringing that up all of a sudden?”

“No, I’m asking if you saw it.”

“Of course I saw it. Yesterday, the terrorist groups in the Middle East and the rebel forces in Afghanistan even issued a joint statement. They said they’d refrain from terrorism in the future and keep their subordinates under control. It was basically a declaration of surrender because they were scared shitless.”

“You shouldn’t let your guard down. It’ll only last for a little while.”

“Even so, aren’t those five masked weirdos incredible?”

Fortunately, it seemed my attempt to change the subject had worked. I breathed an inward sigh of relief and nodded.

“They are.”

“Well, anyway.”

After slurping up a mouthful of noodles, Jin-ho hyung rinsed his mouth with soju and continued.

“You’ve had it rough. A monster wave right after the new year, humans worse than monsters, and now trips to the desert and Africa.”

“What do you mean, rough? It was just something I had to do…”

I suddenly faltered and let the end of the sentence trail off.

Wait a minute. What the hell was this guy saying?

“Sorry, what?”

“What do you think? Exactly what you heard. I took a guess, and I was more or less right.”

“……!”

“Come on. How many people in the entire world could have done something like that? Everyone says they wish all the terrorists would just die, and that they can’t stand the rebel bastards. But who would actually put on a mask and act on it? No, more importantly, who would even have the ability to make it happen?”

At the sight of my round eyes, Jin-ho hyung snorted softly.

“Some people have probably guessed, too, but they’re keeping quiet. There’s no evidence, and it’s not as if they have any reason to blame you. But one low-ranking civil servant happens to know what kind of person the masked man is—and even shares ramyeon with him—so he can casually sound him out like this.”

I rubbed the back of my head, which had somehow gone numb.

I had suspected I would be named as a prime suspect, but I hadn’t expected to get caught this absurdly easily.

“I’m… I’m really not him.”

“Sure. Let’s say that’s true. So when did you get back?”

“……”

Damn it. I was already done for.

I let out a deep sigh, filled my soju glass, and answered.

“Three days ago. No, four.”

“Good. You’re finally being a little more cooperative.”

“Don’t say a word about this anywhere. Forget the fact that it’s classified—you’ll be in danger if you do.”

Team Leader Choi, my family, and I were always surrounded by invisible protection.

Jin-ho hyung wasn’t.

He understood exactly what I meant and smacked his lips.

“Hmm. I feel like some kind of big shot.”

“Before you become a big shot, a bomb might get delivered to you.”

“Maybe. But even if they all know, they won’t be able to touch me, will they? They won’t know what Jin Taekyung might do if he completely loses it. Hah, isn’t this what you call Untouchable?”

Jin-ho hyung laughed without a care and continued.

“By the way, how busy have you been lately that you can’t even keep track of when you came back?”

“Hmm.”

How busy had I been?

I scratched at my thick, overgrown beard and answered.

“I just train day and night. I eat with my family, then go right back to training.”

“Training? Why does someone at your level still need to train?”

“You graduated from a prestigious university, but you spent almost another ten years studying. It’s basically the same thing.”

“You really know how to hit a sore spot. And how are you and I the same? This isn’t just a difference in fields. We’re playing on entirely different levels.”

He had a point. The prestigious university Jin-ho hyung had attended admitted hundreds of students a year, and roughly the same number graduated.

But I still needed training.

There was no end to learning, and *gongbu*—the work of mastering something—didn’t apply only to academics.

*To be more precise, I’m not learning something new so much as slowly going over what I already know.*

In that sense, the training I was doing was more like a review.

It was study for my own sake, and study for the sake of this world.

Unfortunately, I still hadn’t managed to create a complete result.

“Ugh, look at that serious expression. It makes me want to slap you in the cheek.”

“……I’m in the middle of being serious, so could you shut that mouth of yours?”

“Put yourself in my shoes. What would you do if you were me?”

“Hmm. I suppose you’re right. Have a drink.”

We clinked our glasses amicably.

After tossing back his soju and stirring the noodles that had gone completely cold, Jin-ho hyung asked,

“So, is the training going well?”

“More or less. I started preparing about a month ago, so I’m slowly reaching the final stage, but… it isn’t easy.”

This was no exaggeration.

Right now, I was like a child trying to put together a ten-thousand-piece puzzle.

As I checked each piece and fit them together, I felt my own shortcomings and regretted what I lacked. Now, unable to find the final piece, I was groping around in the dark.

And I already knew the name of the darkness covering my eyes.

*The heart demon.*

The dark cloud hanging over my heart did not scatter easily.

My worries about the Murim and the modern world. And… yes, more than anything, the final sight of Kim Hwajong kept coming back to me.

His voice, which seemed as though it could fade away at any moment.

His eyes slowly closing in the red snowfield covered with blood.

Maybe the reason I had come here wasn’t to take the capsule after all.

Maybe I had come because I wanted to feel at ease.

I wanted to meet a friend who lived his own life in a completely different world—not a beloved family member or a companion at my side—and clink glasses with him like we used to.

*Yes. That was it.*

I suddenly felt my heart grow lighter.

I hadn’t completely shaken off the heart demon, but simply acknowledging and accepting every situation and worry had lifted some of the weight from my heart.

At the same time, I realized that the place where I needed to be wasn’t here.

“I’m leaving.”

“The ramyeon’s gone cold. I was going to make some tofu kimchi as a side dish… What? All of a sudden?”

“Yeah. I just thought of something I have to do. Drink by yourself.”

“Are you crazy?”

“No. I’m the landlord. Are you going to start paying rent this month?”

Jin-ho hyung, who had been glaring at me fiercely, immediately bent deeply at the waist.

“Please get home safely, Boss.”

“Yeah, yeah.”

I snorted softly and headed for the front door. Behind me, Jin-ho hyung’s urgent voice rang out.

“Hey, hey! What about the capsule?”

“Next time. I’ll take it next time.”

Even as I answered, I knew.

Maybe next time, I would give the exact same answer and still not take the capsule.

Maybe, just like today, I would only clink glasses with him.

“All right. Hang in there, you bastard.”

With someone’s quiet mutter reaching my ears, I walked on.
```
