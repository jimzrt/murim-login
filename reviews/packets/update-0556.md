<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0556.txt",
      "sha256": "8cd2ae48a484b24bda6640312f5949458fe3fb606604bcbe19f008194334b6f3",
      "bytes": 13690
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "89399ddcc3db18e965e293128666d1ad75f03503432bdd2777f1a091e0a661d4",
      "bytes": 4398
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1c0d42f9dca350bddcbff56b3d03ef0010f01a77fbe8a32025167c74554d640d",
      "bytes": 175723
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f72f3fe17ae83d2e3c7c0b7e8ea42b319a865923aa47fb9c6f953dd786abacac",
      "bytes": 2292
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2c86630117b110b082c3395020e718481ce2c16fae7dd9dbd318d4e5b537d423",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "449355b1dc9177ef376787aca4e5d920d3364f233773c2755dc085191a12a593",
      "bytes": 168439
    }
  ],
  "estimated_tokens": 10165
}
-->

# Durable State Update — Chapter 556

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 556. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 556. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 556,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 556,
    "continuity_sources": [556],
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
    "The Fire Dragon Pavilion’s six-member first mission is to enter Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can’t Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, and leadership of the Fire Dragon Pavilion’s first mission to Nanman.",
    "Mungyeong ended Taekyung’s direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven’s second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam’s transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng’s Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon’s remains.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho’s dispatch there has received no reply for more than seven days.",
    "Taekyung is in the modern world on January 1, 2047, staying with Kim Jeonghee and Hayeon at Team Leader Choi’s mansion, where Cheon Taemin once lived.",
    "The public believes the Lich killed Lee Jungryong and Wu Heixing; Lee is being honored as a Great Cataclysm hero, while Taekyung knows the actual deaths were caused by him.",
    "Go Jun is now Ares Guild’s Vice Guild Master and chief mourner for Lee Jungryong, with dozens of A-rank Hunters serving as his new subordinates; he intends to preserve Lee’s legacy and regards Jin Taekyung and Choi Minwoo as its enemies.",
    "Team Leader Choi deliberately revealed his connection to Cheon Taemin as the old hero’s only living blood relative and intends to acquire the Ares Guild with its influence intact before removing Lee’s corruption.",
    "Go Jun possesses a battered necklace recovered from the ruins of the Arch Lich’s former stronghold; it is not Lee Jungryong’s keepsake, but Go Jun bribed an investigation leader to obtain it because he considers it meaningful.",
    "An unidentified Hunter party is fighting monsters inside a Gate when a surge of mana far beyond a low-level Gate’s capacity creates a Mutated Gate; their fate is unresolved."
  ],
  "continuity_sources": [
    555,
    554
  ],
  "open_questions": [
    "What is the Lord of Heaven’s identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung’s party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo’s political engagement end?",
    "What process created Jang Sam’s mutant form, whether Dark Heaven’s mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What did Lee Jungryong leave Go Jun beyond his dying wish, what is the necklace recovered from the Arch Lich’s ruins, and what will happen to the hunters caught in the Mutated Gate?"
  ],
  "safe_through": 555,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman and 남만을 못 가 as Can’t Go to Nanman.",
    "Render 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 소격변 as Small Cataclysm, 낭중지추 as needle in a bag, 국장 and 국가장 as national funeral, 상주 as chief mourner, 변이 게이트 as Mutated Gate, and 아크 리치 as Arch Lich."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 남만야수궁  | **Nanman Beast Palace**          |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 하남     | **Henan**              |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 계인 | **Buddhist precept seals** | Seals carved into the foreheads of Shaolin martial monks. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 블링크 | **Blink** | Arch Lich movement spell |
| 시부럴좌 | **Lord Sibu-leol** | Online nickname derived from Taekyung's public profanity. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 555
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, and now serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion while holding its unique Title, Fire Dragon Pavilion Master and leading its first mission to Nanman.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 555
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃556화



후우.

한숨과 함께 주위를 훑었다.

축축하고 서늘한 동굴 내부. 미로처럼 얽힌 좁은 통로와 천장에 매달린 뾰족한 종유석. 잔뜩 겁에 질린 피로한 얼굴들.

‘그때랑 똑같군.’

3년. 아니, 무림에서 보낸 시간까지 합한다면 4년 전이다.

그날의 사고는 지울 수 없는 화인(火印)처럼 가슴에 남았고, 이미 복수를 끝마친 지금에도 완전히 잊지 못했다.

“시벌, 옛날 생각나네.”

텁텁하게 뇌까리는 나와 달리, 스켈레톤 킹은 흐뭇하게 웃어 보였다.

“나 역시 마찬가지다. 이건 마치 너희가 말하는 고향에 돌아온 기분이군.”

“…….”

그거 아냐, 인마.

서로 떠올리는 부분이 상당히 어긋나는 것 같은데.

어쩌면 저놈이 내가 한창 하급 게이트를 전전하고 있을 때 마주친 스켈레톤 1이었을지도 모르겠다.

그나저나…….

구구구구궁!

‘마력의 파동이 생각했던 것보다 훨씬 센데?’

때마침 인근에 있었기에 망정이지, 하마터면 열심히 살아가는 생목숨이 스물이나 날아갈 뻔했다.

나는 얼빠진 시선으로 이쪽을 응시하는 헌터들을 향해 손짓했다.

“위험하니까 이쪽으로 오세요.”

팀장으로 보이는 20대 후반의 남자가 눈을 깜빡였다.

“뭐, 뭐요?”

“오시라고. 빨리.”

“그, 그쪽은 누구신데요?”

어두컴컴한 동굴 내부. 상당한 거리를 두고 멀찍이 떨어진 내 얼굴까지 알아보기에는 저들의 수준이 너무 낮다.

머쓱하게 턱을 긁적인 내가 입을 열었다.

“저는…… 어어, 뒤 보세요.”

“예?”

반응이 느리다. 나는 대답 대신 손가락을 튕겼다.

쉭, 퍼엉!

미세한 파공음과 함께 녹색 핏물이 사방으로 튀었다. 동시에 어느 헌터의 등 뒤로 접근하던 고블린의 손에서 녹슨 도끼 한 자루가 힘없이 미끄러졌다.

이어 머리통이 사라진 몸뚱어리가 썩은 통나무처럼 허물어진다.

쿵!

“헉!”

“뒤! 뒤를 조심해라!”

“뭐, 뭐야 이거.”

뭐긴. 지풍(指風)이지.

내심 중얼거린 나는, 황급히 재차 대열을 갖추는 헌터들을 보며 새삼 깨달았다.

‘쟤들이 오는 것보다, 내가 가는 게 빠르겠구나.’

하긴, 중간도 되지 않는 지점에서 고블린을 상대로 버벅거리는 걸 보니 하급 헌터인 것은 둘째치고, 그리 경험 많은 자들이 아니다.

스켈레톤 킹이 금발을 쓸어올리며 진지한 표정을 지었다.

“후, 이 몸이 나서야 할 때로군.”

“가만히 있어. 깝치지 말고.”

“…….”

할 일이 정해지니 망설일 이유가 없다. 나는 그리 서두르지도, 그렇다고 느긋하지도 않은 걸음으로 그들을 향해 걸음을 옮겼다.

저벅.

한 걸음. 그리고 동시에 활짝 펼친 양손에서 뻗어나간 열 줄기의 지풍이 허공을 격하고 쏘아졌다.

쉭, 퍼버버버벅!

한 번 더.

쉬쉬쉭!

다시.

퍼엉!

우두머리쯤으로 보이는 홉 고블린을 마지막으로, 서른 마리에 달하는 고블린들이 머리 없는 사체가 되어 나뒹굴기까지는 찰나의 시간이면 충분했다.

그리고…….

저벅.

세 번째이자 마지막 한 걸음과 함께, 어느 이름 모를 마법사가 라이트(Light) 마법으로 불러온 빛무리가 내 얼굴을 비췄다.

화악.

“……!”

“……!”

보이지 않는 충격과 동요가 동굴 내부를 휩쓸었다.

모두가 넋 나간 시선으로 내 얼굴만을 바라보고 있던 그 순간, 막혀 있던 둑이 터지듯 비명 같은 외침이 곳곳에서 튀어나왔다.

“시, 시벌좌!”

“시부럴좌!”

“지, 지, 지, 진태경!”

그나마 마지막이 낫군.

비록 이름이 여섯 글자로 길어지긴 했지만, 앞의 별명에 비하면 양반이다. 대충 이조참판 정도.

그리고 어떻게 생각해 보면 현 상황에 딱 맞는 이름이기도 했다.

점차 거세지던 진동이 어느덧 지, 지, 지, 지진으로 존나게 흔들리고 있었으니까.

구구구구궁!

설렁거리는 걸음으로 다가온 스켈레톤 킹이 머리 위로 떨어지는 종유석을 피하며 중얼거렸다.

“이 정도로 요란한 걸 보니, 영 심상치 않은데.”

“내 말이.”

기껏해야 E급. 혹은 F급 정도인 이 게이트와는 하남에서 남만야수궁만큼의 거리가 있는 마력이다.

작게 혀를 찬 나는 여전히 경악에 차 있는 헌터들을 향해 손짓했다.

“아까 했던 말인데, 위험하니까 이쪽으로 오……”

다다다다!

“어잇. 깜짝아.”

“언데드 맙소사.”

뭐지, 블링크 마법인가.

확실히 얼굴이 워낙 많이 팔리면 이런 장점이 있다.

두메산골 김씨 할매도 내 이름 정도는 들어봤을 테니, 같은 업계인 헌터는 오죽할까.

말이 떨어지기도 전에 빛의 속도로 뛰어온 스무 명의 헌터들이 두려움과 신뢰가 가득한 눈빛으로 나를 바라본다.

“형님. 팬입니다. 진짜 팬이에요.”

“꺅. 어떡해. 진짜 어떡해애.”

“……고맙긴 한데, 다들 제정신이세요?”

이 상황에서 저런 말이 잘도 나오는 모양이다. 황당함에 고개를 절레절레 흔든 나는 팀장을 찾았다.

그나마 팀장답게 상황의 심각성을 제대로 파악했는지, 굳은 얼굴로 포켓을 뒤지던 그가 내게 뭔가를 건넸다.

“사인 좀 부탁드립니다. 이승엽 헌터님 화이팅이라고 적어 주시면.”

“…….”

“부탁드립니다. 저희 집안 대대로 물려줄 가보로 삼겠습니다.”

“…….”

아. 씨바, 할 말을 잃었습니다.

참담한 마음으로 브리핑용 보드판에 사인을 휘갈긴 내게, 팀장이 조심스럽게 덧붙였다.

“그리고 실례가 안 된다면 욕 한 번만.”

“예?”

“욕이요. 소원입니다.”

“……이 시벌 놈이.”

“감사합니다. 감사합니다!”

“진심이었는데요.”

“헉.”

그리고 그 모습을 심히 부러운 듯 바라보는 한 사람. 아니, 몬스터가 있었다.

“인기가 제법이구나. 간악한 인간이여. 똥을 싸면 유명해지고 사람들이 박수를 쳐 준다더니.”

“…….”

뭔가 순서가 뒤바뀐 것 같은데. 공공장소에서 똥을 싸면 유명해지긴 하겠지만, 보통은 박수 대신 귀싸대기를 치지 않을까.

하지만 스켈레톤 킹의 왜곡된 인식을 바로잡아줄 만큼 충분한 시간은 주어지지 않았다.

내가 입을 떼려던 그 순간, 지진이라도 온 것처럼 흔들리던 동굴 내부에 급격한 움직임이 일어났기 때문이었다.

구구구궁, 쩌저적!

지면이 갈라지고, 천장에는 거미줄 같은 금이 쩍쩍 그어진다. 헌터 중 누군가가 신음처럼 중얼거렸다.

“붕괴……?”

반은 맞고, 반은 틀렸다.

모두가 금방이라도 무너질듯한 천장을 바라보고 있을 때, 지면에서 벌어지는 일까지 파악하고 있던 나만은 그 사실을 알고 있었다.

콰득, 콰드득.

지면에 깔린 단단한 암석을 뚫고 고개를 내미는 새싹.

검붉은 색을 띤 그것이 내가 바라보는 와중에도 무섭게 성장하고 있었다.

가시를 만들고, 꽃봉오리를 터트리고, 그렇게 뿌려진 씨앗이 이내 사방으로 뻗어 나간다.

콰드드드드득!

“뭐, 뭐야!”

“꺄아아악!”

“으헉!”

“잘라! 쳐 내!”

이제야 그 사실을 눈치챈 헌터들이 황급히 움직였다.

그러나 비명을 내지르고, 끝없이 뻗어 나가는 수풀을 무기로 내려쳐도 소용없다.

당장 이 자리에서만 벌어지는 상황이 아니니까.

아무리 나와 스켈레톤 킹이 나선다 해도, 이 짧은 시간 안에 게이트를 전부 돌며 저것들을 처리하는 것은 무리다.

‘이건…….’

단순한 붕괴가 아니다. 변화다.

이 게이트 전체가, 새로운 형태로 탈바꿈하고 있는 것이다.

‘말 그대로 변이(變異). 그 자체.’

그렇게 사람들의 경악 어린 시선 속에서, 변이 게이트는 마지막 변화를 끝마치려 하고 있었다.

쿠구구궁. 쿵!

천장에 번진 실금이 진해지고, 틈새가 아가리를 벌렸다. 그 광경이 마치 동굴이라는 거대한 알이 깨지는 것 같았다.

그리고…….

쩌억!

아무것도 존재하지 않아야 할 천장 너머로부터, 붉은색의 빛과 어스름한 안개에 휩싸인 무언가가 모습을 드러냈다.

동굴과는 비교도 되지 않는 광활한 공간. 울창한 수풀과 습식 사우나처럼 후텁지근한 온도.

“저건.”

“미, 밀림?”

충격으로 모두가 할말을 잃은 그때, 스켈레톤 킹이 나만 들을 수 있는 목소리로 속삭였다.

“간악한 인간이여. 이 몸의 권능이 강해지고 있다.”

비록 지금은 환영 마법으로 본 모습을 가리고 있지만, 스켈레톤 킹의 진정한 정체는 몬스터. 녀석의 힘이 강해졌다는 것은 즉, 한 가지를 의미했다.

‘마력의 양과 밀도.’

보이지 않는다. 그러나 느낄 수 있다.

솨아아아.

온 사방을 잠식한 강대한 마력을.

금방이라도 터질 듯 팽창한 마력이 밀림을 짓누르고 있었다.

이 정도면 A급 게이트에서도 쉽게 느끼기 힘든 수준의 마력이다. 평범한 하급 헌터들이 버틸 수 있을 리 만무했다.

“흐읍. 흡.”

“수, 숨이…….”

서서히 풀려 가는 동공과 비틀거리는 신형.

스무 명에 달하는 헌터 중, 단 한 사람의 예외도 없었다. 빠른 속도로 하나둘씩 혼절하는 그들을 가만히 지켜보는 내 모습에, 스켈레톤 킹이 눈살을 찌푸렸다.

“간악한 인간이여. 너…….”

“이게 나아.”

“뭐?”

“저 사람들이 깨어 있어 봤자 좋을 게 하나 없다고.”

“……!”

스켈레톤 킹의 존재는 최대한 숨겨야 한다. 그렇다면 생명의 지장이 없는 선에서, 처음부터 배제 시키는 게 낫다.

목격자는 적을수록 좋으니까.

털썩.

마지막 한 사람마저 정신을 잃자, 내 눈짓에 고개를 끄덕인 스켈레톤 킹이 손가락을 튕겼다.

콰드드득!

어디서 솟아났는지 모를 무수한 뼈가 헌터들의 주위를 빈틈없이 감싼다. 스켈레톤 킹이 우쭐거리는 표정으로 말했다.

“됐다. 이 몸이 친히 실력을 발휘했으니, 이것으로 저 인간들의 안전은 보장되었다.”

작은 돔 형태를 이룬 그것을 유심히 바라본 내가 중얼거렸다.

“글쎄. 좀 더 보강해야 할 것 같은데.”

“쯧쯧. 간악하고도 불신에 가득 찬 인간이로군. 이 정도면 오우거 무리가 달려들어도 끄떡없을지어다.”

오우거는 등급을 떠나, 무시무시한 근력만은 늘 최상위에 꼽히는 몬스터.

하지만 스켈레톤 킹의 호언장담에도 내 생각은 달라지지 않았다.

“오우거라면 괜찮겠지. 근데 쟤들은 좀 달라 보이는데.”

“어?”

스켈레톤 킹이 멍청한 표정으로 고개를 돌린 곳에는, 광활한 밀림에서 서서히 몸을 일으키고 있는 한 존재가 있었다.

장장 20m에 달하는 신장. 밀림을 메운 무수한 거목보다 두껍고 긴 팔과 다리. 그리고…….

땅을 굽어보는, 거대한 외눈.

사이클롭스(Cyclops).

안개를 전신에 두른 신화 속 거인의 외눈이 우리를 향한다.

이어 으스스한 목소리가 천둥처럼 울려 퍼졌다.

- 침입자. 인간. 죽여라.

그리고 다음 순간.

띠링.



- 당신은 변이 게이트로 강제 이동되었습니다!

- 돌발 퀘스트, [거인의 숲]이 생성되었습니다.



구구구궁!

귓가를 파고드는 시스템 알림과 함께, 밀림이 흔들렸다.

아니. 그보다는 차라리 살아 움직인다고 해야 옳았다.

푸드득!

하늘 위로 솟아오르는 이름 모를 새들의 날갯짓 아래, 괴성과 함께 몸을 일으키는 것은 다름 아닌 수백 그루에 달하는 나무였다.

숱한 이야기 속을 장식하는 고대의 나무 요정들. 엔트들이 잠에서 깨어나 울부짖는다.

- 그워어어어!

- 그우우우우우!

그리고 이 모든 광경을 묵묵히 바라보던 한 사람. 아니, 한 몬스터는 재빠르게 생각을 고쳐먹었다.

“……인간들의 방어막을 보강하겠다.”

“어어, 그래.”

콰드득. 전과는 비교도 안 될 만큼 무수한 뼈들이 솟구쳐 겹겹이 쌓였다.

신중하게 보강 작업을 완료한 스켈레톤 킹이 진지한 눈빛으로 이곳을 향해 진군하는 밀림을 응시했다.

“준비됐어, 진?”

“물론이지, 킹…… 아니, 그런데 이딴 건 또 어디서 배워 온 거야.”

“인터넷. 재밌다.”

“너 이 새끼. 여기서 나가면 폰부터 압수다.”

스켈레톤 킹을 향해 으름장을 놓은 나는 작게 중얼거렸다.

“인벤토리 오픈, 소환.”

명령어와 함께 비어 있던 손아귀에 백염(白炎)의 창 자루가 잡힌다. 오랜만에 느끼는 익숙한 촉감.

전장으로 돌변한 주위를 바라보던 내 입가에 문득 웃음이 맺혔다.

‘가자.’

화륵.

하단전에서 끌어올린 삼 갑자의 열양지기가, 화룡이 되어 전신 사지백해로 뻗어 나갔다.
```

## Final English reading copy

```markdown
# Chapter 556

*Whew.*

I swept my gaze around with a sigh.

A damp, chilly cave. Narrow passages tangled together like a maze, with sharp stalactites hanging from the ceiling. Faces exhausted and terrified out of their minds.

*Just like back then.*

Three years ago. No—if I included the time I’d spent in Murim, it had been four years.

The accident that day remained seared into my heart like an indelible brand, and even now, after taking my revenge, I still couldn’t completely forget it.

“Fuck. This brings back memories.”

Unlike me, who muttered the words thickly under my breath, the Skeleton King smiled fondly.

“I feel the same. It is as though I have returned to what you humans call one’s homeland.”

“……”

You’ve got it wrong, man.

It seemed like we were remembering entirely different things.

For all I knew, this guy might have been Skeleton One—the skeleton I had encountered while spending day after day in low-level Gates.

*Anyway…*

*Rumble-rumble-rumble!*

*The mana wave is much stronger than I expected.*

It was lucky we had been nearby. Otherwise, twenty hardworking living people would almost have been wiped out.

I waved toward the Hunters staring blankly in our direction.

“It’s dangerous, so come over here.”

A man in his late twenties who appeared to be the Team Leader blinked.

“W-What?”

“I said come over here. Hurry.”

“W-Who are you?”

The cave was dark, and they were standing a considerable distance away. Their level was far too low for them to make out my face from that far.

I awkwardly scratched my chin before opening my mouth.

“I’m… Uh, look behind you.”

“What?”

Their reaction was slow. Instead of answering, I snapped my fingers.

*Whoosh—boom!*

With a faint whistle through the air, green blood splattered in every direction. At the same time, a rusty ax slipped limply from the hand of a goblin approaching one of the Hunters from behind.

Then the headless body collapsed like a rotten log.

*Thud!*

“Gah!”

“Behind you! Watch your backs!”

“What the hell is this?”

What else would it be? Finger Qi.

I muttered inwardly as I watched the Hunters hurriedly reform their ranks, then realized something.

*It’ll be faster if I go to them than if they come to me.*

Judging by how they were floundering against goblins before they’d even made it halfway through the Gate, they weren’t just low-level Hunters—they weren’t particularly experienced, either.

The Skeleton King swept back his blond hair and put on a solemn expression.

“Hmph. It seems the time has come for this body to take the field.”

“Stay put. Don’t get cocky.”

“……”

Now that I knew what needed to be done, there was no reason to hesitate. I walked toward them at a pace that was neither hurried nor leisurely.

*Step.*

One step.

At the same time, ten streams of Finger Qi shot through the air from my wide-open hands.

*Whoosh—thud-thud-thud-thud!*

One more time.

*Whoosh-whoosh-whoosh!*

Again.

*Boom!*

By the time the last one—a hobgoblin who looked like the leader—fell, nearly thirty goblins had become headless corpses sprawled across the ground.

And then…

*Step.*

With my third and final step, a sphere of light summoned by an unknown mage using Light magic illuminated my face.

*Flash.*

“……!”

“……!”

An invisible shock wave and wave of agitation swept through the cave.

Everyone was staring at my face with vacant expressions when, like a dam suddenly bursting, cries erupted from every direction.

“L-Lord Fuck!”

“Lord Sibu-leol!”

“J-J-Jin Taekyung!”

The last one was at least better.

The stutter might have stretched my name to six syllables, but compared to the nicknames that came before it, it was downright respectable. About as respectable as a deputy minister.

Come to think of it, the name fit the current situation pretty well.

The vibrations had steadily intensified, and now the whole cave was sh-sh-sh-shaking like a fucking earthquake.

*Rumble-rumble-rumble!*

The Skeleton King sauntered over, dodging a stalactite dropping from above, and muttered,

“This much commotion is most unsettling.”

“Tell me about it.”

The mana here was as far removed from the mana of this Gate—which was E-rank at best, or perhaps F-rank—as Henan was from the Nanman Beast Palace.

I clicked my tongue softly and waved toward the still-stunned Hunters.

“As I said before, it’s dangerous, so come over—”

*Patter-patter-patter-patter!*

“Whoa. You startled me.”

“Undead, have mercy.”

What was this? A Blink spell?

There were certainly advantages to being famous.

Even some old lady named Kim living in the middle of nowhere had probably heard my name. How could Hunters in the same profession not know me?

Before I could finish speaking, all twenty Hunters came running at the speed of light. They stared at me with eyes full of fear and trust.

“Hyung. I’m a fan. A genuine fan.”

“Eek! What do I do? What do I dooo?”

“……I appreciate it, but are you all out of your minds?”

Apparently, they could say things like that in a situation like this. I shook my head in disbelief and searched for the Team Leader.

At least he seemed to understand how serious the situation was. His face rigid, he rummaged through his pocket and handed me something.

“Could I get your autograph? Please write, ‘Go, Hunter Lee Seungyeop!’”

“……”

“Please. I’ll preserve it as a family heirloom and pass it down for generations.”

“……”

Ah. Fuck. I was speechless.

With a miserable look on my face, I scrawled my signature across the briefing board. The Team Leader cautiously added,

“And if it wouldn’t be too much trouble, could you swear once?”

“What?”

“Swear at me. It’s my lifelong wish.”

“……You fucking bastard.”

“Thank you! Thank you!”

“I was serious.”

“Gasp.”

And there was one person—or rather, one monster—watching the scene with profound envy.

“You are rather popular. Wretched human. They say that if one defecates, one becomes famous and the people applaud.”

“……”

Something about that order seemed backward.

Defecating in public might make you famous, but wouldn’t people usually slap you instead of applauding?

Unfortunately, I didn’t have enough time to correct the Skeleton King’s distorted understanding.

The moment I was about to speak, a sudden movement swept through the cave, which had been shaking as if an earthquake were taking place.

*Rumble-rumble—crack!*

The ground split apart, while cracks spread across the ceiling like a spiderweb. One of the Hunters muttered with a groan,

“Collapse…?”

Half right. Half wrong.

While everyone stared at the ceiling, which looked ready to come crashing down at any moment, I was the only one who knew what was happening below as well.

*Crack. Crack-crack.*

A sprout pushed its way through the solid rock covering the ground.

It was dark red, and even as I watched, it grew at a terrifying speed.

Thorns formed. A flower bud burst open. Then the seeds it scattered began spreading in every direction.

*Crack-crack-crack-crack!*

“W-What is that?”

“Eeeeeek!”

“Ugh!”

“Cut it! Chop it down!”

The Hunters had finally noticed what was happening and sprang into action.

But their screams and frantic swings did nothing to stop the undergrowth as it continued stretching endlessly outward.

Because this wasn’t happening only here.

Even if the Skeleton King and I joined in, there was no way we could travel through the entire Gate and deal with all of it in this short a time.

*This is…*

This wasn’t a simple collapse.

It was a transformation.

The entire Gate was changing into an entirely new form.

*Mutation. In the truest sense of the word.*

As the people watched in horror, the Mutated Gate was nearing the end of its final transformation.

*Rumble-rumble-rumble. Boom!*

The hairline cracks spreading across the ceiling darkened, and the gaps opened wide.

It looked as though a gigantic egg in the shape of a cave were breaking apart.

And then…

*Crack!*

Beyond the ceiling, where nothing should have existed, something emerged, wreathed in red light and a murky mist.

A vast space that dwarfed the cave. Dense vegetation. A sweltering temperature like a wet sauna.

“What is that?”

“I-Is it a jungle?”

Everyone was too shocked to speak. Then the Skeleton King whispered in a voice only I could hear.

“Wretched human. This body’s power is growing stronger.”

Although he was hiding his true appearance with illusion magic, the Skeleton King’s true nature was that of a monster.

If his power had grown stronger, that meant only one thing.

*The quantity and density of the mana.*

I couldn’t see it.

But I could feel it.

*Whoosh…*

The immense mana consuming every inch of space.

The mana had swelled to the point of bursting, pressing down on the jungle.

It was a level of mana that would be difficult to sense even in an A-rank Gate. There was no chance ordinary low-level Hunters could withstand it.

“Hhk. Hhk.”

“I-I can’t… breathe…”

Their pupils slowly unfocused, and their bodies staggered.

Not one of the twenty Hunters was spared. One after another, they fell unconscious at an alarming rate.

The Skeleton King frowned as he watched me calmly stand there.

“Wretched human. You…”

“This is better.”

“What?”

“There’s no point in letting them stay awake.”

“……!”

I had to conceal the Skeleton King’s existence as much as possible. If so, it was better to remove these people from the situation from the beginning, as long as doing so didn’t endanger their lives.

The fewer witnesses, the better.

*Thud.*

When the last person finally lost consciousness, the Skeleton King nodded at my signal and snapped his fingers.

*Crack-crack-crack!*

Countless bones rose from somewhere and tightly surrounded the Hunters without leaving a gap. The Skeleton King spoke with a smug expression.

“Done. Since this body has personally demonstrated its abilities, the safety of those humans is guaranteed.”

I studied the small dome-shaped barrier and muttered,

“I don’t know. I think it needs a little more reinforcement.”

“Tsk, tsk. What a wretched and distrustful human you are. Even if a horde of ogres attacked, this would not budge.”

Ogres were monsters whose terrifying strength was always considered among the highest, regardless of their Grade.

But even despite the Skeleton King’s boast, my opinion did not change.

“It’d probably be fine against ogres. But those things look a little different.”

“Huh?”

The Skeleton King turned his head with a foolish expression.

In the vast jungle, something was slowly rising to its feet.

Twenty meters tall.

Arms and legs thicker and longer than the countless giant trees filling the jungle.

And…

A gigantic single eye gazing down at the earth.

A Cyclops.

The one eye of the mythical giant, its entire body wrapped in mist, turned toward us.

Then a chilling voice boomed like thunder.

—Intruders. Humans. Kill.

And the next moment—

> **System**
>
> You have been forcibly moved to the Mutated Gate!
>
> An Unexpected Quest, **Forest of Giants**, has been created.

*Rumble-rumble-rumble!*

Along with the System notification drilling into my ears, the jungle shook.

No. It would be more accurate to say that it came alive.

*Flap-flap!*

Beneath the wingbeats of nameless birds shooting into the sky, something rose with a monstrous cry.

It was none other than hundreds of trees.

Ancient tree spirits featured in countless tales. The Ents awoke from their slumber and roared.

—Gwoooooar!

—Grrrrrrrr!

And there was one person—or rather, one monster—who had been silently watching the entire scene.

He quickly changed his mind.

“……I shall reinforce the humans’ barrier.”

“Uh, yeah.”

*Crack-crack.*

Countless bones, far more numerous than before, shot upward and piled atop one another in layer after layer.

After carefully completing the reinforcement, the Skeleton King stared solemnly at the jungle advancing toward us.

“Ready, Jin?”

“Of course, King… Wait, where the hell did you learn this kind of thing?”

“The internet. It is entertaining.”

“You bastard. Once we get out of here, I’m confiscating your phone first.”

After threatening the Skeleton King, I muttered under my breath,

“Inventory open. Summon.”

At the command, the shaft of White Flame appeared in my empty hand.

The familiar sensation was one I hadn’t felt in a long time.

As I looked around at the surroundings that had transformed into a battlefield, a smile suddenly touched my lips.

*Let’s go.*

*Whoosh.*

Three jiazi of Scorching Yang Qi surged up from my lower dantian, transformed into a fire dragon, and spread through every limb and bone in my body.
```
